"""
CUSTOMER SUCCESS AGENT
Onboarding, retention strategies, upsell opportunities, satisfaction tracking.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def onboarding_plan(customer_name):
    """Generate customer onboarding plan"""
    
    prompt = f"""Create comprehensive onboarding plan for new customer: {customer_name}

**CUSTOMER ONBOARDING PLAN** (Days 1-90)

---

**ONBOARDING PHILOSOPHY:**

First 90 days determine customer lifetime value. Goals:
1. Fast time-to-value (quick wins)
2. Product adoption (using key features)
3. Relationship building (trust and partnership)
4. Prevent buyer's remorse
5. Set up for long-term success

---

**PRE-GO-LIVE (Before installation complete)**

**Week -2: Kickoff Call**

**Attendees:** Customer (sponsor, facilities manager, operations), our team (PM, CSM, engineer)

**Agenda:**
- Introductions and roles
- Project timeline review
- Installation logistics
- Communication plan (who to contact for what)
- Training schedule
- Success metrics definition

**Deliverables:**
- [ ] Project plan document
- [ ] Contact sheet (all parties)
- [ ] Installation schedule
- [ ] Training calendar

**Week -1: Pre-Installation Prep**

- [ ] Site prep checklist sent and confirmed
- [ ] Utility interconnection coordination
- [ ] Safety protocols reviewed
- [ ] Day-of-installation logistics confirmed
- [ ] Welcome package shipped (branded swag, manuals, quick-start guide)

---

**GO-LIVE: Installation & Commissioning**

**Day 1-2: Installation**
- On-site installation team
- Daily progress updates to customer
- Photo documentation
- Safety compliance

**Day 3: Testing & Commissioning**
- System testing (72 hours of monitored operation)
- Fine-tuning and optimization
- Initial performance validation

**Day 4: Training & Handoff**

**Operations Training** (2 hours):
- System overview and components
- Control panel walkthrough
- Monitoring dashboard (web + mobile app)
- Normal operation expectations
- When to call for support

**Maintenance Training** (1 hour):
- Daily/weekly/monthly checks
- Basic troubleshooting
- When to schedule professional service

**Deliverables:**
- [ ] Training materials (videos, PDFs)
- [ ] System credentials (dashboard access)
- [ ] Maintenance schedule
- [ ] Emergency contact card

**Day 5: Celebration & Go-Live**
- Official "ribbon cutting" (photo op, press release if applicable)
- Thank you gift to project champion
- LinkedIn post highlighting partnership
- Internal celebration (team recognition)

---

**WEEK 1-2: EARLY ADOPTION**

**Goals:**
- Ensure system running smoothly
- Customer comfort with monitoring
- Quick problem resolution
- Gather feedback

**Touchpoints:**

**Day 7: Check-in Call** (15 min)
- "How's everything going?"
- Review first week performance data
- Answer any questions
- Confirm monitoring dashboard access

**Day 14: Two-Week Review** (30 min)
- Performance metrics vs. expectations
- Energy savings validation
- Operations feedback
- Schedule first maintenance

**Actions:**
- [ ] Monitor system performance daily (CSM watches dashboard)
- [ ] Proactive outreach if any anomalies detected
- [ ] Quick response to any support tickets (<2 hour response time)
- [ ] Send "Week 1 Performance Summary" email with data/charts

---

**WEEK 3-4: OPTIMIZATION**

**Goal:** Maximize performance and value realization

**Week 3: Optimization Review** (45 min)
- Analyze 3 weeks of operational data
- Identify optimization opportunities
- Adjust settings if needed
- Validate ROI projections vs. actual

**Deliverables:**
- [ ] Performance report (generation, savings, uptime)
- [ ] Comparison to projections
- [ ] Optimization recommendations implemented

**Week 4: First Business Review** (60 min)

**Agenda:**
- 30-day performance summary
- Financial impact (actual savings vs. projected)
- Operational learnings
- Maintenance schedule confirmation
- Feedback and questions
- Introduce account expansion opportunities (if appropriate)

**Attendees:** Customer (decision-maker, operator), our team (CSM, AE if expansion)

---

**MONTH 2-3: MASTERY & ADVOCACY**

**Goals:**
- Customer fully self-sufficient
- Identify expansion opportunities
- Convert to advocate/referral source

**Month 2 Touchpoints:**

**Day 45: Mid-Quarter Check-in** (30 min)
- Performance review
- Any issues or concerns?
- Introduce advanced features (if applicable)
- Request testimonial/case study participation

**Day 60: Quarterly Business Review Prep**
- Gather 60 days of performance data
- Calculate actual ROI
- Prepare formal QBR presentation

**Month 3 Touchpoints:**

**Day 75: Reference Request**
- "You've been a great partner. Would you be willing to be a reference for prospects?"
- Set up peer-to-peer calls
- LinkedIn recommendation request

**Day 90: Quarterly Business Review (QBR)** (60 min)

**Full QBR Format:**

**1. Executive Summary**
- 90-day performance highlights
- Key wins and metrics

**2. Performance Deep-Dive**
- Energy generation: ___ kWh (vs. projected: ___)
- Cost savings: $__k (vs. projected: $__k)
- Uptime: __% (target: 99%+)
- Environmental impact: ___ tons CO2 offset

**3. Operational Review**
- Maintenance completed (scheduled + unscheduled)
- Support tickets (quantity, resolution time)
- Customer satisfaction score

**4. Financial Impact**
- Actual vs. projected savings
- Payback timeline update
- Long-term ROI projection

**5. Feedback & Improvement**
- What's working well?
- What could we improve?
- Feature requests

**6. Forward-Looking**
- Upcoming maintenance schedule
- Expansion opportunities (additional systems, other sites)
- Strategic partnership discussion

**7. Action Items & Next Steps**
- Assign owners and dates for any follow-ups

---

**ONBOARDING SUCCESS METRICS:**

Track these throughout onboarding:

**Operational Metrics:**
- System uptime: Target 99%+
- Performance vs. projection: Within 10%
- Time to first value: <7 days
- Support tickets: <2 per month

**Engagement Metrics:**
- Monitoring dashboard logins: 3+ per week
- Training completion: 100%
- Check-in call attendance: 100%
- QBR attendance: Decision-maker present

**Satisfaction Metrics:**
- Customer satisfaction score (CSAT): 8+/10
- Net Promoter Score (NPS): 8+/10
- Likelihood to refer: High

**Revenue Metrics:**
- On-time payment: Yes
- Expansion opportunity identified: Y/N
- Referrals provided: Y/N

---

**RED FLAGS (At-Risk Customer):**

Watch for these warning signs:

- ⚠️ Low dashboard engagement (<1 login/week)
- ⚠️ Missed check-in calls or QBR
- ⚠️ Multiple support tickets with same issue
- ⚠️ Performance below expectations not addressed
- ⚠️ Decision-maker disengaged
- ⚠️ Payment delays
- ⚠️ Negative feedback not resolved

**If red flags appear:**
1. Executive escalation (our exec calls their exec)
2. On-site visit to resolve issues
3. Performance improvement plan
4. Enhanced support (more frequent check-ins)

---

**GREEN FLAGS (Expansion Opportunity):**

Watch for these positive signals:

- ✅ High engagement (frequent logins, questions)
- ✅ Exceeding performance expectations
- ✅ Executive sponsor actively promoting internally
- ✅ Requesting advanced features or customization
- ✅ Multiple facilities in portfolio (expansion potential)
- ✅ Referring other customers
- ✅ Asking about other products/services

**If green flags appear:**
1. Introduce account expansion conversation
2. Map out other potential sites
3. Offer multi-site discount
4. Fast-track expansion opportunities

---

**ONBOARDING COMMUNICATION CALENDAR:**

| Day | Touchpoint | Owner | Format | Duration |
|-----|------------|-------|--------|----------|
| -14 | Kickoff call | PM | Video | 60 min |
| -7 | Pre-install prep | PM | Email | - |
| 0 | Installation start | PM | On-site | 2 days |
| 3 | Commissioning | Engineer | On-site | 1 day |
| 4 | Training | Engineer | On-site | 3 hours |
| 5 | Go-live celebration | CSM | On-site | 1 hour |
| 7 | Week 1 check-in | CSM | Call | 15 min |
| 14 | Two-week review | CSM | Call | 30 min |
| 21 | Optimization review | CSM | Call | 45 min |
| 30 | First business review | CSM + AE | Video | 60 min |
| 45 | Mid-quarter check-in | CSM | Call | 30 min |
| 75 | Reference request | CSM | Email | - |
| 90 | Quarterly business review | CSM + Exec | Video | 60 min |

---

**ONBOARDING TOOLKIT:**

**Documents:**
- [ ] Welcome letter from CEO
- [ ] Quick start guide (1-pager)
- [ ] Detailed operations manual
- [ ] Maintenance checklist
- [ ] Troubleshooting guide
- [ ] FAQs
- [ ] Contact directory
- [ ] Service level agreement (SLA)

**Digital Assets:**
- [ ] Training videos (operations, maintenance)
- [ ] Dashboard tutorial (screen recording)
- [ ] Knowledge base access
- [ ] Mobile app download links

**Physical:**
- [ ] Welcome box (branded swag: hat, water bottle, sticker)
- [ ] Site signage (optional: "Powered by Renewable Energy")
- [ ] Emergency contact card (laminated)
- [ ] Maintenance log binder

---

**CUSTOMER SUCCESS TEAM ROLES:**

**Customer Success Manager (CSM):**
- Primary relationship owner
- Onboarding orchestration
- Ongoing check-ins and QBRs
- Renewal management
- Expansion opportunity identification

**Implementation/Project Manager (PM):**
- Installation project management
- Timeline and logistics
- Stakeholder coordination
- Handoff to CSM at go-live

**Support Engineer:**
- Technical training
- Troubleshooting assistance
- Performance optimization
- Scheduled maintenance

**Account Executive (AE):**
- Contract and commercial terms
- Expansion sales
- Executive relationship
- Attend key milestones (QBRs)

---

**POST-ONBOARDING (Day 91+):**

Transition to steady-state customer success:

**Ongoing Cadence:**
- Monthly: Performance report (automated email)
- Quarterly: Business review (live meeting)
- Annually: Strategic planning session

**Continuous Activities:**
- Proactive monitoring (daily dashboard checks)
- Scheduled maintenance (per contract)
- Product updates and enhancements
- Industry insights and best practices sharing
- Community building (customer events, user groups)

**Goal:** Turn customer into lifelong partner and advocate.

---

Remember: Onboarding is NOT just about training. It's about building trust, demonstrating value, and creating advocates."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def retention_strategy():
    """Generate customer retention playbook"""
    
    prompt = """Create customer retention strategy and tactics:

**CUSTOMER RETENTION PLAYBOOK**

---

**WHY RETENTION MATTERS:**

- Acquiring new customer costs 5-25x more than retaining existing
- 5% increase in retention = 25-95% increase in profits
- Existing customers spend 67% more than new customers
- Retained customers provide referrals

**Goal:** 95%+ retention rate (industry benchmark: 70-85%)

---

**RETENTION FRAMEWORK:**

**1. DELIVER VALUE** (They get what they paid for)
**2. BUILD RELATIONSHIPS** (They like working with you)
**3. ANTICIPATE NEEDS** (You're proactive, not reactive)
**4. MAKE IT EASY** (Low friction to stay, high friction to leave)
**5. CONTINUOUS IMPROVEMENT** (Always getting better)

---

**STAGE 1: PREVENT CHURN** (Defensive)

**Early Warning System:**

**At-Risk Indicators:**
- Low product usage (dashboard logins <1/week)
- Support tickets not resolved quickly
- Performance below expectations
- Missed QBR or check-in calls
- Payment delays
- Executive sponsor turnover
- Negative NPS score (<7)
- Asking about contract terms (cancellation clause)

**Health Score Model** (0-100):

**Product Usage (30 points):**
- Daily monitoring: 30 pts
- Weekly monitoring: 20 pts
- Monthly monitoring: 10 pts
- No monitoring: 0 pts

**Performance (25 points):**
- Exceeding expectations: 25 pts
- Meeting expectations: 20 pts
- Below expectations (minor): 10 pts
- Below expectations (major): 0 pts

**Engagement (20 points):**
- Attends all QBRs: 20 pts
- Attends some QBRs: 10 pts
- Misses QBRs: 0 pts

**Support (15 points):**
- No unresolved tickets: 15 pts
- 1-2 unresolved tickets: 5 pts
- 3+ unresolved tickets: 0 pts

**Advocacy (10 points):**
- Provided referrals: 10 pts
- Willing to be reference: 5 pts
- Not willing: 0 pts

**Health Score Ranges:**
- **90-100**: Healthy (Green)
- **70-89**: At-risk (Yellow)
- **<70**: Critical (Red)

**Actions by Health Score:**

**Green (90-100):**
- Standard engagement cadence
- Upsell/cross-sell opportunities
- Request referrals and case studies
- Invite to customer advisory board

**Yellow (70-89):**
- Schedule immediate check-in call
- Identify and address concerns
- Increase touchpoint frequency
- CSM escalates to manager

**Red (<70):**
- Executive escalation (VP or CEO involvement)
- On-site visit within 1 week
- Performance improvement plan
- Enhanced support (24/7 access, dedicated engineer)
- Commercial concessions if appropriate (discount, extended warranty)

---

**STAGE 2: INCREASE ENGAGEMENT** (Active)

**Engagement Tactics:**

**1. Regular Communication:**
- Monthly performance reports (automated)
- Quarterly business reviews (live)
- Industry insights newsletter
- Product updates and feature releases
- Best practices and tips

**2. Proactive Support:**
- Monitor systems daily (we see issues before they do)
- Seasonal prep (winterization, storm prep)
- Predictive maintenance alerts
- Optimization recommendations

**3. Community Building:**
- Annual customer conference
- Regional user groups
- Online customer community forum
- Peer networking opportunities
- Executive roundtables

**4. Value-Add Services:**
- Free performance audits (annual)
- Energy market insights
- Regulatory updates (incentives, rebates)
- Sustainability reporting assistance
- Grant writing support for expansions

**5. Recognition Programs:**
- Customer of the month/year
- Sustainability champions award
- Social media features
- Speaking opportunities (webinars, conferences)
- Co-marketing opportunities

---

**STAGE 3: EXPAND RELATIONSHIP** (Growth)

**Expansion Strategies:**

**1. Land and Expand:**
- Start with one system
- Prove value
- Expand to other facilities/sites

**2. Upsell:**
- Enhanced monitoring and analytics
- Extended warranty
- Premium support (24/7, faster response)
- Energy storage integration
- System upgrades (higher capacity)

**3. Cross-Sell:**
- Other renewable energy solutions (solar, wind)
- Energy efficiency consulting
- Demand response programs
- Power purchase agreements
- Maintenance contracts

**Expansion Triggers:**

Watch for these signals:
- System performing above expectations
- Executive sponsor highly satisfied
- Multiple facilities in portfolio
- Growing energy needs
- Expansion plans or new construction
- Increased sustainability focus
- Budget availability

**Expansion Playbook:**

**Month 6:** "How's the system performing? Any thoughts on expanding?"
**Month 12:** "Let's map out your other facilities. Where else could this work?"
**Month 18:** Present expansion proposal with multi-site discount
**Month 24:** Annual strategic planning session (enterprise-wide energy strategy)

---

**STAGE 4: CREATE ADVOCATES** (Evangelism)

**Advocacy Ladder:**

**Level 1: Satisfied Customer**
- Renews contract
- No complaints

**Level 2: Happy Customer**
- Provides positive feedback
- Willing to be case study

**Level 3: Reference**
- Takes peer-to-peer reference calls
- Allows site visits from prospects
- Writes testimonials

**Level 4: Advocate**
- Proactively refers new business
- Speaks at events
- Co-creates content (webinars, videos)
- Joins customer advisory board

**Level 5: Champion**
- Influencer in industry
- Public endorsement (social media, press)
- Strategic partner relationship
- Co-innovation opportunities

**How to Move Up the Ladder:**

1. **Ask at the right time** (after successful milestone)
2. **Make it easy** (provide templates, do the work)
3. **Show appreciation** (thank you gifts, recognition)
4. **Reciprocate** (referral fees, discounts, VIP treatment)

**Referral Program:**

- $5,000 cash or 5% discount for qualified referral
- $10,000 if referral closes
- Public recognition (customer spotlight)
- Exclusive benefits (priority support, beta access)

---

**RENEWAL STRATEGY:**

**Timeline:**

**12 Months Before Renewal:**
- Annual strategic review
- Multi-year renewal discussion
- Expansion opportunities

**6 Months Before Renewal:**
- Renewal intent conversation
- Address any outstanding concerns
- Present renewal proposal (with incentives for multi-year)

**3 Months Before Renewal:**
- Formal renewal contract sent
- Executive-to-executive call
- Negotiate terms if needed

**1 Month Before Renewal:**
- Urgency/expiration reminders
- Final objection handling
- Execute contract

**Goal:** 100% of renewals closed 3+ months before expiration

**Renewal Incentives:**

- 10% discount for 3-year renewal
- 15% discount for 5-year renewal
- Free system upgrades
- Extended warranty
- Priority support

---

**CHURN PREVENTION (When customer wants to leave):**

**Save Protocol:**

**Step 1: Understand Why**
- "Help me understand what's driving this decision"
- Listen actively
- Don't get defensive

**Step 2: Address Concerns**
- If performance issues: immediate remediation plan
- If cost concerns: restructure pricing or payment terms
- If service issues: enhanced support commitment
- If they're unhappy: executive involvement to fix

**Step 3: Offer Incentives**
- Discount for one more year
- Free upgrades or enhancements
- Extended warranty
- Commercial concessions

**Step 4: Make Counter-Offer**
- "Before you decide, can we try [solution] for 90 days?"
- Pause contract (instead of cancel)
- Reduced scope (instead of full termination)

**Step 5: Graceful Exit (if lost)**
- "I'm sorry we couldn't meet your needs"
- "Can we stay in touch? Situations change"
- "Would you be willing to share feedback to help us improve?"
- Exit interview (learn for future)

**Winback Campaign:**

If customer churns:
- Month 3: "How's the alternative working out?"
- Month 6: "We've made improvements based on feedback"
- Month 12: "Let's reconnect - here's what's new"
- Offer special "boomerang customer" incentive

---

**RETENTION METRICS TO TRACK:**

**Lagging Indicators (Outcomes):**
- Customer retention rate (90-day, annual)
- Net revenue retention (includes expansions)
- Customer lifetime value (LTV)
- Churn rate

**Leading Indicators (Predictive):**
- Health scores
- Product usage
- NPS scores
- Support ticket trends
- QBR attendance
- Payment timeliness

**Dashboard Example:**

| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| Retention rate | 95% | 94% | ↑ |
| NPS | 50+ | 62 | ↑ |
| Avg health score | 85+ | 88 | → |
| At-risk customers | <5% | 3% | ↓ |
| Expansion rate | 20% | 25% | ↑ |

---

**CUSTOMER SUCCESS TEAM STRUCTURE:**

**1-50 customers:** 1 CSM (1:50 ratio)
**51-200 customers:** CSM team with tiering:
- Enterprise customers (>$100k): 1:20 ratio
- Mid-market ($25k-100k): 1:40 ratio
- Small (<$25k): 1:100 ratio + automation

**Responsibilities:**
- Onboarding
- QBRs
- Health monitoring
- Renewal management
- Expansion identification
- Advocacy development

---

**RETENTION INVESTMENT:**

Spending on retention (% of revenue):
- 5-7% is typical
- Includes: CSM salaries, tools, customer events, training, support

ROI: Every $1 spent on retention returns $5-10 in retained + expanded revenue

---

**KEY PRINCIPLES:**

1. **Prevent, don't react:** Spot issues early
2. **Deliver outcomes, not outputs:** They don't care about features, they care about savings
3. **Build relationships:** People buy from people they like
4. **Be proactive:** Don't wait for them to ask
5. **Never get comfortable:** Even happy customers can churn
6. **Treat them like they're always being recruited:** Because competitors are always trying

**Mission:** Make customers so successful and happy that leaving becomes unthinkable."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def upsell_opportunities(customer_profile):
    """Identify and present upsell opportunities"""
    
    prompt = f"""Identify upsell and expansion opportunities for customer:

**Customer Profile:** {customer_profile}

**UPSELL OPPORTUNITY ANALYSIS**

---

**UPSELL VS. CROSS-SELL:**

- **Upsell:** Increase value of current solution (bigger, better, more)
- **Cross-sell:** Add complementary solutions (different products/services)

Both grow revenue and deepen customer relationships.

---

**OPPORTUNITY IDENTIFICATION:**

**When to Approach:**

✅ **Green Lights (Go for it):**
- System performing above expectations
- Customer highly satisfied (NPS 9-10)
- Executive sponsor engaged and happy
- On-time payments, no issues
- Customer actively using product
- Recently achieved major milestone
- Budget season (planning for next year)

❌ **Red Lights (Not now):**
- Performance issues unresolved
- Unhappy or frustrated customer
- Payment delays or financial distress
- Leadership turnover
- Active competitive evaluation
- Contract expiring soon (focus on renewal first)

---

**EXPANSION OPPORTUNITY TYPES:**

**1. GEOGRAPHIC EXPANSION** (Other facilities)

**Discovery Questions:**
- "How many other facilities do you have?"
- "Are any of them similar to this site?"
- "What's your energy situation at [other location]?"

**Value Proposition:**
- Economies of scale (multi-site discount)
- Standardized operations across portfolio
- Enterprise-level reporting and management
- Faster implementation (we already know you)

**Offer:**
"We're offering 15% discount for your second site and 20% for sites 3+. 
Plus, we can run preliminary analysis on all your sites for free.
Should we explore this?"

---

**2. CAPACITY EXPANSION** (Bigger system at same site)

**Triggers:**
- Business growing (more energy demand)
- New buildings or equipment
- Current system at full capacity
- High satisfaction with existing system

**Discovery Questions:**
- "Have your energy needs changed since installation?"
- "Are you planning any expansion or new equipment?"
- "Is the current system meeting 100% of your needs?"

**Value Proposition:**
- Incremental addition (not starting over)
- Further reduce grid dependence
- Maximize available water resource
- Marginal cost lower than original (infrastructure exists)

**Offer:**
"Adding 50kW would cost $X, bring your savings to $Y, and payback in Z months.
Want me to run the numbers?"

---

**3. ENHANCED SERVICES** (Premium support, analytics, optimization)

**Upgrade Tiers:**

**BASIC** (Standard contract):
- Business hours support (8am-6pm)
- Quarterly check-ins
- Annual maintenance
- Standard reporting

**PREMIUM** ($5k-10k/year):
- 24/7 emergency support
- Monthly optimization reviews
- Priority service response (<4 hours)
- Advanced analytics dashboard
- Predictive maintenance
- Energy market insights

**ENTERPRISE** ($25k-50k/year):
- Dedicated account team
- On-site engineer (quarterly visits)
- Custom integrations
- White-glove service
- Executive business reviews
- Strategic energy planning

**When to Offer:**
- Customer has complex operations
- High cost of downtime
- Multiple systems
- Executive wants hands-off experience
- Budget for premium services

---

**4. TECHNOLOGY UPGRADES** (Better, newer, faster)

**Upgrade Opportunities:**

**Control Systems:**
- AI-powered optimization ($10k-20k)
- Remote monitoring upgrades ($5k)
- Predictive analytics ($15k/year subscription)

**Physical Components:**
- Higher-efficiency turbine ($30k-50k, +10-15% output)
- Advanced filtration ($20k, extends lifespan)
- Backup systems for redundancy ($40k-60k)

**When to Offer:**
- System 5+ years old
- New technology available
- Customer focused on maximizing ROI
- Payback demonstrated on current system

---

**5. COMPLEMENTARY SYSTEMS** (Cross-sell other solutions)

**Solar + Hydro Hybrid:**
"You have micro-hydro covering nights and cloudy days. 
Adding solar would cover daytime peaks and get you to 100% renewable.
Combined system would cut your grid dependence to near-zero."

**Energy Storage:**
"Add battery storage to bank excess generation for peak demand hours.
That would eliminate demand charges entirely."

**Energy Management:**
"We can integrate smart load management to automatically shift usage to times when your system is generating most."

**EV Charging:**
"Planning to electrify your fleet? We can integrate EV charging powered by your renewable energy."

**When to Offer:**
- Customer achieved sustainability goals (wants more)
- New initiatives (EV fleet, net-zero commitment)
- Available capital budget
- Synergy with existing system

---

**6. ADJACENT SERVICES** (Consulting, training, certification)

**Energy Audits:**
"We can audit your full facility to identify other efficiency opportunities.
Typically find 20-30% more savings."

**Sustainability Reporting:**
"Need help with carbon reporting, ESG metrics, or sustainability certifications?
We can quantify and document your environmental impact."

**Training Programs:**
"Want to upskill your facilities team? We offer certified training on renewable energy systems."

**Grant Writing:**
"There are new incentives available. We can help you apply and maximize your rebates."

---

**UPSELL APPROACH:**

**1. TIMING**

Best times to introduce upsell:
- After QBR (when performance is top of mind)
- At renewal conversation (bundling)
- After major milestone (positive momentum)
- During budget planning season
- When customer asks for more

**2. POSITIONING**

❌ Don't say: "Want to buy more stuff?"

✅ Do say: 
"Based on your success with this system and your goals, I have an idea that could [achieve X]. 
Would you like to hear it?"

**3. FRAMING**

Connect to their goals:
- Cost savings: "This would save you an additional $X/year"
- Sustainability: "This would get you to net-zero by [date]"
- Reliability: "This would eliminate your dependence on [risk]"
- Growth: "This would support your expansion into [market]"

**4. PROOF**

Show similar customers who expanded:
"[Company X] started with one 100kW system, expanded to three sites, and now saves $500k/year. 
I think you have similar potential."

**5. EASY FIRST STEP**

Remove friction:
"Let me run a free assessment and show you the numbers. 
No obligation - just so you know what's possible."

---

**UPSELL MESSAGING SCRIPTS:**

**For Geographic Expansion:**
"I was looking at your portfolio and noticed you have 5 other manufacturing sites. 
If we could replicate the success you're seeing here at even 2-3 of those locations, you'd be saving over $1M/year. 
Want me to run preliminary analysis on those sites? Takes 30 minutes each, no cost."

**For Capacity Upgrade:**
"Congratulations on your facility expansion! With the new production line, your energy needs will increase about 30%. 
Rather than pulling more from the grid, we could expand your micro-hydro system to cover that new load. 
Actually might be cheaper than upgrading your grid service. Want to compare options?"

**For Premium Support:**
"I know uptime is critical for you. What if you had 24/7 emergency support, predictive maintenance alerts, and guaranteed 4-hour response time? 
Some of our enterprise customers value that peace of mind. 
For about $10k/year - which is less than one day of downtime for you - you'd get white-glove service. 
Should I send you the details?"

**For Technology Upgrade:**
"We just released AI-powered optimization that's increasing output by 12-15% for existing systems. 
One-time cost of $15k, which would pay for itself in under a year based on your current savings. 
Want to be one of the first to pilot it?"

**For Complementary System:**
"You're 70% renewable with the micro-hydro. I was thinking - if we added solar on your south-facing roof, you'd hit 95%+ renewable energy. 
That would qualify you for [certification/tax credit] and really amplify your sustainability story. 
Want me to scope it out?"

---

**UPSELL METRICS:**

**Track:**
- Expansion rate: X% of customers expand per year
- Average expansion value: $Y per expanding customer
- Time to first expansion: Z months average
- Net revenue retention: >100% (includes expansions)

**Targets:**
- 30% of customers expand within 24 months
- Average expansion value: 50% of original contract
- 120% net revenue retention

---

**EXPANSION OBJECTIONS:**

**"We don't have budget"**
→ "When does your next budget cycle start? Let's plan ahead."

**"We're happy with what we have"**
→ "That's great! This isn't about fixing something broken - it's about capitalizing on what's working."

**"We need to focus on other priorities"**
→ "I understand. What if this supported those priorities? [Link to their initiatives]"

**"Maybe next year"**
→ "Makes sense. Let's put a placeholder in Q4 to revisit. And I'll keep you updated on any new incentives that might accelerate the timeline."

---

**GOLDEN RULE:**

Upsell because it genuinely helps the customer achieve more, not just to hit quota.

If done right, expansions are:
- Win for customer (more value)
- Win for you (more revenue)
- Win for relationship (deeper partnership)

When approached this way, customers THANK YOU for bringing opportunities to them."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def satisfaction_tracking():
    """Generate customer satisfaction measurement framework"""
    
    prompt = """Create comprehensive customer satisfaction tracking system:

**CUSTOMER SATISFACTION TRACKING FRAMEWORK**

---

**WHY MEASURE SATISFACTION:**

- Early warning system for churn
- Identify improvement opportunities
- Validate product-market fit
- Benchmark against industry
- Track team performance
- Inform product roadmap
- Generate advocates

**Don't just measure - ACT on the data!**

---

**METRIC #1: NET PROMOTER SCORE (NPS)**

**The Question:**
"On a scale of 0-10, how likely are you to recommend [Company] to a colleague or friend?"

**Scoring:**
- **9-10: Promoters** (your advocates)
- **7-8: Passives** (satisfied but unenthusiastic)
- **0-6: Detractors** (unhappy, at-risk)

**NPS Calculation:**
NPS = % Promoters - % Detractors

Example: 50% promoters, 30% passives, 20% detractors = NPS of 30

**Industry Benchmarks:**
- World-class: 70+
- Excellent: 50-70
- Good: 30-49
- Average: 0-29
- Poor: Negative

**When to Survey:**
- Day 30 (post-onboarding)
- Day 90 (first quarter)
- Quarterly ongoing
- After major interactions (support resolution, upgrade)

**Follow-up Questions:**
"What's the primary reason for your score?"

**Action Protocol:**

**For Detractors (0-6):**
1. CSM notified immediately (within 1 hour)
2. Call customer within 24 hours
3. Understand issue and create action plan
4. Executive escalation if needed
5. Follow up until resolved
6. Re-survey after resolution

**For Passives (7-8):**
1. Understand what would make them a 9 or 10
2. Identify opportunities to elevate experience
3. Follow up on specific requests
4. Check in monthly

**For Promoters (9-10):**
1. Thank them!
2. Request testimonial/referral
3. Invite to customer advisory board
4. Feature in case study
5. Offer referral incentive

---

**METRIC #2: CUSTOMER SATISFACTION SCORE (CSAT)**

**The Question:**
"How satisfied are you with [specific interaction/experience]?"

**Scale:** 1-5 (Very Unsatisfied to Very Satisfied)

**When to Use:**
- After support ticket closure
- Post-training session
- After installation/implementation
- Post-QBR or check-in call
- After account issue resolution

**Target:** 4.5+ average

**Action Protocol:**
- Score 1-3: Immediate manager review and follow-up
- Score 4: Understand how to improve to 5
- Score 5: Thank customer, ask for testimonial

---

**METRIC #3: CUSTOMER EFFORT SCORE (CES)**

**The Question:**
"How easy was it to [accomplish task/resolve issue]?"

**Scale:** 1-7 (Very Difficult to Very Easy)

**When to Use:**
- After support interaction
- After onboarding
- After using new feature
- After contract renewal

**Why It Matters:**
Low effort = high loyalty. Customers hate friction.

**Target:** 6+ average

**Action Protocol:**
- Score 1-4: Identify friction points and improve process
- Score 5: Good but room for improvement
- Score 6-7: Document what worked well, replicate

---

**METRIC #4: PRODUCT-SPECIFIC METRICS**

**System Performance Satisfaction:**
"Rate your satisfaction with system performance (energy generation, reliability, uptime)"

**Support Satisfaction:**
"Rate your satisfaction with customer support (responsiveness, resolution, expertise)"

**Value for Money:**
"Rate how well the system delivers value compared to cost"

**Ease of Use:**
"Rate how easy the system is to operate and monitor"

**Each 1-5 scale, measure quarterly**

---

**SURVEY STRATEGY:**

**Frequency:**
- Too often: Survey fatigue, declining response rates
- Too rare: Miss important signals

**Recommended Cadence:**
- **Transactional surveys:** After specific interactions (support, training)
- **Relationship surveys:** Quarterly (NPS, CSAT, Product metrics)
- **Annual survey:** Comprehensive deep-dive

**Survey Length:**
- Transactional: 1-2 questions (30 seconds)
- Quarterly: 5-7 questions (2-3 minutes)
- Annual: 15-20 questions (5-7 minutes)

**Response Rate Optimization:**
- Personal invitation (from CSM, not generic)
- Explain why their feedback matters
- Show past actions taken based on feedback
- Keep it short
- Mobile-friendly
- Incentive (optional): $25 gift card for annual survey

**Target Response Rate:** 40%+ for relationship surveys

---

**QUALITATIVE FEEDBACK:**

Numbers tell you WHAT, stories tell you WHY.

**Open-Ended Questions:**
- "What's working well for you?"
- "What could we improve?"
- "What features or services would you like to see?"
- "What almost prevented you from choosing us?"
- "What would make you recommend us more strongly?"

**Customer Interviews:**
- Quarterly with promoters (understand success drivers)
- Immediately with detractors (damage control)
- Annually with strategic accounts (strategic alignment)

**Win/Loss Analysis:**
- Won deals: What tipped the scales?
- Lost deals: Why did we lose?
- Patterns and themes

---

**HEALTH SCORE (Composite Metric)**

Combine multiple signals into one score (0-100):

**Component 1: Product Usage (30%)**
- Login frequency
- Feature adoption
- Active users

**Component 2: Business Outcomes (25%)**
- Performance vs. expectations
- ROI achievement
- Goal attainment

**Component 3: Engagement (20%)**
- QBR attendance
- Response rates
- Relationship breadth

**Component 4: Satisfaction (15%)**
- NPS score
- CSAT scores
- No escalations

**Component 5: Support (10%)**
- Ticket volume (low is good)
- Resolution satisfaction
- No repeat issues

**Health Score Ranges:**
- **90-100: Thriving** (green) - upsell opportunity
- **70-89: Healthy** (green) - maintain current approach
- **50-69: At-risk** (yellow) - intervention needed
- **<50: Critical** (red) - executive escalation

**Automated Alerts:**
- Health score drops 10+ points: Alert CSM
- Health score below 70: Alert CSM + manager
- Health score below 50: Alert exec team

---

**DASHBOARD & REPORTING:**

**CSM Dashboard (Individual View):**
- My customers' NPS trend
- My customers' health scores
- At-risk customers (action needed)
- Upcoming renewals
- Expansion opportunities

**Management Dashboard (Team View):**
- Team NPS trend
- Customer distribution by health score
- Response rates
- Churn risk analysis
- Benchmarks (vs. targets, vs. industry)

**Executive Dashboard (Company View):**
- Overall NPS and trend
- Customer retention rate
- Net revenue retention
- Top themes from feedback
- Action plan status

---

**FEEDBACK LOOP (Close the Loop):**

**Step 1: COLLECT**
- Survey customers regularly
- Monitor health scores
- Gather qualitative feedback

**Step 2: ANALYZE**
- Identify trends and patterns
- Segment by customer type
- Prioritize issues

**Step 3: ACT**
- Create improvement plans
- Assign owners and dates
- Implement changes

**Step 4: COMMUNICATE**
- Tell customers what you learned
- Show what you're changing
- Ask for continued feedback

**Step 5: MEASURE**
- Did satisfaction improve?
- Did churn decrease?
- Did NPS increase?

**Example Communication:**
"Last quarter, you told us that [issue]. We heard you!
Here's what we've done: [changes made].
Thank you for helping us improve. Keep the feedback coming!"

---

**VOICE OF CUSTOMER (VOC) PROGRAM:**

**Customer Advisory Board:**
- 10-15 customers (mix of industries, sizes)
- Meet quarterly (1-2 hours)
- Preview new features
- Provide strategic input
- Strengthen relationships

**Beta Programs:**
- Invite engaged customers to test new features
- Gather feedback before broad release
- Make them feel like insiders

**Customer Events:**
- Annual user conference
- Regional meetups
- Virtual town halls
- Training workshops

**Recognition:**
- Customer of the month/quarter/year
- Success story features
- Speaking opportunities
- Awards and trophies

---

**SATISFACTION BENCHMARKS (Targets):**

| Metric | Target | World-Class |
|--------|--------|-------------|
| NPS | 30+ | 50+ |
| CSAT | 4.0+ | 4.5+ |
| CES | 6.0+ | 6.5+ |
| Health Score Avg | 80+ | 90+ |
| Response Rate | 40%+ | 60%+ |
| Time to Resolution | <24 hrs | <4 hrs |
| Churn Rate | <10% | <5% |

---

**COMMON PITFALLS:**

❌ **Surveying but not acting** → Customers feel ignored
❌ **Asking too often** → Survey fatigue
❌ **Questions too vague** → Unusable data
❌ **No follow-up** → Missed opportunities
❌ **Only measuring detractors** → Miss chances with promoters
❌ **Measuring but not sharing** → Team doesn't know priorities

---

**SUCCESS STORIES:**

**Before Satisfaction Tracking:**
- Customers churning without warning
- No idea what to improve
- Reactive firefighting

**After Satisfaction Tracking:**
- Churn reduced by 40%
- Product improvements driven by feedback
- Proactive issue resolution
- More promoters and referrals
- Higher retention and expansion

---

**FINAL PRINCIPLE:**

"Customers don't care how much you know until they know how much you care."

Measuring satisfaction isn't about numbers - it's about demonstrating that you listen, care, and continuously improve to serve them better.

Do that, and retention, advocacy, and expansion will follow naturally."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Customer Success Agent initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: onboarding, retention, upsell, satisfaction")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'onboarding':
            customer = sys.argv[2] if len(sys.argv) > 2 else 'New Customer'
            print(onboarding_plan(customer))
        elif cmd == 'retention':
            print(retention_strategy())
        elif cmd == 'upsell':
            profile = sys.argv[2] if len(sys.argv) > 2 else 'Manufacturing customer, 1 system, highly satisfied'
            print(upsell_opportunities(profile))
        elif cmd == 'satisfaction':
            print(satisfaction_tracking())
