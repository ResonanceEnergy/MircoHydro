#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import json

TEMPLATES = [
    ('docs/templates/T002_TankRipple_TimeSeries_Template.csv', 'T002_TankRipple_timeseries_TEMPLATE.csv'),
    ('docs/templates/T003_ELC_Frequency_TimeSeries_Template.csv', 'T003_ELC_timeseries_TEMPLATE.csv'),
]

def safe(s: str) -> str:
    return ''.join(ch if ch.isalnum() or ch in ('-','_') else '_' for ch in s).strip('_')

def main(argv=None):
    ap = argparse.ArgumentParser(description='Create a new run folder with standard naming + templates.')
    ap.add_argument('--root', default='.')
    ap.add_argument('--run-date', required=True, help='YYYY-MM-DD')
    ap.add_argument('--run-num', required=True, type=int)
    ap.add_argument('--desc', default='')
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    desc = safe(args.desc) if args.desc else ''
    run_id = f"{args.run_date}_Run{args.run_num}" + (f"_{desc}" if desc else '')

    raw = root/'tests'/'raw'/run_id
    raw.mkdir(parents=True, exist_ok=True)

    docs_run = root/'docs'/f"run{args.run_num}"
    docs_run.mkdir(parents=True, exist_ok=True)

    for src_rel, dst_name in TEMPLATES:
        src = root/src_rel
        if src.exists():
            shutil.copy2(src, raw/dst_name)

    meta = {
        'run_id': run_id,
        'run_date': args.run_date,
        'run_num': args.run_num,
        'desc': args.desc,
        'raw_folder': str(raw.relative_to(root).as_posix()),
        'required': ['T002_TankRipple_timeseries.csv'],
    }
    (raw/'RUN_META.json').write_text(json.dumps(meta, indent=2) + '\n', encoding='utf-8')

    print('Created:', raw)
    print('Next: place your raw CSVs in the folder, then run:')
    print(f"  python3 scripts/run_one_command.py --root . --run-id {run_id}")

if __name__ == '__main__':
    main()
