
#!/bin/zsh
set -euo pipefail

# MicroHydroV1 - One-Click Pipeline (macOS)
# 1) Import intake_raw CSVs into RnD workbook
# 2) Compute metrics and save plots
# 3) Update Go/No-Go packet and STW matrix
# 4) Build enterprise repository (copy mode)

DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_ROOT="${DIR}"
DEST_ROOT="${DIR}/MicroHydroV1_ENTERPRISE"

if [[ $# -ge 1 ]]; then SRC_ROOT="$1"; fi
if [[ $# -ge 2 ]]; then DEST_ROOT="$2"; fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "[ERROR] python3 not found." >&2
  exit 1
fi

python3 "$DIR/mhv1_pipeline.py" --source "$SRC_ROOT" --dest "$DEST_ROOT"

if [[ -d "$DEST_ROOT" ]]; then
  open "$DEST_ROOT"
fi

echo "[OK] One-Click Pipeline completed: $DEST_ROOT"
