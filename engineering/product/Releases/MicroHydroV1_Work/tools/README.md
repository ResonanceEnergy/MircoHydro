
# MicroHydroV1 Master Integrator

Run locally:

```bash
python3 microhydro_master_integrator.py --archive Archive.zip --out MasterIntegrated_Output --policy policy_config.json --zip-out
```

Outputs:
- `01_SharePoint_Libraries/` cleaned copies of SoT/Releases/Archive
- `02_Canonical_Working_Tree/MicroHydroV1/` merged working tree
- `03_Packages_Original_Zips/` deduplicated embedded packages
- `04_Reports/` inventory + policy flags + conflicts

Edit `policy_config.json` to tune rules.
