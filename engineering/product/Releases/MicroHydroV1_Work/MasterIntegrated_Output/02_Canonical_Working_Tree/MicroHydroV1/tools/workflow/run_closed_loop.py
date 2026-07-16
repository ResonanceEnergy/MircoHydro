#!/usr/bin/env python3
"""MicroHydroV1 - Closed-loop automation (local workstation).

Locked-in resonance metric:
- T-002 PSD peakiness using Pressure_Pa and Time_s.

Flow:
1) Optimize -> cad/params/params_optimized.json
2) Run FreeCAD macro build_all.FCMacro (manual)
3) Import measurements
4) Cut Release ZIP
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

    ap.add_argument('--optimize', action='store_true')
    ap.add_argument('--resonance-csv', default=None)
    ap.add_argument('--import', dest='do_import', action='store_true')
    ap.add_argument('--release', dest='do_release', action='store_true')

    args = ap.parse_args(argv)
    root = Path(args.root).resolve()

    if args.optimize:
        run(['python', str(root/'tools/optimize/optimize_params.py'),
             '--params', str(root/'cad/params/params.json'),
             '--config', str(root/'tools/optimize/opt_config.json'),
             '--out', str(root/'cad/params/params_optimized.json'),
             '--resonance-csv', str(args.resonance_csv) if args.resonance_csv else ''
        ])
        print('
[NEXT] Run FreeCAD GUI macro: cad/macros/build_all.FCMacro')

    if args.do_import:
        imp = root/'automation/import_measurements.py'
        wb = root/'automation/MicroHydroV1_RnD_Export.xlsx'
        cfg = root/'automation/Import_Config.json'
        csvs = sorted(str(p) for p in (root/'tests/raw').rglob('*.csv'))
        if csvs and imp.exists():
            run(['python', str(imp), '--workbook', str(wb), '--config', str(cfg), '--csv', *csvs])

    if args.do_release:
        run(['python', str(root/'tools/release/make_release.py'), '--root', str(root), '--version', args.version, '--date', args.date, '--out', str(root/'dist')])

    print('[DONE]')

if __name__ == '__main__':
    main()
