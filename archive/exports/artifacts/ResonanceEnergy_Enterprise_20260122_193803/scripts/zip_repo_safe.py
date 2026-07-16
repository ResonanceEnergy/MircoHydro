#!/usr/bin/env python3
"""
Safe zipper for the repo:
- Run from repo root
- Avoids ZIP pre-1980 timestamp errors by clamping to 1980-01-01
- Skips .zip files and common junk folders

Run:
  python3 scripts/zip_repo_safe.py
"""
from pathlib import Path
import zipfile
import datetime

REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = REPO_ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

MIN_DT = (1980, 1, 1, 0, 0, 0)
EXCLUDE_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "dist", "build"}

def should_skip(p: Path) -> bool:
    parts = set(p.parts)
    if any(d in parts for d in EXCLUDE_DIRS):
        return True
    if p.suffix.lower() == ".zip":
        return True
    return False

def add_file(z: zipfile.ZipFile, file_path: Path, arcname: str):
    st = file_path.stat()
    dt = datetime.datetime.fromtimestamp(st.st_mtime).timetuple()[:6]
    if dt < MIN_DT:
        dt = MIN_DT
    zi = zipfile.ZipInfo(arcname)
    zi.date_time = dt
    zi.compress_type = zipfile.ZIP_DEFLATED
    with open(file_path, "rb") as f:
        z.writestr(zi, f.read())

def main():
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = ARTIFACTS / f"ResonanceEnergy_Enterprise_{stamp}.zip"
    with zipfile.ZipFile(out, "w") as z:
        for p in REPO_ROOT.rglob("*"):
            if not p.is_file():
                continue
            if should_skip(p):
                continue
            arc = p.relative_to(REPO_ROOT).as_posix()
            add_file(z, p, arc)
    print(f"Created: {out}")

if __name__ == "__main__":
    main()
