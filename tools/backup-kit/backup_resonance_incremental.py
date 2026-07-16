#!/usr/bin/env python3
"""
Incremental Backup - Full Workspace Scanner

Creates/updates a ZIP archive with ONLY new or modified files.
Keeps a manifest so future runs only add changes.

Outputs (in project root):
  - resonance_backup_incremental.zip
  - resonance_backup_manifest.json

Usage:
  python3 backup_resonance_incremental.py
  python3 backup_resonance_incremental.py --hash
  python3 backup_resonance_incremental.py --dry-run
  python3 backup_resonance_incremental.py --repack
"""

import argparse
import hashlib
import json
import time
import zipfile
from pathlib import Path

BACKUP_NAME = "resonance_backup_incremental.zip"
MANIFEST = "resonance_backup_manifest.json"

EXCLUDES = {
    ".git",
    "__pycache__",
    ".DS_Store",
    BACKUP_NAME,
    MANIFEST,
    "resonance_backup.zip",
    "backup_resonance.py",
    "backup_resonance_incremental.py",
}

def is_excluded(path: Path) -> bool:
    p = str(path)
    return any(ex in p for ex in EXCLUDES)

def iter_all_files(root: Path):
    for fp in root.rglob("*"):
        if fp.is_file() and not is_excluded(fp):
            yield fp

def fast_info(fp: Path):
    st = fp.stat()
    return {"size": st.st_size, "mtime_ns": st.st_mtime_ns}

def file_hash(fp: Path, algo: str = "md5", chunk: int = 1024 * 1024):
    h = hashlib.new(algo)
    with fp.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def load_manifest(root: Path) -> dict:
    mf = root / MANIFEST
    if mf.exists():
        try:
            return json.loads(mf.read_text())
        except Exception:
            return {}
    return {}

def save_manifest(root: Path, data: dict):
    (root / MANIFEST).write_text(json.dumps(data, indent=2))

def needs_update(fp: Path, rel: str, manifest: dict, use_hash: bool):
    info = fast_info(fp)
    old = manifest.get(rel)

    if old is None:
        if use_hash:
            info["hash"] = file_hash(fp)
        return True, info

    if info["size"] != old.get("size") or info["mtime_ns"] != old.get("mtime_ns"):
        if use_hash:
            h = file_hash(fp)
            if h == old.get("hash"):
                info["hash"] = h
                return False, info
            info["hash"] = h
        return True, info

    if use_hash and not old.get("hash"):
        info["hash"] = file_hash(fp)
        return True, info

    return False, info

def add_files_to_zip(zip_path: Path, files, relpaths, dry_run: bool):
    if dry_run:
        for rp in relpaths:
            print(f"Would add/update: {rp}")
        return 0

    mode = "a" if zip_path.exists() else "w"
    added = 0
    with zipfile.ZipFile(zip_path, mode, compression=zipfile.ZIP_DEFLATED) as z:
        for fp, rp in zip(files, relpaths):
            z.write(fp, arcname=rp)
            added += 1
    return added

def repack_zip(root: Path, zip_path: Path, manifest: dict, dry_run: bool):
    if not zip_path.exists():
        print("No existing ZIP to repack; skipping.")
        return
    if dry_run:
        print("[dry-run] Would repack ZIP...")
        return

    tmp_zip = zip_path.with_suffix(".tmp.zip")
    with zipfile.ZipFile(tmp_zip, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for rel in sorted(k for k in manifest.keys() if k != "meta"):
            fp = root / rel
            if fp.exists() and fp.is_file() and not is_excluded(fp):
                z.write(fp, arcname=rel)
    tmp_zip.replace(zip_path)
    print(f"Repacked -> {zip_path}")

def main():
    parser = argparse.ArgumentParser(description="Incremental backup to ZIP with manifest")
    parser.add_argument("--hash", action="store_true", help="Use content hash (slower, most accurate)")
    parser.add_argument("--repack", action="store_true", help="Rebuild ZIP cleanly")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    parser.add_argument("--backup-name", default=BACKUP_NAME)
    args = parser.parse_args()

    root = Path.cwd()
    zip_path = root / args.backup_name

    manifest = load_manifest(root)
    manifest.setdefault("meta", {"created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})

    to_add_files, to_add_rel = [], []
    scanned = 0

    for fp in iter_all_files(root):
        scanned += 1
        rel = str(fp.relative_to(root))
        update, info = needs_update(fp, rel, manifest, use_hash=args.hash)
        manifest[rel] = info
        if update:
            to_add_files.append(fp)
            to_add_rel.append(rel)

    if args.repack:
        repack_zip(root, zip_path, manifest, args.dry_run)

    added = add_files_to_zip(zip_path, to_add_files, to_add_rel, args.dry_run)

    if not args.dry_run:
        manifest["meta"]["last_backup"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        save_manifest(root, manifest)

    print("\nSummary:")
    print(f"  Files scanned : {scanned}")
    print(f"  Files updated : {added}")
    print(f"  ZIP path      : {zip_path}")
    print(f"  Manifest      : {root / MANIFEST}")
    print(f"  Mode          : {'hash' if args.hash else 'mtime/size'}"
          f"{' + repack' if args.repack else ''}"
          f"{' + dry-run' if args.dry_run else ''}")

if __name__ == "__main__":
    main()
