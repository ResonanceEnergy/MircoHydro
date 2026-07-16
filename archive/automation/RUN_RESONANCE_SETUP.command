#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 scripts/one_click_bootstrap.py --force
echo "BOOTSTRAP COMPLETE."
read -n 1 -s -r -p "Press any key to close..."
echo ""
