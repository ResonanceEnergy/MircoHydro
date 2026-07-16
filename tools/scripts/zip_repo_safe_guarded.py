#!/usr/bin/env python3
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    rc = subprocess.run(["python3", "scripts/workspace_disk_guard.py", "--path", str(ROOT), "--threshold", "85"]).returncode
    if rc != 0:
        return rc
    return subprocess.run(["python3", "scripts/zip_repo_safe.py"], cwd=str(ROOT)).returncode

if __name__ == "__main__":
    raise SystemExit(main())
