# MicroHydroV1 Measurements Import — Quick Start

**Files in this package**
- `Measurements_Import_Template.csv` — header-only template for data entry.
- `Import_Config.json` — allowed Test_IDs and sensor keyword hints.
- `import_measurements.py` — importer that appends rows to `MicroHydroV1_RnD_Export.xlsx` → `Measurements` (tblMeasurements).

## How to use
1. Prepare one or more CSV files with columns:
   `Timestamp, Test_ID, Sensor, Value, Unit, Baseline_Value, Conditions, Notes`
   (Required: Timestamp, Test_ID, Sensor, Value, Unit).
2. Place the CSV(s) in the same folder as `MicroHydroV1_RnD_Export.xlsx`.
3. Run the importer and pass your CSV filenames, e.g.:
   ```bash
   python import_measurements.py data_run1.csv data_run2.csv
   ```
   If you run it without arguments, it will import **all** `.csv` files next to the workbook **except** the template.
4. Open the workbook in Excel. The **Measurements** table will have your rows, **Pass**/**Rule_Eval** will auto-calc, **Dashboard** and **Trends** will update.

## Notes
- For **T-001 (Jet Coherence)**, leave `Baseline_Value` blank.
- For **T-002 (Tank Ripple)**, provide `Baseline_Value` so the 70% threshold line and pass/fail are computed.
- Sensor names are matched case-insensitively (e.g., `coherence`, `ripple`).
