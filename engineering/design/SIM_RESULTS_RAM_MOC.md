# Digital Bench Results — Ram MOC Simulator v1

**Date:** 2026-07-18 · **Tool:** `tools/design/ram_moc_sim.py` (method of characteristics, dynamic valves, air chamber, fixed-head headstock delivery per ratified architecture) · **Resolves:** decision D-5 (supersedes the fitted η curve) · **Runs:** D-4's Gen 0 metrics (T-001 jet variation, T-002 PSD peakiness) computed on every run.

## Model & calibration (stated plainly)

Physics from first principles: elastic water-hammer in the steel drive pipe (computed wave speed 1,173 m/s), entrance loss, waste-valve disc dynamics (weight vs flow-drag), check valve, polytropic air cushion, rise-pipe delivery to the fixed headstock head. **One calibration constant** — a junction dissipation lump `Kj` (valve-slam + unsteady friction) — anchored to the repo's own USAID commercial datum: **η = 0.667 at r = 6 with Kj = 125** (calibrated 2026-07-18). Everything else is geometry and physics.

## Results at the reference configuration (F = 1.5 m, 300 mm × 45 m steel drive pipe, headstock +9 m)

| Quantity | Simulated |
|---|---|
| Cycle frequency | 0.50 Hz |
| Drive flow swallowed | **17.6 L/s** |
| Delivery to headstock | 1.95 L/s |
| D'Aubuisson efficiency | 0.667 (anchored) |
| Chamber pressure ripple | ~12% |

## Finding 1 — the big design correction: one ram does NOT swallow 100 L/s

The fitted-era Machine B numbers assumed the site's 100 L/s drive flow passes through one ram. The transient model shows the pipe-and-valve dynamics of a 300 mm ram at 1.5 m fall swallow **~18 L/s** — consistent with real manufacturer tables for 12"-class rams (Blake/Rife: roughly 7–15 L/s). Column acceleration under 1.5 m of head over a 45 m pipe simply takes ~2 s per cycle; duty cycle caps the appetite.

**Consequences (honest restatement):**
- **Per-ram output at B-Standard conditions: ~172 W hydraulic at the jet → ≈ 100–120 W electric** — not 556 W.
- The 556 W-class site output requires a **ram bank: 5–6 parallel 300 mm rams** on a manifold (the "B-Max dual-ram" concept generalizes to banking as the standard scaling method). Modularity was already the plan; the sim says it starts earlier than we priced.
- Cost per watt worsens accordingly at small falls; SKU economics must be re-run with per-ram banking (queued: solver update to ingest sim-derived per-ram curves).
- A drive-pipe **length study is now open**: the L/D ≥ 150 rule forces long pipes → slow cycles → low appetite. Literature also supports L ≈ 5–10× fall (much shorter). The sim can sweep this trade directly — potentially several× more flow per ram. **This is the highest-value next simulation.**

## Finding 2 — the η(r) curve: anchored at the operating point, flat at high r (known limitation)

Sweep (Kj = 125): η_sim ≈ 0.62–0.70 across r = 4–20, versus published field behavior declining to ~0.3 by r = 20. The v1 model under-represents high-r losses (mechanism identified: waste-valve reopen leakage during recoil — the reflected wave's energy is recovered elastically in the model but partially dumped in real rams). **Design ruling:** the conservative envelope applies — **η_design(r) = min(η_sim, published-decline curve)**; since every ratified SKU operates at r ≤ 9 (B-Standard r = 6), the divergence barely touches the product envelope, and the sim is anchored exactly where we operate. Model v2 backlog: valve-reopen leakage term; then re-calibrate against the physical bench (the ±10% gate remains supreme).

## Finding 3 — Gen 0 metrics live again (D-4 delivered)

Every run now outputs **T-002 PSD peakiness** (0.2–20 Hz band, delivery pressure) and **T-001 jet-variation** (coefficient of variation of delivery flow). First data: the 60 L air chamber leaves delivery strongly pulsed between strokes (T-001 CoV > 1 at low chamber margin) — **the chamber and rise-pipe conductance need sizing up for jet-quality duty**; the founder's original coherence metric is now the design driver for exactly that sizing. The January 2026 test program is, at last, producing numbers.

## Status of the retired fit

η(r) = 0.85 − 0.03r is retired per D-5. At the operating point it happens to agree with the sim (0.67 vs 0.667) — the fit was right where it mattered and wrong in shape elsewhere, which is exactly why it needed replacing.

## Queue (in order)

1. Drive-pipe length sweep (L = 5F … 150D) — per-ram appetite vs efficiency trade; likely recovers much of Finding 1's power loss.
2. Valve tuning map at the new operating points (weight × stroke) → the field commissioning card.
3. Chamber + rise-pipe sizing for T-001 jet quality (Gen 0 metric as design requirement).
4. Model v2: reopen-leakage; re-anchor; then solver ingestion and full SKU re-statement.
5. Physical bench correlation when hardware exists (±10% model-vs-prototype gate, VALIDATION req 8).
