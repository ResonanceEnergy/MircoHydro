# Engineering — Technical Deep-Dive

Reviewed file-by-file, July 2026. This README is the map of what's real, what's template, and what to build next.

## The product concept

Crossflow (Banki-type) turbine → direct-drive permanent-magnet synchronous generator, packaged as a hybrid plant: hydro primary + 5 kW PV + 2 kW wind + 15 kWh LiFePO₄ on a 48 V DC bus, 10 kW bidirectional inverter, IEEE-1547 grid-tie option, fish-safe intake (<0.3 m/s approach). Design point cited: 150 L/s @ 5 m head. Target: $110–135k installed, 25-year life.

## What's real in this tree

### `specs/`
- **`HYBRID_SYSTEM_MASTER_SPEC.md`** — the cornerstone document. Its "Reality Check" section is correct, honest hydro engineering: full loss cascade (entrance Kₑ=0.5, Darcy-Weisbach friction, part-load derating, generator + converter losses) concluding **actual system efficiency ≈ 33%, not the 62% claimed elsewhere**. Use this as the baseline for everything.
- **`EFFICIENCY_OPTIMIZATION_PLAN_65PCT.md`** — legitimate, ROI-framed upgrade path from 33% → ~48.5% → aspirationally 65% (screen automation, larger penstock, VFD, higher DC bus). The 33→48.5% portion is credible; treat 65% as a stretch goal requiring test data.
- `VALIDATION_REQUIREMENTS.md`, `SIMULATION_FRAMEWORK.md`, `RND_ROADMAP_AND_FINDINGS.md` — blank/bracketed templates, never filled in.
- `flowcube/` — a transparent vortex-visualization display chamber (museums/schools). Physically buildable; ignore the "sacred geometry proof" marketing framing.
- `STELLITE_MATERIALS_STRATEGY.md` — materials notes (Stellite hardfacing, basalt composites); desk research.

### `cad/` and `product/`
- **~7 unique FreeCAD parametric macros** (`build_diffuser`, `build_nozzle`, `build_vanepacks`, `build_retainer`, `build_assembly`, `export_batch`) driven by `params.json`. Genuinely functional Python-for-FreeCAD with defensive coding (wire-closure checks, revolve retries). The originals were duplicated ~10× across the old workspace; this is the deduplicated set.
- **6 real DXF files** — 2-D profiles (diffuser curve, vane sketch, OD/ID circles). No assemblies, no tolerances/GD&T, no manufacturing drawings.
- **Scale mismatch (critical):** `params.json` describes a **~90 mm-diameter desktop demonstrator** (diffuser OD 82 mm, nozzle throat 9 mm). The specs describe a **10–15 kW plant with ~1.2 m runner**. These are two different machines. The CAD models the desk toy, not the product.
- **Blade geometry (critical):** `build_vanepacks` makes flat rectangular vanes patterned in a circle — a placeholder swirl vane, not a crossflow runner. A real Banki runner (curved blades, inlet/outlet angles from standard correlations) has not been modeled.
- No CFD, FEA, or simulation output exists anywhere (no mesh/case/result files of any kind). All "CFD validated" claims are prose.

### `protocols/`
- **`PROTOCOL_001_PHI_TURBINE_DESKTOP_TEST`** — the best engineering artifact in the project: a properly designed ~$130–355 A/B bench test (3D-printed 100 mm runners, submersible pump, flow meter, tach, two-sample t-test, α=0.05, stated H₀/H₁). **Never executed.** Running it (reframed as "characterize the runner"; treat the 21-blade-Fibonacci hypothesis as a genuine open question) would produce the project's first real datum.

### `microhydro-v1/` and `microhydro-v1-sot/`
The "MicroHydroV1" packaging/automation trees (SharePoint/run-ID/evidence-workbook tooling, DAQ logger configs, calibration templates). Note: the `tests/raw/2026-01-22_Run1_*` CSVs (jet coherence 0.93–0.945, ripple 6.8–7.1 mm, power 10.5–11.3 kW) each contain **exactly two rows of round example values** — they are template rows, not measurements. No prototype existed on that date.

### `tests/`
Test-campaign scaffolding from the old Engineering division. Structure is fine; data is absent.

## What was removed from this tree

- Fabricated validation: scripts that print hardcoded efficiency numbers (0.42→0.55, "infinite design life", "99.999999% reliability") are in `../archive/automation/` with their JSON/log outputs. None of them compute physics.
- Unvalidated-science specs (φ-optimization with invented η_φ=1.12 multiplier, Schumann-resonance RPM tuning, RWR magnetic water structuring): moved to `../speculative/`.

## Engineering to-do (priority order)

1. **Run PROTOCOL_001.** Cheap, designed, waiting. First real number wins.
2. **Model a real crossflow runner** at ONE chosen scale; reconcile CAD with spec. Check: by the repo's own cascade, 150 L/s @ 5 m nets ~2.4 kW — the 10–15 kW claim needs ~5–7× more Q·H.
3. **One honest CFD run** (OpenFOAM, nozzle + runner, steady-state torque/efficiency) and one runner FEA. Days of work; replaces all fabricated validation.
4. **BOM + electrical:** select a certified (UL-1741/IEEE-1547) inverter, size wiring/protection, real thermal calc.
5. **Anchor all claims to measured or computed numbers.** The honest story — 33% baseline, 48.5% optimized, real bench data — is fundable. The inflated one is not defensible.
