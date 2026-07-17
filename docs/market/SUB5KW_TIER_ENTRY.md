# Entering Under the Tier — Sub-5 kW Grid-Adjacent Hydro

**Date:** 2026-07-17 · Synthesis of three research sweeps: competitive landscape, feed-in-tariff natural experiments, municipal micro-site niches. Full receipts inline in the research memos; key sources cited.

## Verdict

**The sub-5 kW tier is real, huge by site count, structurally unserved — and it is a graveyard for anyone who enters it as a power project. It is winnable only as a municipal hardware appliance.** Same physics, completely different business.

## Receipt 1 — The tier is where the sites are

- REDAWN screened **8,828 water-network energy-recovery sites** across 6 EU countries: **~89% are <5 kW** (>15 kW = only 3% of locations). [Water 2021, 13:899](https://www.mdpi.com/2073-4441/13/7/899)
- The US Bureau of Reclamation's canal inventory **formally excluded** everything under 5 ft of head or 50 kW — 128 of ~545 drops cut before analysis. The sub-tier was never even counted. [USBR 2012](https://www.usbr.gov/power/CanalReport/FinalReportMarch2012.pdf)
- **17,544 US wastewater plants** discharge 24/7 over drops; exactly **one documented install in our size class worldwide** (1.58 kW, Malaysia). [EPA CWNS 2022](https://www.epa.gov/system/files/documents/2024-05/2022-cwns-summary.pdf), [Water 2021, 13:3259](https://www.mdpi.com/2073-4441/13/22/3259)
- Incumbent floors: InPipe Energy ~20 kW at $15–18k/kW; Emrgy 5–25 kW at $3–4k/kW; Rentricity 2–11 kW custom. Below that: nobody productized.

## Receipt 2 — The graveyard warning (why the tier is empty)

The natural experiment ran three times. The UK paid hydro ≤15 kW **~20p/kWh, RPI-linked, guaranteed 20 years** (≈28–35¢ today) from 2010–2016 — the most generous micro-hydro tariff ever offered. Result: ~650 sub-50 kW installs in nine years nationally, community weir schemes all clustering at **50–100 kW minimum**, and new micro registrations ceased the moment the tariff dropped to 8p. Japan (¥34/kWh) and Switzerland (KEV) produced 50–200 kW markets, never <10 kW. [Ofgem FIT data](https://www.ofgem.gov.uk/sites/default/files/2024-12/FIT_annual_report_SY14.pdf), [DECC Evidence Review](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/456181/FIT_Evidence_Review.pdf)

The killers were never revenue: **size-invariant fixed costs** (permitting, fish pass, civils, grid application) and **O&M that doesn't scale down** — £2,200/yr on a 5 kW UK system is 12.5p/kWh before anything else. [Renewables First](https://renewablesfirst.co.uk/renewable-energy-technologies/hydropower/hydropower-learning-centre/performance-and-financial-analysis/)

**Conclusion: selling kWh at sub-5 kW is disproven at any plausible tariff. The tier isn't empty of opportunity; it's empty of *projects*, because a 2 kW project carries a 50 kW project's overhead.**

## Receipt 3 — The playbook that works at this size (proven by adjacent products)

Cities already buy sub-5 kW energy hardware, at prices per kW that hydro developers would call insane — when it's an **appliance bought on ops-savings and sustainability line items, not a power project**:

- **Beam Global EV ARC** — a 4.3 kW solar unit: NYC's seventh repeat order, **71 units at ~$74,600 each, no RFP** (GSA schedule). [Beam](https://beamforall.com/beam-global-receives-5-3m-order-from-new-york-city/)
- **Bigbelly** solar compactors: ~$7,860/unit, 75 units passed a city consent agenda without debate. Justified by the climate plan, paid back in ops.
- The machinery that makes this work: **micro-purchase thresholds** (<$10–25k = manager's signature, no bid), **$25–35k innovation-office pilots**, **cooperative purchasing** (Sourcewell/GSA — 4–8 week cycles vs 22-month RFPs), and **IRA direct pay** giving municipalities the 30% ITC in cash.

And the regulatory stack at this size is uniquely clean: **FERC qualifying-conduit NOI — free, ~45–60 days, filed as small as 2 kW** ([FERC](https://ferc.gov/how-file-notice-intent-construct-qualifying-conduit-hydropower-facility)); interconnection via the **technology-neutral UL 1741/IEEE 1547 solar-inverter path** (≤$100 fee, days–weeks; Emrgy already rides it); net metering includes hydro in WA/OR/CA/NY/VT/BC/ON.

## The product this demands (design requirements, from evidence)

1. **Appliance, not project:** one SKU per site class, priced **under $25k installed** (below RFP thresholds), ideally a pilot config under $10k.
2. **Zero construction:** drops into an existing structure (PRV vault, effluent channel, canal check) in a day, no concrete, no crane — the Beam/Bigbelly value proposition transplanted to water.
3. **O&M near zero:** the £2,200/yr number is the true enemy. Sealed bearings, no scheduled service <12 months, remote telemetry via the MPPT, swap-not-repair modules.
4. **Certification lives in the inverter:** rectified PMA into a listed UL 1741 SB solar inverter — the documented PowerSpout/Emrgy path. No custom electrical certification.
5. **Paperwork as product:** templated FERC conduit NOI + pre-filled Level-1 interconnection + grant boilerplate (WaterSMART, CWSRF, EECBG) shipped in the box. The customer buys the machine; the machine brings its own permits.

## The three beachheads, ranked

| Beachhead | Why | Numbers |
|---|---|---|
| **1. WWTP effluent channels** | 17,544 US plants, 24/7 clean-ish flow, 1–4 m drops, energy = 30–40% of municipal bills, one install worldwide in-class | behind-the-meter at 8–30¢ retail; ~3 kW × CF 0.7 ≈ 18 MWh/yr ≈ $2.4k/yr + ITC + sustainability-plan value |
| **2. PRV vaults (drinking water)** | 89% of recovery sites are sub-5 kW; incumbents bottom at 20 kW; continuous flow; note: pressurized pipe → needs the PaT/inline variant ("Machine C"), not open-channel units | InPipe charges $15–18k/kW one tier up — massive pricing umbrella |
| **3. Irrigation canal checks** | Volume play — tens of thousands of drops ORNL counted down to 0.6 m; district = fleet buyer; Colorado's ACRE3 program already grant-funds ag hydro | seasonal (CF ~0.25–0.5); price to it; Emrgy validated district appetite one tier up |

Stormwater/culverts: **validated dead end** (storm-sized flows give ~2% capacity factors). Skip.

## Fit to our machines

- **Machine A (crossflow, 3–10 m)** → WWTP outfalls with taller drops, canal drop structures. Boxed, standardized, inverter-native: this is the "weir box appliance."
- **Machine B (ram→Pelton, 0.5–2 m)** → stays the off-grid/stream product; in-town its role is the odd low-head channel site.
- **Machine C (inline PaT/Pelton for pressurized pipe)** → new variant required for the PRV beachhead. Design study needed; Rentricity's Cornell PaT partnership shows the component path.

## GTM sequence (evidence-patterned)

Pilot with one water/wastewater department at <$25k via innovation-office or micro-purchase → consent-agenda repeat orders across the department's sites → Sourcewell/GSA listing → single-utility behind-the-meter savings contracts at fleet scale. Sell avoided construction, ops savings, and the climate-plan line item — **never sell kWh.**
