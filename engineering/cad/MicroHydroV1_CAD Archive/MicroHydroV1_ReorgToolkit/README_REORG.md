
# MicroHydroV1 — Reorg Toolkit

**Purpose:** Rebuild your MicroHydroV1 project into a clean, duplicate‑free, OneDrive‑safe structure and produce a MASTER ZIP.

## Steps
1. Download this toolkit and unzip.
2. Open a terminal in the toolkit folder.
3. Run:

```bash
python reorg_from_zip.py "/absolute/path/to/MICRO HYDRO.zip"
```

4. The script creates:
   - `MicroHydroV1/` (clean repository)
   - `manifest.json` (verification: hashes and duplicates list)
   - `MicroHydroV1_Rebuilt_Clean_Repo_YYYYMMDD_HHMMSSZ.zip` (master ZIP)

**Tip (OneDrive):** If your source is at
`/Users/gripandripphdd/Library/CloudStorage/OneDrive-GripandRipp(2)/MICRO HYDRO.zip`,
pass that full path to the script.
