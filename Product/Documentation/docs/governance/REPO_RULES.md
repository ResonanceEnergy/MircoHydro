# Repo Governance Rules

## 1) Source of Truth
- `main` branch = latest validated, releasable state.
- `dev` branch = integration/staging.
- `feature/*` branches = isolated work.

## 2) Naming conventions
- Test runs: `tests/raw/YYYY-MM-DD_RunN_<shortdesc>/`
- Plots: `tests/results/summary/<TestID>_<metric>.png`
- Drawings: `tests/results/drawings/<Part>_<rev>.pdf`

## 3) Excel policy
- Commit **templates/schemas** only.
- Store run data as CSVs under `tests/raw/`.
- Generate release snapshots of Excel outputs (zip) via `tools/release/`.

## 4) CAD policy
- Single canonical `cad/params/params.json`.
- FreeCAD macros live in `cad/macros/`.
- Exported STEP/STL go to `cad/exports/` (ignored by git).

## 5) Release policy
- Releases are produced by `tools/release/make_release.py`.
- Releases are tagged `vX.Y.Z` and uploaded (SharePoint/GitHub Releases).
