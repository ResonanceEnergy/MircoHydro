"""
LAND ACCESS SPECIALIST AGENT
Property rights, easements, lease negotiations, landowner relations.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def property_analysis(site_location):
    """Analyze property ownership and access requirements"""
    
    prompt = f"""Analyze property requirements for micro-hydro site:

**Location:** {site_location}

**PROPERTY ACCESS ANALYSIS**

---

**STEP 1: PROPERTY IDENTIFICATION**

**Tax Parcel Research:**
- County assessor online database
- Identify all parcels needed:
  - Intake location (Parcel __)
  - Penstock route (Parcels __)
  - Powerhouse (Parcel __)
  - Access road (Parcels __)
  - Transmission line (Parcels __)

**Property Information:**

| Parcel ID | Owner | Acreage | Zoning | Assessed Value | Current Use |
|-----------|-------|---------|--------|----------------|-------------|
| [ID] | [Name] | __ | [Zone] | $__ | Agricultural/Forest/Vacant |
| [ID] | [Name] | __ | [Zone] | $__ | [Use] |

**Ownership Type:**
- Individual: [Name]
- Corporate: [Company name]
- Trust: [Trust name]
- Government: Federal / State / County / City
- Railroad: [Company]
- Utility: [Electric, water, etc.]

**Contact Information:**
- Mailing address: [From tax records]
- Phone: [Research needed]
- Email: [If available]

---

**STEP 2: PROPERTY RIGHTS NEEDED**

**Intake Site:**
- **Rights Needed:** Fee simple or easement for structure
- **Area:** __ sq ft permanent, __ sq ft temporary (construction)
- **Access:** Vehicle access for maintenance (2x per year)
- **Duration:** Perpetual (life of project: 50+ years)

**Penstock Route:**
- **Rights Needed:** Subsurface easement (buried pipe) OR surface if above-ground
- **Dimensions:** __ ft wide × __ ft long corridor
- **Depth:** __ ft below grade (if buried)
- **Restrictions:** No buildings, trees with deep roots

**Powerhouse:**
- **Rights Needed:** Fee simple purchase or long-term lease
- **Area:** __ sq ft (building footprint + setbacks)
- **Improvements:** Building, transformer pad, parking
- **Utilities:** Electric, water (if needed)

**Access Road:**
- **Rights Needed:** Ingress/egress easement
- **Width:** __ ft (12-16 ft typical)
- **Improvements:** Gravel surface, culverts, turnarounds
- **Use:** Construction (heavy trucks) + operations (pickup truck)
- **Frequency:** Heavy during construction, light (monthly) during operations

**Transmission Line:**
- **Rights Needed:** Overhead or underground utility easement
- **Dimensions:** __ ft wide corridor
- **Height:** __ ft (if overhead)
- **Depth:** __ ft (if underground)
- **Vegetation management:** Tree trimming rights

---

**STEP 3: PROPERTY ACQUISITION STRATEGY**

**Option A: FEE SIMPLE PURCHASE**

**Advantages:**
- ✅ Full control (no landlord)
- ✅ Perpetual rights
- ✅ Can mortgage for financing
- ✅ Flexibility for future expansion

**Disadvantages:**
- ❌ High upfront cost
- ❌ Property taxes ongoing
- ❌ Seller may not want to sell

**Typical Uses:**
- Powerhouse site (if small parcel available)
- Remote sites where owner wants to liquidate

**Negotiation:**
- Fair market value: $__ per acre (from comps)
- Offer: $__ (may be premium for hydro use)
- Closing costs: 5-8% (title, escrow, survey)
- **Total Cost:** $__

---

**Option B: LONG-TERM LEASE**

**Advantages:**
- ✅ Lower upfront cost (no purchase)
- ✅ Owner retains ownership (may prefer)
- ✅ Flexibility to walk away at end

**Disadvantages:**
- ❌ Annual payments (lease expense)
- ❌ Landlord consent needed for changes
- ❌ Risk of non-renewal (if term-limited)
- ❌ Harder to finance (lenders prefer ownership)

**Typical Terms:**
- Duration: 25-50 years (with renewal options)
- Payment: $__ per acre per year OR $__ per kW OR % of revenue
- Escalation: CPI or fixed % per year
- Use: Exclusive for hydro generation
- Renewal: Options for 2-3 additional terms

**Negotiation:**
- Agricultural lease comp: $50-200/acre per year
- Hydro lease: $100-500/acre per year OR 2-5% of gross revenue
- Upfront payment: 1-3 years prepaid (gives owner immediate value)
- **Annual Cost:** $__
- **NPV of 25-year lease @ 8%:** $__

---

**Option C: PERPETUAL EASEMENT**

**Advantages:**
- ✅ One-time payment (no annual lease)
- ✅ Perpetual rights (like ownership but narrower)
- ✅ Owner retains underlying ownership (may accept more readily)
- ✅ Mortgageable for financing

**Disadvantages:**
- ❌ Limited to defined use (can't expand easily)
- ❌ Negotiation of terms can be complex
- ❌ May require quiet title action if recordation issues

**Typical Terms:**
- Rights: Construct, operate, maintain, access
- Area: Defined by legal description (metes & bounds)
- Compensation: $__ (lump sum) = __% of fee simple value
- Restrictions: No interference with easement area

**Easement Valuation:**
- **Penstock route:** 25-50% of fee simple (subsurface, minimal impact)
- **Powerhouse site:** 50-75% of fee simple (exclusive use)
- **Access road:** 15-30% of fee simple (shared use possible)
- **Transmission line:** 10-25% of fee simple (overhead, some land use continues)

**Example:**
- Penstock route: 500 ft × 20 ft = 0.23 acres
- Land value: $10k per acre
- Easement value: 30% = $3k per acre × 0.23 = $690
- **Total one-time payment:** $__ (for all easements)

---

**Option D: LICENSE AGREEMENT**

**Advantages:**
- ✅ Simplest, quickest to negotiate
- ✅ Lowest cost
- ✅ Revocable (flexibility for owner)

**Disadvantages:**
- ❌ Revocable (owner can terminate)
- ❌ Not recordable (doesn't run with land)
- ❌ Unfinanceable (lenders won't accept)

**Typical Use:**
- Temporary (construction access)
- NOT recommended for permanent project facilities

---

**STEP 4: NEGOTIATION STRATEGY**

**Research Landowner:**
- **Motivation:** Why might they agree?
  - Additional income (lease/easement payment)
  - Green energy values (environmental landowner)
  - Existing relationship (good neighbor)
  - Estate planning (sell small parcel)
- **Concerns:** What might they object to?
  - Loss of control
  - Aesthetic (powerhouse visible from house)
  - Noise (turbine operation)
  - Access (trucks on their road)

**Value Proposition (to landowner):**
- ✅ Steady income (lease payments or upfront lump sum)
- ✅ No effort (passive income)
- ✅ Green energy (helping environment)
- ✅ Property tax reduction (if easement = conservation easement)
- ✅ Improved access (road improvements benefit landowner too)
- ✅ Economic development (local jobs, tax base)

**Initial Contact:**
- Letter of introduction (professional)
- Phone call (personal touch)
- In-person meeting (best for complex deals)
- Avoid: Email only (impersonal), surprise visits (rude)

**Meeting Agenda:**
1. Introduce yourself and company
2. Explain project (what, where, why)
3. Show maps (visual of footprint)
4. Discuss benefits (income, environment)
5. Address concerns (listen, don't argue)
6. Propose next steps (appraisal, draft agreement)

**Negotiation Tips:**
- ✅ Start high (but not insultingly so) - room to negotiate down
- ✅ Listen more than talk (understand their needs)
- ✅ Offer options (purchase vs. lease vs. easement)
- ✅ Non-monetary value (hunting rights, road improvements, scholarships for kids)
- ✅ Build relationship (Christmas cards, invite to ribbon cutting)
- ❌ Lowball offers (insults landowner, hardens position)
- ❌ Jargon and legales (confuses, alienates)
- ❌ Pressure tactics (they'll dig in)

---

**STEP 5: LEGAL DOCUMENTATION**

**Easement Agreement Contents:**

1. **Parties:** Grantor (landowner), Grantee (hydro developer)
2. **Recitals:** Purpose, background
3. **Grant of Easement:** Legal description, uses permitted
4. **Consideration:** Payment amount and terms
5. **Term:** Perpetual or __ years
6. **Maintenance:** Who maintains what (shared? grantee?)
7. **Access:** Frequency, notice requirements
8. **Restrictions:** What landowner can't do in easement area
9. **Indemnification:** Developer holds landowner harmless
10. **Insurance:** Developer carries $__ liability coverage
11. **Default:** What happens if breach
12. **Termination:** Conditions (if any)
13. **Recording:** To be recorded in county records
14. **Signatures:** Notarized

**Lease Agreement Contents:**
- Similar to easement, plus:
- Rent amount and payment schedule
- Renewal options
- Use restrictions (exclusive vs. non-exclusive)
- Improvements (who owns at end of lease?)
- Assignment (can developer transfer lease?)

**Purchase & Sale Agreement:**
- Standard real estate PSA
- Contingencies:
  - Financing (buyer must secure loan)
  - Permits (project must be permittable)
  - Title (clear title required)
  - Survey (boundary verification)
  - Phase I ESA (environmental assessment)
  - Water rights (if applicable)
- Closing timeline: 90-180 days (allow for due diligence)

**Due Diligence Checklist:**
- [ ] Title report (identify liens, encumbrances)
- [ ] Survey (verify boundaries, locate improvements)
- [ ] Phase I Environmental (contamination risk)
- [ ] Zoning verification (hydro allowed?)
- [ ] Access verification (legal access to public road?)
- [ ] Utility availability (electric, water, sewer if needed)
- [ ] Water rights search (any existing rights?)
- [ ] Endangered species review (desktop)
- [ ] Cultural resources review (archaeological sensitivity)

**Professional Team:**
- Real estate attorney: $5k-15k (negotiation, document drafting)
- Surveyor: $3k-10k (legal description, boundary survey)
- Appraiser: $2k-5k (fair market value for negotiation)
- Title company: $1k-3k (title insurance)

---

**STEP 6: CHALLENGING SITUATIONS**

**Multiple Landowners:**

**Issue:** Penstock crosses 3 properties

**Strategy:**
- Start with most favorable (friendly neighbor, needs income)
- Use first agreement as template for others
- Domino effect (others see neighbor agreed)
- Offer continuity (same terms for all = fair)

**Cost:** Higher (3 separate negotiations, payments)

---

**Absentee Owner:**

**Issue:** Owner lives out of state, hard to contact

**Strategy:**
- Skip tracing (find current contact info)
- Certified letter (shows seriousness)
- Local representative (property manager, attorney)
- Persistence (may take months to connect)

**If Can't Locate:**
- Quiet title action (legal process if truly abandoned)
- Avoid if possible (expensive, time-consuming)

---

**Hostile Landowner:**

**Issue:** Owner opposes project (environmental concerns, libertarian, NIMBYism)

**Strategy:**
- Understand root cause (often fear or misinformation)
- Education (tour similar project, meet satisfied landowner)
- Address concerns (noise? show data. Fish? show passage design)
- Community support (if neighbors support, pressure to cooperate)
- Alternative route (can you avoid their property?)

**Last Resort:**
- Eminent domain (if utility has power of condemnation)
- Walk away (choose different site)

---

**Government Land:**

**Issue:** Route crosses U.S. Forest Service land

**Special Permits:**
- Special Use Permit (USFS)
- Right-of-Way Grant (BLM)
- Timeline: 12-24 months (bureaucracy)
- Cost: Nominal fee + environmental analysis ($50k-200k)
- Conditions: Extensive (environmental, recreational access)

**Advantage:** No purchase cost (rent to gov't low)

**Disadvantage:** Slow process, can't be rushed

---

**STEP 7: ONGOING LANDOWNER RELATIONS**

**During Construction:**
- Notify before work starts
- Limit disturbance (stay in easement area)
- Restore (reseed, fix fences)
- Safety (keep gates closed, avoid livestock)
- Communication (point of contact for complaints)

**During Operations:**
- Annual update (project performance, community benefit)
- Access notification (call/email before site visit)
- Be good neighbor (help with fire prevention, weed control)
- Honor commitments (pay on time, maintain road)

**Conflict Resolution:**
- Minor issues (noise complaint): Address immediately, modify operations if reasonable
- Major disputes (easement breach): Mediation before litigation

**Goal:** Long-term positive relationship (next 50 years!)

---

**STEP 8: COST SUMMARY**

**Property Acquisition/Rights:**

| Item | Option A (Purchase) | Option B (Lease) | Option C (Easement) |
|------|---------------------|------------------|---------------------|
| Powerhouse site | $__ (fee simple) | $__/yr × 25 = $__ NPV | $__ (perpetual easement) |
| Penstock route | $__ | $__/yr × 25 = $__ NPV | $__ |
| Access road | $__ | $__/yr × 25 = $__ NPV | $__ |
| Transmission | $__ | $__/yr × 25 = $__ NPV | $__ |
| **Subtotal** | **$__** | **$__** | **$__** |
| Legal/Closing | $15k | $10k | $15k |
| **TOTAL** | **$__** | **$__** | **$__** |

**Recommendation:** [Purchase / Lease / Easement] because [rationale]

**As % of Total Project Cost:** __% (typically 5-15% for rural sites)

---

**STEP 9: RISK MITIGATION**

**Title Insurance:**
- Protects against defects in title (liens, prior easements)
- Cost: $1k-3k (one-time premium)
- Coverage: Purchase price or easement value

**Survey:**
- Professional surveyor locates boundaries
- Creates legal description (metes & bounds)
- Identifies encroachments
- Cost: $3k-10k

**Legal Review:**
- Attorney reviews all documents before signing
- Identifies unfavorable terms
- Negotiates changes
- Cost: $5k-15k

**Environmental Phase I:**
- Identifies contamination risk (old dumps, tanks)
- Protects buyer from liability
- Cost: $2k-5k

---

**DECISION MATRIX:**

**Proceed if:**
- ✅ Landowner willing (at reasonable terms)
- ✅ Title clear (no major defects)
- ✅ Cost acceptable (<15% of project budget)
- ✅ Access achievable (road improvements feasible)

**Reconsider if:**
- ⚠️ Multiple hostile landowners
- ⚠️ Complex title (litigation likely)
- ⚠️ Excessive cost (>20% of budget)
- ⚠️ No legal access to public road

**Abandon if:**
- ❌ Landowner refuses (no alternative route)
- ❌ Title defects (can't be cured)
- ❌ Cost prohibitive (better sites available)

This systematic approach secures property rights efficiently."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def easement_negotiation(landowner_profile, rights_needed):
    """Strategy for negotiating easements"""
    
    prompt = f"""Develop easement negotiation strategy:

**Landowner:** {landowner_profile}
**Rights Needed:** {rights_needed}

Provide negotiation playbook including:
- Landowner motivation analysis
- Value proposition to present
- Compensation structure options
- Contract terms to negotiate
- Common objections and responses
- Non-monetary incentives
- Negotiation tactics
- Fallback positions

Generate specific scripts for initial contact and key negotiation points."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def lease_vs_purchase(site_characteristics, financial_constraints):
    """Compare lease vs. purchase options"""
    
    prompt = f"""Analyze lease vs. purchase decision:

**Site:** {site_characteristics}
**Budget:** {financial_constraints}

**LEASE VS. PURCHASE COMPARISON**

**Fee Simple Purchase:**

**Costs:**
- Purchase price: $__ (based on $__/acre × __ acres)
- Closing costs: $__ (5-8% of purchase)
- Annual property tax: $__ (__% of assessed value)
- Total upfront: $__
- 25-year total: $__ (NPV)

**Pros:**
- ✅ Full control and ownership
- ✅ Mortgageable (collateral for financing)
- ✅ Perpetual rights (no renewal risk)
- ✅ Can sell/transfer easily
- ✅ Appreciation potential (land may increase in value)

**Cons:**
- ❌ High upfront capital
- ❌ Property taxes ongoing
- ❌ Seller may not want to sell entire parcel

**Best For:**
- Large budget projects
- Permanent installations
- Financed projects (lender requirements)
- Strategic land banking

---

**Long-Term Lease:**

**Costs:**
- Annual lease payment: $__ (per acre OR per kW OR % of revenue)
- Escalation: __% per year
- Security deposit: $__ (1-3 years prepaid)
- Total upfront: $__
- 25-year total: $__ (NPV @ 8% discount)

**Pros:**
- ✅ Low upfront cost (preserves capital)
- ✅ Owner keeps ownership (may prefer)
- ✅ Flexible exit (at end of term)
- ✅ Operational expense (vs. capital)

**Cons:**
- ❌ Annual payments (cash flow burden)
- ❌ Renewal risk (if term-limited)
- ❌ Less attractive to lenders
- ❌ Lease escalation (CPI or fixed %)
- ❌ Landlord approval needed (for changes)

**Best For:**
- Capital-constrained projects
- Landowner prefers income stream
- Uncertain project life
- All-equity financed (no bank preference for ownership)

---

**Perpetual Easement:**

**Costs:**
- One-time easement payment: $__ (__% of fee simple value)
- Annual access fee (if any): $__ (nominal)
- Total upfront: $__
- 25-year total: $__ (NPV)

**Pros:**
- ✅ One-time cost (no ongoing lease)
- ✅ Perpetual rights (like ownership but cheaper)
- ✅ Mortgageable (most lenders accept)
- ✅ Owner retains title (may accept more readily)
- ✅ Lower cost than purchase

**Cons:**
- ❌ Limited to defined use (less flexible than ownership)
- ❌ Negotiation complexity (defining rights)
- ❌ Possible quiet title action needed

**Best For:**
- Limited budget but need permanent rights
- Owner won't sell but will grant easement
- Narrow use (penstock corridor, not full site)
- Most micro-hydro projects (RECOMMENDED)

---

**Cost Comparison Table:**

| Option | Upfront | Year 1-25 Annual | 25-Yr Total (NPV @ 8%) |
|--------|---------|------------------|------------------------|
| Purchase | $__ | $__ (tax) | $__ |
| Lease | $__ | $__ (escalating) | $__ |
| Easement | $__ | $__ (minimal) | $__ |

**Lowest Cost Option:** [Easement typically]

**Best Overall:** [Depends on project needs]

---

**Financial Analysis:**

**Breakeven Analysis:**

If Lease Annual Payment = $10k, Escalating 2%/year
NPV of 25-year lease = $__

If Easement One-Time = $__
Lease is cheaper if: NPV(lease) < Easement cost
Easement is cheaper if: Easement cost < NPV(lease)

**Result:** [Easement / Lease] is more cost-effective

**But Also Consider:**
- Lender requirements (ownership or easement preferred)
- Financing tax benefits (depreciation if owned)
- Exit strategy (owned property has salvage value)
- Risk tolerance (lease renewal risk vs. capital at risk)

---

**Recommendation:**

**For This Project:**

**Primary Recommendation:** [Easement / Lease / Purchase]

**Rationale:**
- Budget: [Fits or doesn't fit]
- Lender requirements: [Owner preference]
- Project size: [Permanent or pilot]
- Landowner preference: [Willing to sell/lease/easement?]

**Negotiation Target:**
- Compensation: $__ (one-time or annual)
- Terms: [Key provisions]
- Contingencies: [Permits, financing]

**Fallback Options:**
- If owner won't [easement], try [lease]
- If cost exceeds $__, consider alternative site

This analysis supports optimal property rights acquisition."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def access_road_requirements(site_access_conditions):
    """Assess road access and improvement needs"""
    
    prompt = f"""Analyze access road requirements:

**Current Conditions:** {site_access_conditions}

**ACCESS ROAD ANALYSIS**

**Existing Access:**
- Road type: Paved / Gravel / Dirt / No road
- Width: __ feet (12-14 ft minimum for construction)
- Surface: Good / Fair / Poor
- Grade: __% (15% max for loaded trucks)
- Bridges: [Condition, weight limit]
- Distance from public road: __ miles
- Ownership: Public / Private / Mixed

**Construction Requirements:**

**Phase 1: Heavy Equipment Delivery**
- Turbine-generator (__ tons, requires lowboy trailer)
- Transformer (__ tons)
- Penstock sections (__ ft long)
- Excavator, concrete truck access
- Weight rating: __ tons (H-20 truck loading)

**Phase 2: Concrete Delivery**
- Ready-mix trucks (10-12 yards = 20 tons)
- Multiple trips (__ cubic yards total)
- Turning radius: 40-50 ft

**Improvements Needed:**

1. **Widening:** __ ft needed (from __ to 14 ft minimum)
   - Cost: $50-150/ft linear ($__ total)

2. **Surface:** 
   - Gravel (6-8 inches compacted)
   - Cost: $10-30/sq yd ($__ total)
   - OR Paving: $50-100/sq yd (if required)

3. **Grading:**
   - Reduce steep sections to <12% grade
   - Cost: $5k-20k (excavation, fill)

4. **Drainage:**
   - Culverts (__ locations, __ diameter)
   - Ditches (lined or unlined)
   - Cost: $2k-5k per culvert

5. **Turnarounds:**
   - Large equipment needs space to maneuver
   - Hammerhead or cul-de-sac design
   - Cost: $5k-15k each

6. **Bridges:**
   - Strengthen or bypass (if underrated)
   - Cost: $20k-200k (or use alternative route)

**Total Road Improvement Cost:** $__

**Operations Access:**
- Monthly site visits (pickup truck)
- Minimal requirements (compared to construction)
- Maintenance: Annual grading ($1k-3k/year)

**Easement/Permits:**
- County road permit (if improving public road)
- Easement from private landowners (if private road)
- Environmental (if stream crossings)
- Cost: $2k-10k

**Recommendation:**
[Improve existing road / Build new road / Use helicopter for equipment (if really remote!)]

Include road costs in project budget: $__ upfront + $__/year ongoing."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=2500
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Land Access Specialist initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: property, negotiate, lease_vs_purchase, access")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'property':
            location = sys.argv[2] if len(sys.argv) > 2 else 'Rural site, 3 parcels, private landowners'
            print(property_analysis(location))
        elif cmd == 'negotiate':
            profile = sys.argv[2] if len(sys.argv) > 2 else 'Farmer, 65 years old, concerned about access'
            rights = sys.argv[3] if len(sys.argv) > 3 else 'Penstock easement across pasture'
            print(easement_negotiation(profile, rights))
        elif cmd == 'lease_vs_purchase':
            characteristics = sys.argv[2] if len(sys.argv) > 2 else '5 acres needed, $500k budget'
            constraints = sys.argv[3] if len(sys.argv) > 3 else 'Prefer to preserve capital'
            print(lease_vs_purchase(characteristics, constraints))
        elif cmd == 'access':
            conditions = sys.argv[2] if len(sys.argv) > 2 else 'Gravel road, narrow, 1 mile from highway'
            print(access_road_requirements(conditions))
