#!/usr/bin/env bash
# Identical logic to .command; kept for Terminal use on CI/automation.
# See Install_MicroHydroV1.command for comments.
set -euo pipefail
OS_NAME=$(uname -s || true)
[[ "$OS_NAME" == "Darwin" ]] || { echo "macOS only"; exit 1; }
MOD_DIR="$HOME/Library/Application Support/FreeCAD/Mod"
TARGET="$MOD_DIR/MicroHydroV1"
APP_BUNDLE_MOD="/Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1"
APP_BUNDLE_MOD_DISABLED="/Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1_DISABLED"
SRC_INPUT="${1:-}"; SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
resolve(){ local p="$1"; if [[ -z "$p" ]]; then if [[ -d "$SCRIPT_DIR/MicroHydroV1" ]]; then echo "$SCRIPT_DIR/MicroHydroV1"; return; fi; if [[ -d "$HOME/Downloads/MicroHydroV1" ]]; then echo "$HOME/Downloads/MicroHydroV1"; return; fi; if ls "$HOME/Downloads"/MicroHydroV1*.zip >/dev/null 2>&1; then echo "ZIP:$HOME/Downloads/$(ls -1 "$HOME/Downloads"/MicroHydroV1*.zip | head -n1)"; return; fi; echo ""; return; fi; p="${p/#~\//${HOME}/}"; if [[ -f "$p" ]]; then case "$p" in *.zip|*.ZIP) echo "ZIP:$p";; *) echo "not a zip"; exit 2;; esac; elif [[ -d "$p" ]]; then echo "$p"; else echo "missing"; exit 2; fi; }
SPEC="$(resolve "$SRC_INPUT")"; [[ -n "$SPEC" ]] || { echo "no source"; exit 2; }
TMP=""; if [[ "$SPEC" == ZIP:* ]]; then Z="${SPEC#ZIP:}"; TMP=$(mktemp -d); unzip -q "$Z" -d "$TMP"; if [[ -d "$TMP/MicroHydroV1" ]]; then SRC="$TMP/MicroHydroV1"; else C=$(find "$TMP" -maxdepth 2 -type d -name MicroHydroV1 | head -n1 || true); [[ -n "$C" ]] || { echo "zip missing MicroHydroV1/"; exit 3; }; SRC="$C"; fi; else SRC="$SPEC"; fi
for s in icons macros QA Drawings CFD; do [[ -d "$SRC/$s" ]] || mkdir -p "$SRC/$s"; done
mkdir -p "$MOD_DIR"; if [[ -e "$TARGET" ]]; then mv "$TARGET" "$TARGET.bak.$(date +%Y%m%d-%H%M%S)"; fi
if command -v rsync >/dev/null 2>&1; then rsync -a "$SRC/" "$TARGET/"; else cp -R "$SRC" "$TARGET"; fi
if command -v matter >/dev/null 2>&1; then xattr -r -d com.apple.quarantine "$TARGET" >/dev/null 2>&1 || true; fi
if [[ -e "$APP_BUNDLE_MOD" ]]; then sudo mv "$APP_BUNDLE_MOD" "$APP_BUNDLE_MOD_DISABLED"; fi
echo "Installed to $TARGET"; for s in icons macros QA Drawings CFD; do [[ -d "$TARGET/$s" ]] && echo OK $s || echo MISSING $s; done

