# Founding Principles Audit — Full Scope

**Date:** 2026-07-16 · **Method:** every founding, vision, ethics, brand, doctrine, and charter document in the repo read; 146 distinct principles extracted with verbatim sources; each audited against the current design (Machine A `engineering/design/DESIGN_BASIS.md`, Machine B `RAM_PELTON_DESIGN.md` + `FULL_SYSTEM_DESIGN.md`, and the decisions in `engineering/GAP_ANALYSIS.md`).

**Verdicts:** ✅ ALIGNED · 🟡 PARTIAL (direction right, work open) · ⚠️ TENSION (design and principle pull against each other) · ❌ VIOLATED (a founding doc's claim or the design breaks the principle today) · ⏸ PREMATURE (business-stage commitment; nothing to audit yet) · 🔒 GATED (speculative claim correctly held behind its own validation gate)

**Bottom line: 42 aligned (1 by founder decision 2026-07-16) · 19 partial · 3 tension · 7 violated · 21 premature · 12 gated.** The violations are all in *documents*, not in the machines — the current design is the most founder-aligned artifact in the repo, and several founding docs now violate their own non-negotiables.

---

## Theme A — Physics, Honesty, Truthful Claims

| Principle (source) | Binding | Audit of current design | Verdict |
|---|---|---|---|
| Physics-first; no over-unity narratives (VISION_FOUNDATION §1) | NON-NEG | Every number solver-derived; energy ledger printed on the system drawing; over-unity content quarantined | ✅ |
| "No magic" foundation (EXEC_SUMMARY) | NON-NEG | Machine B explicitly framed as concentrator, not source | ✅ |
| Numbers not adjectives (GIGA, EVB) | VALUE | Design docs carry numbers with derivations; history note: pre-audit repo violated this wholesale | ✅ |
| No greenwashing/exaggeration (EVB Do's/Don'ts) | COMMIT | Design docs clean. **But `physics_for_kids.md` still tells children "never breaks (infinite lifetime!)" and "Magnetic Water Magic = more power"** — worst remaining offender | ❌ doc |
| Truthful marketing (BOARD_CHARTER) | COMMIT | **`flowcube/Marketing/` still sells "proven 55% efficiency"** — the 55% was a fabricated digital figure; never measured | ❌ doc |
| Validation gates on speculative science (VF §Winter; rnd/SOURCES.md gate; handbook DISCLAIMER) | NON-NEG | Exactly implemented: `speculative/` quarantine, bench A/B slots for φ-blades and fluting, "no production claims unless validated" | ✅ |
| Public performance dashboards from day 1 (VF §3, ALB) | COMMIT | Not yet designed; MPPT telemetry makes it cheap to add | 🟡 |
| Publish successes AND failures (R&D charter) | DOCTRINE | Bench protocol commits to honest null results | ✅ |

## Theme B — Ecology / Water-Kind

| Principle | Audit | Verdict |
|---|---|---|
| Water-kind: run-of-river, screening, return flow (VF §2) | Both machines damless; screened intakes ≤0.3 m/s; 100% return labeled on the drawing | ✅ |
| Work WITH natural forces (EVB CV4, Schauberger doctrine) | Machine B is the purest expression in the whole repo: powered solely by water's own hammer pulse, zero external input, 24/7 | ✅ |
| Fish-friendly: <0.3 m/s, low RPM <600, tip speed <10 m/s, 5–10% bypass flow (R&D charter) | Intake velocity ✓; Machine A runner 299 rpm, tip 4.4 m/s ✓; Machine B wheel 368 rpm, tip 5.8 m/s ✓; **bypass-flow allocation not yet in the site spec** | 🟡 |
| >95% fish survival, propose industry standard (R&D charter HIGHEST priority) | Unmeasurable until field unit exists; design choices all point the right way | 🟡 |
| ≥90% recyclable, LCA, carbon payback <5 yr (VALIDATION_REQUIREMENTS 5, 25) | Steel/HDPE/aluminum-dominant BOM is compatible; no LCA yet | 🟡 |
| Manufacturing/product carbon commitments (EVB) | No manufacturing exists | ⏸ |

## Theme C — Community / Justice

| Principle | Audit | Verdict |
|---|---|---|
| Serviceability, no proprietary lock-in (EVB CV2/CV5) | Deliberate design decision: commodity solar MPPT/battery/inverter, standard bearings, ordinary pipe — repairable at any rural solar shop | ✅ |
| Local manufacturability (EVB CV5; VALIDATION req: ≥80% local components) | Ram body, tank, stand, pipework: local-fab friendly; wheel + PMA need a machine shop — partially local | 🟡 |
| Diesel displacement / energy sovereignty (EXEC, GIGA) | Machine B's market case is literally the 292 diesel-dependent communities analysis | ✅ |
| Co-ownership, 2% revenue, FPIC, training, fair labor, D&I, Ostrom models (VF §3, EVB, GIGA, UP, SC1) | Standing commitments; no entity, revenue, or site yet — nothing to audit, nothing contradicted | ⏸ ×8 |
| Co-design with watershed groups/Indigenous communities (ALB) | Site-survey template should carry community/consent columns — not yet added | 🟡 |

## Theme D — Engineering Quality

| Principle | Audit | Verdict |
|---|---|---|
| Simplicity; minimize moving parts; each component earns its place (EVB CV3) | Machine B: two moving parts in the prime mover, fixed nozzles (spear valves rejected), no gearbox, tank optional. The GAP_ANALYSIS deleted every component that didn't earn its place | ✅ |
| Graceful failure (EVB CV3) | Bypass mode; battery carries loads; runaway-rated shaft/PMA; ram failure = water stops, nothing breaks | ✅ |
| Mechanical over electronic *where feasible* (EVB CV3) | Prime mover fully mechanical; governor function moved to MPPT (electronic) — but it replaces a complex mechanical governor with a $150 commodity part, honoring the *intent* (aging gracefully, field-replaceable) | ✅ note |
| Passive control & robustness (HISTORIC_MILLS lesson 5) | The hydram is the most passive prime mover in existence; MPPT defaults safe | ✅ |
| Site-specific design beats one-size-fits-all (HISTORIC_MILLS lesson 4) | The parametric solver IS this principle as code | ✅ |
| Visible engineering, celebrated mechanism (EVB CV1, MILLS Part 6) | Not yet: turbine house is a closed box. Cheap fix: window/clear panel over the wheel — FlowCube instinct applied to the product | 🟡 |
| Durability 30+ yr (EVB) vs 20–30 (EXEC) vs 25+ (BI) vs "infinite" (PFK) | Founding docs disagree four ways (X4). Design says 25-yr with service. Hydram lineage: Blake rams run a century. Needs one canonical number | ⚠️ docs |
| **75%+ system efficiency** (EVB Mission; VALIDATION req 6) vs 70%+ (North Star) vs 55% "proven" (FlowCube) vs 33% honest baseline | **Physically impossible as written** — the founding docs conflate turbine-component efficiency (75–85% achievable) with system water-to-wire (45–53% best-case). The mission statement's headline number violates its own physics-first non-negotiable | ❌ docs |
| Cost $1,500–2,500/kW (North Star) | Current honest figure 10–50× that; achievable only at volume+scale, never at pico scale. Needs re-anchoring as a long-horizon target with staged milestones | ❌ target |
| 24/7 baseload reliability ≥95% uptime (North Star, EXEC) | The entire design premise; hydram uptime lineage is legendary | ✅ |
| Penstock loss <5% (master spec) vs ≤10% (HB-03) | Docs conflict (X-numeric). Machine B fluted penstock: 3.9% ✓ both. Machine A at DN327: 11.9% — fails both; one pipe size up meets HB-03 | ⚠️ |
| Kaizen, iterate, prototype cycles, ±10% model-vs-prototype gate (VALIDATION 7–9) | Bench ladder = exactly this; the ±10% gate is the bench rig's success criterion | ✅ |
| Crossflow-first turbine doctrine (HB-01) | Machine A honors it; Machine B's Pelton is justified by the head-synthesis exception — doctrine should gain one sentence acknowledging the low-head branch | 🟡 |

## Theme E — Materials

| Principle | Audit | Verdict |
|---|---|---|
| ~~Avoid rare-earth elements~~ (EVB, as originally written) | **RESOLVED 2026-07-16 by founder decision:** ban rescinded; NdFeB permitted with responsible sourcing + magnet recovery at end-of-life (see `docs/business/decisions/DECISION_2026-07-16_rare_earth_materials.md`). Conflict-materials avoidance unchanged | ✅ decided |
| Durable/recyclable/responsibly sourced (EVB, GIGA) | Steel, HDPE, aluminum, LiFePO₄ (cobalt-free — good); no material passport yet | 🟡 |
| Design for disassembly, take-back (EVB, GIGA) | Bolted assemblies, no potting specified — compatible; not yet documented | 🟡 |
| Natural materials for "energetic properties" (Schauberger avatar) | Not adopted; wood/stone/copper on structural merit only | 🔒 |

## Theme F — Brand & Heritage

| Principle | Audit | Verdict |
|---|---|---|
| Honor mills/waterwheels; ancient wisdom + modern precision (EVB mission; MILLS archive) | A tuned 1796 hydram driving a 2026 MPPT is the thesis made physical | ✅ |
| Mill-heritage 7 values (ingenuity, simplicity, durability, nature, local, craft, economic wisdom) | Design maps to all seven; weakest on "craft/visible beauty" (see D) | ✅ |
| Brand attributes: Timeless/Elegant/Resilient/Ingenious/Trustworthy | Trustworthy now has numbers behind it | ✅ |
| **"Four Founding Visionaries" incl. RWR + φ as co-equal founders (BRAND_IDENTITY logo/mission)** | **Directly contradicts VISION_FOUNDATION's own rule** (Winter = exploratory annex, no production claims). BI elevates two ungated hypotheses to founding status. Brand doc needs revision to "three inspirations + gated R&D tracks" | ❌ doc |
| "Consciousness technology" rebrand directive (board_activation_summary) | Contradicts handbook DISCLAIMER and the roadmap's own "90% placebo — do not market" line. Retired by the engineering doctrine | 🔒 |
| Avatar board "Design Review Authority" (visionary_board_charter) | No authority over engineering under the handbook disclaimer; personas remain useful as creative prompts only. Charter should be amended to advisory-inspiration status | 🔒 |

## Theme G — Knowledge & Education

| Principle | Audit | Verdict |
|---|---|---|
| Open knowledge sharing, contribute to open-source hydro tools (EVB) | The repo is public on GitHub with the full solver suite — arguably the strongest single act of alignment to date. **Missing: a LICENSE file** making the openness deliberate | 🟡→✅ |
| Educate on water stewardship; child-facing outreach (EVB CV4, PFK) | Intent aligned; PFK's current text violates Theme A and must be rewritten with the honest numbers (a 40% machine that runs all winter is *plenty* magical for kids) | ❌ doc |
| Training/apprenticeship programs (EVB) | Premature | ⏸ |

## Theme H — Governance & Economics

| Principle | Audit | Verdict |
|---|---|---|
| Design for ROI; systems pay for themselves (EVB CV7) | LCOE is a first-class solver output; the design's economics are stated against diesel/solar honestly | ✅ |
| Sustainability ⇔ profitability inseparable (EVB Vision) | The Machine B niche case is exactly this argument | ✅ |
| Anti-corruption, IFC standards, board oversight, warranty, fair pricing (FUND, BOARD, EVB) | Premature — standing commitments for entity formation | ⏸ ×5 |

## Speculative-side doctrines — status under their own gates

| Doctrine | Own gate | Status |
|---|---|---|
| Spiral/fluted penstock "+5%" (Schauberger; VISIONARY_FRAMEWORK) | Roadmap: "THEORETICAL! validate BEFORE production claims" | 🔒 kept in Machine B design *as geometry*, claims withheld; bench A/B slot reserved — the only honest way to keep it |
| φ blade count / 21-blade Fibonacci (Winter #22) | rnd gate: measured improvement, reproducible | 🔒 PROTOCOL_001 A/B is the gate, unrun |
| Planck/Schumann RPM tuning, consciousness effects | Roadmap itself: "90% placebo — do not market" | 🔒 retired |
| RWR water structuring | RWR plan's own gate: ≥10% plant growth, p<0.05 | 🔒 parked in speculative/; must not appear in brand until passed |
| Tesla 3-phase AC + tight frequency + PFC | proven subset | ✅ PMA is 3-phase; MPPT loading = frequency-optimal operation |
| Tesla bladeless turbine | "60% failure odds — not in roadmap until validated" | 🔒 correctly excluded |
| Callahan paramagnetics ≥5% gate | self-imposed Sept 2026 decision point | 🔒 parked |
| "φ eliminates trial-and-error" (#20) | — | Rejected by handbook doctrine: measurement is the arbiter. The bench exists precisely because trial-and-error with statistics IS the method | 🔒 |

---

## The founding corpus contradicts itself — 9 conflicts needing one canonical answer

| # | Conflict | Proposed canon (for founder ratification) |
|---|---|---|
| X1 | Efficiency: 33 / 45–50 / 55 "proven" / 65 / 70+ / 75+ / 95% across founding docs | Three-number canon: **turbine component ≥70–75%** · **Machine A system 45–53%** · **Machine B system 29–42%**. All other figures retired |
| X2 | Physics-first non-negotiable vs PFK/FlowCube/BI unvalidated claims | Rewrite PFK + FlowCube marketing from the solver; strip "proven 55%" |
| X3 | 3 vs 4 founding visionaries; 80/800 vs 160/1600 counts | **Three inspirations** (Schauberger, Tesla, Winter-exploratory); RWR is a gated product hypothesis, not a founder. Corpus count: state once, cite consistently |
| X4 | Service life 20–30 / 25+ / 30+ / infinite | **25-year design life, 30+ with service program**; "infinite" banned |
| X5 | Community give-back: 2% revenue vs equity/co-op | Both survive as options; board-ratify at entity formation |
| X6 | Flagship 7.5 kW vs 5–50 kW kits | Product ladder from solvers: **B-line 0.2–1.4 kW / A-line 2.5–4 kW / A-uprated 10–15 kW** (site-gated) |
| X7 | Penstock <5% vs ≤10% | **≤10% standard, ≤5% stretch** (HB-03 wins; physics-costed) |
| X8 | Cost $1,500–2,500/kW vs reality | Restate as Year-5+ volume target with staged milestones from the cost model |
| X9 | Avatar board authority vs engineering doctrine | Handbook DISCLAIMER is supreme; board charter amended to "inspiration panel" |

## The unwritten foundations

`FOUNDING_STATEMENT.md`, `VISION_MISSION_VALUES.md`, `NORTH_STAR_METRICS.md`, `MASTER_PLAN.md`, `TAGLINES_MASTER.md` — all title-only stubs. The company's capstone documents were never written; the values live scattered across ETHICS_VALUES_BRAND and VISION_FOUNDATION. Now that the design exists and the contradictions are surfaced, these can be written once, correctly, with the canon above.

## Priority actions from this audit

1. **Ratify the canon table (X1–X9)** — one founder decision session; everything downstream quotes it.
2. **Fix the three violating documents:** rewrite `physics_for_kids.md` honestly, strip "proven 55%" from FlowCube marketing, revise BRAND_IDENTITY to three-inspirations + gated tracks.
3. ~~Decide the rare-earth question~~ — **DONE 2026-07-16:** ban rescinded by founder decision; see decision log.
4. **Add a LICENSE** to make the open-source alignment deliberate rather than accidental.
5. **Write the four capstone stubs** from the ratified canon.
6. **Small design touches from the values:** visible-mechanism window on the turbine house; bypass-flow % and community/consent columns in the site survey; material passport section in the BOM template.

**Closing judgment:** the founders' vision, read in full, is *more* rigorous than the company's own later documents — VISION_FOUNDATION's non-negotiables, the handbook disclaimer, the R&D gates, and the mills archive form a coherent constitution that the current Machine A/B designs obey almost everywhere it's physically possible to obey it. What violates the founding principles today is not the design — it's the marketing layer (PFK, FlowCube, BRAND_IDENTITY) and two impossible numbers (75% system, $1,500/kW) that were written before the physics was done. Fix the documents, ratify the canon, and the company's words and machines will finally say the same thing.
