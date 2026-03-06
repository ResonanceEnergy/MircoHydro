"""
BRAND STRATEGY AGENT  
Positioning, messaging, visual identity, and brand guidelines.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def brand_positioning(company_info=""):
    """Develop brand positioning and strategy"""
    
    prompt = f"""Create comprehensive brand positioning for micro-hydro company:

**Company Context:** {company_info if company_info else 'Micro-hydro power systems provider'}

**BRAND POSITIONING FRAMEWORK**

---

**BRAND FOUNDATION:**

**Mission:** (Why we exist)
"Empower businesses to achieve energy independence through reliable, sustainable micro-hydro solutions."

**Vision:** (Where we're going)
"A world where every business with water resources harnesses that power for clean, affordable energy."

**Values:** (What we stand for)
1. **Sustainability** - Environmental stewardship in everything we do
2. **Reliability** - Systems that work 24/7, year after year
3. **Innovation** - Pushing boundaries of renewable energy technology
4. **Partnership** - Success measured by customer success
5. **Integrity** - Honest, transparent, and ethical in all dealings

---

**POSITIONING STATEMENT:**

**Formula:** For [target customer] who [need statement], [brand name] is the [category] that [unique benefit] because [reason to believe].

**Example:**
"For manufacturing and industrial businesses who need reliable, cost-effective renewable energy, ResonanceEnergy is the micro-hydro power provider that delivers 60%+ energy cost savings and 25+ years of maintenance-free operation because we've engineered systems specifically for 24/7 industrial applications using proven φ-based turbine technology."

---

**TARGET AUDIENCE:**

**Primary:**
- Manufacturing facilities ($10M+ revenue)
- Food processing plants
- Industrial operations
- Large agricultural operations
- Commercial properties with water access

**Demographics:**
- Decision-makers: CFO, COO, Sustainability Directors, Facilities Managers
- Company size: 100-2,000 employees
- Revenue: $10M-$500M
- Located near: Rivers, streams, irrigation channels, water treatment facilities

**Psychographics:**
- Forward-thinking, early adopters
- ROI-focused (need business case, not just environmentalism)
- Frustrated with rising energy costs
- Sustainability goals (public commitments)
- Risk-averse (proven technology over bleeding-edge)
- Value long-term thinking over quick fixes

---

**COMPETITIVE LANDSCAPE:**

**Direct Competitors:**
- Other micro-hydro providers
- Small-scale hydropower installers

**Indirect Competitors:**
- Solar panel companies
- Wind energy providers
- Diesel generators
- Grid electricity (status quo)
- Energy storage/battery companies

**Competitive Advantages:**

vs. **Solar/Wind:**
- ✅ 24/7 generation (not weather-dependent)
- ✅ Higher capacity factor (90% vs. 15-30%)
- ✅ Smaller footprint
- ✅ No moving parts in turbine (lower maintenance)

vs. **Grid:**
- ✅ Fixed costs (no rate increases)
- ✅ Energy independence (no outages)
- ✅ Hedge against price volatility
- ✅ Sustainability benefits

vs. **Other Micro-Hydro:**
- ✅ φ-based turbine design (patent-pending)
- ✅ 25-year track record
- ✅ 99.7% uptime
- ✅ Full-service (not just equipment sales)
- ✅ Proven ROI (18-24 month payback)

---

**UNIQUE VALUE PROPOSITION (UVP):**

**Headline:** "Reliable Renewable Energy That Pays for Itself"

**Subheadline:** "Cut energy costs 60% with micro-hydro systems that generate power 24/7 for 25+ years. Installed in 2 weeks, payback in 18 months."

**Key Benefits:**

1. **Financial:** 
   - 60%+ cost reduction
   - 18-24 month payback
   - 25+ year lifespan = millions in savings
   - 30% federal tax credit
   - Fixed energy costs (hedge against inflation)

2. **Operational:**
   - 24/7 generation (not intermittent like solar/wind)
   - 99.7% uptime (more reliable than grid)
   - Low maintenance (2x/year service)
   - Energy independence (no outages)
   - Scalable (start small, expand later)

3. **Sustainability:**
   - Zero emissions
   - Offset 800+ tons CO2 annually (per 100kW system)
   - Meets ESG goals
   - Enhances brand reputation
   - Attracts eco-conscious customers/employees

4. **Technical:**
   - Patent-pending φ-turbine technology
   - Modular, expandable design
   - Grid-tied or off-grid capable
   - Smart monitoring and optimization
   - Plug-and-play installation

---

**BRAND PERSONALITY:**

**If our brand were a person, they would be:**

- **Confident but not arrogant** - We know our stuff, proven results
- **Practical and pragmatic** - ROI-focused, not preachy about environmentalism
- **Trustworthy and reliable** - Do what we say, deliver on promises
- **Innovative but proven** - Cutting-edge design, but 25 years of data
- **Partnership-oriented** - Your success is our success

**Tone of Voice:**
- **Confident**: Backed by data and results
- **Clear**: No jargon, no fluff, straight talk
- **Educational**: Help customers understand
- **Authentic**: Honest about limitations and trade-offs
- **Optimistic**: Positive about renewable energy future

**Writing Style:**
- Short sentences
- Active voice
- Specific numbers (not "significant savings" but "60% cost reduction")
- Customer-centric language ("you" not "we")
- Stories and examples (not just features)

---

**BRAND MESSAGING PILLARS:**

**Pillar 1: PROVEN RELIABILITY**

**Message:** "Power You Can Count On - 24/7/365"

**Supporting Points:**
- 99.7% uptime over 10 years
- 25+ year lifespan
- Works day and night, rain or shine
- More reliable than the grid
- 50+ installations, zero failures

**Tagline:** "Always On. Always Saving."

---

**Pillar 2: FINANCIAL PERFORMANCE**

**Message:** "An Investment That Pays You Back - Quickly"

**Supporting Points:**
- 60% average energy cost reduction
- 18-24 month payback period
- Millions in lifetime savings
- 30% federal tax credit
- Fixed costs (inflation hedge)

**Tagline:** "Renewable Energy That Makes Cents"

---

**Pillar 3: SUSTAINABILITY LEADERSHIP**

**Message:** "Power Your Business. Power the Planet."

**Supporting Points:**
- Zero emissions, zero guilt
- Offset 800+ tons CO2 per year
- Meet net-zero commitments
- Enhance ESG scores
- Attract conscious customers/talent

**Tagline:** "Good for Business. Great for Earth."

---

**Pillar 4: TURNKEY SIMPLICITY**

**Message:** "We Handle Everything - You Enjoy the Savings"

**Supporting Points:**
- Free site assessment
- Full engineering and permitting
- Installation in 2 weeks
- Comprehensive training
- Ongoing support and maintenance

**Tagline:** "From Concept to Kilowatts in 12 Weeks"

---

**MESSAGING HIERARCHY:**

**Level 1: Elevator Pitch** (15 seconds)
"We help businesses cut energy costs 60% with micro-hydro systems that generate renewable power 24/7. Typical payback in 18 months, then millions in savings over 25+ years."

**Level 2: 60-Second Pitch**
[Elevator pitch] + "Unlike solar or wind, micro-hydro generates constantly, not just when conditions are right. We've installed 50+ systems with 99.7% uptime and zero failures. The process is simple: we assess your site, engineer the system, handle all permits, install in 2 weeks, and provide ongoing support. Most customers are cash-flow positive within 2 years and never look back."

**Level 3: 5-Minute Pitch**
[60-second pitch] + case studies, ROI calculator, technical details, process walkthrough, customer testimonials

---

**BRAND STORY:**

**The Challenge:**
"In 2000, businesses faced a choice: keep paying rising energy costs or gamble on unreliable renewable energy. Neither option was acceptable."

**The Insight:**
"We realized that flowing water - whether rivers, streams, or irrigation channels - offered something solar and wind couldn't: constant, predictable power generation 24/7."

**The Solution:**
"We developed micro-hydro systems specifically for commercial and industrial applications. Systems that would work reliably for decades, pay for themselves quickly, and integrate seamlessly with existing infrastructure."

**The Proof:**
"Over 25 years, we've installed 50+ systems across manufacturing, agriculture, and commercial properties. Not one has failed. Average uptime: 99.7%. Average energy cost reduction: 60%. Our customers have saved over $50 million in energy costs."

**The Vision:**
"Every business with water resources should harness that power. It's reliable. It's economical. It's the right thing to do. And we're here to make it happen."

---

**BRAND PROMISE:**

**"60% Savings. 99% Uptime. 100% Satisfaction."**

We promise:
1. Your system will meet or exceed projected energy generation
2. We'll install on-time and on-budget
3. You'll achieve ROI within 24 months or we'll make it right
4. We'll be responsive, reliable partners for the life of your system

If we don't deliver, we'll fix it - no excuses.

---

**TAGLINE OPTIONS:**

1. "Reliable Power. Renewable Profits."
2. "Energy Independence, Delivered."
3. "Always Flowing. Always Saving."
4. "Harness Nature. Power Business."
5. "The Power of Water. The Proof of Results."
6. "Renewable Energy That Works Around the Clock"
7. "Turn Water into Wealth"
8. "Clean Energy. Clear ROI."

**Recommended:** "Reliable Renewable Energy" (simple, clear, differentiating)

---

**ELEVATOR PITCH VARIATIONS:**

**For CFOs:**
"We install micro-hydro systems that cut energy costs 60% with 18-month payback. After that, it's 20+ years of pure savings - typically millions. Plus, 30% federal tax credit makes the numbers even better."

**For Sustainability Directors:**
"We help you meet net-zero commitments with renewable energy that actually works 24/7. One 100kW system offsets 800 tons of CO2 annually - that's removing 170 cars from the road."

**For Operations Managers:**
"Imagine never worrying about power outages or rate hikes again. Our micro-hydro systems generate power 24/7 with 99.7% uptime and maintenance just twice a year. Set it and forget it."

**For CEOs:**
"We turn your water resources into competitive advantage. Lower costs, energy independence, sustainability leadership - all with proven ROI. Our customers save millions while advancing their ESG goals."

---

**BRAND DIFFERENTIATION:**

**What we're NOT:**
- ❌ A commodity energy company
- ❌ An experimental tech startup
- ❌ Solar/wind with different branding
- ❌ Just an equipment vendor
- ❌ A "green" company that doesn't care about ROI

**What we ARE:**
- ✅ Proven technology with 25-year track record
- ✅ ROI-focused renewable energy solution
- ✅ Full-service partner (not transactional vendor)
- ✅ Engineering-led company (not sales-led)
- ✅ Specialists in 24/7 renewable generation

---

**CATEGORY DEFINITION:**

We're creating/owning the category: **"24/7 Renewable Energy"**

**Category Characteristics:**
- Generates power constantly (not intermittently)
- Baseload capable (not supplemental)
- Predictable output (not weather-dependent)
- Industrial-grade reliability (not residential-grade)
- Proven ROI (not speculative)

**Why This Matters:**
Solar and wind are "intermittent renewables" - good but limited.
We're "constant renewables" - fundamentally different value proposition.

**Category King Strategy:**
If we define and own this category, we win even as the market grows.

---

**BRAND POSITIONING STATEMENT (Final):**

"For commercial and industrial businesses seeking energy cost reduction and sustainability goals, ResonanceEnergy is the 24/7 renewable energy provider that delivers proven ROI through micro-hydro systems engineered for constant power generation, unlike intermittent solar or wind solutions."

---

Use this positioning consistently across all customer touchpoints:
- Website copy
- Sales presentations
- Marketing materials
- Customer communications
- Investor pitches
- PR and media

When everyone tells the same story, the brand becomes powerful."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def messaging_framework():
    """Create messaging framework for different audiences"""
    
    prompt = """Develop targeted messaging for key customer segments:

**MESSAGING FRAMEWORK BY AUDIENCE**

---

**AUDIENCE #1: CFOS (Financial Decision-Makers)**

**What They Care About:**
- ROI, payback period, financial risk
- Capital allocation decisions
- Cost predictability
- Cash flow impact
- Tax implications

**Key Messages:**

**Headline:** "Turn Capital Investment Into Recurring Savings"

**Value Props:**
1. **18-24 Month Payback** - "Faster ROI than most capital investments"
2. **Fixed Energy Costs** - "Hedge against rate increases (averaged 3.5%/year)"
3. **30% Federal Tax Credit** - "Immediate $90k tax benefit on $300k system"
4. **25-Year Cash Flow** - "$4.5M in total savings on $300k investment"
5. **Balance Sheet Benefits** - "Asset that appreciates via energy savings"

**Objection Handling:**
- "How do I justify this to the board?" → Provide IRR, NPV, comparison to alternative investments
- "What's the risk?" → 10-year warranty, 25-year track record, performance guarantee
- "Can we finance?" → Yes - loans, leases, PPAs available

**Call to Action:** "Let's run your numbers - free ROI analysis in 24 hours"

---

**AUDIENCE #2: SUSTAINABILITY DIRECTORS / ESG LEADS**

**What They Care About:**
- Meeting net-zero commitments
- ESG scores and reporting
- Stakeholder perception (investors, customers, employees)
- Credibility (avoiding greenwashing)
- Regulatory compliance

**Key Messages:**

**Headline:** "Meet Your Net-Zero Goals With Credible, Constant Renewable Energy"

**Value Props:**
1. **Material Impact** - "Offset 800+ tons CO2 per year (100kW system)"
2. **24/7 Renewable** - "Unlike solar/wind, true baseload replacement"
3. **ESG Reporting** - "Scope 2 emissions reduction, renewable energy %, verified data"
4. **Certification Support** - "Supports LEED, B Corp, ISO 14001 certifications"
5. **Stakeholder Value** - "Employee pride, customer attraction, investor appeal"

**Proof Points:**
- EPA Renewable Energy Certificates (RECs)
- Third-party verification
- Case studies from B Corps, LEED facilities
- Carbon accounting tools

**Call to Action:** "Calculate your carbon impact - see how many tons you could offset"

---

**AUDIENCE #3: OPERATIONS / FACILITIES MANAGERS**

**What They Care About:**
- Reliability and uptime
- Maintenance burden
- Installation disruption
- Day-to-day operations
- Troubleshooting and support

**Key Messages:**

**Headline:** "Set It and Forget It - Renewable Energy That Just Works"

**Value Props:**
1. **99.7% Uptime** - "More reliable than the grid"
2. **Low Maintenance** - "2x per year service, ~$3k annual cost"
3. **Quick Install** - "2-week installation, minimal disruption"
4. **24/7 Support** - "Direct line to engineers if you ever need us"
5. **Monitoring Dashboard** - "Real-time visibility, automated alerts"

**Practical Benefits:**
- No daily operation needed (fully automated)
- Weather-proof (works through storms, cold, heat)
- No fuel deliveries (unlike generators)
- No battery replacement (unlike solar + storage)

**Call to Action:** "Talk to other facilities managers who run our systems - peer references"

---

**AUDIENCE #4: CEOS / EXECUTIVES**

**What They Care About:**
- Strategic positioning
- Competitive advantage
- Risk management
- Long-term vision
- Brand and reputation

**Key Messages:**

**Headline:** "Turn Your Water Resources Into Strategic Advantage"

**Value Props:**
1. **Cost Leadership** - "Lower costs = higher margins or competitive pricing"
2. **Energy Independence** - "Insulation from grid failures and price volatility"
3. **Market Positioning** - "Sustainability leader in your industry"
4. **Risk Mitigation** - "Diversified energy portfolio reduces dependency"
5. **Talent Attraction** - "Top talent seeks purpose-driven employers"

**Strategic Framing:**
- "Your competitors are evaluating this - first mover advantage"
- "Institutional investors are screening for climate action"
- "Future-proof your operations against energy uncertainty"

**Call to Action:** "30-minute strategic briefing - how this fits your growth plans"

---

**AUDIENCE #5: PROCUREMENT / PURCHASING**

**What They Care About:**
- Vendor evaluation criteria
- Contract terms
- Price comparison
- Performance guarantees
- Service level agreements

**Key Messages:**

**Headline:** "Transparent Pricing. Proven Performance. Total Accountability."

**Value Props:**
1. **Fixed-Price Contract** - "No surprise costs or change orders"
2. **Performance Guarantee** - "Meet projected generation or we make it right"
3. **Comprehensive Warranty** - "10 years parts & labor, 25-year design life"
4. **Certified Installers** - "Licensed, bonded, insured, certified"
5. **References Available** - "50+ installations, talk to any customer"

**Evaluation Criteria:**
- Price: Competitive, all-inclusive
- Quality: ISO certified, UL listed components
- Timeline: 12 weeks from contract to commissioning
- Support: SLA with response time guarantees
- Financial stability: 25 years in business, solid financials

**Call to Action:** "Complete vendor evaluation package - all docs you need for RFP"

---

**AUDIENCE #6: ENGINEERS / TECHNICAL BUYERS**

**What They Care About:**
- Technical specifications
- Engineering quality
- Integration with existing systems
- Permitting and codes
- Long-term reliability

**Key Messages:**

**Headline:** "Engineered for Industrial Applications - Not Adapted From Residential"

**Value Props:**
1. **φ-Based Turbine Design** - "Patent-pending efficiency optimization"
2. **Grid-Tie Ready** - "IEEE 1547 compliant, seamless integration"
3. **Scalable Architecture** - "Modular design, easy to expand"
4. **Proven in Field** - "25 years of operational data, not lab theory"
5. **Full Engineering Support** - "PE-stamped drawings, SCADA integration, ongoing technical support"

**Technical Details:**
- Flow requirements: 50+ GPM minimum
- Head requirements: 10+ feet
- Output: 10kW to 500kW systems
- Efficiency: 85%+ at design point
- Controls: PLC-based, remote monitoring

**Call to Action:** "Technical deep-dive webinar - bring your hardest questions"

---

**AUDIENCE #7: BOARD MEMBERS / INVESTORS**

**What They Care About:**
- Return on investment
- Strategic fit
- Risk profile
- Governance and oversight
- Fiduciary responsibility

**Key Messages:**

**Headline:** "A Capital Investment That Strengthens The Business For Decades"

**Value Props:**
1. **Attractive Returns** - "20-40% IRR on energy savings alone"
2. **Risk Mitigation** - "Reduces exposure to energy price volatility"
3. **Asset Creation** - "Tangible asset with 25+ year life"
4. **ESG Leadership** - "Meets institutional investor expectations"
5. **Proven Track Record** - "25 years, 50+ installations, zero failures"

**Board Presentation Structure:**
- Executive summary (1 slide)
- Strategic rationale (Why now? Why us?)
- Financial analysis (IRR, NPV, payback, cash flow)
- Risk assessment and mitigation
- Implementation plan and timeline
- Recommendation and vote

**Call to Action:** "Board-ready presentation - all materials for informed decision"

---

**AUDIENCE #8: INDUSTRY MEDIA / PRESS**

**What They Care About:**
- Newsworthy angles
- Industry trends
- Innovation
- Impact stories
- Expert commentary

**Key Messages:**

**Headline:** "24/7 Renewable Energy Challenges Solar/Wind Dominance"

**Story Angles:**
1. **Technology Innovation** - "φ-based turbine achieves 92% efficiency"
2. **Market Disruption** - "Constant generation vs. intermittent renewables"
3. **Customer Success** - "Manufacturer cuts energy costs 65%, saves $2M"
4. **Industry Trends** - "Why commercial sector is turning to micro-hydro"
5. **Founder Story** - "Engineer's 25-year mission to perfect micro-hydro"

**Media Value:**
- Expert availability for commentary
- Data and research (industry reports)
- Customer interviews
- Facility tours for photo/video

**Call to Action:** "Media kit available - assets, backgrounders, interview requests"

---

**MESSAGE CONSISTENCY:**

**Core Themes (Always Present):**
1. Reliable (24/7, 99.7% uptime, 25-year track record)
2. Economical (60% savings, 18-24 month payback, millions in lifetime value)
3. Sustainable (Zero emissions, 800+ tons CO2 offset, ESG goals)
4. Proven (50+ installations, no failures, data-backed claims)

**Adapt Emphasis By Audience:**
- CFO → ROI, payback, tax benefits
- Sustainability → CO2 offset, ESG scores, certifications
- Operations → Reliability, low maintenance, ease of use
- CEO → Strategic advantage, competitive positioning
- Procurement → Warranties, guarantees, transparent pricing
- Engineers → Technical specs, design quality, integration
- Board → Returns, risk mitigation, governance
- Media → Innovation, market trends, impact stories

**But Never Lose Core:** Reliable + Economical + Sustainable + Proven

---

**MESSAGING TESTING:**

**A/B Test These Variations:**

**Value Prop Test:**
- Version A: "Cut energy costs 60%"
- Version B: "Save $144k per year"
- Version C: "$4.5M in lifetime savings"

**Urgency Test:**
- Version A: "30% tax credit available now"
- Version B: "Energy rates rising 3.5% annually"
- Version C: "Installation capacity filling up"

**Proof Test:**
- Version A: "99.7% uptime"
- Version B: "50+ installations, zero failures"
- Version C: "Customers save millions"

**CTA Test:**
- Version A: "Get Free ROI Analysis"
- Version B: "Schedule Site Assessment"
- Version C: "Download Buyer's Guide"

Measure: Click-through rate, conversion rate, pipeline generated

---

**MESSAGE MAP (One-Page Reference):**

```
┌─────────────────────────────────────────────────┐
│ CORE PROMISE: Reliable Renewable Energy         │
│ That Pays For Itself                            │
├─────────────────────────────────────────────────┤
│ KEY PILLARS:                                     │
│ • Proven Reliability (99.7% uptime, 25 years)   │
│ • Financial Performance (60% savings, 18mo ROI) │
│ • Sustainability (Zero emissions, ESG goals)    │
│ • Turnkey Simplicity (We handle everything)     │
├─────────────────────────────────────────────────┤
│ PROOF POINTS:                                    │
│ • 50+ installations                              │
│ • Zero failures                                  │
│ • $50M+ in customer savings                      │
│ • 40,000 tons CO2 offset                         │
├─────────────────────────────────────────────────┤
│ DIFFERENTIATION:                                 │
│ • 24/7 generation (not intermittent)            │
│ • Higher capacity factor than solar/wind        │
│ • Faster payback than grid alternatives         │
│ • Lower maintenance than generators             │
└─────────────────────────────────────────────────┘
```

Use this framework to ensure every piece of content reinforces the same strategic positioning while speaking to specific audience needs."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def visual_identity():
    """Design visual identity and brand guidelines"""
    
    prompt = """Create comprehensive visual identity and brand guidelines:

**VISUAL IDENTITY & BRAND GUIDELINES**

---

**BRAND IDENTITY OVERVIEW:**

A brand's visual identity is how it looks, feels, and is recognized. Consistency builds trust and recognition.

**Goals:**
- Instantly recognizable
- Conveys brand personality (reliable, innovative, sustainable)
- Professional and modern
- Works across all mediums (print, digital, physical)
- Timeless (not trendy)

---

**LOGO DESIGN:**

**Primary Logo:**

**Design Elements:**
- **Symbol:** Stylized water droplet with turbine blades inside
  - Represents water (resource) + rotation (energy generation)
  - φ (phi) spiral subtly integrated (golden ratio, efficiency, nature)
  
- **Wordmark:** "ResonanceEnergy" in custom sans-serif font
  - Modern, clean, technical aesthetic
  - "Resonance" in slightly bolder weight than "Energy"
  
- **Tagline:** "Reliable Renewable Energy" below wordmark (optional)

**Color Palette:**
- **Primary Blue:** #0066CC (trust, water, reliability)
- **Accent Green:** #00A86B (sustainability, growth, energy)
- **Dark Gray:** #2C3E50 (professionalism, stability)
- **White:** #FFFFFF (clarity, simplicity)

**Logo Variations:**

1. **Full Horizontal** (primary)
   - Symbol + Wordmark + Tagline
   - Use: Website header, presentations, documents

2. **Stacked**
   - Symbol above Wordmark
   - Use: Square spaces, social media profiles, app icons

3. **Symbol Only**
   - Just the water/turbine mark
   - Use: Favicons, small applications, watermarks

4. **Reversed** (white on dark backgrounds)
   - All variations available in reverse

5. **Monochrome** (all one color)
   - Use: Single-color applications, embroidery

**Logo Usage Rules:**

✅ **DO:**
- Maintain clear space (minimum = height of symbol)
- Use approved color combinations
- Scale proportionally
- Place on high-contrast backgrounds

❌ **DON'T:**
- Stretch or distort
- Recolor outside approved palette
- Add effects (shadows, glows, outlines)
- Place on busy backgrounds
- Recreate or modify

**Minimum Sizes:**
- Print: 0.75 inches wide
- Digital: 120 pixels wide

---

**COLOR SYSTEM:**

**Primary Colors:**

**Resonance Blue** (#0066CC)
- RGB: 0, 102, 204
- CMYK: 100, 50, 0, 20
- Pantone: 300 C
- Use: Logo, primary CTAs, headers, key elements

**Energy Green** (#00A86B)
- RGB: 0, 168, 107
- CMYK: 100, 0, 36, 34
- Pantone: 3395 C
- Use: Accents, highlights, sustainability messaging

**Neutral Gray** (#2C3E50)
- RGB: 44, 62, 80
- CMYK: 45, 23, 0, 69
- Use: Body text, secondary elements

**Secondary Colors:**

**Light Blue** (#E6F2FF) - Backgrounds, subtle highlights
**Light Green** (#E6F9F0) - Success states, positive messaging
**Light Gray** (#F5F7FA) - Backgrounds, dividers
**Dark Gray** (#1A1A1A) - Headings, emphasis text

**Accent Colors (use sparingly):**

**Warning Orange** (#FF9500) - Urgent CTAs, warnings
**Error Red** (#DC3545) - Errors, critical alerts
**White** (#FFFFFF) - Negative space, text on dark

**Color Psychology:**

- Blue → Trust, reliability, water, technology
- Green → Sustainability, growth, natural, eco-friendly
- Gray → Professional, stable, industrial, serious
- White → Clean, simple, efficient, modern

**Accessibility:**

All color combinations must meet WCAG AA standards:
- Text contrast ratio: Minimum 4.5:1
- Large text: Minimum 3:1
- Interactive elements: Clear visual indicators

---

**TYPOGRAPHY:**

**Primary Font Family:** **Inter** (sans-serif)
- Modern, highly legible, professional
- Excellent at small sizes (web + print)
- Free and widely available

**Font Weights:**

**Headings:**
- H1: Inter Bold (700), 48px / 3rem
- H2: Inter Bold (700), 36px / 2.25rem
- H3: Inter SemiBold (600), 28px / 1.75rem
- H4: Inter SemiBold (600), 24px / 1.5rem
- H5: Inter Medium (500), 20px / 1.25rem
- H6: Inter Medium (500), 18px / 1.125rem

**Body Text:**
- Body Large: Inter Regular (400), 18px / 1.125rem, 1.6 line-height
- Body Regular: Inter Regular (400), 16px / 1rem, 1.5 line-height
- Body Small: Inter Regular (400), 14px / 0.875rem, 1.4 line-height
- Caption: Inter Regular (400), 12px / 0.75rem

**Emphasis:**
- Bold: Inter Bold (700)
- Italic: Inter Italic (400)
- Link: Inter Medium (500), underlined

**Alternative Font (Numbers, Data):**
**Roboto Mono** (monospace)
- Use: Financial data, technical specs, code
- Weights: Regular (400), Medium (500), Bold (700)

**Font Usage:**

✅ **DO:**
- Use Inter for 95% of applications
- Maintain hierarchy (don't skip levels)
- Use appropriate line-height (1.4-1.6)
- Left-align body text

❌ **DON'T:**
- Mix too many font families
- Use decorative fonts
- Set body text below 14px
- Use all caps for long passages
- Use light weights on dark backgrounds

---

**IMAGERY STYLE:**

**Photography:**

**Style:**
- **Real, not stock:** Actual installations, real customers
- **Industrial aesthetic:** Manufacturing, facilities, operations
- **Human element:** Workers, managers (not just equipment)
- **Natural context:** Water, landscapes, sustainability
- **Action shots:** Energy being generated, systems running

**Composition:**
- Rule of thirds
- Leading lines (pipes, rivers, infrastructure)
- Depth (foreground, subject, background)
- Natural lighting when possible
- High resolution (min 300 DPI for print)

**Color Treatment:**
- Enhance blues and greens (brand colors)
- Increase contrast slightly
- Avoid heavy filters or effects
- Maintain realism (not over-processed)

**Subject Matter:**

✅ **DO show:**
- Installed systems (hero shots)
- Happy customers (testimonials)
- Flowing water (resource)
- Industrial facilities (target market)
- Environmental context (sustainability)
- Technical details (engineering quality)

❌ **DON'T show:**
- Generic stock photos (fake people, staged)
- Competitors' products
- Unsafe practices
- Poor quality or amateur shots

**Image Overlay Text:**

When adding text over images:
- Dark overlay (40-60% opacity black) for light backgrounds
- Light overlay (20-40% opacity white) for dark backgrounds
- Ensure text contrast ratio meets WCAG standards
- Use bold weights for readability

---

**ICONOGRAPHY:**

**Icon Style:**

- **Line icons:** 2px stroke weight, rounded ends
- **Minimal detail:** Simple, recognizable at small sizes
- **Consistent perspective:** All icons same viewpoint
- **Color:** Primary blue or single color
- **Size:** 24px, 48px, 64px (scale proportionally)

**Icon Library (Core Set):**

**Product Icons:**
- 💧 Water drop (resource)
- ⚡ Lightning bolt (energy)
- 🔄 Circular arrows (renewable, cycle)
- 📊 Graph increasing (savings, growth)
- 🔧 Wrench (maintenance, service)

**Benefit Icons:**
- 💰 Dollar sign (savings, ROI)
- 🌱 Leaf (sustainability)
- ⏱️ Clock (24/7, reliability)
- 📈 Chart up (performance)
- 🛡️ Shield (protection, warranty)

**Process Icons:**
- 🔍 Magnifying glass (assessment)
- 📐 Ruler + compass (engineering)
- ✅ Checkmark (installation)
- 🎓 Graduation cap (training)
- 📞 Phone (support)

**Download:** Custom icon set provided in AI, SVG, PNG formats

---

**GRAPHIC ELEMENTS:**

**Brand Patterns:**

**Water Flow Pattern:**
- Wavy horizontal lines (evoking water flow)
- Use as backgrounds, dividers, subtle texture
- Primary blue at 10-20% opacity

**φ Spiral Pattern:**
- Golden ratio spiral
- Use sparingly (hero sections, special applications)
- Represents harmony, efficiency, natural design

**Usage:**
- Backgrounds (light opacity)
- Transitions between sections
- Decorative elements (not overwhelming)

**Shapes:**

**Preferred:**
- Rounded corners (8px radius standard)
- Circular elements (photos, icons)
- Organic curves (not rigid rectangles)

**Avoid:**
- Sharp, harsh angles
- Overly geometric/robotic
- Chaotic or random shapes

---

**LAYOUT PRINCIPLES:**

**Grid System:**

- **12-column grid** for web layouts
- **Margins:** 80px desktop, 40px tablet, 24px mobile
- **Gutter:** 32px between columns
- **Whitespace:** Generous (don't cram elements)

**Visual Hierarchy:**

1. **Primary:** What you want them to see first (headline, hero image)
2. **Secondary:** Supporting information (subheadline, benefits)
3. **Tertiary:** Details and actions (body text, CTAs)

**Layout Patterns:**

**Hero Section:**
- Large headline (H1)
- Compelling subheadline (Body Large)
- Primary CTA button
- Hero image or video (right side or full background)
- Height: 80vh minimum

**Content Sections:**
- Section headline (H2)
- Optional description (Body Regular)
- 2-4 content blocks (columns)
- Visual element (image, icon, chart)
- Padding: 120px top/bottom

**Call-to-Action Sections:**
- Contrasting background (primary blue or energy green)
- Centered headline (white text)
- Large CTA button (white background, blue text)

---

**BUTTON STYLES:**

**Primary Button:**
- Background: Primary Blue (#0066CC)
- Text: White, Inter SemiBold (600), 16px
- Padding: 16px 32px
- Border-radius: 8px
- Hover: Darken 10%
- Use: Main actions (Get Started, Request Demo, Sign Up)

**Secondary Button:**
- Background: Transparent
- Border: 2px solid Primary Blue
- Text: Primary Blue, Inter SemiBold (600), 16px
- Padding: 14px 30px (accounts for border)
- Border-radius: 8px
- Hover: Background Primary Blue, Text White
- Use: Secondary actions (Learn More, View Case Studies)

**Tertiary Button:**
- Background: Transparent
- Text: Primary Blue, Inter SemiBold (600), 16px, underline
- Hover: Energy Green
- Use: Tertiary actions (links, less critical CTAs)

**Button Sizing:**
- Large: 56px height (hero CTAs)
- Medium: 48px height (standard)
- Small: 40px height (compact layouts)

---

**BRAND APPLICATION EXAMPLES:**

**Business Cards:**
- Front: Logo, Name, Title, Contact
- Back: Tagline, Website, Pattern
- Size: 3.5" x 2"
- Stock: Premium matte, 16pt

**Letterhead:**
- Logo top left
- Address bottom left
- Contact info bottom right
- Subtle water pattern watermark

**Email Signature:**
- Name (Bold, 16px)
- Title (Regular, 14px)
- Logo (150px wide)
- Phone | Email | Website
- Social icons (optional)

**PowerPoint Template:**
- Title slide: Full-width image, overlay text, logo bottom right
- Content slides: Logo top right, content left-aligned, pattern footer
- Fonts: Inter throughout
- Colors: White backgrounds, blue/green accents

**Website:**
- Header: Logo left, navigation right, sticky on scroll
- Footer: 4 columns (About, Services, Resources, Contact)
- Responsive: Mobile-first design
- Load time: <3 seconds

**Social Media:**
- Profile photo: Symbol only (stacked logo)
- Cover photo: Hero image + tagline
- Post graphics: Consistent template (brand colors, fonts, patterns)
- Video: Lower-third with logo + URL

**Vehicle Wraps:**
- Large logo + phone number (visible from distance)
- Tagline + website
- Primary blue base, white accents
- High-contrast for visibility

**Apparel:**
- Polo shirts: Embroidered logo (chest)
- T-shirts: Screen-printed logo (front), tagline (back)
- Hats: Embroidered symbol on front
- Safety vests: Reflective logo (back)

---

**BRAND VOICE & MESSAGING:**

**Tone:** Confident, Clear, Knowledgeable, Approachable

**Writing Style:**
- Short sentences (15-20 words average)
- Active voice ("We deliver results" not "Results are delivered")
- Second person ("You'll save 60%" not "Customers save 60%")
- Specific numbers ("$144k/year" not "significant savings")
- Avoid jargon (explain technical terms)

**Words We Use:**
✅ Reliable, proven, robust, efficient, sustainable, renewable, savings, ROI, independence, 24/7, constant, consistent

**Words We Avoid:**
❌ Cheap, expensive, complicated, experimental, risky, unpredictable, maybe, hope, try

---

**BRAND GUIDELINES ENFORCEMENT:**

**Who's Responsible:**
- Marketing team: Primary guardians
- Designers: Must follow guidelines
- Sales: Use approved materials only
- All employees: Represent brand consistently

**Approval Process:**
- All external materials must be reviewed by marketing
- Use brand asset library (no freelance logo creation)
- When in doubt, ask

**Brand Asset Library:**
Centralized repository with:
- Logo files (all formats)
- Color codes
- Font files
- Icon sets
- Photography
- Templates (PPT, Word, Canva)
- Brand guidelines PDF

**Access:** Shared drive, brand portal, or DAM system

---

**MEASURING BRAND CONSISTENCY:**

**Quarterly Brand Audit:**
- Review all customer-facing materials
- Check website, social media, presentations
- Identify inconsistencies
- Update offending materials
- Train team on corrections

**Brand Recognition Metrics:**
- Unaided brand awareness (surveys)
- Logo recognition tests
- Brand recall (after 1 exposure)
- Consistency score (internal audit)

**Target:** 95%+ consistency across all touchpoints

---

Remember: Strong brands are built on consistency. Every interaction reinforces (or weakens) the brand. Make every touchpoint count."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def brand_guidelines():
    """Generate complete brand guidelines document"""
    
    prompt = """Create comprehensive brand guidelines document:

**BRAND GUIDELINES DOCUMENT**
**Version 1.0 | January 2026**

---

## TABLE OF CONTENTS

1. Introduction
2. Brand Story
3. Brand Strategy
4. Visual Identity
5. Voice & Messaging
6. Applications
7. Digital Guidelines
8. Print Guidelines
9. Environmental Graphics
10. Co-Branding
11. Legal & Compliance
12. Contact & Resources

---

## 1. INTRODUCTION

**Purpose of This Guide:**

This brand guidelines document is the definitive resource for how our brand should look, sound, and behave across all touchpoints. It ensures consistency, builds recognition, and protects our brand equity.

**Who Should Use This:**
- Marketing and creative teams
- Sales and business development
- External agencies and vendors
- Partners and resellers
- Anyone creating branded materials

**How to Use This Guide:**
- Reference before creating any branded material
- Use provided templates when available
- Ask marketing team if something isn't covered
- When in doubt, prioritize clarity and consistency

---

## 2. BRAND STORY

**Our Origin:**

Founded in 2000 by engineer Sarah Martinez, we saw an opportunity others missed. While the world chased solar and wind, we recognized that flowing water offered something unique: constant, predictable renewable energy.

Twenty-five years later, we've proven the vision. Over 50 installations. Zero failures. $50+ million in customer savings. 40,000 tons of CO2 offset. And we're just getting started.

**Our Purpose:**

Empower businesses to achieve energy independence through reliable, sustainable micro-hydro solutions.

**Our Vision:**

A world where every business with water resources harnesses that power for clean, affordable energy.

**Our Values:**

1. **Reliability** - Systems that work 24/7, year after year
2. **Sustainability** - Environmental stewardship in everything we do
3. **Innovation** - Pushing boundaries of renewable energy technology
4. **Partnership** - Success measured by customer success
5. **Integrity** - Honest, transparent, and ethical always

---

## 3. BRAND STRATEGY

**Positioning Statement:**

"For commercial and industrial businesses seeking energy cost reduction and sustainability goals, ResonanceEnergy is the 24/7 renewable energy provider that delivers proven ROI through micro-hydro systems engineered for constant power generation, unlike intermittent solar or wind solutions."

**Brand Promise:**

"60% Savings. 99% Uptime. 100% Satisfaction."

**Target Audience:**

Primary: Manufacturing, food processing, industrial operations, large agricultural operations, commercial properties with water access

Decision-makers: CFOs, COOs, Sustainability Directors, Facilities Managers

**Competitive Differentiation:**

- **vs. Solar/Wind:** 24/7 generation (not weather-dependent)
- **vs. Grid:** Fixed costs, energy independence
- **vs. Competitors:** Proven track record, higher reliability, full service

**Brand Personality:**

If our brand were a person: Confident but not arrogant, practical, trustworthy, innovative but proven, partnership-oriented

---

## 4. VISUAL IDENTITY

### 4.1 LOGO

**Primary Logo:**
[Visual: Full horizontal logo with symbol + wordmark + tagline]

**Clear Space:**
Maintain minimum clear space equal to the height of the water drop symbol on all sides.

**Minimum Size:**
- Print: 0.75 inches wide
- Digital: 120 pixels wide

**Logo Variations:**

1. **Full Horizontal** - Default for most applications
2. **Stacked** - For square formats
3. **Symbol Only** - Small applications, favicons
4. **Reversed** - White on dark backgrounds
5. **Monochrome** - Single-color applications

**Logo Don'ts:**
❌ Do not stretch or distort
❌ Do not change colors outside approved palette
❌ Do not add effects (shadows, glows)
❌ Do not place on busy backgrounds
❌ Do not recreate or modify

### 4.2 COLOR PALETTE

**Primary Colors:**

**Resonance Blue** - #0066CC
- RGB: 0, 102, 204
- CMYK: 100, 50, 0, 20
- Pantone: 300 C

**Energy Green** - #00A86B
- RGB: 0, 168, 107
- CMYK: 100, 0, 36, 34
- Pantone: 3395 C

**Neutral Gray** - #2C3E50
- RGB: 44, 62, 80
- CMYK: 45, 23, 0, 69

**Secondary Colors:**
- Light Blue: #E6F2FF
- Light Green: #E6F9F0
- Light Gray: #F5F7FA
- Dark Gray: #1A1A1A
- White: #FFFFFF

**Accent Colors (use sparingly):**
- Warning Orange: #FF9500
- Error Red: #DC3545

**Color Usage:**
- Resonance Blue: Primary CTAs, headers, logo
- Energy Green: Accents, sustainability messaging
- Neutral Gray: Body text, secondary elements
- White: Backgrounds, negative space

### 4.3 TYPOGRAPHY

**Primary Typeface: Inter**

**Headings:**
- H1: Inter Bold, 48px
- H2: Inter Bold, 36px
- H3: Inter SemiBold, 28px
- H4-H6: Inter SemiBold/Medium, 20-24px

**Body Text:**
- Large: Inter Regular, 18px, 1.6 line-height
- Regular: Inter Regular, 16px, 1.5 line-height
- Small: Inter Regular, 14px, 1.4 line-height

**Data/Numbers: Roboto Mono**

**Typographic Hierarchy:**
Always maintain visual hierarchy. Don't skip heading levels. Use appropriate line-height for readability (1.4-1.6 for body text).

### 4.4 IMAGERY

**Photography Style:**
- Real installations and customers (not stock photos)
- Industrial aesthetic
- Human element present
- Natural lighting
- High resolution (300 DPI minimum)

**Subjects to Show:**
✅ Installed systems, happy customers, flowing water, industrial facilities, environmental context, technical details

**Subjects to Avoid:**
❌ Generic stock photos, competitors' products, unsafe practices, poor quality images

**Image Treatment:**
- Enhance blues and greens
- Increase contrast slightly
- Maintain realism (no heavy filters)
- Overlay text with appropriate contrast (40-60% dark overlay)

### 4.5 GRAPHIC ELEMENTS

**Brand Patterns:**

**Water Flow Pattern:**
Wavy horizontal lines evoking water flow. Use as subtle backgrounds or dividers. Primary blue at 10-20% opacity.

**φ Spiral Pattern:**
Golden ratio spiral representing harmony and natural design. Use sparingly for hero sections.

**Shapes:**
- Rounded corners (8px radius standard)
- Circular elements preferred
- Organic curves, not rigid rectangles

---

## 5. VOICE & MESSAGING

**Brand Voice:**

- **Confident:** Backed by data and results
- **Clear:** No jargon, straight talk
- **Educational:** Help customers understand
- **Authentic:** Honest about trade-offs
- **Optimistic:** Positive about renewable future

**Writing Style:**
- Short sentences (15-20 words)
- Active voice
- Second person ("you")
- Specific numbers ("60% savings" not "significant savings")
- Avoid jargon or explain it

**Messaging Hierarchy:**

**Headline:** "Reliable Renewable Energy That Pays for Itself"

**Subheadline:** "Cut energy costs 60% with micro-hydro systems that generate power 24/7 for 25+ years. Installed in 2 weeks, payback in 18 months."

**Supporting Points:**
1. Proven reliability (99.7% uptime, 25-year track record)
2. Financial performance (60% savings, 18-24 month ROI)
3. Sustainability (zero emissions, ESG goals)
4. Turnkey service (we handle everything)

**Key Messages by Audience:**

- **CFOs:** ROI, payback, tax benefits
- **Sustainability Directors:** Carbon offset, ESG scores
- **Operations:** Reliability, low maintenance
- **CEOs:** Strategic advantage, competitive positioning

**Words We Use:**
✅ Reliable, proven, efficient, sustainable, renewable, savings, ROI, independence, constant, 24/7

**Words We Avoid:**
❌ Cheap, experimental, risky, unpredictable, maybe, hope, try

---

## 6. APPLICATIONS

### 6.1 BUSINESS CARDS
- Size: 3.5" x 2"
- Front: Logo, name, title, contact
- Back: Tagline, website, pattern
- Stock: Premium matte, 16pt

### 6.2 LETTERHEAD
- Logo top left
- Address bottom left
- Contact bottom right
- Subtle watermark

### 6.3 EMAIL SIGNATURE
- Name (Bold, 16px)
- Title (Regular, 14px)
- Logo (150px wide)
- Contact info
- Social icons (optional)

### 6.4 PRESENTATIONS
- Title slide: Full-width image + overlay text
- Content slides: Logo top right, left-aligned content
- Fonts: Inter throughout
- Colors: White backgrounds, blue/green accents

### 6.5 DOCUMENTS
- Cover: Hero image + title
- Headers: Logo right, page number left
- Body: Inter Regular, 11pt, 1.5 line-height
- Footers: Company name, date, confidentiality notice

---

## 7. DIGITAL GUIDELINES

### 7.1 WEBSITE

**Header:**
- Logo left, navigation right
- Sticky on scroll
- Mobile: Hamburger menu

**Footer:**
- 4 columns: About, Services, Resources, Contact
- Social icons
- Copyright notice

**Color Usage:**
- Backgrounds: White, Light Gray
- CTAs: Resonance Blue
- Accents: Energy Green
- Text: Dark Gray

**Responsive Design:**
- Mobile-first approach
- Breakpoints: 320px, 768px, 1024px, 1440px
- Touch-friendly buttons (min 48px)

### 7.2 SOCIAL MEDIA

**Profile Photos:**
- Use stacked logo or symbol only
- Consistent across all platforms

**Cover/Banner Images:**
- Hero installation image + tagline
- Update quarterly with latest projects

**Post Graphics:**
- Templates provided in Canva
- Maintain brand colors and fonts
- Include logo on all graphics

**Platform-Specific:**

**LinkedIn:** Professional, B2B focus, case studies, thought leadership
**Twitter:** Industry news, quick tips, engagement
**Facebook:** Community building, visual storytelling
**YouTube:** Installation time-lapses, customer testimonials, how-to videos
**Instagram:** Visual inspiration, behind-the-scenes, sustainability focus

### 7.3 EMAIL MARKETING

**Templates:**
- Header: Logo + navigation
- Hero: Image + headline + CTA
- Body: 600px wide, single column
- Footer: Unsubscribe + social icons

**Best Practices:**
- Subject lines: 40 characters or less
- Preview text: 80-100 characters
- Mobile-optimized (60%+ opens on mobile)
- One primary CTA per email

---

## 8. PRINT GUIDELINES

### 8.1 BROCHURES
- Tri-fold format (8.5" x 11")
- Hero image on cover
- Benefits inside left
- Case study inside middle
- Contact/CTA inside right

### 8.2 DATA SHEETS
- 2-page format
- Technical specs
- Performance data
- Installation details
- Pricing (separate insert if varies)

### 8.3 CASE STUDIES
- Cover: Customer logo + result headline
- Page 1: Challenge, Solution
- Page 2: Results (metrics), Testimonial
- Page 3: Visuals, Next Steps CTA

### 8.4 TRADESHOW MATERIALS
- Banners: 8ft retractable, hero image + tagline
- Booth graphics: Modular, easy setup
- Handouts: One-pagers, USB drives with digital assets
- Swag: Branded water bottles, notebooks, pens

---

## 9. ENVIRONMENTAL GRAPHICS

### 9.1 SIGNAGE
- Installation sites: "Powered by ResonanceEnergy" sign
- Office: Logo + tagline at entrance
- Directional: Consistent fonts and colors

### 9.2 VEHICLE WRAPS
- Large logo + phone number
- Tagline + website
- Primary blue base, white text
- High-contrast for visibility

### 9.3 APPAREL
- Polo shirts: Embroidered logo (chest)
- T-shirts: Screen-printed logo (front)
- Hats: Embroidered symbol
- Safety gear: Reflective logo (back)

---

## 10. CO-BRANDING

**When Partnering with Others:**

**Logo Placement:**
- Our logo should be equal size or larger than partner
- Maintain clear space between logos
- Use vertical divider if needed

**Approval Required:**
- All co-branded materials must be approved by marketing
- Review for brand consistency
- Ensure partner brand guidelines respected

**Examples:**
- Joint case studies
- Webinars with partners
- Co-sponsored events

---

## 11. LEGAL & COMPLIANCE

**Trademark:**
"ResonanceEnergy" and logo are registered trademarks. Use ® symbol on first mention in formal documents.

**Copyright:**
All brand assets copyright [Year] ResonanceEnergy. All rights reserved.

**Usage Restrictions:**
- Internal use and approved partners only
- No modification without approval
- No use that implies endorsement without agreement

**Disclaimer:**
Performance results are based on actual installations. Individual results may vary based on site conditions.

---

## 12. CONTACT & RESOURCES

**Brand Guardians:**
- Marketing Director: [Name, email]
- Creative Director: [Name, email]

**Questions?**
Contact marketing team: brand@resonanceenergy.com

**Resources:**
- Brand asset library: [URL]
- Templates: [URL]
- Brand guidelines PDF: [URL]

**Last Updated:** January 2026
**Next Review:** July 2026

---

**Remember:** This is a living document. As the brand evolves, these guidelines will be updated. Check for the latest version quarterly."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Brand Strategy Agent initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: positioning, messaging, visual, guidelines")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'positioning':
            info = sys.argv[2] if len(sys.argv) > 2 else ""
            print(brand_positioning(info))
        elif cmd == 'messaging':
            print(messaging_framework())
        elif cmd == 'visual':
            print(visual_identity())
        elif cmd == 'guidelines':
            print(brand_guidelines())
