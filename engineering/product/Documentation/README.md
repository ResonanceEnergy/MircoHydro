# MicroHydroV1 — Repository (Source of Truth)

This repository is the **canonical source** for MicroHydroV1 engineering assets:
- **Docs** (master narrative, procedures, reports)
- **Automation** (data import + validation scripts)
- **CAD** (FreeCAD macros + parameter sets)
- **Tests** (run folders, results, plots, drawings)

## Quick start
1. Put new raw data CSVs into `tests/raw/<YYYY-MM-DD_RunN>/`.
2. Run the importer in `automation/` to append into the canonical workbook (template lives under `docs/templates/`).
3. Run CAD generation macros using the `cad/params/params.json` parameters.
4. Create a release bundle using `tools/release/make_release.py`.

## Canonical rules
- **One** canonical `params.json` in `cad/params/`.
- **One** canonical importer script in `automation/`.
- **Never edit inside ZIPs**; all edits happen in this repo.

See `docs/governance/REPO_RULES.md` for governance + naming conventions.
