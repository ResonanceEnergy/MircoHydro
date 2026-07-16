# MicroHydro / Resonance Energy

Modular low-head micro-hydro power systems — crossflow turbine + PMSG with solar/wind/battery hybrid integration, targeting irrigation canals and off-grid sites (5–50 kW class).

**Project status (honest baseline, July 2026):** concept/paper stage. No prototype has been built or tested yet. The credible engineering baseline is **~33% system efficiency as-designed, with a realistic optimization path to ~48.5%** (see `engineering/specs/HYBRID_SYSTEM_MASTER_SPEC.md` "Reality Check" and `EFFICIENCY_OPTIMIZATION_PLAN_65PCT.md`). Any higher figures found in archived documents are unvalidated — see `ASSESSMENT.md`.

## Repository layout

| Path | Contents |
|---|---|
| `ASSESSMENT.md` | Full independent assessment of the project and this repo (July 2026) |
| `docs/strategy/` | Business strategy: GIGA enterprise blueprint, ethics/values/brand, execution plans, pivots |
| `docs/market/` | Site scouting & market analysis: Alberta workflow, 175-location continental analysis, global top-10 sites, Uruguay/Paraguay |
| `docs/business/` | Division charters, funding strategy, IP/patent strategy, partnerships, governance |
| `docs/reports/` | Historical audits, consolidation reports, and completion reports (treat claims with caution — see ASSESSMENT.md) |
| `engineering/` | Specs, CAD (FreeCAD parametric macros + DXF), test protocols, MicroHydroV1 source-of-truth tree — see `engineering/README.md` |
| `research/` | Visionary research corpus (160 visionaries / insights database), references, reference-library shells |
| `tools/` | Working utilities: backfill/consolidation scripts, backup engine, Groq-based drafting agents |
| `speculative/` | **Quarantined unvalidated-science material** (φ/golden-ratio claims, water structuring, RWR module) — read `speculative/README.md` before using anything here externally |
| `archive/` | Legacy trees (deduplicated), automation scripts whose outputs were fabricated, old exports. `archive/DEDUP_MANIFEST.csv` lists every duplicate removed |
| `MISSING_CONTENT_MANIFEST.csv` | Files still empty after recovery — awaiting content from the original OneDrive source |

## Provenance of this structure

This tree was consolidated on 2026-07-16 from the original workspace (2,972 files, 53% empty from a failed OneDrive migration, ~10× duplication):

- 805 empty files were restored from in-repo copies and zip archives
- 1,927 byte-identical duplicates were removed (logged in `archive/DEDUP_MANIFEST.csv`)
- 366 files remain empty pending the original OneDrive source (`MISSING_CONTENT_MANIFEST.csv`)
- Nothing was deleted: everything is either in its canonical location or under `archive/`

## Next steps (from ASSESSMENT.md)

1. Backfill remaining empty files from OneDrive
2. Run `engineering/protocols/.../PROTOCOL_001` — the desktop turbine A/B bench test (~$300, well-designed, never executed) — to produce the project's first real measurement
3. Rebuild the CAD at one chosen scale with a real crossflow runner profile
4. Fill the Alberta site-scouting CSV with 10 real candidate sites using the documented workflow
5. Keep all external-facing claims anchored to the 33% → 48.5% engineering baseline
