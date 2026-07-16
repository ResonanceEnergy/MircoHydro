# Design Basis — MicroHydro Crossflow System (from first principles)

**Date:** 2026-07-16 · **Status:** baseline v1 — supersedes all prior efficiency/output figures.
**Model:** `tools/design/crossflow_design.py` — the single source of truth. Every number below is its output; change the model, not the documents.

## Design rules (stated, so they can be challenged)

Classical Banki-Michell method (Mockmore & Merryfield) with conservative, field-realistic efficiencies:

| Parameter | Rule | Value |
|---|---|---|
| Nozzle coefficient | Cv | 0.98 |
| Jet velocity | V₁ = Cv·√(2g·H_net) | derived |
| Attack angle | α | 16° |
| Blade inlet angle | tan β₁ = 2·tan α | 29.8° |
| Speed ratio | U₁/V₁ = cos α / 2 | 0.48 |
| Jet thickness | s₀ = 0.087·D₁ | derived |
| Runner width | b = Q / (V₁·s₀) | derived |
| Inner diameter | D₂ = 0.66·D₁ | derived |
| Blade radius | r_b = 0.163·D₁ | derived |
| Blade count | N_b | 26 (A/B test range 20–30) |
| Turbine peak efficiency | field-built crossflow | **0.70** (theory max 0.878; labs 0.80–0.85) |
| Generator (PMSG, direct drive) | | 0.90 |
| Power electronics | rectifier·MPPT·inverter | 0.90 |
| Intake/screen | | 0.95 |
| Penstock | Darcy-Weisbach, Swamee-Jain f, HDPE | sized for ≤ ~10% loss |

No spiral penstock, no vortex nozzle, no φ multipliers, no ram-pump boost — see `../GAP_ANALYSIS.md` for why each was removed.

## Reference design A — current design point (150 L/s, 5 m, 50 m penstock)

**This is a 3.5 kW machine.** Penstock DN355 (ID 327 mm), v = 1.79 m/s, head loss 0.60 m → H_net 4.40 m. Jet 9.11 m/s through a 24.4 mm × 676 mm nozzle. Runner **D₁ 280 mm × 676 mm wide**, 26 blades of 45.6 mm radius, running at **299 rpm** (direct-drive friendly; runaway 538 rpm — the PMSG and electronics must survive this). Output: 4.3 kW shaft → **3.49 kW electric**, water-to-wire **47.5% of gross head** — achieved by design cleanup alone, no exotics. Fish screen ≥ 0.50 m² net open area. Annual energy: **16.8 MWh/yr** on a year-round stream (CF 0.55); **7.6 MWh/yr** on irrigation-canal duty (CF 0.25).

## Reference design B — the honest 10 kW class (280 L/s, 10 m)

To sell a 10+ kW machine, this is the site it needs: penstock ID 460 mm, runner **D₁ 400 mm × 603 mm**, 306 rpm, **14.0 kW electric at 50.9%** water-to-wire. Annual ~67 MWh/yr (CF 0.55) → **LCOE ≈ $0.13/kWh at $95k installed** — competitive against diesel today. Site scouting should filter for this class: **Q·H ≥ 2.5 m⁴/s with year-round flow.**

## Economics honesty box

At the current design point, even at $75k installed, LCOE is $0.44/kWh (stream) to $0.96/kWh (canal). The product becomes economic through *site selection* (Q·H), not through efficiency heroics: the step from design A to design B multiplies energy by 4 at ~1.3× the cost. This is the central commercial finding of the whole physics audit.

## Validation ladder

1. **Bench rig** (`BENCH_RIG_DESIGN.md`) — 100 mm runner, ~$300: measures the real turbine efficiency curve and settles the blade-count question. → validates the η_t = 0.70 assumption (bench target ≥ 0.55 with 3D-printed runner).
2. **CFD single run** (OpenFOAM, nozzle + runner) — cross-checks torque before any metal is cut for the field runner.
3. **Field prototype at design A scale** on a surveyed site → validates the full cascade.
4. Only after (3): production cost-down and design B commitments.

## Open engineering items

Runner shaft & bearing sizing (280 mm runner, 4.3 kW, 299 rpm → ~137 N·m torque), casing and nozzle mechanism detail, PMSG selection (300 rpm, 5 kW, 48 V-bus compatible — or use MPPT wide-input), draft geometry (runner above tailwater, free discharge, air gap), governor strategy (electronic load control vs flow control).
