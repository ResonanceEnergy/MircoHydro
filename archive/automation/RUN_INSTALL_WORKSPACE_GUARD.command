#!/bin/bash
set -e
cd "$(dirname "$0")"

mkdir -p scripts

#############################################
# 1) Workspace disk guard (fail-fast)
#############################################
cat > scripts/workspace_disk_guard.py <<'PY'
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
PY
chmod +x scripts/workspace_disk_guard.py

#############################################
# 2) Guarded wrappers (no edits to originals)
#############################################
cat > scripts/render_handbooks_guarded.py <<'PY'
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
    return subprocess.run(["python3", "scripts/render_handbooks.py"], cwd=str(ROOT)).returncode

if __name__ == "__main__":
    raise SystemExit(main())
PY
chmod +x scripts/render_handbooks_guarded.py

cat > scripts/zip_repo_safe_guarded.py <<'PY'
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
PY
chmod +x scripts/zip_repo_safe_guarded.py

cat > scripts/build_all_guarded.py <<'PY'
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
PY
chmod +x scripts/build_all_guarded.py

#############################################
# 3) One-click guarded runners
#############################################
cat > RUN_BUILD_ALL_GUARDED.command <<'SH2'
#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 scripts/build_all_guarded.py
echo ""
echo "DONE (guarded)."
read -n 1 -s -r -p "Press any key to close..."
echo ""
SH2
chmod +x RUN_BUILD_ALL_GUARDED.command

cat > RUN_RENDER_GUARDED.command <<'SH3'
#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 scripts/render_handbooks_guarded.py
echo ""
echo "DONE (guarded render)."
read -n 1 -s -r -p "Press any key to close..."
echo ""
SH3
chmod +x RUN_RENDER_GUARDED.command

echo "✅ Workspace Disk Guard installed."
echo "✅ Use: RUN_BUILD_ALL_GUARDED.command (double click)"
echo "✅ Or: RUN_RENDER_GUARDED.command (double click)"
