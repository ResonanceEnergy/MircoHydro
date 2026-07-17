# Machine B — Full System Design (headstock architecture)

**Date:** 2026-07-16 · **Schematic:** `full_system_schematic.svg` · **Solver:** `../../tools/design/ram_pelton_design.py`
**Reference site (B-Standard):** 1.5 m natural fall, 100 L/s drive flow.

Water path, end to end: **river → screened intake → drive pipe → hydram → rise pipe → headstock tank → fluted penstock → twin nozzles (jets) → Pelton wheel → tailrace → river.** All water returns; consumption is zero.

## Component schedule (reference site)

| # | Component | Specification | Function / notes |
|---|---|---|---|
| 1 | Screened intake | 0.35 m² net open area, ≤0.3 m/s approach, fish-safe, ice-shielded box | feeds drive pipe; the only structure touching the river |
| 2 | Drive pipe | **rigid steel, 300 mm ID × 45 m**, laid on the 1.5 m fall (L/D = 150 ✓) | the power stroke — water-hammer column; rigidity is non-negotiable |
| 3 | Hydram | commercial-class, **tunable waste valve** (stroke + weight), integral air chamber, η = 0.67 at lift ratio 6 | passive engine of the system; waste water exits at the ram straight back to river |
| 4 | Rise pipe | DN80 poly × ~14 m, carries **11.2 L/s** up to the tank | delivery side; low velocity (2.2 m/s), ordinary pipe is fine here |
| 5 | **Headstock tank** | **4 m³ at EL +9.0 m** above nozzle centerline (hillside bench or stand), vented, overflow back to stream | three jobs: pressure reference for the jets, surge/boost storage, air separation & silt settling before the penstock |
| 6 | **Fluted penstock** | **DN100 × 15 m, helical internal rifling**, f = 0.019 → 0.35 m loss → **8.65 m at the nozzle**, v = 1.4 m/s | tank-to-manifold pressure line; fluting per project design (bench A/B slot reserved to measure rifled vs smooth on this exact pipe class) |
| 7 | Nozzle manifold — twin jets | **N1: 33.5 mm fixed** (continuous duty) · **N2: 33.5 mm behind a ball valve** (boost duty) | jet velocity 12.6 m/s; fixed bores — flow is constant, so no spear valves needed |
| 8 | Turbine | **Pelton, 300 mm PCD, 368 rpm** (runaway ~660 — PMA and mounts rated for it) | jet/wheel ratio 1:9 at the bucket rule limit |
| 9 | PMA | direct-drive permanent-magnet alternator on the wheel shaft, 300–600 rpm class | no gearbox, no belts |
| 10 | Electronics | rectifier → **solar MPPT** → 48 V LiFePO₄ (heated enclosure) → inverter | MPPT loading doubles as the electronic governor — holds the wheel at optimum speed |
| 11 | Tailrace | open channel, turbine house floor to river | 100% return, ~2 m run |

## Operating modes

| Mode | Nozzles | Output | Duration | Use |
|---|---|---|---|---|
| **Continuous** | N1 | **556 W** (13.3 kWh/day) | 24/7/365 | base power — fridge, lights, comms, well pump cycling |
| **Boost** | N1 + N2 | **~996 W** | ~6 min per full tank, 50% duty (tank refills in ~6 min) | motor starts, power tools, kettle — the headstock's party trick |
| Bypass | none (jets valved off) | 0 W; ram keeps filling tank → overflow | maintenance | wheel/PMA service without touching the ram |

The boost mode is what the headstock buys over a tankless (air-chamber-direct) build: **dispatchable surge power** from stored water, plus silt settling and a stable pressure reference. Cost of that: the tank, its bench/stand, and ~14 m more rise pipe.

## Energy ledger (per the schematic strip)

Stream delivers 100 L/s × 1.5 m = **1,472 W** → ram (0.67) → **948 W** in the jet circuit → wheel (0.75) → PMA (0.85) → MPPT/rectifier (0.92) → **556 W** at the battery bus. Water-to-wire **38%**. Every stage is on the diagram; nothing is claimed that isn't in the ledger.

## Scaling (same drawing, different kit — from the solver grid)

| Site | Drive kit | Headstock EL | Wheel | Continuous out |
|---|---|---|---|---|
| 0.75 m / 100 L/s | 300 mm × 45 m | +6.0 m | 273 mm | 263 W |
| 1.0 m / 100 L/s | 300 mm × 45 m | +7.0 m | 288 mm | 368 W |
| **1.5 m / 100 L/s (ref)** | **300 mm × 45 m** | **+9.0 m** | **300 mm** | **556 W** |
| 1.5 m / 200 L/s | 400 mm × 60 m (or 2× rams) | +13.5 m | 290 mm | ~1,000 W |
| 2.0 m / 200 L/s | 400 mm × 60 m (or 2× rams) | +17.0 m | 285 mm | ~1,370 W |

One wheel + one PMA covers the whole range; only the drive kit and headstock elevation change.

## Design items still open

Waste-valve tuning map (the commissioning procedure), headstock siting rule (hillside bench vs stand — stand height caps practical H_d on flat ground), penstock fluting A/B (rifled vs smooth, this pipe class, on the bench), Turgo option below 8 m jet head, N2 auto-valve (load-sensing boost), winter enclosure details for ram and tank overflow.
