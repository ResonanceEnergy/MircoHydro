#!/usr/bin/env python3
"""MicroHydroV1 - minimal validation gate (v0.3.0)."""

import argparse
from pathlib import Path

REQUIRED_DIRS = ['docs','automation','cad','tests','tools']

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    args = ap.parse_args(argv)
    root = Path(args.root)
    missing = [d for d in REQUIRED_DIRS if not (root/d).exists()]
    if missing:
        raise SystemExit('Missing required dirs: ' + ', '.join(missing))
    print('[OK] basic structure present')

if __name__ == '__main__':
    main()
