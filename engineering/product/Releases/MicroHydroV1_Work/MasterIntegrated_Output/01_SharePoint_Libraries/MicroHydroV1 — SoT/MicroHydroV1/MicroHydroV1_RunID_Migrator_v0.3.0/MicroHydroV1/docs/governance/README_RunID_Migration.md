# Run_ID Column + Migrator (v0.3.0)

## Why
The auto-fill evidence system can select the correct run by matching `Run_ID`. This migrator:
- Adds `Run_ID` column to `Measurements`
- Backfills it from `Conditions`/`Notes`

## Expected token format
Use tokens like:
- `2026-01-22_RUN3`
- `2026-01-22_Run3`

Place the token in `Conditions` or `Notes` for each measurement row.

## Run
```bash
python tools/workflow/migrate_add_run_id.py --workbook automation/MicroHydroV1_RnD_Export.xlsx
```

### Write to a new file
```bash
python tools/workflow/migrate_add_run_id.py   --workbook automation/MicroHydroV1_RnD_Export.xlsx   --out automation/MicroHydroV1_RnD_Export_with_RunID.xlsx
```

## Optional: custom token regex
```bash
python tools/workflow/migrate_add_run_id.py --workbook ... --pattern "(\d{4}-\d{2}-\d{2}_RUN\d+_FR\d+)"
```
