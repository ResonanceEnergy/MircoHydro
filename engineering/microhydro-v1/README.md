# MicroHydroV1 — Phase 3 Automation Pack (macOS + Auto‑Open Releases)

This pack adds **one‑command run automation**, **run folder creation**, **preflight QA**, and **launchers**.

It is designed to work with the MicroHydroV1 repo structure:
- `docs/ cad/ automation/ tests/ data/ tools/`

Locked‑in resonance metric:
- **T‑002 PSD peakiness** using `Time_s` + `Pressure_Pa` in the **0.2–20 Hz** band.

## What’s inside

- `scripts/new_run.py` — creates a new run folder with standard naming and copies templates.
- `scripts/preflight_t002.py` — validates `Time_s` monotonicity, estimates `fs`, computes peakiness + dominant Hz.
- `scripts/run_one_command.py` — end‑to‑end wrapper: preflight → optimize/import/release → evidence.
- `launch_mac.sh` — macOS launcher.
- `docs/POWER_AUTOMATE_EXTENSIONS.md` — optional flow upgrades for per‑run releases.
- `RELEASES_URL_SAMPLE.txt` — paste your Releases library URL here.

## Quick start (macOS)

1) Make launcher executable (one‑time):
```bash
chmod +x ./launch_mac.sh
```

2) Set your SharePoint Releases library URL (one‑time per terminal session):
```bash
export MICROHYDRO_RELEASES_URL='https://<your-sharepoint-releases-library-url>'
```

3) Create a run folder:
```bash
python3 scripts/new_run.py --root . --run-date YYYY-MM-DD --run-num 3 --desc TankRipple
```

4) Put raw CSVs in `tests/raw/<run-id>/` (must include `T002_TankRipple_timeseries.csv`).

5) Run:
```bash
./launch_mac.sh YYYY-MM-DD_Run3_TankRipple
```

After the ZIP is created, macOS will:
- open the local `dist/` folder in Finder
- open your SharePoint **Releases** library in the browser (if `MICROHYDRO_RELEASES_URL` is set)

## CAD note
CAD build is still manual (as intended):
- FreeCAD GUI → Macro → `cad/macros/build_all.FCMacro`
