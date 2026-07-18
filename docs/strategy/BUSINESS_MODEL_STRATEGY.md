# Business Model & Strategy — Get In Where We Fit In

**Date:** 2026-07-17 · **Status:** founder-directed strategic frame, v1.
**Thesis in one line:** the world's most numerous water-power sites were never captured because the enabling technology didn't exist — it does now, and we build the market for them instead of fighting incumbents for theirs.

---

## 1. Product architecture (locked, per founder)

Three SKUs, two modules, one factory:

| SKU | Composition | Site | Role |
|---|---|---|---|
| **Kit** (generation cartridge alone) | wheel + PMA + MPPT + electronics, short penstock | site *has* fall (≥2–3 m or existing drop structure) | efficient direct capture, ~45–50% w2w |
| **Kit + Ram** (combined) | same cartridge + ram front-end module | flat sites, 0.5–2 m fall | head synthesizer — unlocks zero-rated sites |
| **Ram alone** | tuned ram, no generation parts | customer wants water, not watts | the 230-year proven market (Rife/AIDFI class); cash flow + lead generation |

The generation cartridge is identical across SKUs 1–2; the ram is identical across SKUs 2–3. Every site's configuration is computed by the solver from two field measurements. **Custom design per site, zero custom engineering per site** — the solar industry's trick applied to water.

## 2. The "why now" — what prohibited waste-energy capture before, and what unlocked it

This is the heart of the strategy. Each historical blocker has flipped within roughly the last decade:

| Then (why sites stayed dead) | Now (the unlock) |
|---|---|
| Mechanical governors — costly, fiddly, the classic failure part | **MPPT electronic loading**: a $150 solar charge controller governs the turbine for free |
| Custom engineering study per site ($1000s, weeks) | **Parametric solver**: two measurements → full dimensioned config in seconds (already in the repo) |
| Grid interconnection or nothing; certification per device | **Solar's DC ecosystem**: UL-listed inverters carry the certification; batteries make off-grid the default; FERC conduit NOI is free and 45 days |
| Lead-acid batteries — 3-year life, constant care | **LiFePO₄** — 15-year, maintenance-free storage |
| Cast/welded fabrication; foundry economics | **CNC, 3D printing, molded composites** — Cadens/ORNL demonstrated $2.8k/kW micro-hydro via additive manufacture |
| Finding sites = walking creeks with a level | **LIDAR/DEM + satellite + public inventories** — drops are findable in software (ORNL already CNN-detects canal drops from imagery) |
| Monitoring = truck rolls | **Cellular/LoRa telemetry** riding the MPPT's data for free |
| Reaching scattered rural buyers = impossible economics | **Content channels** — the homestead/off-grid audience is aggregated on YouTube; the authority vacuum (Home Power magazine, dead 2019) is unclaimed |

**Strategic statement:** the incumbents' categories were shaped by the *old* constraint set (big sites, arrays, projects, engineers). We are the first mover shaped entirely by the *new* one. That is what "build our own market" means concretely — not fighting for their sites, but activating the millions of sites their cost structures still can't see.

## 3. The business model

**Who pays, in order of arrival:**
1. **Off-grid/remote owners** (homesteads, lodges, camps, farms) displacing diesel at $0.50–2.00/kWh — direct, full-margin hardware sales. The beachhead.
2. **Water-adjacent businesses** (hatcheries, estates, ranches) buying ops savings — direct + dealer.
3. **Institutions** (districts, municipalities, Indigenous energy programs) — the appliance playbook: sub-threshold pilots, consent-agenda repeats, grant stacking (Wah-ila-toos/REACHE, REAP, WaterSMART). Later, at fleet scale.

**Revenue streams:**
- Hardware (3 SKUs + drive-pipe kits + winterization module) — the core.
- **Site activation as the product wrapper**: the customer buys "this spot on your land, producing" — survey app + config + kit + permits-in-box as one price. The solver and paperwork templates make this nearly zero-marginal-cost and impossible for a parts-seller to match.
- Install/commissioning (own crews early — HDD-adjacent skills apply — then certified installer network).
- Telemetry/monitoring subscription (optional, cheap, sticky; also feeds the performance dataset that becomes the marketing).

**Cost structure discipline:** standard modules only; no per-site engineering ever; certification inherited, not earned; marketing = content, not ads.

## 4. The unconventional moves (cunning, in order of leverage)

1. **The Site Atlas.** Use public LIDAR/DEM, hydrography, canal and barrier inventories (the same public data ORNL and AMBER used) to **pre-map candidate drops before anyone asks** — starting with Alberta and the beachhead regions. The atlas becomes a proprietary data asset: we walk into a region already knowing where its unused energy is. Nobody in the industry owns this at micro scale. It also turns marketing inside-out: instead of waiting for buyers, we can tell a landowner "your property has a site."
2. **Own the vacated authority channel.** Home Power magazine's death left off-grid hydro with no trusted voice. Honest numbers + real builds + the solver as a free public tool = the channel becomes the brand. Free site-checks generate the lead list.
3. **Permits in the box.** Templated conduit NOIs, pre-filled interconnection forms, grant boilerplate. The paperwork moat costs us nothing after the first template and kills the #1 historical project-killer for every customer.
4. **Ride the ram's existing trust network.** Rife-style dealers and AIDFI-style NGOs already reach our customers with our keystone component. Partner, don't rebuild.
5. **Fleet-by-stealth.** Every telemetry-connected unit reports real performance. After ~50 units, we own the only honest field dataset in the category — which becomes the institutional sales weapon (verifiable claims vs the industry's vaporware norm).

## 5. Compete vs. build — the explicit answer

We do **not** compete with the big boys on their ground: no arrays, no 50 kW+ projects, no municipal RFPs at first, no venture-scale burn. Their cost structures cannot follow us down (Emrgy needs arrays; Turbulent needs concrete; Natel needs 300 kW), and ours cannot follow them up yet. Contact with their tier happens later, if at all, from below — via fleet aggregation of small sites — on ground the atlas and the dataset have already prepared.

**Sequence:** Ram-alone + Kit-alone sales now (proven markets, immediate revenue) → Kit+Ram flat-site activation (the new category) → institutional fleets (the appliance playbook) → only then, optionally, the tier fight — armed with data, molds, and margin instead of hope.

## 6. What must be true (the honest gates, unchanged)

The strategy inherits the validation ladder: η_ram coupling holds up (digital bench: MOC simulation, then physical), the cartridge hits its numbers, first ten installs perform to spec on telemetry. Every strategic claim above dies or lives by those three gates — the business model is designed so that even the smallest validated version (ram-alone sales) is a real business while the gates are cleared.

*Supersedes the four-machine commercial framing; A/C/D remain design assets. Companion docs: MARKET_MAP_LOW_HEAD.md, SUB5KW_TIER_ENTRY.md, THE_WINDOW.md, DESIGN_HISTORY_AUDIT.md (decision queue D-1..D-5 still open).*
