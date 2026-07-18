# Internal Data & Dataset Audit

**Date:** 2026-07-18 · Sweep of every CSV/XLSX/data-bearing file in the repo for measured datasets relevant to ram/resonance/tuning work.

## Verdict: zero measured data exists anywhere in the repo. What exists is a complete, well-designed data ARCHITECTURE awaiting measurements.

| Asset | Contents | Status |
|---|---|---|
| `research/topics/MASTER_PRODUCTION_PACKAGE 2/08_Electrical_Control_Unit/ELC_Frequency_Response.xlsx` | 1×1 empty sheet | shell |
| `.../06_Penstock_Flow_Unit/PENSTOCK_FLOW_DATA.xlsx` | 1×1 empty | shell |
| `.../05_Tank_Hydraulics_Unit/TANK_Ripple_Model.xlsx` + `04_Hydram_Research_Unit/TANK_Ripple_Model.xlsx` | 1×1 empty | shells |
| `.../11_Bench_Test_Pack/*` (Jet_Coherence_Datasheet, Tank_Ripple_Datasheet, Bench_Test_Tracker, Results_Intake_Template) | headers/templates | schemas, no data |
| Gen 0 `tests/raw/T-001..T-004` CSVs | 2 synthetic example rows each | schemas, no data |
| `StageB_DataLog_Synthetic.csv` (CAD archive) | 6 rows, explicitly synthetic; operator "Nathan" | **valuable schema**: Vane_Angle × Swirl_Direction × Head × Q → ΔP — the founder's intended experiment design |
| PT_Calibration / DAQ_Logger_Config templates | blank | calibration program scaffolding |
| Everything else (audit CSVs, inventories, manifests) | repo metadata, not physics | n/a |

## Actions taken / queued
1. The **StageB schema is adopted** as the standard sweep-output format: the MOC simulator's parameter sweeps will emit rows in the founder's own schema (extended with eta, freq, T-001/T-002 metrics), unifying decision D-4 — the digital bench populates the very workbooks Gen 0 built. *(Queued: emitter function in `ram_moc_sim.py`.)*
2. The empty xlsx shells stay as-is until real data exists (no synthetic filler — canon).
3. External datasets identified for import when needed: Lansford & Dugan 1941 tables (open access), Johanis stroke×weight grid, Watt's test tables — for sim validation curves (queued with model v2 correlation work).
