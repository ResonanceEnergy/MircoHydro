#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 scripts/build_all.py
echo "BUILD-ALL COMPLETE."
read -n 1 -s -r -p "Press any key to close..."
echo ""
