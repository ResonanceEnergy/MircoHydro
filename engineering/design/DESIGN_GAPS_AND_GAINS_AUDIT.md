# Master Audit — All Research vs Our Design: Gaps & Gains

**Date:** 2026-07-19 · **Founder directive:** "take all the research and audit against our design — find gaps and ways we can make gains." · **Inputs:** Findings 1–11 (digital bench), COMPONENT_TECH_SCAN, both receipts files, RAM_RESONANCE_RESEARCH, POWERTRAIN_AUDIT, ENERGY_LOSS_BUDGET, Schauberger/Keely/water-memory/implosion evidence files, GWVPP_AUDIT, ENGINEERING_DEPT_AUDIT, PRD, market docs. Everything below cites where it came from; nothing new is asserted.

---

## PART 1 — GAINS LEDGER (ranked by value ÷ effort)

### Power & efficiency (per ram at reference site; bank = ×6)

| # | Gain | Δ | Effort/cost | Source |
|---|---|---|---|---|
| G-1 | **Self-tuning servo holding the knee vs field drift** | **+29–42% in field terms** — worth more than all hardware levers combined | $150 BOM (sensor+actuator+MCU), firmware done in sim (F8) | Finding 8 |
| G-2 | **Runner quality 0.75 → 0.85 (0.91 measured ceiling)** | +15–24 W | make/buy: cast or high-res-printed cups vs kit wheel | Loss budget L1; Bristol 91% [M] |
| G-3 | **Generator kV match (REQ-P9)** | +6–8 W | dyno day + winding selection or 100 mm PCD | Powertrain audit §3 |
| G-4 | **Modern MPPT (0.92→0.965)** | +5–6 W | component swap, $0 design | Loss budget L5 |
| G-5 | **Nozzle Cv 0.98 + honeycomb conditioning** | +3–5 W + predicted CoV halving | machining + $30 honeycomb | Loss budget L3; Finding 11 |
| G-6 | Valve light-tune where site water allows | up to +6% | commissioning card (done, F5/F6) | Finding 5/6 |
| G-7 | DN100 rise pipe | +1.1 W | pipe size change | Loss budget (sim-verified) |
| G-8 | Drive pipe L/D 100–250 (30–75 m not 150) | ≈ cost gain: hundreds of $ steel per site + η | spec change (done, F4) | Finding 4 |
| **Stack** | **88 → ~114 W buildable, ~125–133 W stretch per ram; bank 530 → 685–800 W** | | | Loss budget §max-output |

### Strategic gains (from receipts + market audits — each currently owned by NOBODY)

| # | Gain | Evidence it's open | Action |
|---|---|---|---|
| S-1 | **Only manufacturer on Earth publishing measured efficiency curves** | receipts: zero vendors publish curves; the one measured pico number worldwide came from a customer's blog | publish our sim+bench curves with error bars — instant category-of-one |
| S-2 | **Measured water-stewardship claims** ("discharge leaves the river better") | stewardship spec; no competitor has water-quality data; GWVPP's fish claim is contested | instrument DO/turbidity/temp on demo — grant-channel gold |
| S-3 | **Cold-climate package** | tech scan: industry's best winter offering is a blog post; GWVPP open basins are ice-exposed with zero cold data | REQ-P5 built out + marketed as the northern machine |
| S-4 | **The PowerPal vacuum**: the $2.3k integrated pico unit is DEAD (distributor domain for sale) | receipts | our entry SKU priced into that exact slot inherits its market |
| S-5 | **UL1741/CSA hydro path + fleet telemetry** | receipts: no listed hydro unit exists; no fleet telemetry product exists | REQ-S2 posture + VRM/ESP32 telemetry — two white spaces, one demo unit |
| S-6 | **Sub-100 L/s moat is physics** | GWVPP audit: vortex industry's flow floor ~1,000 L/s; crossover ~100–150 L/s | nobody can follow us down — say so in every pitch, with the arithmetic |
| S-7 | **IP trio on verified-open ground** | IP_DISCLOSURE_FRAME: zero-recoil phase-lock, bank coordination, generation-optimized control all searched-empty; F8 servo = reduction-to-practice narrative | draft disclosures NOW — HydroHammer's pending patent (priority 2020) is a ticking clock |
| S-8 | **The Stuttgart redo** (fluted-pipe ΔP study on the D-6 rig) | Schauberger file: Pöpel 1952 never replicated; 2025 curved-pipe literature says direction is real | cheap instrumentation; publishable either way; founder-lineage story |

---

## PART 2 — GAPS REGISTER (ranked by risk)

**Canon & truth-keeping**
- **GAP-1 (found BY this audit): FULL_SYSTEM_DESIGN is stale canon.** It still states 556 W continuous, single ram swallowing 100 L/s, Pelton 300 mm @ 368 rpm, 33.5 mm nozzles, DN80 rise, η=0.67 flat — all superseded by Findings 1/4/5/10, D-1 (Turgo), the powertrain audit (150 PCD, 754 rpm, 9.5 mm twin jets), and the loss budget. **Fixed this commit: supersession banner added pointing to live sources.** Full rewrite = the X2 pass, now overdue.
- GAP-2: VALIDATION_REQUIREMENTS still has `[X]` placeholders (P0-5) — 25 gates, none quantified. Blocks any claim of "validated."
- GAP-3: Solver ingestion pending — ram_pelton_design still carries the retired η fit; SKU economics not yet restated from v2 curves (queue #4).

**Engineering physics**
- GAP-4: **High-r η decline still under-modeled** (F10: 0.63 @ r=20 vs published ~0.3). v3 needs reopen-against-pressure dynamics. Conservative envelope protects us meanwhile.
- GAP-5: **Bank interaction unmodeled** — 6 rams on one manifold/headstock: surge coupling, phase behavior unknown. Also the evidence base for IP claim (b). Highest-value NEW sim.
- GAP-6: **Hydrology/flow-duration method** — the largest unmodeled site variable (dept audit #13). Every per-site energy number assumes constant flow; real rivers don't. Needs a flow-duration ingestion tool + seasonal output envelope per SKU.
- GAP-7: Egg vessel (D-8) has no engineering drawing: volume/wall calc, cradle loads, tangential inlet geometry, silt-drain, vent/overflow sizing. (Vented = atmospheric = **no CSA B51 exposure** — a quiet win worth recording.)
- GAP-8: Manifold spec written (loss budget) but not yet a drawing; housing clearance/splash-back spec (2–5% at stake) same.

**Regulatory & quality system**
- GAP-9: CSA B51 chamber memo unwritten (path known: ≤42.5 L exemption analysis or CRN bladder vessel — F9). One memo closes REQ-S1.
- GAP-10: DFMEA (REQ-S3) still missing — runaway, burst, freeze, islanding.
- GAP-11: Instrument register/calibration/uncertainty program absent (dept audit #11) — gates ALL future measured claims, including stewardship deltas (S-2).
- GAP-12: Drawings/structured BOM/ECO process (P1 items) — the egg, manifold, and cold package all now need real drawings.

**Evidence & bench**
- GAP-13: **Zero physical measurements company-wide** — every number is sim. The ±10% correlation gate is the single tallest wall between us and customer-facing claims. Cheapest first hardware: TecQuipment H31 calibrated ram bench (receipts) + REQ-P9 dyno day.
- GAP-14: D-6/D-7 rig not yet spec'd as hardware (three-arm conditioning + vortex nozzle + ΔP fluting study + T-002 egg-settling share one rig — one design, four ratified questions).
- GAP-15: Stewardship instrumentation (DO/turbidity/temp) not yet in the demo-unit BOM (~$800 adds the entire S-2 evidence program).

**Market & strategy**
- GAP-16: Canal strategy not yet re-scoped after GWVPP ruling (THE_WINDOW amendment pending: low-flow laterals/structure-prohibited reaches only).
- GAP-17: IP disclosures undrafted while a competitor's patent is pending (S-7 clock).
- GAP-18: Bench roster items unbuilt but cheap and queued: Tesla-valve snifter A/B, magnetic valve return, e-bike-hub dyno map — each a possible publication/IP nugget.

---

## PART 3 — THE SEQUENCED PLAY (what to do, in order)

**Now (digital, $0):** bank-interaction sim (GAP-5, feeds IP) → solver ingestion + SKU restatement (GAP-3) → flow-duration tool (GAP-6) → THE_WINDOW canal amendment (GAP-16) → CSA B51 memo (GAP-9) → egg + manifold drawings (GAP-7/8) → draft the three IP disclosures (GAP-17/S-7).
**First dollars (~$3–6k):** REQ-P9 dyno day + Motenergy/SRNE samples (G-3/G-4) → D-6/D-7/ΔP/T-002 combined rig spec + build (GAP-14, answers four ratified questions at once) → stewardship instrument kit (GAP-15) → TecQuipment-class calibrated ram bench or equivalent (GAP-13 — the correlation gate).
**The compounding asset:** every measured curve those dollars produce lands in S-1 (publish what nobody publishes) — the same spend buys engineering truth AND the marketing moat.

**One-line verdict: the design itself has no unfixable holes — the audit found stale canon (fixed), one physics gap with a guard rail (high-r), and a queue of cheap, sequenced work; the gains ledger says the same water yields up to +50% electric and the same evidence program that unlocks claims also builds the only moats nobody else in the receipts can touch.**
