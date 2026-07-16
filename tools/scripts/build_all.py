#!/usr/bin/env python3
"""
BUILD-ALL — FULL PIPELINE

Steps:
1) Run upgraded bootstrap
2) Enforce handbook structure
3) Preflight validate (fail fast)
4) Ensure ReportLab installed
5) Render PDFs
6) Safe ZIP archive
"""

from __future__ import annotations
import subprocess, datetime, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT/"artifacts"
ART.mkdir(exist_ok=True)

def run(cmd):
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    print(">>> RUN:", " ".join(cmd))
    print(p.stdout)
    print(p.stderr)
    return p.returncode

def ensure_reportlab():
    try:
        import reportlab
        return True
    except Exception:
        pass
    return run([sys.executable, "-m", "pip", "install", "--user", "reportlab"]) == 0

def main():
    print("# BUILD-ALL START")

    # 1) bootstrap
    run(["python3", "scripts/one_click_bootstrap.py", "--force"])

    # 2) automate
    run(["python3", "scripts/automate_handbooks.py", "--report", "artifacts/handbook_automation_report.md"])

    # 3) preflight
    rc = run(["python3", "scripts/preflight_handbooks.py", "--report", "artifacts/preflight_report.md"])
    if rc != 0:
        print("STOP — Preflight failed.")
        return

    # 4) reportlab
    if not ensure_reportlab():
        print("STOP — ReportLab install failed.")
        return

    # 5) render
    run(["python3", "scripts/render_handbooks.py"])

    # 6) zip
    run(["python3", "scripts/zip_repo_safe.py"])

    (ART/"build_all_report.md").write_text(f"Build-All Completed — {datetime.datetime.now()}\n", encoding="utf-8")
    print("BUILD-ALL COMPLETE.")

if __name__ == "__main__":
    main()
