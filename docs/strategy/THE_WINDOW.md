# The Window — Competing on Design: Energy-Waste Capture

**Date:** 2026-07-17 · Synthesis of the full market/competitive research corpus + solver arithmetic (`tools/design/`). This is the design-led wedge against the funded incumbents.

## The window, named

**Every low-head drop structure on earth is built with an energy *dissipator* — a stilling basin, baffle blocks, riprap — engineered on purpose to destroy exactly the energy we want.** Canals, wastewater outfalls, dam compensation-flow valves, industrial discharges: the energy is already being wasted *by design*, the civil structure is already built and paid for, and destroying that energy actually costs the owner money (scour, erosion, basin maintenance).

**The product thesis: replace energy dissipators with energy capturers.** Same footprint, same water, no new civil works — and capturing the energy *reduces* the destructive forces the owner currently pays to manage. That's not a power project; that's an infrastructure upgrade with a payback.

## Why the big boys are beatable on design — the physics

Canonical contested site: 2.0 m drop, 1.0 m³/s → **19.6 kW gross**.

| Technology | Real water-to-wire | Power captured | Capex basis | 25-yr energy @ $0.10 |
|---|---|---|---|---|
| Turbulent vortex | **~50%** (field survey: 67% of 36 plants run <60%; MDPI Energies 2023) | 9.8 kW | ~$9k/kW retail (E4C) | $773k |
| Emrgy module | ~30% (kinetic-class capture) | 5.9 kW | $3–4k/kW | $464k |
| Archimedes screw | ~70% (plus gearbox O&M, crane install) | 13.7 kW | ~$6.5k/kW | $1,082k |
| **Boxed draft-tube propeller (ours)** | **~75%** | **14.7 kW** | **$2.8k/kW proven feasible** (Cadens/ORNL: 6.5 kW 3D-printed plant, $18k total) | **$1,159k** |

**Same site, our box earns ~$64k more than a vortex over 25 years and costs half as much to install.** The incumbents aren't protected by better machines — they're protected by having *any* productized offer. Their designs each carry a structural weakness:

- **Turbulent:** the vortex basin is poured-in-place concrete — a construction project per site — and the vortex concept itself is the efficiency ceiling (most field plants under 60%). They also charge €750 just to study your site.
- **Emrgy:** modules avoid civils but capture kinetic-class energy — low yield per site — and they only sell multi-MW arrays with district-scale counterparties.
- **Screws:** genuinely efficient but multi-tonne custom steel, cranes, gearboxes (the O&M item), and $/kW that worsens as size shrinks.
- **Natel:** excellent machine (94% peak, fish-safe thick blades), wrong tier — 300 kW floor, project business.

## The five design moves that open the window

1. **Draft tube or die.** At 1–3 m head, half the available energy leaves as velocity below the runner. A properly designed molded draft tube is the single highest-value piece of hydraulic engineering at this scale — it's why a boxed propeller at 75% beats a vortex at 50%. This is pure design skill, zero exotic physics, and our solver methodology extends to it directly.
2. **Manufacture, don't fabricate.** The Cadens/ORNL result ($2.8k/kW via large-format 3D printing; ORNL's whole SMH program) proves the cost collapse comes from making turbine + flume + draft tube as **molded/printed composite modules** instead of welded steel and site concrete. One mold amortizes across every unit; incumbents re-engineer per site.
3. **Fish-safe without screens, Natel-style.** Thick blunt leading edges → no fine screens → +10% net energy and the biggest O&M item deleted. Published design direction; nobody has brought it below 100 kW.
4. **Certification lives in the solar inverter; permits live in the box.** Rectified PMA → UL 1741 SB string inverter (the documented PowerSpout/Emrgy path), templated FERC conduit NOI (free, 45–60 days, filed as small as 2 kW), pre-filled Level-1 interconnection. Paperwork as product.
5. **Sell the dissipator replacement, not the kWh.** The pitch to a district/city: "your drop structure destroys 15 kW around the clock and erodes itself doing it; this box bolts into it in a day, harvests 75% of that, and reduces basin scour." Ops + infrastructure framing (the Bigbelly/Beam pattern) with energy as the payback engine.

## The product line this defines

| Machine | Envelope | Market |
|---|---|---|
| **Machine D — "the Box"** (new flagship) | molded draft-tube propeller unit, **5–25 kW, 1–3 m drops, 0.5–2.5 m³/s**, drop-in to existing check/outfall/weir structures | head-to-head vs Emrgy/Turbulent on design: 1.3–1.5× their energy at ⅓–½ their install cost |
| Machine A (crossflow) | 2.5–15 kW, 3–10 m | streams, taller outfalls, estates |
| Machine B (ram→Pelton) | 0.2–1.4 kW, 0.5–2 m natural fall | off-grid diesel displacement (unchanged) |
| Machine C (inline PaT) | 1–20 kW pressurized | PRV vaults, compensation-flow valves |

**Energy-waste capture is the unifying brand across all four**: dissipated canal drops (D), wasted pressure (C), unpowered weirs (A), dead flat rivers (B). One company: *we capture the energy the water system already throws away.*

## Honest risks

Vortex/Emrgy comparative efficiencies are from field surveys and class physics, not head-to-head tests — the claim must eventually be measured on a shared site basis. The $2.8k/kW manufacturing figure is one demonstrated data point (Cadens), not our BOM. Draft-tube design at 1–3 m is genuinely hard engineering (cavitation, part-load behavior) — it is *the* R&D bet of Machine D. And Emrgy's EaaS financing model is a moat independent of hardware; matching it eventually requires capital.

## Next design work (in order)

1. **Machine D concept study:** extend the solver with a propeller/Kaplan module + draft-tube recovery model; size the standard box for the 1–3 m × 0.5–2.5 m³/s envelope; runner and draft-tube geometry from the same first-principles discipline as A/B.
2. **Manufacturing cost model:** molded flume/draft tube + printed runner vs welded steel — target BOM to hit ≤$2.5k/kW at 10 kW.
3. **Machine C PaT selection study** (Cornell-style pump-as-turbine, off-the-shelf).
4. Digital bench (water-hammer sim for B; CFD for D's draft tube) per the digital-first validation directive.
