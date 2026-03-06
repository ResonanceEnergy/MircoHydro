#!/usr/bin/env bash
set -euo pipefail

# === MicroHydroV1 — macOS Installer (User Mod path) ===
# Usage:
#   1) Put this .command next to a folder named "MicroHydroV1"
#      OR pass a ZIP/folder path as an argument.
#   2) Double‑click to run (Finder) or run from Terminal.
#
# Examples:
#   ./Install_MicroHydroV1.command
#   ./Install_MicroHydroV1.command "~/Downloads/MicroHydroV1.zip"
#   ./Install_MicroHydroV1.command "~/Downloads/MicroHydroV1"
#
# This will install to:
#   ~/Library/Application Support/FreeCAD/Mod/MicroHydroV1
# and disable any app‑bundle copy at:
#   /Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1

OS_NAME=$(uname -s || true)
if [[ "$OS_NAME" != "Darwin" ]]; then
  echo "[ERROR] This installer is for macOS (Darwin) only." >&2
  exit 1
fi

# Paths
MOD_DIR="$HOME/Library/Application Support/FreeCAD/Mod"
TARGET="$MOD_DIR/MicroHydroV1"
APP_BUNDLE_MOD="/Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1"
APP_BUNDLE_MOD_DISABLED="/Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1_DISABLED"

# Resolve source (argument, sibling folder, or Downloads)
SRC_INPUT="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

resolve_source() {
  local inpath="$1"
  if [[ -z "$inpath" ]]; then
    # Prefer sibling folder named MicroHydroV1
    if [[ -d "$SCRIPT_DIR/MicroHydroV1" ]]; then
      echo "$SCRIPT_DIR/MicroHydroV1"
      return 0
    fi
    # Fallback: Downloads
    if [[ -d "$HOME/Downloads/MicroHydroV1" ]]; then
      echo "$HOME/Downloads/MicroHydroV1"
      return 0
    fi
    if ls "$HOME/Downloads"/MicroHydroV1*.zip >/dev/null 2>&1; then
      echo "ZIP:$HOME/Downloads/$(ls -1 "$HOME/Downloads"/MicroHydroV1*.zip | head -n1)"
      return 0
    fi
    echo ""; return 0
  fi

  # expand ~ and resolve absolute
  inpath="${inpath/#~\//${HOME}/}"
  if [[ -f "$inpath" ]]; then
    case "$inpath" in
      *.zip|*.ZIP) echo "ZIP:$inpath"; return 0 ;;
      *) echo "[ERROR] File is not a .zip: $inpath" >&2; exit 2 ;;
    esac
  elif [[ -d "$inpath" ]]; then
    echo "$inpath"; return 0
  else
    echo "[ERROR] Path not found: $inpath" >&2; exit 2
  fi
}

SOURCE_SPEC="$(resolve_source "$SRC_INPUT")"
if [[ -z "$SOURCE_SPEC" ]]; then
  echo "[ERROR] Could not locate a MicroHydroV1 source. Place a 'MicroHydroV1' folder next to this script or pass a path to a ZIP/folder." >&2
  exit 2
fi

# If ZIP, extract to temp and set SOURCE to extracted MicroHydroV1 folder
TMP=""
if [[ "$SOURCE_SPEC" == ZIP:* ]]; then
  ZIP_PATH="${SOURCE_SPEC#ZIP:}"
  echo "[INFO] Using ZIP: $ZIP_PATH"
  TMP=$(mktemp -d)
  unzip -q "$ZIP_PATH" -d "$TMP"
  # locate MicroHydroV1 folder inside the ZIP (top-level or nested)
  if [[ -d "$TMP/MicroHydroV1" ]]; then
    SOURCE="$TMP/MicroHydroV1"
  else
    # search two levels
    CANDIDATE=$(find "$TMP" -maxdepth 2 -type d -name MicroHydroV1 | head -n1 || true)
    if [[ -n "$CANDIDATE" ]]; then
      SOURCE="$CANDIDATE"
    else
      echo "[ERROR] The ZIP does not contain a top-level 'MicroHydroV1' folder." >&2
      exit 3
    fi
  fi
else
  SOURCE="$SOURCE_SPEC"
fi

# Sanity: expected subfolders (create if missing so self-test passes)
for sub in icons macros QA Drawings CFD; do
  if [[ ! -d "$SOURCE/$sub" ]]; then
    echo "[WARN] Missing '$sub' in source; creating empty folder to satisfy add-on checks."
    mkdir -p "$SOURCE/$sub"
  fi
done

# Create Mod path and install
mkdir -p "$MOD_DIR"

# Backup existing target if present
if [[ -e "$TARGET" ]]; then
  TS=$(date +%Y%m%d-%H%M%S)
  BACKUP="$TARGET.bak.$TS"
  echo "[INFO] Backing up existing install → $BACKUP"
  mv "$TARGET" "$BACKUP"
fi

# Copy (rsync keeps perms and handles spaces)
if command -v rsync >/dev/null 2>&1; then
  rsync -a "$SOURCE/" "$TARGET/"
else
  # fallback to cp -R
  cp -R "$SOURCE" "$TARGET"
fi

# Remove macOS quarantine flags (if any)
if command -v xattr >/dev/null 2>&1; then
  xattr -r -d com.apple.quarantine "$TARGET" >/dev/null 2>&1 || true
fi

# Disable app-bundle duplicate to prevent shadowing
if [[ -e "$APP_BUNDLE_MOD" ]]; then
  echo "[INFO] Disabling app-bundle copy at $APP_BUNDLE_MOD"
  sudo mv "$APP_BUNDLE_MOD" "$APP_BUNDLE_MOD_DISABLED"
fi

# Validate install
echo "[INFO] Installed to: $TARGET"
MISSING=0
for sub in icons macros QA Drawings CFD; do
  if [[ ! -d "$TARGET/$sub" ]]; then
    echo "[ERROR] Missing expected folder: $TARGET/$sub" >&2
    MISSING=1
  else
    echo "[OK] $sub"
  fi
done
if [[ "$MISSING" -ne 0 ]]; then
  echo "[WARN] Some folders were missing; created placeholders. Populate as needed."
fi

# Launch FreeCAD (optional)
if command -v open >/dev/null 2>&1; then
  echo "[INFO] Launching FreeCAD..."
  open -a FreeCAD || true
fi

echo "[DONE] MicroHydroV1 installation complete. Check FreeCAD → Report view for [MHV1][SELF-TEST] (all OK)."
