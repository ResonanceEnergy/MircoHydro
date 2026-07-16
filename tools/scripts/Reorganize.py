#!/usr/bin/env python3
"""Reorganize ResonanceEnergy Enterprise repo with **zero data loss**.

✅ Designed for SharePoint/OneDrive synced folders.
✅ Default behavior is SAFE:
   - DRY-RUN by default (no changes)
   - COPY to a new destination folder when --apply
   - SHA256 manifests for src/dst
   - Verification that every copied file matches

What gets cleaned/streamlined:
- macOS cruft: __MACOSX/, .DS_Store, ._ resource forks -> _Archive/_macos/
- Duplicate folder copies: "99_Operations 2" and "99_Operations 3" -> _Archive/duplicates/
- Backups: _BACKUPS/ and resonance_backup_manifest.json -> _Archive/backups/
- Root-level libraries/bundles:
    OffGrid_* -> _Reference_Library/
    MicroHydroV1_* -> _Packages/MicroHydroV1/
- Artifact hygiene:
    artifacts/*.zip -> artifacts/builds/
    artifacts/ResonanceEnergy_Enterprise_* (extracted builds) -> _Archive/build_extracts/
- Legacy toolkit:
    Tools Folder Kit/ -> Tools/_Legacy_Kit/

USAGE
-----
1) Dry-run (recommended first):
   python3 reorganize_resonance_repo.py --src /path/to/ResonanceEnergy_Enterprise_POPULATED

2) Apply (copy mode, safest):
   python3 reorganize_resonance_repo.py --src /path/to/ResonanceEnergy_Enterprise_POPULATED --apply

3) Apply (move mode, only after you trust it):
   python3 reorganize_resonance_repo.py --src /path/to/ResonanceEnergy_Enterprise_POPULATED --apply --mode move

OUTPUTS
-------
Destination will contain:
  reorg_report/
    MOVE_PLAN.csv
    manifest_src.csv
    manifest_dst.csv
    SUMMARY.md

Notes:
- In move mode, source files are deleted ONLY after dst hash matches.
- Empty folders are cleaned after deletions.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Tuple


# ---------------------------- hashing ----------------------------

def sha256_file(p: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


# ---------------------------- filesystem helpers ----------------------------

def safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def rel_to_root(p: Path, root: Path) -> str:
    return p.resolve().relative_to(root.resolve()).as_posix()


def walk_files(root: Path) -> Iterable[Path]:
    for p in root.rglob('*'):
        if p.is_file():
            yield p


def is_macos_junk(rel: str) -> bool:
    p = Path(rel)
    return (
        '__MACOSX' in p.parts
        or p.name == '.DS_Store'
        or p.name.startswith('._')
    )


# ---------------------------- rules ----------------------------

@dataclass
class MoveRule:
    name: str
    predicate: Callable[[str], bool]
    mapper: Callable[[str], str]


def build_rules() -> list[MoveRule]:
    def rule_macos(rel: str) -> bool:
        return is_macos_junk(rel)

    def map_macos(rel: str) -> str:
        return f"_Archive/_macos/{rel}"

    def rule_dup_ops(rel: str) -> bool:
        return rel.startswith('99_Operations 2/') or rel.startswith('99_Operations 3/')

    def map_dup_ops(rel: str) -> str:
        root = rel.split('/')[0]
        rest = '/'.join(rel.split('/')[1:])
        return f"_Archive/duplicates/{root}/{rest}"

    def rule_backups(rel: str) -> bool:
        return rel.startswith('_BACKUPS/') or rel == 'resonance_backup_manifest.json'

    def map_backups(rel: str) -> str:
        if rel == 'resonance_backup_manifest.json':
            return f"_Archive/backups/{rel}"
        return f"_Archive/backups/{rel.split('/', 1)[1]}"

    def rule_offgrid(rel: str) -> bool:
        return rel.startswith('OffGrid_')

    def map_offgrid(rel: str) -> str:
        root = rel.split('/')[0]
        rest = '/'.join(rel.split('/')[1:])
        return f"_Reference_Library/{root}/{rest}"

    def rule_microhydro(rel: str) -> bool:
        return rel.startswith('MicroHydroV1_')

    def map_microhydro(rel: str) -> str:
        root = rel.split('/')[0]
        rest = '/'.join(rel.split('/')[1:])
        return f"_Packages/MicroHydroV1/{root}/{rest}"

    def rule_tools_kit(rel: str) -> bool:
        return rel.startswith('Tools Folder Kit/')

    def map_tools_kit(rel: str) -> str:
        rest = rel.split('/', 1)[1]
        return f"Tools/_Legacy_Kit/{rest}"

    def rule_artifacts_extract(rel: str) -> bool:
        parts = rel.split('/')
        return len(parts) >= 3 and parts[0] == 'artifacts' and parts[1].startswith('ResonanceEnergy_Enterprise_')

    def map_artifacts_extract(rel: str) -> str:
        parts = rel.split('/')
        folder = parts[1]
        rest = '/'.join(parts[2:])
        return f"_Archive/build_extracts/{folder}/{rest}"

    def rule_artifacts_zips(rel: str) -> bool:
        return rel.startswith('artifacts/') and rel.lower().endswith('.zip')

    def map_artifacts_zips(rel: str) -> str:
        return f"artifacts/builds/{Path(rel).name}"

    return [
        MoveRule('macos_junk', rule_macos, map_macos),
        MoveRule('duplicate_ops', rule_dup_ops, map_dup_ops),
        MoveRule('backups', rule_backups, map_backups),
        MoveRule('reference_offgrid', rule_offgrid, map_offgrid),
        MoveRule('packages_microhydro', rule_microhydro, map_microhydro),
        MoveRule('tools_legacy_kit', rule_tools_kit, map_tools_kit),
        MoveRule('artifacts_extract', rule_artifacts_extract, map_artifacts_extract),
        MoveRule('artifacts_zips', rule_artifacts_zips, map_artifacts_zips),
    ]


def map_rel(rel: str, rules: list[MoveRule]) -> Tuple[str, str]:
    for r in rules:
        if r.predicate(rel):
            return r.mapper(rel), r.name
    return rel, 'keep'


# ---------------------------- execution ----------------------------

def copy_with_verify(src: Path, dst: Path) -> Tuple[int, bool]:
    safe_mkdir(dst.parent)
    shutil.copy2(src, dst)
    return src.stat().st_size, sha256_file(src) == sha256_file(dst)


def write_manifest(root: Path, out_csv: Path) -> None:
    with out_csv.open('w', newline='', encoding='utf-8') as fp:
        w = csv.writer(fp)
        w.writerow(['rel', 'bytes', 'sha256'])
        for p in walk_files(root):
            w.writerow([rel_to_root(p, root), p.stat().st_size, sha256_file(p)])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True, help='Source repo folder')
    ap.add_argument('--dst', default=None, help='Destination folder (default: SRC__RESTRUCTURED_TIMESTAMP)')
    ap.add_argument('--mode', choices=['copy', 'move'], default='copy', help='copy (recommended) or move (delete src after verified copy)')
    ap.add_argument('--apply', action='store_true', help='Actually perform changes (default: dry-run)')
    ap.add_argument('--report', default='reorg_report', help='Report folder name under destination')
    args = ap.parse_args()

    src_root = Path(args.src).expanduser().resolve()
    if not src_root.exists() or not src_root.is_dir():
        raise SystemExit(f'--src not found or not a folder: {src_root}')

    stamp = __import__('datetime').datetime.now().strftime('%Y%m%d_%H%M%S')
    dst_root = Path(args.dst).expanduser().resolve() if args.dst else src_root.parent / f"{src_root.name}__RESTRUCTURED_{stamp}"

    rules = build_rules()

    plan = []
    for f in walk_files(src_root):
        rel = rel_to_root(f, src_root)
        new_rel, rule = map_rel(rel, rules)
        plan.append((rel, new_rel, rule, f.stat().st_size))

    # Always write plan somewhere
    plan_root = dst_root if args.apply else (dst_root.parent / (dst_root.name + '_DRYRUN'))
    safe_mkdir(plan_root)
    report_root = plan_root / args.report
    safe_mkdir(report_root)

    plan_csv = report_root / 'MOVE_PLAN.csv'
    with plan_csv.open('w', newline='', encoding='utf-8') as fp:
        w = csv.writer(fp)
        w.writerow(['old_rel', 'new_rel', 'rule', 'bytes'])
        w.writerows(plan)

    if not args.apply:
        print('[DRY-RUN] Plan written:', plan_csv)
        print('[DRY-RUN] No files copied/moved.')
        return 0

    # Execute copy + verify
    total_bytes = 0
    ok_count = 0
    for old_rel, new_rel, rule, sz in plan:
        sp = src_root / old_rel
        dp = dst_root / new_rel
        b, ok = copy_with_verify(sp, dp)
        total_bytes += b
        ok_count += int(ok)
        if not ok:
            raise SystemExit(f'Hash mismatch after copy: {old_rel} -> {new_rel}')

    # Manifests
    write_manifest(src_root, report_root / 'manifest_src.csv')
    write_manifest(dst_root, report_root / 'manifest_dst.csv')

    # Optional move cleanup
    if args.mode == 'move':
        for old_rel, new_rel, rule, sz in plan:
            sp = src_root / old_rel
            dp = dst_root / new_rel
            if dp.exists() and sha256_file(sp) == sha256_file(dp):
                sp.unlink()
        # remove empty dirs
        for d in sorted([p for p in src_root.rglob('*') if p.is_dir()], reverse=True):
            try:
                d.rmdir()
            except OSError:
                pass

    summary = report_root / 'SUMMARY.md'
    summary.write_text(
        "# Reorg Summary\n\n"
        f"- src: {src_root}\n"
        f"- dst: {dst_root}\n"
        f"- files processed: {len(plan)}\n"
        f"- bytes copied: {total_bytes}\n"
        f"- verified copies: {ok_count}/{len(plan)}\n\n"
        "Artifacts:\n"
        "- MOVE_PLAN.csv\n"
        "- manifest_src.csv\n"
        "- manifest_dst.csv\n",
        encoding='utf-8'
    )

    print('DONE. Summary:', summary)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
