# Machine B — Ram-Pump → Jet → Impulse Turbine (Low-Head Unit)

**Date:** 2026-07-16 · **Status:** design v1 · **Solver:** `tools/design/ram_pelton_design.py` (single source of truth — regenerate every number here from it).

## Architecture

Stream → screened intake → **rigid steel drive pipe** → hydram → **air chamber** (≥10× per-cycle delivery volume, snifter valve) → pressure line → **fixed nozzle** → Pelton/Turgo wheel → direct-drive PMA → rectifier + solar-MPPT → battery/loads.

**No elevated headstock.** The air chamber smooths delivery so the nozzle's back-pressure *is* the delivery head — the tank, tower, and hill requirement are deleted from the install. (Optional storage-tank module only where terrain already provides elevation.)

This is the companion to Machine A (direct crossflow, `DESIGN_BASIS.md`). Machine selection rule from `../GAP_ANALYSIS.md`: **natural fall ≥3 m → Machine A; fall 0.5–2 m → Machine B; below ~0.4 m → no feasible machine, skip the site.**

## Provenance

Built on the repo's own established rules: `engineering/specs/technology/02_Hydram/HYDRAM_GUIDE.md` (USAID relation q·L = E·Q·F, E ≈ 0.66 commercial / 0.33 home-built; fall ≥ 0.5 m; drive-pipe high-sensitivity) and Volume G's energy bound and bench-first ladder. The solver extends the constant-E USAID relation with the published behavior that ram efficiency falls with lift ratio: η(r) = 0.85 − 0.03r, clamped [0.20, 0.72] — which reproduces the USAID 0.66 figure at r ≈ 6.

## The coupled operating point (the design contribution)

Electric output is P = ρgQF · η_ram(r) · η_turb · η_PMA · η_elec, which **falls monotonically as lift ratio r rises** — so peak power is always the *lowest* r the impulse wheel tolerates. The operating point is therefore set by hardware constraints, not by efficiency tuning: nozzle bore ≥ 6 mm (clog floor), wheel PCD ≤ 300 mm and ≥ 9× nozzle bore (bucket rule), shaft speed within the PMA band (300–2,000 rpm), and jet head ≥ 6 m (impulse practicality floor). The solver sweeps r and returns the max-power feasible point.

## Solved operating points (chain: η_ram(r) × 0.75 turbine × 0.85 PMA × 0.92 electronics)

| Fall (m) | Drive Q (L/s) | r* | H_d (m) | η_ram | jet (mm) | PCD (mm) | rpm | **W out** | kWh/day | water-to-wire |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | 30 | 12.0 | 6.0 | 0.49 | 12 | 110 | 844 | **42** | 1.0 | 29% |
| 0.5 | 100 | 12.0 | 6.0 | 0.49 | 22 | 200 | 462 | **141** | 3.4 | 29% |
| 0.75 | 100 | 8.0 | 6.0 | 0.61 | 30 | 273 | 338 | **263** | 6.3 | 36% |
| 1.0 | 60 | 6.0 | 6.0 | 0.67 | 29 | 256 | 361 | **231** | 5.6 | 39% |
| 1.0 | 100 | 7.0 | 7.0 | 0.64 | 32 | 288 | 347 | **368** | 8.8 | 38% |
| 1.0 | 200 | 10.0 | 10.0 | 0.55 | 32 | 289 | 413 | **633** | 15.2 | 32% |
| 1.5 | 100 | 6.0 | 9.0 | 0.67 | 33 | 299 | 379 | **578** | 13.9 | 39% |
| 1.5 | 200 | 9.0 | 13.5 | 0.58 | 32 | 290 | 478 | **1,001** | 24.0 | 34% |
| 2.0 | 100 | 6.0 | 12.0 | 0.67 | 31 | 278 | 470 | **771** | 18.5 | 39% |
| 2.0 | 200 | 8.5 | 17.0 | 0.59 | 32 | 285 | 545 | **1,369** | 32.9 | 35% |

Full grid in the solver. Drive pipe (rigid steel, sized at ~1.5 m/s, length ≥6× fall within the L/D 150–1000 window): 200 mm × 30 m (30 L/s class) to 400 mm × 60 m (200 L/s class).

## What the numbers say

1. **The machine works from 0.5 m of fall** — where nothing on the market does — but output there is modest (40–140 W class). The product's heart is **1–2 m of fall with 100–200 L/s: 370–1,370 W continuous, 9–33 kWh/day** — full-homestead power, 24/7, through winter.
2. **Water-to-wire lands at 29–42%**, confirming the design-phase chain estimate (~40% at F ≥ 1 m) and beating the 15–25% reported for untuned DIY attempts. The margin comes from three controllables: rigid drive pipe at correct length, tunable waste valve, and nozzle matched to the ram's optimum delivery pressure.
3. **The wheel constraints, not the ram, set the operating point.** At small falls the 6 m jet-head floor forces high lift ratios and crushes ram efficiency (0.5 m fall → r = 12 → η 0.49). Design lever worth studying: a Turgo runner (tolerates larger jet/wheel ratio, runs at lower head) could relax the floor to ~4 m and recover several points at the smallest falls.
4. **Consistent hardware envelope:** every point from 60–200 L/s lands in a 250–300 mm wheel at 330–550 rpm with a 20–33 mm jet — one wheel SKU + one PMA covers nearly the whole product range; only the ram/drive-pipe kit scales with the site.

## SKU sketch (from the grid)

- **B-Small** — falls 0.5–1 m, drive 30–60 L/s: 40–230 W. 200–250 mm drive kit.
- **B-Standard** — falls 1–2 m, drive 100 L/s: 370–770 W. 300 mm drive kit, 280 mm wheel.
- **B-Max** — falls 1–2 m, drive 200 L/s (or 2× parallel rams): 630–1,370 W. 400 mm kit or dual B-Standard rams on one manifold.

## Open design items (still paper)

Waste-valve tuning map (stroke/weight vs frequency — the field-commissioning procedure), air-chamber volume and snifter spec per SKU, Turgo-vs-Pelton study below 8 m jet head, delivery-line friction at the 30+ L/s delivery flows of B-Max (checked small, needs a real pipe size), winter enclosure detail, and the validation ladder from Volume G (bench ram → measured η(r) curve to replace the fitted one).
