#!/usr/bin/env python3
"""
Guarded Build-All:
- checks workspace disk usage first (fail-fast at 85%)
- then runs the existing build_all pipeline (or falls back to your original build_all.py)
"""
from __future__ import annotations
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(cmd: list[str]) -> int:
    return subprocess.run(cmd, cwd=str(ROOT)).returncode

def main() -> int:
    # guard at start
    rc = run(["python3", "scripts/workspace_disk_guard.py", "--path", str(ROOT), "--threshold", "85"])
    if rc != 0:
        return rc

    # If you have scripts/build_all.py already, use it.
    # Otherwise, fall back to running the usual sequence.
    if (ROOT / "scripts" / "build_all.py").exists():
        rc = run(["python3", "scripts/build_all.py"])
        return rc

    # Fallback sequence if build_all.py isn't present
    rc = run(["python3", "scripts/automate_handbooks.py", "--report", "artifacts/handbook_automation_report.md"])
    if rc != 0: return rc

    rc = run(["python3", "scripts/preflight_handbooks.py", "--report", "artifacts/preflight_report.md"])
    if rc != 0: return rc

    # guard again before heavy steps
    rc = run(["python3", "scripts/workspace_disk_guard.py", "--path", str(ROOT), "--threshold", "85"])
    if rc != 0: return rc

    rc = run(["python3", "scripts/render_handbooks_guarded.py"])
    if rc != 0: return rc

    rc = run(["python3", "scripts/zip_repo_safe_guarded.py"])
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
