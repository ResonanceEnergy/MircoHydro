#!/usr/bin/env python3
import os, json, hashlib, time, socket, zipfile
from pathlib import Path
import argparse, shutil

def hash_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for chunk in iter(lambda:f.read(8192),b''): h.update(chunk)
    return h.hexdigest()

def load_manifest(p):
    return json.loads(p.read_text()) if p.exists() else {}

def save_manifest(p,data): p.write_text(json.dumps(data,indent=2))

parser=argparse.ArgumentParser()
parser.add_argument('--mode',required=True)
parser.add_argument('--hash',action='store_true')
args=parser.parse_args()

config=json.load(open(Path(__file__).parent/'backup_config.json'))
proj=Path(config['project_root']).expanduser()
manfile=proj/'backup_manifest.json'
man=load_manifest(manfile)
now=time.strftime('%Y%m%d_%H%M%S')
inc_zip=proj/f'incremental_{now}.zip'
full_dir=proj/'_BACKUPS'; full_dir.mkdir(exist_ok=True)
toupload=full_dir/'_TO_UPLOAD'; toupload.mkdir(exist_ok=True)
full_zip=full_dir/f'ResonanceEnergy_backup_v{now}.zip'

changed=[]
for p in proj.rglob('*'):
    if p.is_file():
        rel=p.relative_to(proj).as_posix()
        st=p.stat(); size=st.st_size; mt=int(st.st_mtime)
        entry=man.get(rel)
        if not entry or entry['size']!=size or entry['mtime']!=mt:
            if args.hash and entry and entry.get('hash')==hash_file(p):
                continue
            changed.append(rel)
            man[rel]={'size':size,'mtime':mt}
            if args.hash:
                man[rel]['hash']=hash_file(p)

if args.mode!='dry':
    with zipfile.ZipFile(inc_zip,'w',zipfile.ZIP_DEFLATED) as z:
        for rel in changed:
            z.write(proj/rel, rel)
    # full backup
    with zipfile.ZipFile(full_zip,'w',zipfile.ZIP_DEFLATED) as z:
        for p in proj.rglob('*'):
            if p.is_file(): z.write(p,p.relative_to(proj).as_posix())
        z.writestr(
    "VERSION.txt",
    f"""version: {now}
project_root: {proj}
"""
)

timestamp: {now}
machine: {socket.gethostname()}
project_root: {proj}')
    shutil.copy2(full_zip, toupload/full_zip.name)
    save_manifest(manfile,man)

print('Done. Changed:', changed)
