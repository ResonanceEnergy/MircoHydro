# Physics Proof — Full System at the Ratified Operating Point

**Date:** 2026-07-18 · **Source run:** `tools/design/export_full_system.py` (MOC digital bench, calibrated per SIM_RESULTS) · **Data:** `engineering/data/full_system_timeseries.json` (50 Hz × 20 s steady state), `full_system_operating_point.json` · **Feeds:** the Blender visualization (every animated quantity below is from this run, not artistic license).

## The machine, end to end (actual numbers from the run)

| Stage | Quantity | Value | Where it comes from |
|---|---|---|---|
| River fall | F | **1.5 m** | site (B-Standard reference) |
| Drive pipe | 300 mm × 30 m steel (L/D=100) | wave speed **a = 1173 m/s** | a=√(K/ρ/(1+KD/Ee)) — Finding 4 optimum |
| Waste valve | 8 mm stroke, Wf=0.65 | cycle ≈ **0.9 Hz** fundamental | Finding 6 knee (min-recoil point) |
| Ram appetite | Q | **14.8 L/s** | MOC solution |
| Delivery | q to +9.0 m headstock | **1.82 L/s** (157,000 L/day) | MOC solution |
| Ram efficiency | η (D'Aubuisson) | **0.736** | q·Hd/(Q·F) |
| Air chamber | 40 L (exemption-class, Finding 9) | pressure ride ≈ **88–92 kPa** gauge | polytropic cushion |
| Penstock | 90 mm HDPE × 12 m | loss **0.018 m** (0.2%) | Darcy-Weisbach |
| Twin jets | 2 × **9.5 mm** | jet velocity **12.9 m/s** | Vj = 0.97·√(2g·8.98) |
| Turgo wheel | PCD 150 mm | **754 rpm** (runaway 1358) | u/Vj = 0.46 |
| Jet power | ½ρq·Vj² | **151 W** hydraulic | |
| Shaft power | ×0.75 | **113 W** | canon chain (bench supersedes) |
| **Electric** | ×0.85 PMA ×0.92 MPPT | **88 W continuous ≈ 700 kWh/yr** | per ram; 6-ram bank ≈ **530 W / 4.2 MWh/yr** |

## Proof 1 — energy conservation (no free lunch, audited per window)

Over the recorded 20 s window: energy in = ρg·(drive volume)·F = **4.36 kJ**; energy delivered to the headstock = ρg·(delivered volume)·Hd = **3.21 kJ**; dissipated (valve slam, junction, friction, waste-flow exit) = **1.15 kJ**. Delivered/in = 0.736 = η exactly — the books close. η < 1 everywhere on every run (enforced by unit test `test_energy_conservation_bound` in CI). The ram lifts 12% of the water through 6× the height — a pressure transformer, never an energy amplifier.

## Proof 2 — the water-hammer spike, honestly characterized

Column velocity reaches **0.40 m/s** before slam. The full-Joukowsky ceiling for instantaneous closure is ΔH = a·Δv/g = **47.8 m** — the 30×-amplification lore is real *as an upper bound*. But the operating machine's measured junction peak is only **9.9 m**: the finite valve closure (8 mm stroke over ~40 ms), the calibrated junction dissipation, and — chiefly — the **check valve opening at ~9 m and dumping the spike's flow into the chamber** clamp the transient at just above delivery head. That is the correct physics of a *working* ram: the spike doesn't need to be huge, it needs to reach h_delivery + valve losses; everything above that is wasted stress. Design consequences, on the record: (a) chamber design pressure is governed by the **blocked-delivery fault case** (~4.7 bar full Joukowsky), not normal operation (~1 bar) — both comfortably inside commodity PN10 bladder-vessel ratings (REQ-S1); (b) drive-pipe fatigue amplitude in normal service is small (hoop stress ~a few MPa — infinite life, per COMPONENT_TECH_SCAN §3).

## Proof 3 — the cycle mechanics visible in the time-series

The exported series shows, each cycle: valve open → column accelerates (Q0 ramps) → drag closes valve (x_v→0 in ~40 ms) → junction head jumps to ~9.9 m → check valve passes a slug into the chamber (V_air compresses ~40→38 L, P_ch rises) → column rebounds, check closes → chamber's gas cushion pushes the slug up the rise pipe smoothly (Qd nearly constant ≈1.8 L/s while inflow is pulsed) → valve reopens near the zero-recoil crossing (this configuration IS the Finding-6 knee) → repeat at ~0.9 Hz. The valve exhibits ~2 micro-bounces per fundamental cycle (visible in x_v; the naive event counter reads 1.85 Hz — the debounced fundamental is ~0.9 Hz, consistency noted per Finding 8's chatter lesson).

## Caveats (canon discipline)

Absolutes carry the single-point Kj calibration caveat until model v2 + physical bench (±10% gate). The downstream chain efficiencies (0.75/0.85/0.92) are canon design values, not measurements — Bristol's measured 91% Turgo runner ceiling says our 0.75 is conservative. The 6-ram bank number assumes independent rams (bank interaction study open). Penstock run (12 m) is a site assumption, stated. **Nothing in the visualization is invented: every animated channel (valve position, pressures, flows, wheel speed) is this run's data.**
