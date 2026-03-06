#!/usr/bin/env python3
"""MicroHydroV1 - Release packager with MANIFEST.json (v0.3.0)."""

from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path
import zipfile

DEFAULT_INCLUDE = ['docs','automation','cad/params','cad/macros','tests/raw','tests/results','tools']

def sha256_file(p: Path, chunk=1024*1024) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(chunk), b''):
            h.update(b)
    return h.hexdigest()

def iter_files(root: Path, rel: str):
    p = root/rel
    if p.is_file():
        yield p
    elif p.is_dir():
        for f in p.rglob('*'):
            if f.is_file() and f.name not in ('.DS_Store',):
                yield f

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--version', required=True)
    ap.add_argument('--date', required=True)
    ap.add_argument('--out', default='dist')
    ap.add_argument('--include', nargs='*', default=DEFAULT_INCLUDE)
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    out = Path(args.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    zip_name = out / f"MicroHydroV1_Release_{args.version}_{args.date}.zip"

    manifest = {'project':'MicroHydroV1','version':args.version,'date':args.date,'files':[]}
    files=[]
    for rel in args.include:
        for f in iter_files(root, rel):
            files.append(f)

    with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for f in sorted(files, key=lambda x: x.as_posix()):
            relpath = f.relative_to(root).as_posix()
            manifest['files'].append({'path': relpath, 'bytes': f.stat().st_size, 'sha256': sha256_file(f)})
            z.write(f, arcname=f'MicroHydroV1/{relpath}')
        z.writestr('MicroHydroV1/MANIFEST.json', json.dumps(manifest, indent=2))

    print('Created:', zip_name)

if __name__ == '__main__':
    main()
