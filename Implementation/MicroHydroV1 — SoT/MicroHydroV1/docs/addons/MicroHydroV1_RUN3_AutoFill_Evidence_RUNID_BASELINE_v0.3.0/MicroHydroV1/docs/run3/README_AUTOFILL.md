# Auto-fill Evidence Doc (RUN-3) — Run_ID + Baseline Row Support

## What it does
- Computes T-002 resonance peakiness (max/median PSD in 0.2–20 Hz) from Time_s,Pressure_Pa
- Filters workbook Measurements to the requested Run_ID:
  - If Run_ID column exists (and you pass --run-id-column), it uses that.
  - Otherwise, it matches the Run_ID string inside Conditions/Notes (configurable).
- Pulls test values + pass/fail for T-001/T-003/T-004
- For T-002 ripple reduction:
  - Uses explicit baseline row if present (same Run_ID, and baseline indicated in Sensor/Conditions/Notes)
  - Otherwise uses Baseline_Value column
  - Computes reduction % and PASS/FAIL (<= 0.70 × baseline)
- Populates the Evidence Template DOCX and saves a populated DOCX

## Command
```bash
python tools/workflow/autofill_evidence_doc.py   --root .   --run-id 2026-01-22_RUN3   --t002 tests/raw/RUN3/T002_TankRipple_timeseries.csv   --workbook automation/MicroHydroV1_RnD_Export.xlsx   --out-doc docs/run3/RUN3_Evidence_2026-01-22_RUN3.docx   --out-plot tests/results/summary/T002_PSD_Peakiness.png
```

## If you add a Run_ID column later
```bash
python tools/workflow/autofill_evidence_doc.py --run-id-column Run_ID ...
```
