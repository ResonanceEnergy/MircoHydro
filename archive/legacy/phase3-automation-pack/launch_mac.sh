#!/bin/bash
# MicroHydroV1 Phase 3 Launcher (macOS)
# One-time:
#   chmod +x ./launch_mac.sh
# Optional (auto-open Releases after ZIP cut):
#   export MICROHYDRO_RELEASES_URL='https://<your-sharepoint-releases-library-url>'
# Usage:
#   ./launch_mac.sh YYYY-MM-DD_RunN[_Desc]
set -e
RUNID="$1"
if [ -z "$RUNID" ]; then
  echo "Usage: ./launch_mac.sh YYYY-MM-DD_RunN[_Desc]"
  exit 1
fi
python3 scripts/run_one_command.py --root . --run-id "$RUNID"
