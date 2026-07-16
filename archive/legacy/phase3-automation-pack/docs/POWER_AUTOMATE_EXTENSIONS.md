# Power Automate Extensions (Phase 3)

Optional enhancements for **solo + per‑run** operation.

## A) Raw data arrives → infer Run_ID
Trigger: file created under `tests/raw/`
Actions:
1. Infer Run_ID from the parent folder name (e.g., `2026-01-22_Run3`).
2. Set metadata:
   - Artifact Type = TestData
   - Status = Draft
   - Release ID = `R-YYYY-MM-DD` (derived from Run_ID date)
   - Version Tag = `RUN3` (derived from Run_ID)
3. Teams notification with a link to the run folder.

## B) Evidence generated → auto‑tag Approved
Trigger: file created under `docs/run*/` matching `*_Evidence_*.docx`
Actions:
- Artifact Type = EvidenceDoc
- Status = Approved

## C) Release ZIP uploaded → announce
Trigger: file created in Releases library
Actions:
- Status = Approved
- Teams post: release name + link

## D) Import log list (optional)
Create SharePoint List `MicroHydroV1_ImportLog`:
- Run_ID (text)
- Imported_At (datetime)
- Rows_Added (number)
- Source_Folder (link)
- Notes (multiline)
