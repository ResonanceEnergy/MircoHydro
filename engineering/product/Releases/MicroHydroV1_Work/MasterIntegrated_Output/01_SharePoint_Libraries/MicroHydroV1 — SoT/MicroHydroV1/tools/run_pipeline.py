#!/usr/bin/env python3
"""MicroHydroV1 - One-command pipeline runner (v0.3.0).

Runs:
- validate_repo.py (optional)
- import_measurements.py (optional)
- make_release.py (optional)

FreeCAD macro run is optional and typically done in GUI:
  cad/macros/build_all.FCMacro
"""

from __future__ import annotations
import argparse
import subprocess
from pathlib import Path

def run(cmd: list[str]):
    print('[RUN]', ' '.join(cmd))
    subprocess.check_call(cmd)

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--version', required=True)
    ap.add_argument('--date', required=True)
    ap.add_argument('--validate', action='store_true')
    ap.add_argument('--import', dest='do_import', action='store_true')
    ap.add_argument('--release', dest='do_release', action='store_true')
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()

    if args.validate:
        v = root/'tools/validate/validate_repo.py'
        if v.exists():
            run(['python', str(v), '--root', str(root)])

    if args.do_import:
        imp = root/'automation/import_measurements.py'
        wb = root/'automation/MicroHydroV1_RnD_Export.xlsx'
        cfg = root/'automation/Import_Config.json'
        csvs = sorted(str(p) for p in (root/'tests/raw').rglob('*.csv'))
        if csvs and imp.exists():
            run(['python', str(imp), '--workbook', str(wb), '--config', str(cfg), '--csv', *csvs])
        else:
            print('[WARN] importer or CSVs missing')

    if args.do_release:
        mk = root/'tools/release/make_release.py'
        if mk.exists():
            run(['python', str(mk), '--root', str(root), '--version', args.version, '--date', args.date, '--out', str(root/'dist')])

    print('[DONE]')

if __name__ == '__main__':
    main()
