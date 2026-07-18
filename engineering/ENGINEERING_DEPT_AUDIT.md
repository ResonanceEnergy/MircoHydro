# Engineering & Testing Department Audit

**Date:** 2026-07-18 · Full sweep of every engineering work product, system, and tool across all design generations. Graded EXISTS (A–F) / PARTIAL / MISSING. Companion: `../docs/strategy/PRD_BUSINESS_TO_ENGINEERING.md` (the fix program, mapped to the business model).

## Headline findings

1. **Three design generations coexist without an architecture-of-record.** Gen 0 (φ/resonance experimental rig + its automation), Gen 1 (honest crossflow rebaseline), Gen 2 (ram→Pelton Machine B) each have live artifacts that contradict each other. RESOLVED as of this audit by founder ratification: **Machines A/B (Gen 1/2 designs, canon numbers) are the products; Gen 0 is the experimental annex whose metrics (T-001/T-002) now run inside the digital bench (D-4).** Superseded specs (HYBRID master spec, TECH_SPEC) get supersession banners rather than deletion.
2. **The QMS layer is grade F — nearly absent.** No FMEA, no risk register, no change control (CHANGELOG empty), no design-review records, no structured BOM, no supplier/material specs, no standards-compliance matrix, no calibration program.
3. **The most acute single gap is safety-regulatory: the air chamber is a pressure vessel** (spec'd 150 L PN10) with **zero pressure-vessel engineering** — no design calc, no relief valve, no proof/burst plan, no CSA B51 pathway. This legally blocks Alberta installation and is now REQ-S1 in the PRD.
4. **Zero automated tests on the design toolchain.** The audit caught a crash bug in `ram_moc_sim.py` mid-development (undefined attributes — since fixed and the tool now runs and is calibrated), proving the point: the canonical solvers guard the company's claims and have no guardrails themselves.
5. **CAD is sprawl, not system:** 6 divergent `params.json` copies against a written single-source rule; STEP "models" are 29-byte placeholders; zero toleranced dimensions anywhere; no drawings, no revision index. The governance docs (REPO_RULES, validate_repo.py, CI) exist and are good — they're just not enforced against the real tree.
6. **Requirements aren't requirements yet.** VALIDATION_REQUIREMENTS' 25 gates are well-shaped but unquantified (`[X]` placeholders) and unmapped to any test. No traceability matrix exists.
7. **What's genuinely strong:** the adversarial-physics culture (GAP_ANALYSIS, physics_audit, DESIGN_BASIS — grade A), the Gen 0 automation/release skeleton (importer, evidence autofill, repo validator, CI, semver — grade B), and now a running, calibrated transient simulator. The department's core is real; its wrapper is missing.

## Detailed grades

| System | Grade | Key evidence |
|---|---|---|
| Design solvers (crossflow, ram-Pelton, MOC sim) | B / C+ / B− (post-fix) | first-principles, documented; **no unit tests, no input validation, no CI** |
| CAD system | D | 6 divergent params.json; placeholder STEPs; no tolerances/GD&T/drawings; archive sprawl |
| Test infrastructure (Gen 0) | C− | automation layer B; but pass/fail thin (T-003/T-004 have none), raw data = synthetic stubs, calibration = blank templates, no uncertainty budgets, no instrument register |
| Specs & requirements | C | 25 gates exist but unquantified + unmapped; superseded specs still live beside canon |
| QMS (FMEA, ECO, BOM, reviews, suppliers, safety, standards matrix) | **F** | effectively none; BOM = markdown tables missing known items (winter package, battery heat) |
| Doc/release governance | B− | REPO_RULES, MANIFEST/semver, validate_repo, CI — good skeleton, unenforced |

## Top 15 gaps, ranked by risk (full detail in PRD backlog)

1. Pressure-vessel safety package (air chamber → CSA B51) — legal blocker
2. DFMEA/PFMEA (runaway, burst, hammer, freeze, islanding)
3. Standards-compliance matrix (CSA C22.1, UL 1741-SA/IEEE 1547, B51, IEC 60193/61362)
4. Requirements traceability matrix (quantified reqs ↔ design ↔ test ↔ result)
5. Unit tests + input validation + CI for solvers (bug already caught once)
6. Architecture-of-record (ratified above; enforce with supersession banners)
7. Structured BOM with part numbers/revs/suppliers (+ the missing winter items)
8. Engineering change control (ECO/ECN + revision index)
9. CAD canonicalization (one params.json; real solid models; enforce validate_repo)
10. Drawing standards (tolerances, GD&T, stack-up, title blocks, release)
11. Calibration & metrology program (instrument register, traceable certs, uncertainty budgets)
12. FEA/structural validation (shaft/runner at runaway, vessel)
13. Hydrology/flow-duration method (the largest unmodeled site variable)
14. Design-review + V&V records (gates named, no records)
15. IP invention disclosure for the coupling math (dated, witnessed; currently nothing)

Honorable mentions: reliability/service-life test plan, O&M manual + spares kit, commissioning FAT/SAT records, governor/overspeed control design, fish-screen compliance record.
