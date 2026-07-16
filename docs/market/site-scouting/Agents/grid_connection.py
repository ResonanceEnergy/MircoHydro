"""
GRID CONNECTION ANALYST AGENT
Utility interconnection, electrical infrastructure, net metering, PPA.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def interconnection_analysis(project_specs, utility_info):
    """Analyze grid interconnection requirements and costs"""
    
    prompt = f"""Analyze grid interconnection for micro-hydro:

**Project:** {project_specs}
**Utility:** {utility_info}

**GRID INTERCONNECTION ANALYSIS**

---

**PROJECT SUMMARY:**
- Capacity: __ kW
- Generation Profile: Baseload (hydro runs 24/7)
- Location: [Address/coordinates]
- Interconnection Type: Behind-meter / Net metering / Wholesale

---

**UTILITY IDENTIFICATION:**

**Serving Utility:**
- Name: [Electric utility]
- Type: Investor-owned (IOU) / Municipal / Cooperative / PUD
- Service Territory: [Counties served]
- Contact: [Interconnection department, phone, email]
- Website: [Interconnection application portal]

**Regulatory Authority:**
- State: [State utility commission]
- Interconnection Standards: [IEEE 1547, state-specific rules]
- Net Metering: Available / Not available (check state law)
- Feed-In Tariff: Available / Not available
- Renewable Portfolio Standard (RPS): Micro-hydro eligible? Yes/No

---

**INTERCONNECTION PROCESS:**

**STEP 1: Pre-Application Consultation (Optional but Recommended)**

**Actions:**
- Contact utility interconnection coordinator
- Discuss project (size, location, technology)
- Verify grid capacity availability
- Understand local rules and timelines
- Request interconnection application

**Duration:** 1-2 weeks (initial call), 30-60 days (pre-app study if needed)
**Cost:** Free (initial) or $500-2,000 (formal pre-app study)

**Key Questions:**
- Is capacity available at nearest substation?
- Are distribution line upgrades needed?
- What's typical timeline for similar projects?
- Any special requirements for hydro (vs. solar)?

---

**STEP 2: Submit Interconnection Application**

**Application Package:**
- [ ] Completed application form (utility-specific)
- [ ] One-line diagram (electrical schematic)
- [ ] Site plan (showing project location, utility connection point)
- [ ] Equipment specifications (generator, inverter if used, protective relays)
- [ ] UL 1741 certification (for inverter-based systems)
- [ ] Proof of site control (lease, purchase agreement)
- [ ] Application fee: $__

**Submittal Method:**
- Online portal (preferred by many utilities)
- Mail/hand delivery (if no portal)

**Duration:** Immediate (if online), 1-2 weeks (if mail)

---

**STEP 3: Utility Review - Initial Screening**

**Fast-Track Eligibility (for small projects <25 kW typically):**
- Simplified process (15-30 days)
- Lower fees
- Minimal studies

**Standard Review:**
- Feasibility study (does grid have capacity?)
- System impact study (does project cause voltage/frequency issues?)
- Timeline: 30-90 days (feasibility), 90-180 days (full study if needed)

**Cost:**
- Feasibility study: $1k-5k
- System impact study: $10k-50k (if required, typically for projects >2 MW)
- Interconnection facilities study: $5k-20k

**Typical Results for Micro-Hydro (<500 kW):**
- ✅ Fast-track approved (if line capacity adequate, no upgrades needed)
- ⚠️ Conditional approval (minor upgrades required)
- ❌ Denied / Major upgrade required (rare for small projects, but possible in weak grids)

---

**STEP 4: Facility Upgrades (if required)**

**Common Upgrades:**

**Transformer:**
- **If Needed:** Existing service transformer undersized
- **Cost:** $5k-20k (pad-mount), $10k-50k (pole-mount with new pole)
- **Timing:** 3-6 months (equipment procurement)
- **Who Pays:** Developer (upfront) OR utility (in rate base)

**Distribution Line Extension:**
- **If Needed:** Nearest connection point >1,000 feet away
- **Cost:** $50k-150k per mile (overhead), $200k-500k per mile (underground)
- **Timing:** 6-12 months
- **Who Pays:** Developer (upfront) with potential rebate if line benefits other customers

**Substation Upgrades:**
- **If Needed:** Substation at capacity (rare for <1 MW projects)
- **Cost:** $100k-1M+
- **Timing:** 12-24 months
- **Who Pays:** Typically allocated among all users (not just hydro)

**Protective Relaying:**
- **Required:** Ensures safe disconnection during grid outages
- **Equipment:**
  - Reclosing relays (prevent energizing de-energized line)
  - Voltage and frequency relays (detect off-nominal conditions)
  - Transfer trip (remote command to disconnect)
- **Cost:** $10k-30k (equipment + installation)
- **Who Pays:** Developer

**Total Upgrade Cost Range:** $15k-250k (highly site-specific)

**Strategy:** Site selection near existing strong lines = huge cost savings

---

**STEP 5: Interconnection Agreement**

**Agreement Terms:**

**1. Interconnection Facilities:**
- Developer installs: [List - meter, disconnect, relays]
- Utility installs: [List - if any utility-side work]
- Cost allocation: [Who pays what]

**2. Operation:**
- Voltage regulation: [Requirements]
- Power factor: [Typically 0.95 leading to 0.95 lagging]
- Harmonics: [IEEE 519 limits]
- Frequency: 60 Hz ± 0.1 Hz

**3. Metering:**
- Meter type: Net meter / Bidirectional / Dual meter
- Data: 15-minute intervals (typical)
- Read frequency: Monthly

**4. Maintenance & Testing:**
- Initial commissioning test (utility witness)
- Periodic testing: Annual or every 5 years
- Maintenance outages: Advance notice required (48-72 hours typical)

**5. Insurance:**
- General liability: $1M-2M per occurrence
- Property damage: Adequate to rebuild
- Certificate of insurance: Provide to utility annually
- Utility named as additional insured

**6. Term:**
- Duration: 20-30 years (or life of project)
- Termination: [Conditions]
- Renewal: Automatic or negotiated

**7. Fees:**
- Standby charges: $__ per kW-month (if behind-meter and using utility as backup)
- Interconnection fees: $__ per month (if any)
- Metering fees: $__ per month (if special meter required)

**Negotiation Tips:**
- Standard agreement (limited negotiation for small projects)
- Focus on: Standby charges (try to eliminate), testing frequency (annual vs. 5-year)
- Legal review: $2k-5k (attorney review before signing)

**Execution:** Developer and utility sign → project can proceed to construction

---

**STEP 6: Construction & Commissioning**

**Notification:**
- Notify utility of construction start date
- Schedule interconnection installation (coordinate with utility crew if needed)

**Witness Test:**
- Utility inspects installation
- Tests protective relays (trip settings, speed)
- Verifies metering
- Duration: 4-8 hours on-site

**Energization:**
- Utility gives permission to operate
- Developer starts generation
- Monitor first 24-48 hours (ensure no issues)

**Duration (from agreement to energization):** 6-12 months (equipment procurement + construction)

---

**TOTAL INTERCONNECTION COSTS:**

| Item | Cost Range | This Project Estimate |
|------|------------|----------------------|
| Application & Studies | $1k-50k | $__ |
| Utility Upgrades | $0-250k | $__ |
| Developer Equipment | $10k-50k | $__ |
| Legal/Consulting | $5k-15k | $__ |
| **TOTAL** | **$16k-365k** | **$__** |

**Cost per kW:** $__ (benchmark: $150-500/kW for typical small projects)

**As % of Total Project Cost:** __% (typically 10-25%)

---

**REVENUE SCENARIOS:**

**Scenario 1: NET METERING (Behind-the-Meter)**

**Concept:** Generation offsets customer's load, meter runs backward

**Eligibility:**
- Available in __ states (check DSIRE database)
- Capacity limit: Often 1 MW or 110% of customer load
- Micro-hydro eligible? [Check state rules - some limit to solar]

**Value:**
- Retail rate: $___ per kWh (customer's rate)
- No wholesale spread (full retail value)
- **Annual Revenue:** __ MWh × $___ = $__

**Pros:**
- ✅ Highest $/kWh (retail vs. wholesale)
- ✅ Simple billing (net meter)
- ✅ Reduces customer's bill (may have business case without needing to "sell" power)

**Cons:**
- ⚠️ Need customer with adequate load (hydro generation < customer use)
- ⚠️ Policy risk (net metering under attack in some states)
- ⚠️ Standby charges (if utility charges for being connected)

---

**Scenario 2: WHOLESALE GENERATION / POWER PURCHASE AGREEMENT**

**Concept:** Sell power to utility at wholesale rate

**Process:**
1. Negotiate PPA with utility or wholesale market
2. Contract terms: Rate, escalation, duration (10-25 years typical)
3. Monthly settlement based on metered generation

**Wholesale Rates:**
- Avoided cost: $0.03-0.06/kWh (what utility avoids by not generating)
- Market rate: $0.04-0.08/kWh (spot market, fluctuates)
- Premium PPA: $0.08-0.12/kWh (if utility has renewable mandate)

**Annual Revenue:**
- __ MWh × $___ = $__

**Pros:**
- ✅ Sellable to any utility (not tied to specific customer)
- ✅ Long-term contract (revenue certainty)
- ✅ No load matching requirement (generate 24/7)

**Cons:**
- ⚠️ Lower rate (wholesale vs. retail)
- ⚠️ Negotiation required (may be difficult)
- ⚠️ Utility may not be interested (small project, administrative burden)

---

**Scenario 3: COMMUNITY SOLAR / GREEN TARIFF**

**Concept:** Subscribers buy power (often at retail rate) from specific renewable project

**Eligibility:** Requires state program or utility offering

**Value:**
- Subscription rate: $0.10-0.15/kWh (retail or near-retail)
- RECs: Retained by subscribers
- **Annual Revenue:** __ MWh × $___ = $__

**Pros:**
- ✅ Retail or near-retail rates
- ✅ Multiple customers (diversified revenue)
- ✅ Marketing value (local, clean energy)

**Cons:**
- ⚠️ Administrative (customer acquisition, billing)
- ⚠️ Subscriber churn risk
- ⚠️ May not be available (check state)

---

**REVENUE RECOMMENDATION:**

**Primary Strategy:** [Net metering / Wholesale PPA / Community solar]

**Rationale:** [Based on availability, rates, project size]

**Backup Strategy:** [If primary not available]

---

**REGULATORY COMPLIANCE:**

**Federal:**
- FERC: Exempt (if qualifying facility <80 MW) OR small power producer
- PURPA: May qualify for must-take, avoided-cost PPA

**State:**
- Net metering: __ kW limit (check eligibility)
- Interconnection standards: [State-specific or IEEE 1547]
- RPS: Micro-hydro eligible? [Tier, value]

**Utility:**
- Tariffs: [Rate schedule applies]
- Interconnection manual: [Utility-specific requirements]

---

**TECHNICAL REQUIREMENTS:**

**Generator Specifications:**
- Synchronous vs. Induction vs. Inverter-based
- Voltage: 480V (typical for <500 kW) OR 12.47 kV (if larger)
- Frequency: 60 Hz
- Power factor: 0.95 (typical requirement)

**Protective Relays (IEEE 1547):**
- Overvoltage (120% of nominal): 0.16 sec trip
- Undervoltage (50% of nominal): 0.16 sec trip
- Overfrequency (60.5 Hz): 0.16 sec trip
- Underfrequency (59.3 Hz): 0.16 sec trip
- Anti-islanding: Detect loss of grid, disconnect <2 sec

**Equipment:**
- Relay package: $10k-25k
- Disconnect switch: $2k-5k (visible, lockable)
- Metering: $2k-10k (revenue-grade, bidirectional)

**Testing:**
- Factory testing (manufacturer)
- Field testing (before energization)
- Periodic testing (5 years typical)
- Cost: $3k-10k per test

---

**INTERCONNECTION TIMELINE SUMMARY:**

**Month 1-2:** Pre-application consultation
**Month 3:** Submit interconnection application
**Month 4-6:** Utility review and studies
**Month 7:** Interconnection agreement signed
**Month 8-12:** Equipment procurement and installation
**Month 13:** Witness test and energization

**Total:** 12-15 months (from start to operation)

**Critical Path:** Equipment lead time (turbine, transformer) = 6-9 months

---

**RISK ANALYSIS:**

**Technical Risks:**
- Inadequate grid capacity: Medium likelihood, High impact
  - Mitigation: Pre-app consultation, site near strong lines
- Equipment failure: Low likelihood, Medium impact
  - Mitigation: Quality equipment, preventive maintenance, insurance

**Regulatory Risks:**
- Net metering eliminated: Low-Medium likelihood (policy risk), High impact
  - Mitigation: Long-term PPA, diversify revenue (RECs)
- Interconnection denial: Low likelihood (for small projects), High impact
  - Mitigation: Professional design, early utility coordination

**Financial Risks:**
- Interconnection cost overrun: Medium likelihood, Medium-High impact
  - Mitigation: Detailed feasibility study, contingency budget (20%)

**Overall Interconnection Risk:** Low-Medium (hydro is mature, well-understood by utilities)

---

**RECOMMENDATIONS:**

**Site Selection:**
- ✅ Choose sites within 0.5 miles of existing distribution line (ideally 3-phase, 12.47 kV or higher)
- ✅ Verify line capacity (drive route, check for other large loads, substations)
- ❌ Avoid remote sites (interconnection cost can be project-killer)

**Utility Relations:**
- ✅ Early consultation (before site commitment)
- ✅ Professional design (hire experienced engineer for one-line diagram)
- ✅ Clear communication (respond promptly to utility questions)
- ✅ Flexibility (negotiate, don't demand)

**Contingency:**
- Budget 20-30% above utility estimate (costs can escalate)
- Allow 3-6 months buffer in schedule (utilities often behind)

**Decision:**
- Proceed if interconnection cost <20% of total project cost
- Reconsider if >30% (may indicate poor site selection)

This analysis ensures successful and cost-effective grid connection."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def net_metering_analysis(state, project_size):
    """Analyze net metering policies and value"""
    
    prompt = f"""Analyze net metering for project:

**State:** {state}
**Project Size:** {project_size}

Research and provide:
- Net metering availability and caps
- Eligible technologies (hydro included?)
- Compensation mechanism (net vs. buy-all-sell-all)
- System size limits
- Aggregate cap (statewide limit)
- Virtual net metering (community projects)
- Excess generation credit (annual true-up)
- Standby charges (if any)
- Value comparison to wholesale rates

Provide specific state rules and utility tariff references."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def ppa_structure(project_generation, market_rates):
    """Design power purchase agreement structure"""
    
    prompt = f"""Structure power purchase agreement:

**Generation:** {project_generation}
**Market Rates:** {market_rates}

**PPA TERM SHEET**

Design comprehensive PPA including:

**Commercial Terms:**
- Contract Duration: 15-25 years (with extension options)
- Energy Rate: $__ per kWh
  - Fixed OR Escalating __% per year OR Indexed (e.g., CPI + __%)
- Capacity Payment: $__ per kW-month (if applicable)
- REC Ownership: Developer retains / Buyer takes / Shared
- Minimum Take: Annual MWh buyer must purchase

**Delivery:**
- Delivery Point: [Project meter / Substation / Load center]
- Scheduling: [Firm / As-available]
- Curtailment: [Force majeure, grid emergency]
- Penalties: [Shortfall, overgeneration]

**Performance:**
- Guaranteed Capacity Factor: __% (with tolerance)
- Performance Testing: [Annual verification]
- Liquidated Damages: $__/MWh for shortfall

**Risk Allocation:**
- Resource risk: Developer (hydro flow variability)
- Regulatory risk: Shared (permits) / Buyer (rate changes)
- Interconnection: Developer (cost and timeline)

**Termination:**
- Defaults: [Payment, performance]
- Cure periods: [30-90 days typical]
- Early termination: [Penalty = __ × annual revenue]

**Financial Security:**
- Performance Bond: $__ (5-10% of contract value)
- Letter of Credit: $__ (alternative)

**Comparison to Market:**
- Wholesale rate: $0.04-0.06/kWh
- PPA offer: $__/kWh
- Premium: __% (justification: renewable, baseload, local)

**Negotiation Strategy:**
- Start high ($0.10+/kWh), negotiate down
- Emphasize advantages: Baseload (vs. solar/wind), local, job creation
- Offer longer term for higher rate
- Flexibility: Escalator, REC ownership, performance guarantees

Provide buyer-ready PPA draft terms."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

def utility_tariff_research(utility_name):
    """Research utility rates and interconnection policies"""
    
    prompt = f"""Research utility policies for {utility_name}:

**UTILITY TARIFF RESEARCH**

Provide comprehensive analysis:

**1. Utility Profile:**
- Type: IOU / Muni / Coop / PUD
- Service territory: [Counties, population]
- Customers: __ (residential, commercial, industrial)
- Renewable energy programs: [Description]

**2. Retail Rates:**
- Residential: $__ per kWh (tiered or flat?)
- Commercial: $__ per kWh (demand charge?)
- Industrial: $__ per kWh
- Time-of-use: [If available, on-peak/off-peak rates]

**3. Net Metering:**
- Available: Yes / No
- Eligible technologies: Solar, Wind, Hydro, Biogas
- System size limit: __ kW
- Excess generation credit: [Annual / Monthly / Real-time]
- Standby charges: $__ per kW-month

**4. Feed-In Tariff:**
- Available: Yes / No
- Rate: $__ per kWh
- Contract term: __ years
- Eligibility: [Requirements]

**5. Interconnection:**
- Application fee: $__
- Study costs: $__ (estimated)
- Timeline: __ months (typical)
- Equipment requirements: [Relays, meters, etc.]

**6. Renewable Programs:**
- Green tariff: [Description, rate premium]
- Community solar: [Availability]
- REC purchase program: [Rate]

**7. Avoided Cost:**
- Published rate: $__ per kWh
- PURPA obligation: Yes / No
- Historical trends: [Increasing / Stable / Decreasing]

**8. Contact Information:**
- Interconnection coordinator: [Name, phone, email]
- Economic development: [If assistance available]
- Renewable energy dept: [Contact]

**9. Relevant Tariffs:**
- Schedule [Number]: [Description, relevant provisions]
- Net metering rider: [Number]
- Interconnection rules: [Document name]

**10. Recommendations:**
- Best revenue path: [Net metering / PPA / Wholesale]
- Expected rate: $__ per kWh
- Challenges: [Any known issues with hydro interconnections]

Include links to all referenced documents and tariffs."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Grid Connection Analyst initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: interconnection, net_metering, ppa, tariff")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'interconnection':
            specs = sys.argv[2] if len(sys.argv) > 2 else '100 kW, rural location'
            utility = sys.argv[3] if len(sys.argv) > 3 else 'Pacific Power'
            print(interconnection_analysis(specs, utility))
        elif cmd == 'net_metering':
            state = sys.argv[2] if len(sys.argv) > 2 else 'Oregon'
            size = sys.argv[3] if len(sys.argv) > 3 else '75 kW'
            print(net_metering_analysis(state, size))
        elif cmd == 'ppa':
            generation = sys.argv[2] if len(sys.argv) > 2 else '800 MWh/year'
            rates = sys.argv[3] if len(sys.argv) > 3 else 'Wholesale $0.05/kWh'
            print(ppa_structure(generation, rates))
        elif cmd == 'tariff':
            utility = sys.argv[2] if len(sys.argv) > 2 else 'Seattle City Light'
            print(utility_tariff_research(utility))
