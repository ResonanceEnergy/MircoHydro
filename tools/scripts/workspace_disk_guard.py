#!/usr/bin/env python3
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

def disk_used_pct(path: Path) -> tuple[float, float, float]:
    u = shutil.disk_usage(str(path))
    total = u.total / (1024**3)
    free = u.free / (1024**3)
    used = (u.total - u.free) / (1024**3)
    pct = 100.0 * used / total if total else 0.0
    return pct, total, free

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=".", help="Path inside workspace to check (default: .)")
    ap.add_argument("--threshold", type=float, default=85.0, help="Fail if used %% >= threshold (default: 85)")
    args = ap.parse_args()

    p = Path(args.path).resolve()
    pct, total, free = disk_used_pct(p)

    if pct >= args.threshold:
        print("!" * 88)
        print(f"WORKSPACE DISK GUARD TRIPPED: {pct:.1f}% used (threshold={args.threshold:.1f}%)")
        print(f"Workspace path: {p}")
        print(f"Disk total: {total:.1f} GB | Free: {free:.1f} GB")
        print("ACTION: Move/clean files or switch workspace volume before rendering/zip/export.")
        print("STOPPING to prevent partial outputs / disk-full crashes.")
        print("!" * 88)
        return 2

    print(f"Workspace disk OK: {pct:.1f}% used (< {args.threshold:.1f}%). Free={free:.1f} GB")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
