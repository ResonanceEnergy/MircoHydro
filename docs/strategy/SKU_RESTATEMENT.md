# SKU Restatement — All Numbers From the v2 Digital Bench (Queue #4 Closed)

**Date:** 2026-07-19 · Every figure below traces to `ram_moc_sim.py` v2 (Kj=100, leak 0.3%, conservative envelope) via `ram_pelton_design.eta_ram_sim()` / `q_per_ram_300()`, the chain factors of ENERGY_LOSS_BUDGET, and Finding 12 (bank stagger). The retired η fit is dead in the solver. Absolutes still carry the bench-correlation caveat (±10% gate); ratios are canon-grade.

## The ladder (reference class: 1.5 m fall, r = 6, tuned knee, per-ram q = 1.74 L/s v2)

| SKU | Config | Electric (baseline chain) | Electric (buildable chain: runner .85, PMG .90, MPPT .965, Cv .98) | Water delivered | Notes |
|---|---|---|---|---|---|
| **B-Pico** | 1 × 100 mm ram, pico site | ~10 W class | ~13 W | **~17,000 L/day to +9 m** | water-first SKU; power is trickle-charge (telemetry, lighting). Fills the dead PowerPal's market position at the water+power entry |
| **B-Solo** | 1 × 300 mm ram | **~82 W** (v2 knee, honest restatement from 88) | **~105 W** | ~150,000 L/day | the demo/correlation unit |
| **B-Standard** | 6-ram bank, staggered manifold | **~490 W** + 6.7 W stagger recovery ≈ **495 W** | **~630 W** | ~900,000 L/day (or any split water/power) | stagger cuts headstock ripple 90%, peak intake draw −35% (Finding 12) — smaller screen/channel = cheaper civils-free install |
| **B-Max** | 12-ram bank | ~0.99 kW | **~1.26 kW** | ~1.8 ML/day | two manifolds, one headstock; boost mode serves motor starts |
| Boost (any SKU) | N2 valve open, headstock draw-down | ~1.8× continuous for tank-limited minutes | same ratio | — | the headstock's dispatchable party trick, unchanged |

**Annual energy:** stop quoting ×8760 flat. Per-site annual = SKU output × site flow-duration envelope from `tools/design/flow_duration.py` (companion tool, this commit). Marketing floor: use the P75 season, not the wet-month peak.

**Chain provenance:** jet ×0.941 (Cv .97) × runner 0.75 × PMG 0.85 × MPPT 0.92 baseline; buildable per ENERGY_LOSS_BUDGET levers G-2..G-5. High-r sites (r > 9) automatically take the published-decline envelope via `eta_ram_sim()` — the solver can no longer overpromise at high lift.

**What changed vs the legacy sheet:** 556 W single-ram fiction → 495 W six-ram bank truth; flat η → envelope; Pelton 300 → Turgo 150 (D-1/REQ-P9 pending dyno); DN80 rise → DN100 (+1.1 W, F9); annual kWh now site-honest. Grant applications and pitch decks must cite THIS table.
