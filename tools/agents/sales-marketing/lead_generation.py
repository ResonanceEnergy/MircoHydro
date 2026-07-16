"""
LEAD GENERATION AGENT
Prospect identification, qualification, nurturing, and scoring.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def identify_prospects(industry, criteria=""):
    """Identify ideal prospects matching criteria"""
    
    prompt = f"""Identify high-value prospects for micro-hydro solutions:

**Target Industry**: {industry}
**Criteria**: {criteria}

**IDEAL CUSTOMER PROFILE (ICP):**

**1. DEMOGRAPHICS**
- Company size: [employees, revenue]
- Industry verticals: [specific types]
- Geographic locations: [regions/states]
- Business model: [B2B, B2C, etc.]

**2. FIRMOGRAPHICS**
- Annual energy spend: $___+
- Facility characteristics: [square footage, operations]
- Current energy sources: [grid, diesel, etc.]
- Pain points: [cost, reliability, sustainability goals]

**3. DECISION-MAKERS TO TARGET**
- Titles: [CFO, COO, Sustainability Director, etc.]
- Departments: [Operations, Finance, Facilities]
- Reporting structure

**4. BUYING SIGNALS**
- Recent funding/expansion
- Sustainability commitments
- Energy infrastructure projects
- Cost reduction initiatives
- Regulatory compliance needs

**5. DISQUALIFIERS**
- Too small (energy usage below threshold)
- No suitable water resources
- Budget constraints
- Recent competitive installation

---

**PROSPECTING SOURCES:**

**LinkedIn Sales Navigator:**
- Search filters: [specific criteria]
- Boolean search strings
- Saved searches to create

**Industry Databases:**
- Manufacturing directories
- Agriculture associations
- Commercial real estate databases
- Industrial facility lists

**Website Visitor Identification:**
- Companies visiting pricing page
- Download gated content
- Multiple return visits
- High engagement (3+ pages, 2+ minutes)

**Trade Shows & Events:**
- Upcoming events to attend
- Attendee lists to acquire
- Speaking opportunities

**Referrals & Partnerships:**
- Current customer referrals
- Engineering firm partnerships
- Energy consultant networks

---

**PROSPECTING WORKFLOW:**

**Week 1-2: List Building**
- Compile 500+ target companies
- Enrich with contact data
- Score by fit (A, B, C tiers)
- Assign to sales reps

**Week 3-4: Outreach**
- Multi-channel campaigns (email, LinkedIn, phone)
- Personalized messaging per tier
- Value-focused approach

---

**TARGET COMPANY LIST (Top 50 examples):**

| Company | Industry | Location | Annual Revenue | Energy Spend Est. | Decision-Maker | Fit Score | Next Action |
|---------|----------|----------|----------------|-------------------|----------------|-----------|-------------|
| [Company 1] | Manufacturing | [State] | $__M | $__k | [Name, Title] | A | Call |
| [Company 2] | Agriculture | [State] | $__M | $__k | [Name, Title] | A | Email |
| [Company 3] | Commercial | [State] | $__M | $__k | [Name, Title] | B | LinkedIn |

Generate list with real research in your industry and geography."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

def qualify_leads(lead_info):
    """Score and qualify leads using BANT framework"""
    
    prompt = f"""Qualify this lead using BANT framework:

**Lead Info**: {lead_info}

**BANT QUALIFICATION:**

**B = BUDGET**
- Do they have budget allocated? [Y/N/Unknown]
- Estimated budget range: $___ to $___
- Budget authority: [Who controls it?]
- Budget timing: [Current FY / Next FY / Future]
- **Score (0-25)**: __/25

**A = AUTHORITY**
- Is this the decision-maker? [Y/N]
- Decision-making process: [Individual / Committee / Board]
- Key stakeholders: [List names, roles]
- Economic buyer: [Who signs the check?]
- **Score (0-25)**: __/25

**N = NEED**
- Pain points: [Specific problems]
- Impact of NOT solving: [Consequences]
- Urgency level: [Critical / Important / Nice-to-have]
- Existing alternatives: [Current solutions]
- **Score (0-25)**: __/25

**T = TIMELINE**
- When do they want to implement? [Date/Quarter]
- What's driving the timeline? [Event, deadline, goal]
- Are there blockers? [Regulatory, budget, resources]
- Realistic timeline: [Assessment]
- **Score (0-25)**: __/25

---

**OVERALL LEAD SCORE: __/100**

**Classification:**
- **90-100**: Hot Lead (A) - Immediate follow-up
- **70-89**: Warm Lead (B) - Active nurturing
- **50-69**: Cool Lead (C) - Long-term nurturing
- **Below 50**: Disqualified - Add to newsletter only

---

**QUALIFICATION QUESTIONS ANSWERED:**

✅ Do they have a clear business problem we can solve?
✅ Can they afford our solution?
✅ Are we talking to the right person?
✅ Is there a defined timeline?
✅ What's the competitive landscape?
✅ What are the blockers to closing?

---

**RECOMMENDED NEXT STEPS:**

**If Hot Lead (A):**
1. Schedule discovery call within 48 hours
2. Send ROI calculator
3. Prepare custom proposal
4. Involve executive sponsor if needed

**If Warm Lead (B):**
1. Send case study relevant to their industry
2. Schedule exploratory call next week
3. Add to nurturing sequence
4. Connect on LinkedIn

**If Cool Lead (C):**
1. Add to long-term nurturing campaign
2. Send quarterly check-ins
3. Share educational content
4. Monitor for buying signals

**If Disqualified:**
1. Document reason in CRM
2. Add to newsletter (stay top of mind)
3. Set reminder to revisit in 12 months
4. Request referrals if appropriate

---

**RED FLAGS (Disqualify or deprioritize):**
- No budget and no path to budget
- Not the decision-maker and unwilling to introduce us
- No clear pain point or urgency
- Unrealistic expectations (price, timeline, ROI)
- Poor cultural fit
- Demanding or difficult personality
- Just "gathering information" with no intent

---

**GREEN FLAGS (Prioritize):**
- Budget allocated this quarter/year
- Executive sponsor engaged
- Clear, urgent pain point
- Realistic expectations
- Fast decision-making process
- Previous relationship or referral
- Already researching solutions
- Competitive evaluation underway

**QUALIFICATION VERDICT**: [Hot / Warm / Cool / Disqualified]

**Confidence Level**: [High / Medium / Low]

**Action Plan**: [Specific next steps with dates]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def nurture_sequence(lead_type):
    """Generate lead nurturing email sequence"""
    
    prompt = f"""Create a lead nurturing sequence for: {lead_type}

**NURTURING EMAIL SEQUENCE** (Automated drip campaign)

---

**EMAIL 1: Welcome / Value Introduction** (Day 1)

**Subject Line**: [Compelling subject - 50 chars]

**Preview Text**: [15-20 words]

**Email Body**:
[Personalized greeting]

[Pain point acknowledgment]

[Brief value proposition]

[One clear CTA]

[Signature]

**CTA**: [Download resource / Schedule call / Watch demo]

---

**EMAIL 2: Educational Content** (Day 3)

**Subject Line**: [Educational hook]

**Email Body**:
[Share valuable insight, data, or case study]

[No hard sell - pure value]

[Link to blog post or guide]

**CTA**: [Learn more / Download guide]

---

**EMAIL 3: Social Proof** (Day 7)

**Subject Line**: [Customer success story]

**Email Body**:
[Mini case study]

[Specific results with numbers]

[Similar company/industry to prospect]

**CTA**: [Read full case study / See more results]

---

**EMAIL 4: Problem-Solution** (Day 14)

**Subject Line**: [Address specific pain point]

**Email Body**:
[Deep dive on one problem we solve]

[How we solve it differently]

[Expected outcomes]

**CTA**: [Calculate your ROI / Get free assessment]

---

**EMAIL 5: Objection Handling** (Day 21)

**Subject Line**: [Address common objection]

**Email Body**:
[Proactively address concern]

[Evidence/proof points]

[Risk reversal]

**CTA**: [FAQ page / Schedule Q&A call]

---

**EMAIL 6: Urgency/Scarcity** (Day 28)

**Subject Line**: [Time-sensitive offer or insight]

**Email Body**:
[Limited-time offer / Seasonal opportunity]

[Cost of inaction]

[Clear next step]

**CTA**: [Schedule call this week / Claim offer]

---

**EMAIL 7: Last Chance** (Day 35)

**Subject Line**: [Breaking up / Final outreach]

**Email Body**:
[Acknowledge no response]

[One more value offer]

[Easy opt-out or re-engage option]

**CTA**: [Should I keep in touch? Yes/No]

---

**SEQUENCE RULES:**

- Personalize: Use first name, company name, industry
- Mobile-optimized: 50-75 words per email
- One CTA: Single clear action per email
- Track engagement: Opens, clicks, replies
- A/B test: Subject lines and CTAs

**SEGMENTATION:**

- **Hot Leads**: Faster sequence (every 2-3 days)
- **Warm Leads**: Standard sequence (above)
- **Cool Leads**: Slower sequence (weekly touches)

**EXIT CRITERIA:**

- Lead replies → Move to sales conversation
- High engagement (3+ opens/clicks) → Sales outreach
- No engagement after 7 emails → Move to quarterly newsletter
- Unsubscribe → Remove from list

**RE-ENGAGEMENT:**

If lead goes cold after initial interest:
- Wait 90 days
- Send "circling back" email with new angle
- New content, new case study, new offer"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

def lead_scoring_model():
    """Generate comprehensive lead scoring framework"""
    
    prompt = """Design a lead scoring model for micro-hydro sales:

**LEAD SCORING FRAMEWORK** (0-100 points)

---

**DEMOGRAPHIC SCORING (0-30 points)**

**Company Size:**
- 500+ employees: 10 points
- 100-500 employees: 7 points
- 50-100 employees: 5 points
- <50 employees: 2 points

**Annual Revenue:**
- $100M+: 10 points
- $50-100M: 7 points
- $10-50M: 5 points
- <$10M: 2 points

**Industry Fit:**
- Manufacturing/Industrial: 10 points
- Agriculture/Food Processing: 8 points
- Commercial Real Estate: 6 points
- Hospitality/Resorts: 5 points
- Other: 2 points

---

**BEHAVIORAL SCORING (0-40 points)**

**Website Engagement:**
- Visited pricing page: 10 points
- Downloaded ROI calculator: 10 points
- Watched demo video: 8 points
- Read 3+ blog posts: 5 points
- Visited careers page: -5 points (hiring, not buying)

**Email Engagement:**
- Clicked CTA: 8 points
- Opened 3+ emails: 5 points
- Forwarded to colleague: 7 points
- Unsubscribed: -50 points

**Content Downloads:**
- Case study: 10 points
- Technical whitepaper: 8 points
- Buyers guide: 7 points
- Blog subscription: 3 points

**Event Attendance:**
- Attended webinar: 10 points
- Trade show booth visit: 8 points
- Requested meeting: 15 points

---

**QUALIFICATION SCORING (0-30 points)**

**BANT Elements:**
- Budget confirmed: 10 points
- Decision-maker identified: 10 points
- Clear need articulated: 5 points
- Timeline within 6 months: 5 points

**Engagement Quality:**
- Asked detailed questions: 8 points
- Requested proposal: 15 points
- Multiple stakeholders engaged: 7 points
- Responded quickly (<24 hrs): 5 points

---

**NEGATIVE SCORING (Deductions)**

- Student/academic inquiry: -20 points
- Competitor intelligence: -50 points
- Job seeker: -30 points
- Unrealistic expectations: -10 points
- Rude/demanding: -15 points
- Wrong geographic location: -20 points

---

**LEAD SCORE RANGES:**

**90-100 points: HOT LEAD (A)**
- **Action**: Immediate sales outreach (same day)
- **Assignment**: Senior AE
- **Cadence**: Daily follow-up until contact made
- **Goal**: Discovery call within 48 hours

**70-89 points: WARM LEAD (B)**
- **Action**: Sales outreach within 2-3 days
- **Assignment**: Standard AE
- **Cadence**: 3x/week for 2 weeks
- **Goal**: Qualification call within 1 week

**50-69 points: COOL LEAD (C)**
- **Action**: Marketing nurture sequence
- **Assignment**: Automated email + SDR check-ins
- **Cadence**: Weekly touches
- **Goal**: Warm up over 30-60 days

**Below 50: UNQUALIFIED**
- **Action**: Newsletter only
- **Assignment**: Marketing automation
- **Cadence**: Monthly content
- **Goal**: Stay top-of-mind, monitor for score changes

---

**SCORE DECAY:**

Leads lose points over time if no engagement:
- -5 points per week of inactivity
- -20 points if no engagement in 30 days
- Score resets to 0 after 90 days of inactivity

**Score Boost Events:**
- Referral from customer: +20 points
- Executive introduction: +25 points
- RFP/RFQ received: +30 points

---

**AUTOMATED WORKFLOWS BY SCORE:**

**When lead reaches 70+:**
- Auto-notify assigned sales rep
- Send personalized outreach email
- Add to high-priority calling list
- Create task in CRM: "Contact within 24 hours"

**When lead reaches 90+:**
- Urgent notification to sales manager
- Auto-schedule follow-up task
- Flag in CRM dashboard
- Send Slack alert to sales team

**When lead drops below 50:**
- Remove from active sales pipeline
- Add to long-term nurture
- Update lead status to "Nurture"

---

**TRACKING & REPORTING:**

**Weekly Metrics:**
- New leads by score tier
- Score changes (up/down trends)
- Conversion rate by score tier
- Time-to-close by score tier

**Monthly Review:**
- Are high-scoring leads converting?
- Are low-scoring leads being nurtured?
- Do we need to adjust point values?
- Are sales following up appropriately?

---

**CONTINUOUS OPTIMIZATION:**

**Quarterly Analysis:**
1. Review closed deals - what was their score progression?
2. Review lost opportunities - did we miss warning signs?
3. Adjust point values based on actual conversion data
4. A/B test different scoring thresholds

**Win/Loss Analysis:**
- Won deals: Average score at close
- Lost deals: Where did score plateau?
- No-decision: What score indicates stalled deals?

Use data to refine model every quarter."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3500
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Lead Generation Agent initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: prospects, qualify, nurture, scoring")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'prospects':
            industry = sys.argv[2] if len(sys.argv) > 2 else 'manufacturing'
            print(identify_prospects(industry))
        elif cmd == 'qualify':
            info = sys.argv[2] if len(sys.argv) > 2 else 'CFO at 500-person manufacturer, $50M revenue, wants to reduce energy costs'
            print(qualify_leads(info))
        elif cmd == 'nurture':
            lead_type = sys.argv[2] if len(sys.argv) > 2 else 'warm lead'
            print(nurture_sequence(lead_type))
        elif cmd == 'scoring':
            print(lead_scoring_model())
