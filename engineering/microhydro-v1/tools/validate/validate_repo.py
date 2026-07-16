#!/usr/bin/env python3
"""MicroHydroV1 - Repo/SoT validation (SharePoint-friendly).

Purpose
- Catch structural drift, duplicates, and naming violations before publishing a Release.

Design
- Works on a local copy of the SoT folder (synced via OneDrive) OR on an extracted release bundle.
- Fails fast with actionable messages.

Usage
    python validate_repo.py --root /path/to/MicroHydroV1
"""

from __future__ import annotations
import argparse
import re
from pathlib import Path

REQUIRED_DIRS = ['docs', 'cad', 'automation', 'tests', 'data', 'tools']
CANONICAL_FILES = [
    ('cad/params/params.json', 'Canonical CAD parameter file'),
    ('automation/import_measurements.py', 'Canonical importer script'),
]
RUN_FOLDER_RE = re.compile(r'^\d{4}-\d{2}-\d{2}_Run\d+_.+$')


def find_all(root: Path, pattern: str):
    return list(root.rglob(pattern))


def fail(msg: str):
    raise SystemExit(msg)


def check_required_dirs(root: Path):
    missing = [d for d in REQUIRED_DIRS if not (root / d).exists()]
    if missing:
        fail(f"Missing required dirs: {missing}")


def check_high_risk_present(root: Path):
    for rel, desc in CANONICAL_FILES:
        if not (root / rel).exists():
            fail(f"Missing required canonical file: {rel} ({desc})")


def check_canonical_unique(root: Path):
    params = find_all(root, 'params.json')
    allowed = (root / 'cad' / 'params' / 'params.json').resolve()
    dupes = [p for p in params if p.resolve() != allowed]
    if not allowed.exists():
        fail('Missing canonical cad/params/params.json')
    if dupes:
        fail('Found duplicate params.json outside cad/params/:
' + '
'.join(str(p) for p in dupes))


def check_run_folder_names(root: Path):
    raw = root / 'tests' / 'raw'
    if not raw.exists():
        return
    bad = []
    for child in raw.iterdir():
        if child.is_dir() and child.name not in ('.gitkeep',):
            if not RUN_FOLDER_RE.match(child.name):
                bad.append(child.name)
    if bad:
        fail('Bad tests/raw run folder names (expected YYYY-MM-DD_RunN_shortdesc):
' + '
'.join(bad))


def check_no_release_zips_in_sot(root: Path):
    zips = find_all(root, '*.zip')
    bad = [z for z in zips if 'archive' not in z.parts]
    if bad:
        fail('ZIP archives found outside archive/. Move them to Releases or Archive.
' + '
'.join(str(z) for z in bad))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.', help='Path to MicroHydroV1 SoT root')
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.exists():
        fail(f"Root does not exist: {root}")

    check_required_dirs(root)
    check_high_risk_present(root)
    check_canonical_unique(root)
    check_run_folder_names(root)
    check_no_release_zips_in_sot(root)

    print('[OK] MicroHydroV1 validation passed:', root)


if __name__ == '__main__':
    main()
