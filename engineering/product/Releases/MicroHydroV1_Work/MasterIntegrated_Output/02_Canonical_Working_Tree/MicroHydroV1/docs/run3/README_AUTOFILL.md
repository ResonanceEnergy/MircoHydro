# Auto-fill Evidence Doc (RUN-3)

## What it does
- Computes T-002 resonance peakiness (max/median PSD in 0.2–20 Hz)
- Computes dominant frequency in that band
- Pulls latest T-001/T-002/T-003/T-004 value + pass/fail from automation/MicroHydroV1_RnD_Export.xlsx (Measurements sheet)
- For T-002: also pulls Baseline_Value and computes reduction % and PASS/FAIL (<= 0.70 * baseline)
- Fills the Evidence Template DOCX and saves a populated DOCX
- Optionally generates the PSD plot PNG

## Command
```bash
python tools/workflow/autofill_evidence_doc.py   --root .   --run-id 2026-01-22_RUN3   --t002 tests/raw/RUN3/T002_TankRipple_timeseries.csv   --workbook automation/MicroHydroV1_RnD_Export.xlsx   --out-doc docs/run3/RUN3_Evidence_2026-01-22_RUN3.docx   --out-plot tests/results/summary/T002_PSD_Peakiness.png
```
