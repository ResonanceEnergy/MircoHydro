#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 scripts/render_handbooks_guarded.py
echo ""
echo "DONE (guarded render)."
read -n 1 -s -r -p "Press any key to close..."
echo ""
