#!/bin/bash
# Resonance: one-click incremental backup launcher (Mac)
# Lives in a separate Tools folder. Reads project root from: RESONANCE_PROJECT_ROOT.txt
# Runs backup engine in Tools folder: backup_resonance_incremental.py

set -e
TOOL_DIR="$(cd "$(dirname "$0")" && pwd)"
CFG_FILE="$TOOL_DIR/RESONANCE_PROJECT_ROOT.txt"
ENGINE="$TOOL_DIR/backup_resonance_incremental.py"

if [ ! -f "$CFG_FILE" ]; then
  echo "ERROR: Config file not found: $CFG_FILE"
  echo "Create it and put your project root path on the last line."
  read -p "Press RETURN to close..."
  exit 1
fi

# Read the last non-empty, non-comment line
PROJECT_ROOT=$(grep -v '^#' "$CFG_FILE" | sed '/^\s*$/d' | tail -n 1)

if [ -z "$PROJECT_ROOT" ] || [ "$PROJECT_ROOT" = "/PASTE/YOUR/PROJECT/ROOT/HERE" ]; then
  echo "ERROR: Project root not set in $CFG_FILE"
  echo "Open the file and paste the FULL path to your project root folder on the last line."
  read -p "Press RETURN to close..."
  exit 1
fi

if [ ! -d "$PROJECT_ROOT" ]; then
  echo "ERROR: Project root folder does not exist: $PROJECT_ROOT"
  echo "Fix the path in $CFG_FILE"
  read -p "Press RETURN to close..."
  exit 1
fi

if [ ! -f "$ENGINE" ]; then
  echo "ERROR: Backup engine not found in Tools folder: $ENGINE"
  echo "Make sure backup_resonance_incremental.py is in the SAME folder as this .command file."
  read -p "Press RETURN to close..."
  exit 1
fi

echo "Tools folder : $TOOL_DIR"
echo "Project root : $PROJECT_ROOT"
echo "Engine       : $ENGINE"
echo ""

echo "Running incremental backup --repack ..."
cd "$PROJECT_ROOT"
python3 "$ENGINE" --repack

echo ""
echo "DONE. Backup files were written inside your project root:" 
echo "  - resonance_backup_incremental.zip"
echo "  - resonance_backup_manifest.json"
echo ""
read -p "Press RETURN to close..."
