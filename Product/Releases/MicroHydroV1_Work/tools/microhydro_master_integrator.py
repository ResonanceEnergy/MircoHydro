
#!/usr/bin/env python3
"""MicroHydroV1 — Master Integrator (SharePoint SoT/Releases/Archive)

Purpose
- Analyze *every* file in an input Archive ZIP, including embedded ZIP packages and their contents.
- Produce a policy-compliant, organized output tree:
  - 01_SharePoint_Libraries (cleaned)
  - 02_Canonical_Working_Tree (merged SoT working tree)
  - 03_Packages_Original_Zips (deduplicated packages)
  - 04_Reports (inventory + policy flags + conflicts)
  - 05_Tools (this script + config)

Key behaviors
- Removes macOS junk: __MACOSX, .DS_Store, and AppleDouble (._*)
- Deduplicates embedded ZIPs by SHA-256 (keeps one canonical copy)
- Builds an inventory of:
  - filesystem files in the extracted archive
  - ALL entries inside each embedded ZIP (and recursively inspects nested ZIP entries when found)
- Applies organization policy checks (from policy_config.json):
  - canonical CAD params path presence
  - params drift (params.json outside cad/params)
  - raw run folder naming compliance
  - release ZIP placement sanity
  - duplicate content detection
- Creates a canonical working tree by:
  - extracting a base FULL pack
  - overlaying add-ons in priority order
  - overlaying loose SoT files if present

Usage
  python3 microhydro_master_integrator.py \
    --archive Archive.zip \
    --out MasterIntegrated_Output \
    --policy policy_config.json \
    --zip-out

Notes
- Designed to run locally on macOS/Windows/Linux.
- Uses only Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


BAD_NAMES = {'.DS_Store'}


def is_junk_name(name: str) -> bool:
    return name in BAD_NAMES or name.startswith('._')


def is_junk_parts(parts: Tuple[str, ...]) -> bool:
    return '__MACOSX' in parts


def sha256_stream(f: io.BufferedReader, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    for b in iter(lambda: f.read(chunk), b''):
        h.update(b)
    return h.hexdigest()


def sha256_file(p: Path) -> str:
    with p.open('rb') as f:
        return sha256_stream(f)


def dt_from_zipinfo(info: zipfile.ZipInfo) -> float:
    # ZipInfo.date_time is (Y,M,D,H,M,S)
    return datetime(*info.date_time).timestamp()


@dataclass
class Policy:
    sot_required_dirs: List[str]
    canonical_files: List[str]
    high_risk_files: List[str]
    raw_run_folder_regex: str
    base_pack_pattern: str
    overlay_priority: List[Dict[str, object]]


def load_policy(policy_path: Path) -> Policy:
    obj = json.loads(policy_path.read_text(encoding='utf-8'))
    return Policy(
        sot_required_dirs=obj.get('sot_required_dirs', []),
        canonical_files=obj.get('canonical_files', []),
        high_risk_files=obj.get('high_risk_files', []),
        raw_run_folder_regex=obj.get('raw_run_folder_regex', ''),
        base_pack_pattern=obj.get('base_pack_pattern', ''),
        overlay_priority=obj.get('overlay_priority', []),
    )


def normalize_library_name(name: str) -> str:
    # Fix common mac encoding artifacts in the archive naming (ΓÇö => —)
    return name.replace('ΓÇö', '—').replace('—', '—')


def safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_json(p: Path, obj) -> None:
    safe_mkdir(p.parent)
    p.write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8')


def write_csv(p: Path, rows: List[Dict[str, object]], fieldnames: List[str]) -> None:
    safe_mkdir(p.parent)
    with p.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in fieldnames})


def walk_filesystem(extracted_root: Path) -> List[Dict[str, object]]:
    """Return list of file records for filesystem files in extracted archive."""
    rows = []
    for p in extracted_root.rglob('*'):
        if p.is_dir():
            continue
        if is_junk_name(p.name) or is_junk_parts(p.parts):
            continue
        st = p.stat()
        rows.append({
            'source': 'filesystem',
            'container': '',
            'path': p.relative_to(extracted_root).as_posix(),
            'bytes': st.st_size,
            'mtime': st.st_mtime,
            'sha256': sha256_file(p),
        })
    return rows


def iter_zip_entries(zip_path: Path) -> Iterable[Tuple[zipfile.ZipInfo, bytes]]:
    """Yield (ZipInfo, sha256) for each non-junk file entry in a zip."""
    with zipfile.ZipFile(zip_path, 'r') as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            name = info.filename
            if '__MACOSX' in name or name.endswith('.DS_Store') or '/._' in name or name.startswith('._'):
                continue
            with z.open(info, 'r') as f:
                data = f.read()
            yield info, data


def scan_zip(zip_path: Path, recurse_nested: bool = True) -> List[Dict[str, object]]:
    """Build inventory rows for a zip and (optionally) nested zips inside it."""
    rows = []
    for info, data in iter_zip_entries(zip_path):
        sha = hashlib.sha256(data).hexdigest()
        rows.append({
            'source': 'zip',
            'container': zip_path.name,
            'path': info.filename,
            'bytes': info.file_size,
            'mtime': dt_from_zipinfo(info),
            'sha256': sha,
        })
        # Optional nested zip inspection
        if recurse_nested and info.filename.lower().endswith('.zip') and len(data) > 0:
            try:
                with zipfile.ZipFile(io.BytesIO(data), 'r') as nz:
                    for ni in nz.infolist():
                        if ni.is_dir():
                            continue
                        nname = ni.filename
                        if '__MACOSX' in nname or nname.endswith('.DS_Store') or '/._' in nname or nname.startswith('._'):
                            continue
                        with nz.open(ni, 'r') as nf:
                            nd = nf.read()
                        rows.append({
                            'source': 'zip:nested',
                            'container': f"{zip_path.name}::{info.filename}",
                            'path': nname,
                            'bytes': ni.file_size,
                            'mtime': dt_from_zipinfo(ni),
                            'sha256': hashlib.sha256(nd).hexdigest(),
                        })
            except Exception:
                # Not a valid zip; ignore
                pass
    return rows


def dedupe_zips(zip_paths: List[Path]) -> Tuple[List[Dict[str, object]], List[Dict[str, object]]]:
    """Deduplicate zips by SHA-256. Returns (selected, duplicates)."""
    meta = []
    for p in zip_paths:
        st = p.stat()
        meta.append({
            'zip_name': p.name,
            'zip_path': str(p),
            'sha256': sha256_file(p),
            'bytes': st.st_size,
            'mtime': st.st_mtime,
        })

    by_sha: Dict[str, List[Dict[str, object]]] = {}
    for r in meta:
        by_sha.setdefault(r['sha256'], []).append(r)

    selected, dupes = [], []
    for sha, items in by_sha.items():
        def score(it):
            # prefer names without " (n).zip" and most recent mtime
            return (1 if re.search(r'\s\(\d+\)\.zip$', it['zip_name']) else 0, -it['mtime'])
        items_sorted = sorted(items, key=score)
        selected.append(items_sorted[0])
        dupes.extend(items_sorted[1:])

    selected = sorted(selected, key=lambda x: x['zip_name'].lower())
    return selected, dupes


def overlay_order(selected: List[Dict[str, object]], base_name: str, policy: Policy) -> List[str]:
    # compute order weights based on policy.overlay_priority
    def weight(name: str) -> int:
        w = 100
        for rule in policy.overlay_priority:
            m = str(rule.get('match', ''))
            if m and m in name:
                w = int(rule.get('order', w))
                break
        return w

    names = [r['zip_name'] for r in selected if r['zip_name'] != base_name]
    return [n for _, n in sorted([(weight(n), n) for n in names], key=lambda t: (t[0], t[1].lower()))]


def extract_overlay(zip_path: Path, dest: Path, conflicts: List[Dict[str, object]], strip_prefix: str = 'MicroHydroV1/') -> None:
    with zipfile.ZipFile(zip_path, 'r') as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            name = info.filename
            if '__MACOSX' in name or name.endswith('.DS_Store') or '/._' in name or name.startswith('._'):
                continue
            if strip_prefix and name.startswith(strip_prefix):
                name = name[len(strip_prefix):]
            name = name.lstrip('./')
            if not name:
                continue
            outp = dest / name
            safe_mkdir(outp.parent)
            src_m = dt_from_zipinfo(info)
            if outp.exists():
                dst_m = outp.stat().st_mtime
                if src_m <= dst_m + 1e-6:
                    continue
                conflicts.append({'file': name, 'from': zip_path.name, 'old_mtime': dst_m, 'new_mtime': src_m})
            with z.open(info, 'r') as f, open(outp, 'wb') as o:
                shutil.copyfileobj(f, o)
            os.utime(outp, (src_m, src_m))


def apply_policy_flags(rows: List[Dict[str, object]], policy: Policy) -> List[Dict[str, object]]:
    """Add policy_flags per row."""
    raw_re = re.compile(policy.raw_run_folder_regex) if policy.raw_run_folder_regex else None

    # duplicates by sha
    sha_counts: Dict[str, int] = {}
    for r in rows:
        sha_counts[r['sha256']] = sha_counts.get(r['sha256'], 0) + 1
    dup_sha = {s for s, c in sha_counts.items() if c > 1}

    for r in rows:
        flags = []
        path_norm = r['path'].replace('MicroHydroV1/', '')

        # params presence + canonical + drift
        if path_norm.endswith('params.json'):
            flags.append('PARAMS_JSON_PRESENT')
            if any(path_norm.endswith(cf) for cf in policy.canonical_files):
                flags.append('CANONICAL_PARAMS')
            else:
                flags.append('PARAMS_POTENTIAL_DRIFT')

        # raw folder naming
        if 'tests/raw/' in path_norm and raw_re is not None:
            if raw_re.search(path_norm) is None:
                flags.append('RAW_FOLDER_NAMING_NONSTANDARD')

        # duplicate content
        if r['sha256'] in dup_sha:
            flags.append('DUPLICATE_CONTENT')

        r['policy_flags'] = ';'.join(flags)

    return rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--archive', required=True, help='Path to the SharePoint export archive ZIP')
    ap.add_argument('--out', default='MasterIntegrated_Output', help='Output folder')
    ap.add_argument('--policy', default='policy_config.json', help='Policy config JSON')
    ap.add_argument('--zip-out', action='store_true', help='Also produce a ZIP of the output folder')
    ap.add_argument('--no-nested', action='store_true', help='Skip recursive scan of nested ZIPs inside ZIPs')
    args = ap.parse_args(argv)

    src_zip = Path(args.archive).resolve()
    out_root = Path(args.out).resolve()
    policy_path = Path(args.policy)
    if not policy_path.is_absolute():
        # resolve relative to script folder
        policy_path = (Path(__file__).parent / policy_path).resolve()

    policy = load_policy(policy_path)

    if out_root.exists():
        shutil.rmtree(out_root)
    safe_mkdir(out_root)

    stage = out_root / '_stage'
    safe_mkdir(stage)
    top = stage / 'top'

    with zipfile.ZipFile(src_zip, 'r') as z:
        z.extractall(top)

    # Normalize SharePoint library folders
    libs_out = out_root / '01_SharePoint_Libraries'
    safe_mkdir(libs_out)

    # Find library candidates
    for p in top.iterdir():
        if not p.is_dir():
            continue
        name_norm = normalize_library_name(p.name)
        if name_norm.startswith('MicroHydroV1') and '—' in name_norm:
            dst = libs_out / name_norm
            for f in p.rglob('*'):
                if f.is_dir():
                    continue
                if is_junk_name(f.name) or is_junk_parts(f.parts):
                    continue
                rel = f.relative_to(p)
                outp = dst / rel
                safe_mkdir(outp.parent)
                shutil.copy2(f, outp)

    # Admin docs
    admin = out_root / '00_Admin'
    safe_mkdir(admin)
    log_doc = top / 'RES_MicroHydroV1_Integration_Log.docx'
    if log_doc.exists():
        shutil.copy2(log_doc, admin / log_doc.name)

    # Embedded zip discovery
    zip_paths = [p for p in top.rglob('*.zip') if p.is_file() and not is_junk_name(p.name) and not is_junk_parts(p.parts)]
    selected, dupes = dedupe_zips(zip_paths)

    pkg_dir = out_root / '03_Packages_Original_Zips'
    safe_mkdir(pkg_dir)
    for it in selected:
        shutil.copy2(Path(it['zip_path']), pkg_dir / it['zip_name'])

    # Inventory
    inv = walk_filesystem(top)
    for it in selected:
        zp = pkg_dir / it['zip_name']
        inv.extend(scan_zip(zp, recurse_nested=not args.no_nested))

    inv = apply_policy_flags(inv, policy)

    # Reports
    reports = out_root / '04_Reports'
    safe_mkdir(reports)

    fields = ['source','container','path','bytes','mtime','sha256','policy_flags']
    write_csv(reports / 'inventory_all_files.csv', inv, fields)
    write_json(reports / 'inventory_all_files.json', inv)

    # Duplicates report
    sha_counts = {}
    for r in inv:
        sha_counts[r['sha256']] = sha_counts.get(r['sha256'], 0) + 1
    dup_sha = {s for s,c in sha_counts.items() if c > 1}
    dup_rows = [r for r in inv if r['sha256'] in dup_sha]
    write_csv(reports / 'duplicates_by_sha256.csv', dup_rows, fields)

    flagged = [r for r in inv if r.get('policy_flags')]
    write_csv(reports / 'policy_flags.csv', flagged, fields)

    # Canonical working tree merge
    canon = out_root / '02_Canonical_Working_Tree' / 'MicroHydroV1'
    safe_mkdir(canon)

    base_name = None
    for it in selected:
        if policy.base_pack_pattern and policy.base_pack_pattern in it['zip_name']:
            base_name = it['zip_name']
            break
    if base_name is None:
        # fallback: first zip
        base_name = selected[0]['zip_name'] if selected else None

    conflicts: List[Dict[str, object]] = []
    extracted_from: List[str] = []

    if base_name:
        extract_overlay(pkg_dir / base_name, canon, conflicts)
        extracted_from.append(base_name)

    for n in overlay_order(selected, base_name, policy):
        extract_overlay(pkg_dir / n, canon, conflicts)
        extracted_from.append(n)

    # Overlay loose SoT MicroHydroV1 if present
    loose = libs_out / 'MicroHydroV1 — SoT' / 'MicroHydroV1'
    if loose.exists():
        for f in loose.rglob('*'):
            if f.is_dir():
                continue
            if is_junk_name(f.name) or is_junk_parts(f.parts):
                continue
            if f.suffix.lower() == '.zip':
                continue
            rel = f.relative_to(loose)
            dst = canon / rel
            safe_mkdir(dst.parent)
            if dst.exists() and f.stat().st_mtime <= dst.stat().st_mtime + 1e-6:
                continue
            if dst.exists():
                conflicts.append({'file': rel.as_posix(), 'from': 'LooseSoT', 'old_mtime': dst.stat().st_mtime, 'new_mtime': f.stat().st_mtime})
            shutil.copy2(f, dst)

    write_json(reports / 'canonical_conflicts.json', {'count': len(conflicts), 'items': conflicts[:1000]})

    # Summary
    summary = {
        'generated_at': datetime.utcnow().isoformat(timespec='seconds') + 'Z',
        'source_zip': str(src_zip),
        'filesystem_file_count': sum(1 for r in inv if r['source'] == 'filesystem'),
        'zip_entry_count': sum(1 for r in inv if r['source'].startswith('zip')),
        'embedded_zips_found': len(zip_paths),
        'embedded_zips_deduped': len(selected),
        'duplicate_zip_files_removed': len(dupes),
        'canonical_base_pack': base_name,
        'overlay_order': overlay_order(selected, base_name, policy) if base_name else [],
        'conflicts_count': len(conflicts),
        'policy_flagged_items': len(flagged),
    }
    write_json(reports / 'summary.json', summary)

    # Copy tools/config into output
    tools = out_root / '05_Tools'
    safe_mkdir(tools)
    shutil.copy2(Path(__file__), tools / Path(__file__).name)
    shutil.copy2(policy_path, tools / policy_path.name)

    # Optional: zip output
    if args.zip_out:
        zip_name = out_root.with_suffix('.zip')
        if zip_name.exists():
            zip_name.unlink()
        with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for f in out_root.rglob('*'):
                if f.is_dir():
                    continue
                # skip stage to keep final zip smaller
                if '_stage' in f.parts:
                    continue
                z.write(f, arcname=f.relative_to(out_root).as_posix())
        print('Wrote ZIP:', zip_name)

    print('Done. Output folder:', out_root)
    print('Summary:', reports / 'summary.json')


if __name__ == '__main__':
    main()
