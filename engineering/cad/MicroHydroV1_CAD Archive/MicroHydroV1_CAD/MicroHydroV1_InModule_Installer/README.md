# MicroHydroV1 — In-Module Installer (macOS)

This package installs a patched `InitGui.py` and copies your SDK’s `QA/Drawings/CFD` folders **inside** the module folder so the add-on finds them.

## What you need
- Your full SDK folder (from `MicroHydroV1_Complete_Engineering_Package.zip`) that contains `QA/`, `Drawings/`, `CFD/` at its root.

## How to use
1) Quit FreeCAD.
2) Double-click `Install_MicroHydroV1_InModule.command`.
3) When prompted, select the **SDK root** (the folder that has `QA`, `Drawings`, `CFD`).
4) The script will:
   - Create `/Applications/FreeCAD.app/Contents/Resources/Mod/MicroHydroV1/QA` (and Drawings, CFD)
   - Copy contents from your SDK into those folders
   - Install the new `InitGui.py`
5) Launch FreeCAD and check the Report View for `[MHV1][SELF-TEST]` lines (all should be `OK`).
6) Commands appear under Tools → Customize → Commands as `MHV1_*`.
