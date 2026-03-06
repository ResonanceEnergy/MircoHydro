"""
REGULATORY SCOUT AGENT
Permit research, regulatory compliance, water rights, environmental laws.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def permit_requirements(location, project_size):
    """Research required permits for micro-hydro project"""
    
    prompt = f"""Research permit requirements for micro-hydro project:

**Location:** {location}
**Project Size:** {project_size}

**PERMITTING REQUIREMENTS REPORT**

---

**FEDERAL PERMITS:**

**1. FERC (Federal Energy Regulatory Commission)**

**Jurisdiction Trigger:**
- Navigable waterway (Section 23(b) of FPA)
- Federal lands
- Interstate commerce
- >5 MW (typically)

**Project Classification:**

**If <5 MW on non-navigable water:** Likely EXEMPT
✅ **Conduit Exemption** (if using existing conduit/canal)
✅ **Small Hydro Exemption** (if <10 MW, no federal lands)
❌ **Full License** (rare for micro-hydro <100 kW)

**Application Type Recommendation:** [Exemption / License / Not Required]

**Timeline:** 
- Exemption: 6-12 months
- License: 2-5 years

**Cost:** 
- Exemption: $10k-30k
- License: $100k-500k+

**Key Requirements:**
- [ ] Preliminary Permit (if needed for site control)
- [ ] Environmental assessment
- [ ] Fish & wildlife consultation
- [ ] Recreation plan
- [ ] Public notice and comment

**FERC Strategy:**
- **If Navigable:** Must file with FERC (no exceptions)
- **If Non-Navigable:** Verify state jurisdiction only
- **Conduit Exception:** Easiest path if using irrigation canal, water treatment outflow, etc.

---

**2. U.S. ARMY CORPS OF ENGINEERS**

**Section 404 Permit (Clean Water Act):**

**Triggers:**
- Fill in wetlands
- Structure in "Waters of the U.S." (WOTUS)
- Dredging

**Likely Applicability:** High (intake, weir, or diversion structures)

**Permit Types:**

**Nationwide Permit 17 (Hydropower):**
- Pre-authorized for small hydro
- Conditions: <½ acre impact, no endangered species, state water quality cert
- **Timeline:** 60-90 days
- **Cost:** $5k-15k

**Individual Permit:**
- Needed if impacts exceed NWP thresholds
- **Timeline:** 6-12 months
- **Cost:** $50k-150k

**Requirements:**
- [ ] Wetland delineation
- [ ] Functional assessment
- [ ] Mitigation plan (if impacts significant)
- [ ] State 401 water quality certification

**Strategy:** Design to minimize wetland impacts, stay under NWP limits

---

**3. ENVIRONMENTAL PROTECTION AGENCY (EPA)**

**Clean Water Act Compliance:**

**Section 401 Water Quality Certification:**
- Required before Corps 404 permit
- Issued by STATE (not EPA directly)
- Verifies project won't violate state water quality standards
- **Timeline:** 60-120 days
- **Cost:** $2k-10k

**NPDES Permit (if construction >1 acre):**
- Stormwater discharge permit
- Construction BMPs required
- **Timeline:** 30-60 days
- **Cost:** $1k-5k

---

**4. U.S. FISH & WILDLIFE SERVICE / NOAA FISHERIES**

**Endangered Species Act (ESA) Consultation:**

**Triggers:**
- Threatened/endangered species in project area
- Critical habitat
- Federal permit/funding/action

**Process:**
1. **Biological Assessment** (prepared by applicant)
2. **Consultation** with USFWS (terrestrial) or NOAA (anadromous fish)
3. **Biological Opinion** (agency determination)
4. **Incidental Take Permit** (if needed)

**Timeline:** 6-18 months (can be critical path)

**Common Species Concerns:**
- Salmon (Pacific Northwest)
- Sturgeon (major rivers)
- Mussels (Southeast)
- Manatees (Florida)

**Mitigation Measures:**
- Fish screens (1mm mesh for fry)
- Fish ladders/bypass
- Minimum instream flows
- Seasonal restrictions (spawning periods)

**Cost:** $20k-100k (depending on species complexity)

**Strategy:** Early consultation, design fish-friendly systems

---

**STATE PERMITS:**

**Water Rights (VARIES BY STATE):**

**Prior Appropriation States (West):**
- File for water right permit
- "First in time, first in right"
- Must prove beneficial use
- Adjudication process
- **Timeline:** 6-18 months
- **Cost:** $5k-20k

**Riparian Rights States (East):**
- Rights attached to property ownership
- "Reasonable use" doctrine
- Less formal permitting (but still required)
- **Timeline:** 3-6 months
- **Cost:** $2k-10k

**Hybrid States:**
- Combination of systems
- Research state-specific rules

**Key Requirements:**
- [ ] Application with flow calculations
- [ ] Public notice (newspaper, adjacent owners)
- [ ] Environmental assessment
- [ ] Instream flow study
- [ ] Non-consumptive use designation (water returned to stream)

**State-Specific Research Needed:** [State water resources agency website]

---

**State Dam Safety:**

**Triggers:**
- New dam/weir >6 feet high
- Modification of existing dam
- Varies by state

**Dam Hazard Classification:**
- **Low Hazard:** Failure causes minimal damage
- **Significant Hazard:** Possible damage to structures
- **High Hazard:** Loss of life risk

**Requirements:**
- [ ] Engineering design by PE
- [ ] Stability analysis
- [ ] Emergency Action Plan (EAP)
- [ ] Regular inspections

**Timeline:** 6-12 months
**Cost:** $10k-50k (design + review)

**Strategy:** Minimize dam height, run-of-river design avoids dam safety

---

**State Environmental Review (SEPA/NEPA equivalent):**

**Process:**
- Environmental checklist/assessment
- Public review period
- Determination of Significance (DS/FONSI)
- Full EIS (if significant impacts)

**Timeline:** 
- Mitigated DNS: 3-6 months
- EIS: 12-24 months

**Cost:** 
- DNS: $10k-30k
- EIS: $100k-500k+

---

**State Fish Passage:**

**Requirements (if anadromous fish present):**
- Upstream passage (fish ladder)
- Downstream passage (bypass, screens)
- Design standards (water velocity, jump heights)
- Monitoring and adaptive management

**Cost:** $50k-500k (can be significant)

**Exemptions:** 
- Existing barriers upstream
- Non-anadromous waters
- State determination of no passage needed

---

**Other State Permits:**

- **Hydraulic Project Approval (HPA)** - WA, OR, CA work in streams
- **Streambed Alteration Agreement** - CA
- **Floodplain Development Permit** - many states
- **Coastal Zone Management** - coastal areas

---

**LOCAL PERMITS:**

**County/City:**

- **Conditional Use Permit** (if not outright permitted use)
- **Building Permit** (powerhouse structure)
- **Grading Permit** (excavation >50 cubic yards)
- **Electrical Permit** (interconnection)
- **Road Access Permit** (if construction traffic)

**Timeline:** 3-6 months (concurrent with state)
**Cost:** $5k-20k

**Zoning Compliance:**
- Verify allowed use in zone
- Setbacks from property lines
- Height restrictions (transmission poles)
- Noise limits (turbine operation)

---

**UTILITY INTERCONNECTION:**

**Process:**
1. **Interconnection Application** (utility-specific form)
2. **Feasibility Study** (grid capacity assessment)
3. **System Impact Study** (if >2 MW typically)
4. **Interconnection Agreement** (legal contract)

**Standards:**
- IEEE 1547 (technical requirements)
- UL 1741 (equipment certification)
- State interconnection rules

**Timeline:** 3-9 months
**Cost:** $5k-30k (studies + equipment)

**Requirements:**
- [ ] Protective relaying
- [ ] Anti-islanding protection
- [ ] Utility disconnect
- [ ] Insurance ($1-2M liability typical)

---

**COMPREHENSIVE TIMELINE:**

**Pre-Application Phase (6-12 months):**
- Feasibility study
- Environmental surveys
- Conceptual design
- Landowner agreements

**Application Phase (12-24 months):**
- Submit all permit applications (concurrent where possible)
- Agency review and requests for information
- Public comment periods
- Revisions and resubmittals

**Critical Path Items:**
- ESA consultation (if required): 6-18 months
- FERC license (if required): 2-5 years
- State water rights: 6-18 months
- Dam safety review: 6-12 months

**Total Timeline (typical micro-hydro):** 18-36 months from start to permit-in-hand

---

**PERMITTING COST SUMMARY:**

| Permit Category | Low End | High End |
|-----------------|---------|----------|
| FERC (if req'd) | $10k    | $500k    |
| Corps 404       | $5k     | $150k    |
| State water rights | $5k  | $20k     |
| State environmental | $10k | $500k+   |
| ESA consultation | $20k   | $100k    |
| Dam safety      | $10k    | $50k     |
| Local permits   | $5k     | $20k     |
| Utility interconnection | $5k | $30k  |
| **TOTAL RANGE** | **$70k** | **$1.4M** |

**Typical Small Project (<100 kW):** $100k-300k in permitting costs

**As % of Total Project:** 15-30% (can be major cost component)

---

**RISK MITIGATION STRATEGIES:**

**1. Early Agency Consultation:**
- Pre-application meetings (FERC, Corps, state agencies)
- Identify fatal flaws early
- Build relationships

**2. Avoid Federal Triggers:**
- Non-navigable streams
- Private land (no federal nexus)
- Conduit exemptions
- Small scale (<100 kW less scrutiny)

**3. Minimize Impacts:**
- Run-of-river (no storage, smaller dam safety issues)
- Fish-friendly design
- Small footprint (<½ acre wetland impact)

**4. Concurrent Processing:**
- Submit all applications simultaneously
- Don't wait for one before starting another
- Saves 6-12 months

**5. Professional Help:**
- Environmental consultant ($50k-150k)
- Permitting attorney ($20k-50k)
- Worth it for projects >$500k

---

**PERMITTING CHECKLIST:**

**Research Phase:**
- [ ] Identify all applicable permits (federal, state, local)
- [ ] Download application forms and instructions
- [ ] Review timelines and fees
- [ ] Pre-application meetings with agencies

**Documentation Phase:**
- [ ] Environmental surveys (biology, wetlands, cultural)
- [ ] Engineering drawings (30% design minimum)
- [ ] Hydrologic studies (flow, water quality)
- [ ] Property control (ownership or lease)

**Application Phase:**
- [ ] Complete applications (all required fields)
- [ ] Pay fees
- [ ] Submit via required method (online/mail/in-person)
- [ ] Track submission dates (for timeline management)

**Review Phase:**
- [ ] Respond promptly to agency questions
- [ ] Provide supplemental information
- [ ] Attend public hearings if required
- [ ] Negotiate conditions

**Approval Phase:**
- [ ] Receive permits (get originals/certified copies)
- [ ] Understand conditions and restrictions
- [ ] Post bonds if required
- [ ] Begin construction within validity period

---

**COMMON PITFALLS:**

❌ **Underestimating Timeline:** Permitting takes longer than construction
❌ **Incomplete Applications:** Delays processing by months
❌ **Missing an Obscure Permit:** Stops construction, expensive fix
❌ **Poor Agency Relations:** Adversarial approach backfires
❌ **Inadequate Environmental Analysis:** Agencies reject, restart
❌ **No Public Outreach:** Opposition delays or kills projects

✅ **Success Factors:**
- Professional team (engineer, biologist, attorney)
- Early and frequent agency communication
- Over-document (more data better than less)
- Flexibility to modify design based on feedback
- Patience (permitting is slow, can't be rushed)

---

**STATE-SPECIFIC RESOURCES:**

[Provide for specific state]:
- State environmental agency
- Water resources department
- Dam safety office
- Fish and wildlife agency
- Public utility commission
- Renewable energy office

**Federal Resources:**
- FERC: www.ferc.gov
- U.S. Army Corps: www.usace.army.mil/Missions/Civil-Works/Regulatory-Program-and-Permits/
- EPA: www.epa.gov/cwa-404
- USFWS: www.fws.gov/endangered

This comprehensive guide helps navigate the complex regulatory landscape."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def water_rights_analysis(state, water_source):
    """Analyze water rights requirements"""
    
    prompt = f"""Analyze water rights for micro-hydro project:

**State:** {state}
**Water Source:** {water_source}

**WATER RIGHTS ANALYSIS**

---

**STATE CLASSIFICATION:**

**{state} Water Law System:** [Prior Appropriation / Riparian / Hybrid]

---

**PRIOR APPROPRIATION STATES (Western U.S.):**

**Principle:** "First in time, first in right"

**States:** AK, AZ, CO, ID, KS, MT, NE, NV, NM, ND, OK, OR, SD, UT, WA, WY

**Process:**
1. **File Application:** State water resources agency
2. **Public Notice:** 30-60 days (newspaper + adjacent owners)
3. **Protest Period:** Objections from existing rights holders
4. **Agency Review:** Beneficial use, water availability
5. **Permit Issuance:** Conditional on construction timeline
6. **Proof of Beneficial Use:** After system built, finalize right

**Key Concepts:**
- **Priority Date:** Date of application filing (earlier = senior right)
- **Point of Diversion:** Exact location (lat/long)
- **Rate (CFS):** Maximum instantaneous flow
- **Duty:** Annual volume (acre-feet)
- **Purpose:** Must be "beneficial use" (power generation qualifies)
- **Non-Consumptive:** Micro-hydro returns water (huge advantage)

**Typical Timeline:** 12-24 months

**Cost:** $10k-30k (application, engineering, legal)

**Key Advantage for Hydro:** 
Non-consumptive use means:
- Water returned to stream (not depleted)
- Doesn't impact downstream users
- Easier to obtain than agricultural/municipal rights
- Often "conditional" right (doesn't displace existing uses)

---

**RIPARIAN RIGHTS STATES (Eastern U.S.):**

**Principle:** Rights attached to land ownership along watercourse

**States:** Most states east of Mississippi

**Process:**
1. **Registration:** Less formal than appropriation (varies by state)
2. **Reasonable Use:** Can't unreasonably harm other riparians
3. **Permit (in some states):** Environmental review + water withdrawal
4. **Property Ownership:** Must own land adjacent to stream

**Key Concepts:**
- **Riparian Land:** Property touching the watercourse
- **Reasonable Use:** Balancing test (your use vs. others)
- **Natural Flow vs. Reasonable Use:** Evolution of doctrine

**Typical Timeline:** 6-12 months

**Cost:** $5k-15k

**Key Issue:** 
- Must own riparian land (can't divert to non-riparian property)
- If hydro system on someone else's land, need complex agreements

---

**HYBRID STATES:**

**Characteristics:** Mix of both systems (e.g., California, Oregon)
- Surface water: Prior appropriation
- Groundwater: Different rules
- Pre-existing riparian rights: Grandfathered

**Research State-Specific Rules:** Critical in these states

---

**FEDERAL RESERVED RIGHTS:**

**Concept:** Federal government has senior water rights for federal lands

**Implications:**
- Indian reservations (Winters Doctrine)
- National parks/forests
- Military bases
- Federal reserved rights can trump state-issued permits

**Due Diligence:** Check for federal lands upstream/downstream

---

**MICRO-HYDRO SPECIFIC CONSIDERATIONS:**

**Non-Consumptive Use:**

✅ **Major Advantage:**
- Water passes through turbine, returns to stream
- No depletion (unlike agriculture, municipal use)
- Minimal impact on downstream users

⚠️ **But Must Address:**
- **Dewatered Reach:** Section between intake and tailrace
- **Minimum Instream Flow:** Bypass flow to maintain ecosystem
- **Fish Passage:** If anadromous species present

**Application Requirements:**

**Technical Information:**
- Point of diversion (GPS coordinates)
- Diversion rate (CFS): Turbine design flow
- Annual volume (acre-feet): Calculate from operational hours
- Return flow point (tailrace location)
- Consumptive use: 0% (all returned)
- Storage: Typically none (run-of-river)

**Engineering Drawings:**
- Site plan showing intake, penstock, powerhouse, tailrace
- Diversion structure design
- Fish screen details (if required)

**Hydrologic Study:**
- Flow duration curve (from USGS or StreamStats)
- Proposed diversion vs. available flow
- Minimum bypass flow proposal (10-30% of mean annual flow typical)

**Environmental Assessment:**
- Fish and wildlife impacts
- Recreation impacts
- Water quality (temperature, dissolved oxygen)

---

**MINIMUM INSTREAM FLOW REQUIREMENTS:**

**Purpose:** Maintain aquatic ecosystem and downstream uses

**Typical Methods:**

**1. Percentage of Mean Annual Flow:**
- 10-30% bypass (common range)
- Higher for sensitive species
- Lower for degraded streams

**2. Tennant Method (Montana Method):**
| Season | % of Avg Flow | Condition |
|--------|---------------|-----------|
| Oct-Mar | 10% | Fair |
| Apr-Sep | 30% | Good |

**3. Wetted Perimeter Method:**
- Maintain critical riffle habitat
- Field measurements required

**4. Instream Flow Incremental Methodology (IFIM):**
- Complex, habitat-based
- Required for large projects
- $50k-200k cost

**Impact on Project:**
- Reduces available water for generation
- Lower revenue (e.g., 20% bypass = 20% generation loss)
- Design turbine for "available flow after bypass"

---

**EXISTING RIGHTS RESEARCH:**

**Water Rights Database:**
- State water resources agency website
- Search by:
  - Stream name
  - Township/Range
  - Priority date
  - Owner name

**Key Questions:**
1. **Senior Rights Upstream?**
   - Could divert water during drought
   - Reduces your flow

2. **Senior Rights Downstream?**
   - Your diversion might harm them
   - Could face curtailment (shut off)

3. **Pending Applications?**
   - Others seeking same water
   - First to file wins

**Due Diligence Checklist:**
- [ ] Obtain water rights map for watershed
- [ ] List all upstream rights (priority date, rate, purpose)
- [ ] Identify any downstream minimum flow requirements
- [ ] Check for pending applications or protests
- [ ] Review recent drought curtailment orders (if applicable)

---

**PERMITTING STRATEGY:**

**Favorable Factors (support application):**
✅ Non-consumptive use (all water returned)
✅ Green energy (renewable, carbon-free)
✅ Economic benefit (jobs, tax base)
✅ No new storage (run-of-river = low impact)
✅ Existing infrastructure (re-powering old mill)
✅ Community support (letters from local government)

**Unfavorable Factors (challenge application):**
❌ Over-appropriated stream (all water already claimed)
❌ Endangered species (ESA complications)
❌ Protests from existing rights holders
❌ Significant dewatered reach (>1 mile)
❌ Popular recreation area (kayaking, fishing)
❌ Tribal water rights or treaty fishing

**Overcoming Objections:**
- Increase bypass flow (reduce diversion)
- Fish passage (ladders, screens)
- Recreation enhancements (access, parking)
- Monitoring and adaptive management
- Habitat improvement (offset impacts)

---

**CONDITIONAL vs. FINAL PERMIT:**

**Conditional/Preliminary Permit:**
- Issued first (reserves right to apply water to beneficial use)
- Requires "due diligence" (progress toward completion)
- Validity period: 5-10 years typical
- Extensions possible if actively developing

**Final/Certificated Permit:**
- After construction complete
- Proof of beneficial use submitted
- Inspected by state engineer
- Permanent right (subject to continued use)

**Risk:** Conditional permit expires if project not built = loss of priority date

---

**TRANSFER OR CHANGE OF USE:**

**If Existing Water Right Present:**
- Old mill with historical water right
- Agricultural right on property
- Municipal right no longer needed

**Process:**
- File change application (easier than new right)
- Show no harm to other users
- May need to reduce quantity (if consumptive → non-consumptive)

**Advantages:**
- Retain senior priority date (very valuable)
- Faster than new appropriation
- Less opposition (right already exists)

**Example:** Old irrigation right (100 acre-feet/year consumptive) → Hydro (500 acre-feet/year non-consumptive but zero depletion) = Allowed in most states

---

**COST-BENEFIT ANALYSIS:**

**Costs:**
- Application Fee: $1k-5k
- Engineering (hydrology, diversion design): $10k-30k
- Environmental Studies: $10k-50k
- Legal (if protests): $10k-50k
- **Total: $30k-135k**

**Benefits:**
- Legal right to use water (essential for project)
- Priority date (protection against future users)
- Transferable (adds value to property)
- Permanent (with continued use)

**Risk of Not Obtaining:**
- ❌ Project illegal (operating without right)
- ❌ Cease and desist order (shut down)
- ❌ Fines ($1k-10k per day in some states)
- ❌ Can't sell power (utility won't buy from illegal project)
- ❌ Can't get financing (banks require legal rights)

**Conclusion:** Proper water right is non-negotiable for legitimate project

---

**TIMELINE EXAMPLE (Prior Appropriation State):**

**Month 1-2:** Prepare application (hire engineer, gather data)
**Month 3:** File application, pay fees
**Month 3-4:** Public notice period (protests possible)
**Month 5-12:** Agency review, requests for information
**Month 12-18:** Permit issuance (if no protests)
**Add 6-24 months if protests, hearings, appeals**

**Year 2-5:** Construct project (under conditional permit)
**Year 5:** File proof of beneficial use, receive final permit

---

**RED FLAGS (problematic situations):**

🚩 **Over-Appropriated Basin:** State declares no water available
🚩 **Adjudication in Progress:** Courts determining all rights (freeze on new permits)
🚩 **Endangered Species:** ESA consultation could require extreme bypass flows
🚩 **Tribal Rights:** Unresolved claims or treaty fishing areas
🚩 **Interstate Compact:** (e.g., Colorado River) - federal involvement

**If Any Red Flags Present:** Consult water rights attorney before investing heavily

---

**RECOMMENDED APPROACH:**

**Phase 1: Preliminary Assessment (low cost)**
- Research state water law
- Review online water rights database
- Identify obvious red flags
- Go/No-Go decision

**Phase 2: Professional Analysis (if feasible)**
- Hire water rights consultant or attorney
- Detailed rights search
- Pre-application consultation with state agency
- Refine project design to match water availability

**Phase 3: Application (if green light)**
- Full engineering and environmental studies
- Submit complete application
- Respond to agency questions
- Obtain permit

**Don't Skip Steps:** Investing in construction before water right secured = major risk

This analysis provides a solid foundation for water rights strategy."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def environmental_compliance(project_details):
    """Environmental regulations and compliance strategy"""
    
    prompt = f"""Develop environmental compliance strategy:

**Project:** {project_details}

**ENVIRONMENTAL COMPLIANCE FRAMEWORK**

---

**REGULATORY OVERVIEW:**

Environmental review required under:
- **Federal:** NEPA, ESA, Clean Water Act, Fish & Wildlife Coordination Act
- **State:** SEPA/CEQA equivalent, state ESA, water quality
- **Local:** Critical areas ordinances, shoreline management

**Trigger:** Any federal permit, funding, or action = Full federal review

---

**STEP 1: ENVIRONMENTAL BASELINE**

**Biological Resources:**

**Aquatic:**
- [ ] Fish species inventory (resident + anadromous)
- [ ] Threatened/Endangered species (ESA Section 7)
- [ ] Critical habitat designation
- [ ] Essential fish habitat (EFH for salmon)
- [ ] Spawning areas and timing
- [ ] Migration corridors

**Terrestrial:**
- [ ] Wildlife surveys (spotted owl, grizzly, etc.)
- [ ] T&E species on-site or nearby
- [ ] Nesting sites, dens, roosts
- [ ] Migration routes

**Vegetation:**
- [ ] Wetland delineation (Corps methodology)
- [ ] Riparian habitat assessment
- [ ] T&E plants
- [ ] Invasive species present

**Aquatic Habitat Quality:**
- [ ] Water temperature (7-day average max)
- [ ] Dissolved oxygen
- [ ] pH, turbidity, conductivity
- [ ] Substrate composition (spawning gravel)
- [ ] Macroinvertebrates (biological indicator)

**Survey Timing:**
- **Spring:** Amphibian breeding, songbird nesting
- **Summer:** Fish (low flows, best visibility), plants flowering
- **Fall:** Salmon spawning, bat surveys
- **Winter:** Eagles, overwintering habitat

**Cost:** $20k-100k depending on survey intensity and species complexity

---

**STEP 2: IMPACT ASSESSMENT**

**Construction Phase Impacts:**

**Temporary:**
- Sediment discharge (turbidity)
- Vegetation clearing
- Noise (pile driving, excavation)
- Access road construction
- Workforce presence (disturbance)

**Permanent:**
- Intake structure (physical barrier)
- Dewatered reach (reduced flow between intake and tailrace)
- Altered flow regime
- Habitat loss (footprint of facilities)

**Operational Phase Impacts:**

**Hydrologic:**
- **Flow Alteration:** Daily/seasonal patterns changed
- **Peak Flows:** Attenuated if storage
- **Low Flows:** Bypass flow maintained
- **Temperature:** Could increase in dewatered reach
- **Sediment:** Reduced transport capacity

**Biological:**
- **Fish Entrainment:** Juveniles pulled into intake (injury/mortality)
- **Fish Impingement:** Pinned against screens
- **Passage Barrier:** Blocks migration (upstream/downstream)
- **Habitat Fragmentation:** Isolated populations
- **Predation:** Concentrated prey at barriers
- **Disease:** Crowding in tailrace

**Impact Significance Criteria:**
- **Negligible:** <1% population effect
- **Minor:** 1-5% population effect
- **Moderate:** 5-10% population effect
- **Major:** >10% population effect or listed species take

---

**STEP 3: AVOIDANCE & MINIMIZATION**

**Hierarchy:** Avoid > Minimize > Mitigate

**Avoidance Strategies (best):**
- **Site Selection:** Choose streams without T&E species
- **Timing:** Construct outside sensitive periods (avoid spawning, nesting)
- **Design:** Run-of-river (no dam) reduces impacts

**Minimization Strategies:**
- **Intake Design:** 
  - Self-cleaning screens (rotating, traveling)
  - 1-2 mm mesh (protect fry)
  - Low approach velocity (<0.5 ft/sec)
- **Bypass Flows:** 
  - Adaptive management (higher flows in critical months)
  - 30-50% mean annual flow in high-quality habitat
- **Dewatered Reach:**
  - Minimize length (<500 feet ideal)
  - Maintain wetted perimeter at minimum flow
- **Fish Passage:**
  - Upstream: Fish ladder (vertical slot, Denil, pool & weir)
  - Downstream: Bypass pipe, surface collector
- **Construction BMPs:**
  - Silt fences, sediment basins
  - Work during low flow period (summer)
  - Isolate work area (cofferdams)

---

**STEP 4: MITIGATION**

**Compensatory Mitigation (if impacts unavoidable):**

**On-Site:**
- Habitat enhancement in tailrace
- Riparian planting (shade, bank stability)
- Large woody debris placement (fish cover)
- Side channel restoration

**Off-Site:**
- Barrier removal elsewhere in watershed
- Stream restoration (increase total habitat)
- Hatchery supplementation (controversial)
- Conservation easements

**Mitigation Ratios:**
- 1:1 (minimum) - Replace what's lost
- 2:1 or 3:1 (often required) - Compensate for uncertainty

**Cost:** $50k-500k depending on mitigation scope

---

**STEP 5: MONITORING & ADAPTIVE MANAGEMENT**

**Pre-Construction Baseline:**
- Fish populations (electrofishing, snorkel surveys)
- Habitat metrics (wetted width, depth, substrate)
- Water quality (temp, DO)
- **Duration:** 1-2 years (capture variability)

**Construction Monitoring:**
- Turbidity (real-time meters, trigger for stop-work)
- Compliance with BMPs
- Wildlife/nest monitoring (if active nests present)

**Post-Construction (Operational) Monitoring:**

**Year 1-3 (intensive):**
- Fish populations (compare to baseline)
- Passage effectiveness (PIT tags, radio telemetry)
- Entrainment/mortality (netting at tailrace)
- Water quality (temperature logger every 15 min)
- Bypass flow compliance (flow meter)

**Year 4-10 (reduced):**
- Annual fish surveys
- Water quality spot checks
- Visual inspections

**Adaptive Management Triggers:**
- Population decline >20%: Increase bypass flow
- High entrainment: Modify screens or shut down during critical period
- Temperature exceedance: Shade enhancement or flow increases

**Reporting:** Annual to agencies (USFWS, NOAA, state fish & wildlife)

**Cost:** $20k-50k per year (Years 1-3), $5k-10k per year (Years 4-10)

---

**ENDANGERED SPECIES ACT (ESA) COMPLIANCE:**

**Section 7 Consultation (if federal action):**

**Process:**
1. **Biological Assessment (BA):** Prepared by applicant/consultant
   - Species likely present
   - Effects determination (No Effect / May Affect)
   - Conservation measures proposed

2. **Initiate Consultation:** Submit BA to USFWS or NOAA
   
3. **Biological Opinion (BO):** Agency's conclusion
   - Not Likely to Adversely Affect (NLAA) → Concurrence letter
   - Likely to Adversely Affect (LAA) → Full consultation
   
4. **Incidental Take Statement (ITS):** If "take" authorized
   - Amount/extent of take allowed
   - Reasonable and prudent measures (RPMs)
   - Terms and conditions (mandatory)
   
5. **Reasonable and Prudent Alternative (RPA):** If jeopardy found
   - Alternative way to proceed (e.g., different site, smaller size)

**Timeline:** 
- Informal consultation: 30-90 days
- Formal consultation: 135 days (often longer in practice)

**Outcome Scenarios:**

✅ **No Effect:** No consultation needed (rare)
✅ **NLAA:** Concurrence letter, proceed (best outcome)
⚠️ **LAA, non-jeopardy:** ITS issued, proceed with conditions
❌ **Jeopardy:** Must accept RPA or abandon project

**Critical Success Factors:**
- High-quality BA (hire experienced bio consultant)
- Early coordination with agencies
- Conservative effects analysis
- Robust conservation measures
- Flexibility to modify project based on feedback

---

**SECTION 10 HABITAT CONSERVATION PLAN (HCP):**

**When Needed:** Private action (no federal permit), but take likely

**Process:**
1. Prepare HCP (similar to BA but more detailed)
2. Submit to USFWS/NOAA
3. Public review (30 days)
4. Incidental Take Permit (ITP) issued

**Timeline:** 12-24 months
**Cost:** $100k-500k (complex)

**Typically Not Required for Small Hydro** (usually have Corps permit, so Section 7 applies)

---

**FISH PASSAGE REQUIREMENTS:**

**Legal Drivers:**
- Federal Power Act (FERC license condition)
- Endangered Species Act (BO terms & conditions)
- State law (e.g., WA requires passage unless exempted)
- Clean Water Act (401 certification condition)

**Design Standards:**

**Upstream Passage (Fish Ladder):**
- **Type:** Vertical slot, pool & weir, Denil
- **Attraction Flow:** 5-10% river flow
- **Velocity:** <4 ft/sec for salmon, <2 ft/sec for trout
- **Pool Depth:** 4-6 feet
- **Jump Height:** <12 inches
- **Entrance:** Low velocity zone, continuous flow

**Downstream Passage:**
- **Type:** Bypass pipe, surface collector, turbine screen
- **Attraction:** Surface flow (juveniles are surface-oriented)
- **Velocity:** Sweeping velocity > approach velocity

**Cost:**
- Upstream ladder: $100k-500k
- Downstream bypass: $50k-200k
- **Total: $150k-700k** (can be deal-breaker for small projects)

**When Passage NOT Required:**
- Existing barrier upstream (passage already blocked)
- Non-anadromous stream (no migratory fish)
- State determination of no benefit (e.g., poor upstream habitat)

**Strategy:** Site selection to avoid passage requirements (huge cost savings)

---

**WATER QUALITY CERTIFICATION (§401):**

**Process:**
1. Submit application to state environmental/water quality agency
2. Public notice (30 days)
3. Agency review (up to 1 year)
4. Certification issued (or denied or waived)

**Typical Conditions:**
- Minimum bypass flow
- Water temperature limits (e.g., <18°C for salmon)
- Dissolved oxygen (>6 mg/L)
- Construction BMPs (turbidity <10 NTU increase)
- Monitoring and reporting

**Timeline:** 60-120 days (but can request extensions up to 1 year)

**Denial:** Rare, but possible if water quality standards can't be met
- Example: High temperature stream + low bypass flow = temp exceedance

**Workarounds:** Increase bypass flow, shade enhancement, deeper intake

---

**ENVIRONMENTAL COST SUMMARY:**

| Item | Cost Range |
|------|------------|
| Baseline Surveys (1-2 year) | $50k-200k |
| Biological Assessment (ESA) | $30k-100k |
| Mitigation (habitat restoration) | $50k-500k |
| Fish Passage (if required) | $150k-700k |
| Monitoring (10-year program) | $150k-300k |
| **TOTAL ENVIRONMENTAL COMPLIANCE** | **$430k-1.8M** |

**As % of Total Project Cost:** 25-50% for projects with complex environmental issues

**This Can Make or Break a Project:** Site selection to avoid issues is critical

---

**COMPLIANCE CHECKLIST:**

**Pre-Development:**
- [ ] Environmental baseline surveys (biology, wetlands, water quality)
- [ ] T&E species review (USFWS website, state lists)
- [ ] Critical habitat maps
- [ ] Early agency coordination (USFWS, NOAA, state fish & wildlife)

**Permitting Phase:**
- [ ] Biological Assessment (if federal permit)
- [ ] ESA Section 7 consultation
- [ ] Wetland delineation and functional assessment
- [ ] Water quality certification application
- [ ] Mitigation plan development

**Construction Phase:**
- [ ] Construction BMPs implemented (inspections)
- [ ] Turbidity monitoring (real-time)
- [ ] Qualified environmental monitor on-site
- [ ] Stop-work authority if problems arise
- [ ] Photo documentation

**Operational Phase:**
- [ ] Bypass flow compliance (continuous monitoring)
- [ ] Water quality monitoring (temperature, DO)
- [ ] Fish population monitoring (annual surveys)
- [ ] Passage effectiveness studies (if ladders built)
- [ ] Annual reporting to agencies
- [ ] Adaptive management (adjust operations if needed)

**Long-Term:**
- [ ] Maintain monitoring program (10+ years often required)
- [ ] Implement adaptive management (triggers for increased protection)
- [ ] Mitigation site maintenance (if off-site mitigation)
- [ ] Permit renewal (if term-limited)

---

**RISK MANAGEMENT:**

**High-Risk Situations (proceed with caution):**
🔴 ESA-listed species present (especially salmon)
🔴 Critical habitat on-site
🔴 Popular fishery (stakeholder opposition)
🔴 No existing passage barrier upstream (will be first barrier)

**Lower-Risk Situations:**
🟢 Non-anadromous stream
🟢 Existing barrier upstream (passage not required)
🟢 Previously disturbed site (old mill)
🟢 Small project (<50 kW, minimal footprint)

**Risk Mitigation:**
- Site selection (choose low-risk sites)
- Early coordination (agencies, stakeholders, tribes)
- Conservative design (high bypass flows, fish-friendly)
- Budget contingency (20-30% for environmental)
- Professional team (experienced bio consultant)

This framework ensures environmental compliance while maximizing project viability."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def compliance_calendar(project_timeline):
    """Create regulatory compliance timeline"""
    
    prompt = f"""Create comprehensive regulatory compliance calendar:

**Project Timeline:** {project_timeline}

**REGULATORY COMPLIANCE CALENDAR**

---

**INTEGRATED PERMITTING TIMELINE**

**Goal:** Minimize critical path, maximize concurrent processing

---

**YEAR 1: PRE-APPLICATION PHASE**

**QUARTER 1 (Months 1-3): Planning & Baseline**

**Month 1:**
- Week 1-2: Assemble project team (engineer, environmental consultant, attorney)
- Week 3: Desktop research (species lists, water rights database, permit requirements)
- Week 4: Schedule pre-application meetings with agencies

**Month 2:**
- Week 1: Pre-app meeting - FERC (if potentially jurisdictional)
- Week 2: Pre-app meeting - Corps of Engineers (404 permit)
- Week 3: Pre-app meeting - State water resources (water right)
- Week 4: Pre-app meeting - State fish & wildlife (ESA, passage)

**Month 3:**
- Environmental field work begins:
  - Wetland delineation
  - Fish surveys (begin if season appropriate)
  - Habitat assessment
  - Water quality baseline
- Hydrologic analysis (flow data, StreamStats)
- Conceptual design (30%)

**QUARTER 2 (Months 4-6): Continued Baseline & Design**

**Month 4-5:**
- Continue seasonal field surveys
  - Spring: Amphibians, nesting birds
  - Summer: Fish (best visibility), plants
- Preliminary engineering (60% design)
- Begin property negotiations (lease or purchase)

**Month 6:**
- Complete Year 1 baseline surveys
- Preliminary engineering complete (90% design)
- Cost estimates refined
- Go/No-Go decision point

**QUARTER 3-4 (Months 7-12): Application Preparation**

**Month 7-9:**
- Year 2 field surveys (capture inter-annual variability)
- Draft permit applications:
  - Water right application
  - Corps 404 application
  - FERC exemption (if required)
  - State environmental review (SEPA checklist)
- Biological Assessment (ESA)
- Wetland mitigation plan

**Month 10-12:**
- Finalize applications (all supporting documents)
- Secure property control (signed lease/purchase)
- Obtain signed landowner consent forms
- Public outreach (brief neighbors, local government)

---

**YEAR 2: APPLICATION & REVIEW**

**QUARTER 1 (Months 13-15): Submit Applications**

**Month 13:**
- Week 1: Submit state water right application
  - Public notice published (newspaper)
  - Adjacent owner notification
  - 30-day protest period begins
  
- Week 2: Submit Corps 404 application (Nationwide Permit 17)
  - Triggers state 401 water quality certification
  - Public comment period (30 days)

- Week 3: Submit FERC exemption application (if required)
  - Public notice
  - 60-day comment period

- Week 4: Submit state environmental review (SEPA/CEQA)
  - Determination of significance (DS/FONSI)

**Month 14:**
- Initiate ESA Section 7 consultation
  - Submit Biological Assessment to USFWS/NOAA
  - Informal consultation (30-60 days)
  - Possible formal consultation (135 days)

**Month 15:**
- Respond to initial agency questions
- Submit any supplemental information requested
- Track all submission and response dates

**QUARTER 2 (Months 16-18): Review Period**

**Month 16-18:**
- Agency review ongoing (all applications)
- Water right protest period ends (Month 16)
  - If protests: Schedule hearing
  - If no protests: Agency technical review continues
- Corps public comment period ends
- Respond to additional agency questions
- Negotiate permit conditions

**Milestones:**
- State environmental determination (Month 17-18)
  - FONSI (Finding of No Significant Impact) = proceed
  - DS (Determination of Significance) = EIS required (add 12-18 months)

---

**QUARTER 3 (Months 19-21): Consultation & Negotiation**

**Month 19-20:**
- ESA consultation ongoing
  - Biological Opinion expected (Month 20)
  - If LAA: Incidental Take Statement issued
  - Terms & conditions defined

**Month 21:**
- Water quality certification review
  - State agency site visit (typical)
  - Draft conditions proposed
  - Negotiate bypass flows, monitoring

**QUARTER 4 (Months 22-24): Permit Issuance**

**Month 22:**
- Corps 404 Nationwide Permit verification
  - With 401 certification
  - Construction conditions specified

**Month 23:**
- State water right permit issued (conditional)
  - Beneficial use deadline set (e.g., 5 years)
  - Construction milestone requirements

**Month 24:**
- FERC exemption issued (if required)
- State environmental determination final
- Local permits (building, grading) submitted
- **ALL PERMITS IN HAND** ✅

---

**YEAR 3: CONSTRUCTION PREPARATION & START**

**QUARTER 1 (Months 25-27): Procurement & Mobilization**

**Month 25:**
- Finalize design (100% construction drawings)
- Bid packages issued
- Contractor selection
- Equipment procurement (long-lead items)
  - Turbine-generator (6-9 month lead time)
  - Transformers (3-6 months)

**Month 26:**
- Pre-construction meeting with agencies
- Environmental monitor hired
- Construction BMPs installed (silt fence, etc.)
- Access road improvements

**Month 27:**
- In-water work window opens (check permits)
  - Typical: July-September (low flow, no spawning)
- Begin construction:
  - Intake structure
  - Penstock installation

**QUARTER 2-4 (Months 28-36): Construction**

**Month 28-30:**
- Intake/diversion structure complete
- Penstock installation
- Powerhouse construction
- Environmental monitoring (turbidity, wildlife)
- Weekly agency updates (if required by permit)

**Month 31-33:**
- Turbine-generator installation
- Electrical work (switchgear, interconnection)
- Fish screens installed and tested
- Bypass flow measurement system

**Month 34-36:**
- Commissioning and testing
- Utility interconnection energized
- Final inspections (building, electrical, environmental)
- Post-construction reporting to agencies

---

**YEAR 4: OPERATIONS & MONITORING**

**Month 37-48:**
- Begin commercial operations
- Monitoring program:
  - Flow (continuous, SCADA)
  - Water quality (temperature, DO - continuous)
  - Fish surveys (annual, Month 40)
  - Annual reporting to agencies (Month 48)
- Adaptive management:
  - Adjust bypass flows if needed
  - Screen maintenance/improvements
- Water right final permit application:
  - Proof of beneficial use submitted (Month 48)
  - State inspection
  - Final/certificated water right issued

---

**YEARS 5-10: LONG-TERM MONITORING**

**Annual Tasks:**
- Fish population surveys (summer)
- Water quality spot checks (quarterly)
- Passage effectiveness (if ladders - Years 5, 7, 10)
- Annual report to agencies (due each year)
- Adaptive management adjustments as needed

**Year 10:**
- Final monitoring report
- Transition to maintenance-only (no research)
- Retain long-term flow and temperature monitoring
- Permit compliance audits (periodic)

---

**CRITICAL PATH ANALYSIS:**

**Longest-Duration Items (drive overall timeline):**

1. **ESA Consultation:** 6-18 months (if formal consultation required)
2. **Water Right:** 12-24 months (especially in over-appropriated basins)
3. **FERC License:** 24-60 months (if full license vs. exemption)
4. **Environmental Review:** 6-24 months (depending on EIS requirement)
5. **Equipment Procurement:** 6-9 months (turbine lead time)

**Strategy to Reduce Timeline:**

✅ **Concurrent Processing:**
- Submit ALL applications in same month (Month 13)
- Agencies review in parallel
- Saves 6-12 months vs. sequential

✅ **Pre-Application Coordination:**
- Early agency meetings (identify issues before applying)
- Pre-file with FERC (if applicable)
- Draft applications with agency input

✅ **Complete Applications:**
- All supporting studies upfront
- No requests for additional information
- Faster review

✅ **Professional Team:**
- Experienced consultants know agency expectations
- Fewer revisions required
- Credibility with reviewers

❌ **Avoid Delays:**
- Incomplete applications (restart review)
- Missing surveys (must wait for next field season)
- Property access issues (can't proceed without control)
- Public opposition (hearings, appeals)

---

**CONTINGENCY PLANNING:**

**If Protest on Water Right (Month 16):**
- Add 6-12 months for hearing and decision
- Alternative: Negotiate with protestant (increase bypass flow, monitoring)

**If ESA Jeopardy Finding:**
- Accept Reasonable & Prudent Alternative (smaller project)
- OR appeal (add 12-24 months)
- OR abandon site and choose different location

**If EIS Required:**
- Add 12-18 months to environmental review
- Budget +$200k-500k
- Often a project-killer for small hydro

**If Permit Denial:**
- Request reconsideration (6-12 months)
- Appeal to court (12-36 months)
- Modify project and re-apply (12-24 months)
- OR move to different site

---

**PERMIT RENEWAL/COMPLIANCE:**

**Ongoing Requirements:**

**Annual:**
- Monitoring reports (fish, water quality)
- Compliance certification (bypass flows maintained)
- Fee payments (if applicable)

**Every 5 Years:**
- Dam safety inspection (if applicable)
- Comprehensive performance review

**Every 30-50 Years:**
- FERC license renewal (if licensed project)
- Water right renewal (some states)
- Re-consultation under ESA (if conditions change)

---

**CALENDAR SUMMARY:**

**Total Time to Permit: 24 months** (typical)
**Total Time to Operation: 36 months** (if construction starts Month 25)

**Fast-Track Possible:** 18 months (if simple project, no ESA issues, all agencies cooperative)
**Worst Case:** 60+ months (if FERC license, ESA conflicts, EIS, protests, appeals)

**Recommendation:** Plan for 30-month timeline with 12-month contingency

This comprehensive calendar keeps project on schedule and compliant."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Regulatory Scout initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: permits, water_rights, environmental, calendar")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'permits':
            location = sys.argv[2] if len(sys.argv) > 2 else 'Washington State'
            size = sys.argv[3] if len(sys.argv) > 3 else '75 kW'
            print(permit_requirements(location, size))
        elif cmd == 'water_rights':
            state = sys.argv[2] if len(sys.argv) > 2 else 'Oregon'
            source = sys.argv[3] if len(sys.argv) > 3 else 'Small creek'
            print(water_rights_analysis(state, source))
        elif cmd == 'environmental':
            details = sys.argv[2] if len(sys.argv) > 2 else '100 kW, salmon stream, 500ft dewatered reach'
            print(environmental_compliance(details))
        elif cmd == 'calendar':
            timeline = sys.argv[2] if len(sys.argv) > 2 else '36-month project'
            print(compliance_calendar(timeline))
