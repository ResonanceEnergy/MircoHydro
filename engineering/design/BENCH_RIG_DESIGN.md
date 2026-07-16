# Bench Rig Design — 100 mm Crossflow Test Turbine

**Purpose:** produce this project's first measured efficiency curve, and settle the blade-count question (Fibonacci 21 vs uniform 26 vs 30) with real data. Supersedes the rig sketch in PROTOCOL_001; test methodology (A/B, two-sample t-test, α = 0.05) carries over unchanged.

**Derived from the same model as the field unit** (`tools/design/crossflow_design.py --Q 0.00185 --H 1.5 --bench --D1 0.100`):

| Parameter | Value |
|---|---|
| Design flow | 1.85 L/s (111 L/min) |
| Gross head | 1.5 m (pump-driven closed loop) |
| Jet | 5.1 m/s, **8.7 mm × 42 mm** rectangular nozzle |
| Runner | **D₁ 100 mm, D₂ 66 mm, width 42 mm**, 26 blades r = 16.3 mm, β₁ ≈ 30° |
| Design speed | ~470 rpm (runaway ~840 rpm) |
| Hydraulic power at runner | ~25 W |
| Expected shaft power | 12–16 W (η_t 0.5–0.65 for printed runner) |

## Bill of materials (~CAD $250–350)

| Item | Spec | Est. |
|---|---|---|
| Pump | utility/pond pump ≥ 8,000 L/h @ ≥ 2.5 m head, 230–300 W | $80–120 |
| Reservoir | 60–100 L tote | $15 |
| Pipe & fittings | 2" (55 mm ID) PVC ×3 m, ball valve, unions | $40 |
| Nozzle | 3D-printed converging duct → 8.7 × 42 mm exit (print with runners) | $5 filament |
| Runners | 3× printed (21 / 26 / 30 blades), PETG, 30%+ infill | $15 |
| Shaft & bearings | 8 mm steel shaft, 2× 608-2RS bearings, pillow blocks | $25 |
| Dyno/generator | 775-size DC motor as generator + 10 W power resistors (0.5–10 Ω bank) | $30 |
| Instrumentation | INA226 V/I module + ESP32 (electrical power), laser tach ($15), pressure gauge 0–30 kPa at nozzle inlet ($15), flow by bucket-and-stopwatch (free, ±2%) | $45 |
| Frame | plywood + brackets, splash tray | $30 |

## Measurement plan

- **Head:** pressure gauge at nozzle inlet + elevation to jet centerline. **Flow:** timed fill of a 20 L pail ×5, take mean (do this at every operating point — pump curves lie).
- **Shaft efficiency via electrical proxy:** η_t·η_gen = P_elec / (ρ·g·Q·H_nozzle). Characterize the DC machine first (spin it with a drill at known rpm/torque or use its datasheet k_t) so η_gen can be divided out; otherwise report the combined number — it's still a valid A/B comparator.
- **Efficiency curve:** sweep load resistance at fixed flow → rpm varies → plot η vs U/V₁. Peak should land near U/V₁ ≈ 0.45–0.50 — landing there is itself a validation of the design rules.
- **A/B protocol:** 21 vs 26 vs 30 blades, same nozzle, ≥ 5 runs each, two-sample t-test as per PROTOCOL_001. Report the null result honestly if that's what the water says.

## Success criteria

1. Any measured peak η_t ≥ 0.45 (printed runner) → design rules validated, proceed toward field scale.
2. Peak efficiency at U/V₁ within 0.40–0.55 → velocity-triangle model confirmed.
3. Blade-count winner (or null) established with p < 0.05.

## Print files

Runner geometry is generated parametrically by `tools/design/build_crossflow_runner.FCMacro` (FreeCAD ≥ 0.20): set `Nb` in the params block to 21/26/30, run, export STL. The macro builds true arc blades (r_b = 0.163·D₁, β₁ = 30°) between end disks with an 8 mm bore hub — this replaces the flat-vane `build_vanepacks` geometry, which is not a crossflow runner.
