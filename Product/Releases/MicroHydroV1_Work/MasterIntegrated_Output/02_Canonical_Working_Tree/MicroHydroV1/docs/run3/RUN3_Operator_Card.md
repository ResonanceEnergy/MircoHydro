# MicroHydroV1 — RUN‑3 Operator Card (v0.3.0)

**Standards locked:** `Time_s` + `Pressure_Pa` @ **100 Hz** • Resonance metric: **T‑002 PSD Peakiness** (0.2–20 Hz)

## Folder + filenames (SoT)
- `tests/raw/RUN3/`  ← drop all raw files here
- **T‑002 waveform (required):** `tests/raw/RUN3/T002_TankRipple_timeseries.csv`
  - Columns: `Time_s,Pressure_Pa`
  - ≥ 30 s steady state at 100 Hz

## Capture checklist (bench)
### Pre‑run
- PT installed, leak‑free, grounded
- Logger set to **100 Hz**, export `Time_s` and `Pressure_Pa`
- Record **30 s** steady state per flow condition

### Tests
- **T‑001:** coherence ≥ 0.90
- **T‑002:** ripple ≤ 0.70 × baseline + record timeseries
- **T‑003:** drift ≤ 0.1 Hz (no hunting)
- **T‑004:** power 10–12 kW band

## One‑command pipeline (local)
From `MicroHydroV1/` root:

### A) Optimize → Import → Release (recommended)
```bash
python tools/workflow/run_closed_loop.py --root . --version v0.3.0 --date 2026-01-22   --optimize --resonance-csv tests/raw/RUN3/T002_TankRipple_timeseries.csv   --import --release
```

### B) Manual CAD build step (FreeCAD)
- Run `cad/macros/build_all.FCMacro` (or `tools/cad/build_all_use_optimized.FCMacro`)

## Quick QA gates
- Confirm `Pressure_Pa` has no NaNs and `Time_s` is monotonic
- Confirm PSD peakiness plot looks less “spiky” than baseline
- Confirm workbook dashboard updates after import

## If stuck
- Wrong headers? Must be `Time_s,Pressure_Pa`
- Noisy signal? check grounding + PT mount depth + bubbles
