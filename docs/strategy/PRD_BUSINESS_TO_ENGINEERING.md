# PRD — Designing and Building to the Business Model

**Date:** 2026-07-18 · **Founder directive:** "design and build our products to this business model so it works for what is required."
**Method:** every requirement below is *derived from* a ratified business commitment (Alberta launch plan, Canada grant model, appliance strategy, canon X1–X9) — not from engineering preference. Each carries its source, its acceptance test, and its phase gate. This document starts the requirements-traceability matrix the department audit found missing.

## A. Safety & regulatory requirements (P0 — before any pitch or install)

| Req | Requirement | Derived from | Acceptance |
|---|---|---|---|
| **REQ-S1** | Air chamber engineered as a pressure vessel: design calc incl. simulated transient peaks (MOC sim output), relief valve spec'd, proof-test plan, **CSA B51 compliance pathway documented** (or re-design below B51 thresholds — volume×pressure exemption analysis first: a smaller chamber may legally avoid vessel classification; the sim's chamber-sizing study feeds this directly) | Alberta legal install (ALBERTA_LAUNCH_PLAN Part 1C) | stamped calc or documented exemption |
| REQ-S2 | Electrical package: CSA-certified components end-to-end (cCSAus inverter UL1741-SB class, C22.1 wiring methods), SPE-1000 field evaluation plan for the assembled unit | Alberta permits; appliance model | inspection pass on demo unit |
| REQ-S3 | DFMEA covering: turbine runaway (rated 1.8×N), chamber overpressure, water-hammer on delivery leg, freeze/frazil, drive-pipe burst, islanding (grid variants) | grant-channel due diligence; EVB graceful-failure value | reviewed FMEA with mitigations closed |
| REQ-S4 | DFO-ready environmental dossier per product (damless, ≤0.3 m/s screen, 100% return) + Alberta Water Act pathway memo | 3–5 yr timeline compression (launch plan) | pre-filed memo acknowledged by AEPA |

## B. Product requirements from the appliance model (P0/P1)

| Req | Requirement | Derived from | Acceptance |
|---|---|---|---|
| REQ-P1 | **Install ≤ 1 day, 2 people, zero concrete, zero crane** — skid + earth anchors + surface pipe | appliance thesis; Bigbelly/Beam pattern | timed demo install |
| REQ-P2 | **Sub-$25k installed price** for the pilot SKU (below municipal/band micro-purchase thresholds) | SUB5KW_TIER_ENTRY GTM | costed BOM at target |
| REQ-P3 | **O&M: no scheduled service < 12 months**; swap-not-repair modules; any rural solar shop can service the electrical | UK FIT autopsy (O&M killed the tier); EVB serviceability | service manual + spares kit defined |
| REQ-P4 | Telemetry standard on every unit (MPPT cloud data), feeding the public dashboard + performance dataset | dataset moat; VF §3 dashboard commitment | live dashboard on demo |
| REQ-P5 | **−40 °C northern package**: heated/insulated ram dog-house, buried/insulated delivery, LiFePO₄ heated enclosure, cistern-integration kit (float valve, overflow) | Canada grant model; northern conditions | winter survival of demo season |
| REQ-P6 | **Ram bank scaling** as the standard growth path (per digital-bench Finding 1: ~18 L/s per 300 mm ram) — manifold design, N-ram skid layouts, per-ram isolation valves | SIM_RESULTS finding 1; SKU ladder X6 | bank of 2 demo'd |
| REQ-P7 | Permits-in-box: templated Water Act memo, DFO self-assessment, interconnection form (if grid), grant boilerplate shipped with product docs | fixed-cost kill strategy | complete pack for one province |
| REQ-P8 | Load-module menu implemented: battery/loads · heat-dump (northern) · productive-use kit (program channel) · (miner-heater only in private channel) | load-module strategy + channel rules | heat-dump module spec'd for demo |
| **REQ-P9** | **Generator/wheel speed-match analysis at BOM freeze**: 754 rpm (150 mm PCD @ r=6 site) sits below benchmark PMG band (1,200–2,400 rpm). Resolve via smaller PCD (100 mm → 1,131 rpm), kV/winding selection into MPPT window, or (last resort) belt step-up — decided by dyno data | POWERTRAIN_AUDIT §3 (founder challenge 2026-07-19) | dyno curve showing MPPT lock across seasonal head range |

## C. Engineering-system requirements (the audit's fix program, phased)

**P0 — before any external claim or community pitch (now → 3 mo):**
1. Unit tests + input validation + CI for all four solvers (audit #5 — a crash bug was already caught once).
2. Architecture-of-record enforcement: supersession banners on HYBRID_SYSTEM_MASTER_SPEC/TECH_SPEC; canon numbers only in live docs (X1/X2).
3. CAD canonicalization: ONE params.json, `validate_repo.py` run in CI against the real tree.
4. REQ-S1 exemption analysis (chamber sizing below vessel thresholds if possible — cheapest compliance is not being in scope).
5. Requirements traceability skeleton: this PRD + VALIDATION_REQUIREMENTS quantified (replace every `[X]`) and mapped to tests.

**P1 — before first sale/install (3–9 mo):**
6. DFMEA (REQ-S3); structured BOM with part numbers/revs/suppliers incl. winter items; ECO process (one-page, founder-signed).
7. Drawing package for the demo unit (toleranced, title-blocked, released).
8. Instrument register + calibration records + uncertainty budget for the bench (efficiency claims carry ±bounds from here on).
9. Drive-pipe length study + valve tuning map + chamber sizing (SIM queue 1–3) → SKU numbers restated from sim.
10. IP invention disclosure: the coupled ram-bank→headstock→jet operating-point method, dated and witnessed.

**P2 — before scale/fleet (9–24 mo):**
11. FEA on runner/shaft at runaway; standards-compliance matrix completed; model v2 + bench correlation (±10% gate); reliability/service-life plan; FAT/SAT commissioning records; O&M manual.

## D. What this changes about the product, honestly

The digital bench has already forced one restatement: **per-ram output at the reference site is ~100–120 W electric, not 556 W** — the B-Standard offer becomes a ram-bank (or the drive-pipe study recovers appetite per ram). All public numbers wait for SIM queue 1–3 + the solver re-run. This is the requirements process working exactly as the business model needs it to: the grant channel and municipal buyers will diligence our claims; the only survivable posture is that every number already survived us first.

*Traceability continues in: ENGINEERING_DEPT_AUDIT (gaps), SIM_RESULTS_RAM_MOC (evidence), DECISION log (authority), VALIDATION_REQUIREMENTS (gates — quantification pass queued as P0-5).*
