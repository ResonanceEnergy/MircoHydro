# Archive

Historical material preserved for the record. Nothing in here should be treated as evidence of project status.

- **`automation/`** — the automation/"validation"/"deployment" scripts and their outputs from Jan–Feb 2026. **Important:** these scripts do not compute or contact anything. The "digital design validation" results (36% → 39.5% → 55% efficiency, "infinite design life", "99.999999% reliability") are hardcoded literals in the source; the "university deployments" (60 universities, 120 agents) write local JSON files and reach no one; `2100_PROOF_MASTER_SYSTEM.sh` is entirely `echo` statements. The completion reports in `docs/reports/` that cite these outputs inherit the same problem. Kept as a record and a caution.
  - Security notes: `openclaw_integration.py` contains a `curl | bash` install from an unverified domain (currently broken by a missing import — leave it broken). `ZERO_DATA_LOSS_RECOVERY.sh` uses `rsync --delete` (destructive if pointed at a stale backup). `automate_all.py` is an infinite hourly LLM-API loop.
- **`legacy/`** — deduplicated remains of the old workspace trees (MASTER_PRODUCTION_PACKAGE, MICRO HYDRO NEW, SoT archives, zips). The canonical copies of anything current live in `engineering/`, `docs/`, `research/`, `tools/`.
- **`exports/`** — old point-in-time exports (docs export 2026-01-25, enterprise artifacts).
- **`audits/`** — the Feb 2026 audit index and duplicate-analysis files.
- **`DEDUP_MANIFEST.csv`** — every duplicate file dropped during the 2026-07-16 consolidation and the canonical copy that was kept.

Excluded entirely from the consolidation (they were byte-level mirrors of the main tree): `_CONSOLIDATION_BACKUP/`, `_BACKUPS/`.
