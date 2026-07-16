# MicroHydroV1 — RUN‑3 Evidence Summary (Template)

## 1. Run identity
- **Run ID:** YYYY‑MM‑DD_RUN3
- **Operator:** Nathan
- **Location:** ________
- **Date/time:** ________

## 2. Configuration (link to params)
- **Params file:** `cad/params/params.json` (or `params_optimized.json` if used)
- **Change note:** __________________________________________

## 3. Test results (summary)
| Test | Metric | Requirement | Result | Pass/Fail | Evidence link |
|---|---:|---:|---:|---|---|
| T‑001 | Coherence | ≥ 0.90 | ____ | ____ | tests/results/summary/T001_*.png |
| T‑002 | Ripple | ≤ 0.70×baseline | ____ | ____ | tests/results/summary/T002_*.png |
| T‑002 | Resonance peakiness | minimize | ____ | n/a | tests/results/summary/T002_PSD_Peakiness.png |
| T‑003 | ELC drift | ≤ 0.1 Hz | ____ | ____ | tests/results/summary/T003_*.png |
| T‑004 | Power | 10–12 kW | ____ | ____ | tests/results/summary/T004_*.png |

## 4. Resonance metric details (T‑002)
- **Sampling:** 100 Hz
- **Signal:** Pressure_Pa
- **Band:** 0.2–20 Hz
- **Peakiness definition:** max(PSD)/median(PSD)
- **Observed dominant peak (Hz):** ____

## 5. Artifacts checklist
- [ ] Raw CSVs saved under `tests/raw/RUN3/`
- [ ] Optimized params saved (if applicable)
- [ ] CAD exports in `cad/exports/` (STEP/STL)
- [ ] Workbook updated `automation/MicroHydroV1_RnD_Export.xlsx`
- [ ] Evidence plots exported under `tests/results/summary/`
- [ ] Release ZIP created and uploaded to Releases

## 6. Notes / anomalies
- __________________________________________
