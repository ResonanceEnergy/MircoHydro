# MicroHydroV1 - v0.3.0 FULL Pack (LOCKED-IN resonance metric)

## Locked-in resonance metric
Primary resonance metric: **T-002 hydraulic ripple PSD peakiness**
- Signal column: Pressure_Pa
- Time column: Time_s
- Band: 0.2-20 Hz
- Score: max(PSD)/median(PSD) in band (lower is better)

## Quick start (closed loop)
```bash
python tools/workflow/run_closed_loop.py --root . --version v0.3.0 --date 2026-01-22   --optimize --resonance-csv tests/raw/<run>/T002_timeseries.csv   --import --release
```

## Data capture format
Use `docs/templates/T002_TankRipple_TimeSeries_Template.csv`.
