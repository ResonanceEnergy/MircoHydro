# MicroHydroV1 - v0.3.0 (LOCKED-IN Resonance Metric)

## Locked-in resonance metric
Primary resonance metric = **T-002 hydraulic ripple PSD peakiness**:
- Compute PSD on a steady-state segment
- Score = max(PSD) / median(PSD) in 0.2-20 Hz band (lower is better)

## Run optimizer
```bash
python tools/optimize/optimize_params.py   --params cad/params/params.json   --config tools/optimize/opt_config.json   --out cad/params/params_optimized.json   --resonance-csv <your_T002_timeseries.csv>   --signal-col Pressure_Pa --fs 100
```

## Run pipeline
```bash
python tools/run_pipeline.py --root . --version v0.3.0 --date 2026-01-22 --validate --import --release
```

## CAD build
In FreeCAD GUI: run `cad/macros/build_all.FCMacro`.
