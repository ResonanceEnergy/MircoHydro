# Importer Patch: Stamp Run_ID into Measurements

This patch updates `automation/import_measurements.py` so that every imported row has a `Run_ID`.

## What changes
- Adds `Run_ID` to the importer’s optional columns.
- Ensures the workbook Measurements sheet has a `Run_ID` header (added if missing).
- Stamps Run_ID per imported row:
  1) Use Run_ID column in CSV if present
  2) Else use `--run-id` argument
  3) Else derive from the CSV path (matches tokens like `YYYY-MM-DD_RUN3` in folder/file name)

## Usage examples
Import files and stamp Run_ID explicitly:
```bash
python automation/import_measurements.py --excel automation/MicroHydroV1_RnD_Export.xlsx --run-id 2026-01-22_RUN3   tests/raw/RUN3/T001_JetCoherence.csv   tests/raw/RUN3/T002_TankRipple_Run3.csv
```

Import files without specifying --run-id (it will derive from folder/file name if present):
```bash
python automation/import_measurements.py --excel automation/MicroHydroV1_RnD_Export.xlsx   tests/raw/2026-01-22_RUN3/T002_TankRipple_timeseries.csv
```

## Recommended
- Run the Run_ID migrator once on historical data.
- Ensure your importer always writes Run_ID going forward.
