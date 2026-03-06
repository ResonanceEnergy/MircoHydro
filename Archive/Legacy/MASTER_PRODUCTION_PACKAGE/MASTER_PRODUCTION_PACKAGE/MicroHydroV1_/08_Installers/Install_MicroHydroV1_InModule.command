#!/bin/bash
set -e

APP_MOD_PATH="/Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1"

echo "[MicroHydroV1 In-Module Installer]"
echo "This will copy QA/Drawings/CFD into: $APP_MOD_PATH"

echo "\nSelect your MicroHydroV1 SDK root (folder that contains QA, Drawings, CFD):"
SRC_DIR=$(osascript -e 'tell app "System Events" to POSIX path of (choose folder with prompt "Choose MicroHydroV1 SDK root (with QA/Drawings/CFD)")')

if [ ! -d "$SRC_DIR" ]; then
  echo "[ERROR] Invalid folder selected."; exit 1
fi

# Ensure destination
if [ ! -d "$APP_MOD_PATH" ]; then
  echo "Creating module directory: $APP_MOD_PATH"
  sudo mkdir -p "$APP_MOD_PATH"
fi

# Create in-module resource folders
for d in QA Drawings CFD; do
  if [ ! -d "$APP_MOD_PATH/$d" ]; then
    echo "Creating $APP_MOD_PATH/$d"
    sudo mkdir -p "$APP_MOD_PATH/$d"
  fi
  if [ -d "$SRC_DIR/$d" ]; then
    echo "Copying $d ..."
    sudo rsync -a "$SRC_DIR/$d/" "$APP_MOD_PATH/$d/"
  else
    echo "[WARN] $d not found in selected source; creating empty folder."
  fi
done

# Install InitGui.py
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "Installing InitGui.py ..."
sudo cp "$SCRIPT_DIR/InitGui.py" "$APP_MOD_PATH/InitGui.py"
sudo chmod 644 "$APP_MOD_PATH/InitGui.py"

echo "\n[OK] Installation complete."
echo "Restart FreeCAD and look for [MHV1][SELF-TEST] lines showing OK for QA/Drawings/CFD."
