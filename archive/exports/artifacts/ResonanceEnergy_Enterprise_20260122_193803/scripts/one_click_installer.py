import os, sys, zipfile, datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def zip_project(out_path: Path, root: Path):
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in root.rglob('*'):
            if p.is_file():
                rel = p.relative_to(root)
                # skip existing zips inside artifacts
                if rel.suffix.lower() == '.zip':
                    continue
                z.write(p, rel.as_posix())

def main():
    artifacts = PROJECT_ROOT / 'artifacts'
    artifacts.mkdir(exist_ok=True)
    stamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    out = artifacts / f"ResonanceEnergy_Enterprise_{stamp}.zip"
    zip_project(out, PROJECT_ROOT)
    print(f"Created: {out}")

if __name__ == '__main__':
    main()
