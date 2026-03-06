#!/usr/bin/env python3
"""MicroHydroV1 - Auto-embed optimized params into canonical params.json.

1) Run optimizer -> cad/params/params_optimized.json
2) Embed into canonical params.json with a change note:
   python tools/cad/apply_optimized_params.py --root . --note "v0.3.0: optimized for T-002 PSD peakiness (Pressure_Pa @100Hz)"

Safety:
- Creates a timestamped backup of the current params.json.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import datetime as dt


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.', help='MicroHydroV1 root')
    ap.add_argument('--note', required=True, help='Change note to stamp into Meta')
    ap.add_argument('--force', action='store_true', help='Allow embedding even if params_optimized.json missing')
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    params = root/'cad/params/params.json'
    opt = root/'cad/params/params_optimized.json'

    if not params.exists():
        raise SystemExit('Missing canonical params.json: ' + str(params))
    if not opt.exists() and not args.force:
        raise SystemExit('Missing params_optimized.json: ' + str(opt))

    ts = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup = params.with_name(f'params_BACKUP_{ts}.json')
    backup.write_text(params.read_text(encoding='utf-8'), encoding='utf-8')

    base_obj = json.loads(params.read_text(encoding='utf-8'))
    new_obj = json.loads(opt.read_text(encoding='utf-8')) if opt.exists() else base_obj

    meta = dict(base_obj.get('Meta', {}))
    meta['Version'] = meta.get('Version', 'v0.3.0')
    meta['ChangeNote'] = args.note
    meta['ChangeNoteTime'] = dt.datetime.now().isoformat(timespec='seconds')
    new_obj['Meta'] = meta

    params.write_text(json.dumps(new_obj, indent=2) + '
', encoding='utf-8')

    print('[OK] Embedded optimized params into:', params)
    print('[OK] Backup saved at:', backup)


if __name__ == '__main__':
    main()
