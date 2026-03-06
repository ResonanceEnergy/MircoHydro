# Power Automate Blueprints - MicroHydroV1 (SoT -> Review -> Release)

These flows automate governance and routing in SharePoint. They do not execute FreeCAD or local Python.

## Flow A: New Raw Data Arrives (tests/raw)
Trigger: file created under tests/raw/
Actions:
- Set metadata: Artifact Type=TestData, Status=Draft
- Notify Teams + create task: Import measurements, review dashboard, attach evidence

## Flow B: Workbook Updated -> Request Review
Trigger: automation/MicroHydroV1_RnD_Export.xlsx modified
Actions:
- Set Status=Review
- Notify Teams

## Flow C: Release Candidate Gate
Trigger: key items Approved
Actions:
- Create task: Cut Release v0.3.0
- Notify: Run tools/workflow/run_closed_loop.py --release
