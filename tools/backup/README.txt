
NEXT CHAT — QUICK START

1) FreeCAD Add-on
   - Unzip MicroHydroV1_Addon_macOS.zip into your User Mod folder:
     ~/Library/Application Support/FreeCAD/Mod/MicroHydroV1/
   - Restart FreeCAD and run: MHV1_GenerateAll → MHV1_RunQA → MHV1_ExportAll → MHV1_GenDrawings
   - Or use the one‑click macro (MHV1_run_all.FCMacro) with WS_ROOT set to your workspace path.

2) Append Drawings to Master
   - After PDFs appear in Tests/Results/Summary/Drawings/, upload them; we’ll auto‑insert Appendix A into MicroHydroV1_Master.docx and re-zip a final deliverable.

3) Importer (optional)
   - Drop CSVs into MicroHydroV1/Automation and run: python import_measurements.py
   - Open MicroHydroV1_RnD_Export.xlsx → Measurements table updates (Pass/Rule_Eval).

This package contains:
- chat_log.txt (this conversation’s condensed log)
- placeholders for addon/workspace so you can attach local files next time
- docs/next_steps.md for copy-paste guidance during the call
