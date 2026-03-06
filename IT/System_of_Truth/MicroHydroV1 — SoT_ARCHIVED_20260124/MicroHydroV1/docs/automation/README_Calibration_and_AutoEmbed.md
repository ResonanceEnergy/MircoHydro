# Calibration + Auto-Embed (MicroHydroV1)

## Pressure transducer calibration (Pressure_Pa @ 100 Hz)
Workbook: `docs/templates/PT_Calibration_PressurePa_TimeS_100Hz.xlsx`

- Enter 5-10 calibration points (Voltage_V vs Pressure_Pa)
- The sheet computes Sensitivity and Offset
- Paste raw waveform into `Voltage_to_Pressure` if you log voltage

## Auto-embed optimized params
After running optimizer:

```bash
python tools/cad/apply_optimized_params.py --root . --note "v0.3.0: optimized for T-002 PSD peakiness (Pressure_Pa @100Hz)"
```

## Build CAD with optimized params
- Preferred: FreeCAD GUI -> Macro -> `cad/macros/build_all.FCMacro`
- Optional shim: `tools/cad/build_all_use_optimized.FCMacro`
