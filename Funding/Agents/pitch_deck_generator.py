"""
PITCH DECK GENERATOR AGENT
Creates investor pitch decks and presentation materials.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv(dotenv_path='../.env')

# Initialize Groq client
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)

def generate_deck(stage, audience='investors'):
    """
    Generate complete pitch deck outline with slide-by-slide content.
    
    Stages: seed, series_a, series_b, growth
    Audiences: investors, partners, customers, grants
    """
    
    prompt = f"""You are a pitch deck expert who has helped raise $500M+. Create a comprehensive pitch deck for {stage} fundraising to {audience}.

PITCH DECK: 15-20 SLIDES

For each slide, provide:
- Slide number and title
- Key visual concept (what to show)
- Talking points (what to say)
- Data to include (specific metrics)
- Design guidance (layout, emphasis)

---

**SLIDE 1: TITLE SLIDE**

Visual: Company logo, tagline, beautiful micro-hydro image

Content:
- Company name
- Tagline: [One sentence that captures essence]
- Presenter name and title
- Date
- Confidential notice

Talking Points:
- "Thank you for taking the time..."
- "We're [Company], and we're [doing what]..."
- Set expectations: "I'll cover X, should take Y minutes, happy to dive deep on any topic"

---

**SLIDE 2: THE HOOK** (30 seconds to grab attention)

Visual: Striking statistic or image that illustrates the problem

Content:
- One powerful statistic about the problem
- Visual representation of scale/impact
- Brief context

Talking Points:
- Lead with the most compelling fact
- Make it personal/relatable
- "This is why we exist"

Example: "97% of the world's hydropower potential remains untapped—while energy costs surge and grids strain. The solution is right in front of us."

---

**SLIDE 3: PROBLEM** (make them feel the pain)

Visual: Three panels showing different problem dimensions

Content:
- Problem dimension 1: [Economic - energy costs rising]
- Problem dimension 2: [Technical - grid reliability issues]
- Problem dimension 3: [Environmental - carbon emissions]
- "This affects [X million people / $Y market]"

Talking Points:
- Walk through each dimension
- Use specific examples
- "Existing solutions fall short because..."

---

**SLIDE 4: SOLUTION** (your unique insight)

Visual: Product image/diagram, before/after comparison

Content:
- Our solution in one sentence
- How it works (simplified)
- Key innovation (what makes it different)
- "3x better / 10x cheaper / 100x scalable"

Talking Points:
- "We've developed [technology/approach] that..."
- Explain the innovation clearly
- "This is possible because [unique insight]"

---

**SLIDE 5: PRODUCT** (prove it works)

Visual: Product photos, technical diagram, demo video screenshot

Content:
- What we've built
- Key specifications
- Unique features (3-5 bullet points)
- Technology readiness level

Talking Points:
- "Here's what it actually looks like..."
- Walk through key features
- Address obvious questions

---

**SLIDE 6: TRACTION** (show momentum)

Visual: Growth chart (up and to the right), customer logos

Content:
- Revenue: $__ (or MRR, ARR, pipeline)
- Customers: __ signed, __ in pipeline
- Growth rate: __% month-over-month
- Key milestones achieved
- Notable customers/partners

Talking Points:
- "We launched X months ago and..."
- Emphasize growth rate, not just absolute numbers
- "This proves [market demand / technical feasibility / team execution]"

---

**SLIDE 7: MARKET OPPORTUNITY** (show the size of the prize)

Visual: TAM/SAM/SOM circles, market segmentation

Content:
- TAM (Total Addressable Market): $__B
- SAM (Serviceable Addressable Market): $__B
- SOM (Serviceable Obtainable Market): $__M
- Market growth rate: __% CAGR
- Market drivers (trends supporting growth)

Talking Points:
- "We're going after a $XB market..."
- Bottom-up calculation: "X potential customers × $Y per customer = $Z"
- "Market is growing because [tailwinds]"

---

**SLIDE 8: BUSINESS MODEL** (how you make money)

Visual: Revenue model diagram, unit economics

Content:
- Revenue streams (hardware, services, recurring)
- Pricing model
- Unit economics:
  * Customer acquisition cost (CAC): $__
  * Lifetime value (LTV): $__
  * LTV:CAC ratio: __:1
  * Gross margin: __%
  * Payback period: __ months

Talking Points:
- "We make money by..."
- "Our unit economics are strong: [key metrics]"
- Path to profitability

---

**SLIDE 9: GO-TO-MARKET STRATEGY**

Visual: Sales funnel, channel strategy diagram

Content:
- Target customer profile
- Sales channels (direct, partners, online)
- Customer acquisition strategy
- Sales cycle length
- Expansion strategy

Talking Points:
- "We reach customers through..."
- "We've validated this approach with..."
- Scale plan

---

**SLIDE 10: COMPETITION** (why you win)

Visual: Competitive matrix or positioning chart

Content:
- Key competitors (3-5)
- Competitive advantages (your unique strengths)
- Barriers to entry / moats
- "We win because..."

Talking Points:
- "There are alternatives, but..."
- Be honest but confident
- "Our sustainable advantage is [moat]"

---

**SLIDE 11: TECHNOLOGY / IP** (if applicable)

Visual: Patent diagram, technology architecture

Content:
- Proprietary technology
- Patents (filed / granted)
- Trade secrets
- Technical advantages
- Defensibility

Talking Points:
- "Our technology is defensible because..."
- Don't over-explain, but show depth
- "This would take competitors X years to replicate"

---

**SLIDE 12: TRACTION DEEP DIVE** (case studies)

Visual: Before/after photos, customer testimonials

Content:
- 2-3 customer case studies
- Results achieved (quantified)
- Customer quotes
- Proof of ROI

Talking Points:
- "Let me show you a real example..."
- Walk through specific implementation
- "This is repeatable"

---

**SLIDE 13: FINANCIAL PROJECTIONS** (where you're going)

Visual: 5-year revenue/profit chart

Content:
- Historical (if applicable): Years -2, -1, 0
- Projected: Years 1, 2, 3, 4, 5
- Revenue: $__ → $__ → $__ → $__ → $__
- Gross margin: __% → __% → __%
- EBITDA: $__ → $__ → $__
- Key assumptions

Talking Points:
- "With this investment, here's where we're headed..."
- "We'll reach $XM revenue by Year 3"
- "Assumptions: [growth rate, margins, market share]"
- Be conservative but ambitious

---

**SLIDE 14: USE OF FUNDS** (what you'll do with the money)

Visual: Pie chart or waterfall chart

Content:
- Raise amount: $__M
- Allocation:
  * Product development: __% ($__)
  * Sales & marketing: __% ($__)
  * Team: __% ($__)
  * Operations: __% ($__)
  * Working capital: __% ($__)
- Key hires (list specific roles)
- Milestones this funding achieves

Talking Points:
- "This investment gets us to [next major milestone]"
- "Specifically, we'll invest in..."
- "These are the key hires that will unlock..."

---

**SLIDE 15: TEAM** (why you)

Visual: Headshots, logos of previous companies

Content:
- Founder(s): Name, title, relevant experience
- Key team members (3-5)
- Advisors / board members
- Relevant credentials (education, past exits, domain expertise)
- "We've built [X] before" or "We've worked at [Y]"

Talking Points:
- "We're uniquely positioned to execute because..."
- Brief relevant history for each person
- "We've done this before" (if applicable)

---

**SLIDE 16: TRACTION TIMELINE** (momentum visualization)

Visual: Timeline showing key milestones achieved

Content:
- Month 0: Founded
- Month 3: First prototype
- Month 6: First customer
- Month 12: $XK revenue
- Month 18: [Current state]
- Future milestones (with this funding)

Talking Points:
- "Let me show you how far we've come..."
- "We've achieved this with only $X raised"
- "With this round, we'll reach [next milestones]"

---

**SLIDE 17: THE ASK**

Visual: Simple, clean slide focused on the ask

Content:
- Raising: $__M
- Structure: [Equity / SAFE / Convertible]
- Valuation: $__M (or range)
- Timeline: Closing in [X weeks/months]
- Use of funds: [Brief summary]
- This gets us to: [Key milestone]

Talking Points:
- Direct and confident
- "We're raising $XM to [achieve goal]"
- "We're in conversations with [other investors] and plan to close by [date]"
- Create urgency but don't be desperate

---

**SLIDE 18: VISION** (where this goes long-term)

Visual: Inspiring future vision image

Content:
- 5-year vision
- 10-year vision
- Impact on world
- "We believe [future state]"

Talking Points:
- Paint the picture of the future
- "This isn't just about our company, it's about..."
- Inspirational close

---

**SLIDE 19: THANK YOU / Q&A**

Visual: Contact information, company logo

Content:
- "Thank you"
- Contact: email, phone, website
- "Questions?"

Talking Points:
- "Thank you for your time"
- "What questions do you have?"
- Be prepared for tough questions

---

**SLIDE 20: APPENDIX** (have these ready, don't present unless asked)

Additional slides to have ready:
- Detailed financial model
- Technical specifications
- Market research details
- Customer pipeline
- Competitive analysis deep dive
- Team bios (extended)
- Cap table
- Customer references

---

**DESIGN PRINCIPLES**:
1. One idea per slide (don't crowd)
2. More visuals, less text
3. Large fonts (24pt minimum)
4. Consistent color scheme
5. Professional photography
6. Clean, modern design
7. Limit bullet points (3-5 max)

**PRESENTATION TIPS**:
1. Practice 20+ times
2. Time yourself (15-20 minutes for content, save time for Q&A)
3. Tell a story, don't just present slides
4. Make eye contact, not slide contact
5. Show passion but stay professional
6. Know your numbers cold
7. Anticipate questions
8. Bring energy
9. Be confident but coachable
10. Close with a clear ask

**WHAT INVESTORS ARE REALLY EVALUATING**:
- Team (can these people execute?)
- Market (is this big enough?)
- Product (does it work?)
- Traction (is there momentum?)
- Business model (will this make money?)
- Competition (can they win?)
- Use of funds (is this the right amount?)
- Returns potential (10x+ possible?)

Make every slide earn its place. If it doesn't advance the story, cut it."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def one_pager(audience='investors'):
    """
    Generate one-page executive summary for quick review.
    """
    
    prompt = f"""You are creating a one-page executive summary for {audience}. This is what gets you in the door.

ONE-PAGER TEMPLATE (fits on single page):

**[COMPANY LOGO]**
**[COMPANY NAME]** | [Tagline]
[Website] | [Contact]

---

**THE OPPORTUNITY** (2-3 sentences)
[Describe the problem and market opportunity in compelling terms]

**OUR SOLUTION** (2-3 sentences)
[What you've built and why it's better]

**TRACTION** (3-4 key metrics)
• Revenue: $__ [or pipeline, MRR, ARR]
• Customers: __ [signed + pipeline]
• Growth: __% month-over-month
• Key partnerships: [1-2 notable names]

**MARKET** (2 sentences)
• Total addressable market: $__B
• Growing at __% annually driven by [trends]

**BUSINESS MODEL** (1-2 sentences)
• Revenue model: [How you make money]
• Unit economics: LTV $__, CAC $__, __:1 ratio

**COMPETITIVE ADVANTAGE** (3-4 bullets)
• [Key differentiator #1]
• [Key differentiator #2]
• [Key differentiator #3]
• Patents: __ filed/granted

**TEAM** (3-5 people)
• [Name], CEO - [Relevant experience]
• [Name], CTO - [Relevant experience]
• [Name], [Title] - [Relevant experience]
• Advisors: [Notable names if applicable]

**FINANCIALS** (3-year projection)
| | Year 1 | Year 2 | Year 3 |
|---------|--------|--------|--------|
| Revenue | $__M | $__M | $__M |
| Margin | __%| __% | __% |

**USE OF FUNDS** ($__M raise)
• Product development: __%
• Sales & marketing: __%
• Team expansion: __%
• Operations: __%

**THE ASK**
Raising $__M [equity/SAFE/convertible] at $__M valuation
Funds will be used to [achieve specific milestone]
Timeline: Closing [Month Year]

**CONTACT**
[Name], [Title]
[Email] | [Phone]
[LinkedIn]

---

**DESIGN NOTES**:
- Clean, professional layout
- Use company colors/branding
- Include logo and product image
- Bullet points over paragraphs
- Lots of white space
- Print-friendly (black & white legible)
- PDF format, not editable

**DISTRIBUTION STRATEGY**:
- Attach to intro emails
- Hand out at conferences
- Leave behind after meetings
- Post on company website
- Include in data room

Make this so compelling that {audience} immediately want to learn more."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def demo_day_pitch(duration=3):
    """
    Generate script for demo day / pitch competition.
    
    Duration in minutes: 3, 5, or 10
    """
    
    prompt = f"""You are a pitch competition coach. Create a {duration}-minute demo day pitch script that wins.

**{duration}-MINUTE PITCH SCRIPT**

Time allocation:
- Hook: {duration * 0.1:.0f} seconds
- Problem: {duration * 0.15:.0f} seconds  
- Solution: {duration * 0.2:.0f} seconds
- Traction: {duration * 0.2:.0f} seconds
- Market/Business Model: {duration * 0.15:.0f} seconds
- Ask: {duration * 0.1:.0f} seconds
- Close: {duration * 0.1:.0f} seconds

---

**[0:00-0:{duration * 0.1:.0f}] THE HOOK** 
"[One powerful sentence that captures attention]"

Example: "Right now, 97% of the world's hydropower potential is wasted—while we're spending billions on new power plants."

---

**[0:{duration * 0.1:.0f}-0:{duration * 0.25:.0f}] THE PROBLEM**
"[Set up the problem in visceral terms]"

Script:
- "[Specific example or statistic]"
- "[Who is affected]"
- "[Cost of inaction]"
- "[Why existing solutions fail]"

Example: "Energy costs have doubled in rural areas. 250 million people live within 5 miles of small rivers—but can't access that clean, local power because traditional hydro costs $5-10M per megawatt."

---

**[0:{duration * 0.25:.0f}-0:{duration * 0.45:.0f}] THE SOLUTION**
"[Introduce your innovation clearly and confidently]"

Script:
- "We've developed [product name]—[what it is in one sentence]"
- "Here's how it works: [2-3 sentences explaining the innovation]"
- "This makes us [3x better / 10x cheaper / 100x more scalable]"
- [Show product photo/demo if possible]

Example: "We've developed the φ-Spiral Turbine—a revolutionary design based on golden ratio mathematics that generates 3x more power from the same water flow. It installs in 2 days instead of 2 years, and costs $1,000/kW instead of $5,000/kW."

---

**[0:{duration * 0.45:.0f}-0:{duration * 0.65:.0f}] TRACTION**
"[Prove this is working and there's momentum]"

Script:
- "We launched [time ago] and here's what we've achieved:"
- "Revenue: $__ [or specific traction metric]"
- "Customers: [Number and notable names]"
- "Growing at __% month-over-month"
- "This proves [market demand / technical feasibility / team execution]"

Example: "We launched 8 months ago. We've now installed 12 systems generating $45K in monthly revenue, growing 40% month-over-month. Our customers include [notable name], and we have 30 more in our pipeline worth $2.5M."

---

**[0:{duration * 0.65:.0f}-0:{duration * 0.80:.0f}] MARKET & BUSINESS MODEL**
"[Show the opportunity and how you capture value]"

Script:
- "We're going after a $__B market"
- "Our customers pay us $__ per unit"
- "Our gross margins are __%"
- "Unit economics: [one key metric showing this is profitable]"

Example: "We're going after a $47 billion distributed energy market. Each system costs $50K and generates $15K in annual recurring revenue. Our gross margins are 65%, and customer payback is under 3 years."

---

**[0:{duration * 0.80:.0f}-0:{duration * 0.90:.0f}] THE ASK**
"[Clear, confident, specific]"

Script:
- "We're raising $__M"
- "This gets us to [specific milestone]"
- "We're backed by [existing investors/advisors if any]"
- "Timeline: [when you're closing]"

Example: "We're raising $2M to scale manufacturing and expand our sales team from 2 to 10 people. This gets us to $5M in ARR by end of next year. We're backed by Y Combinator and closing in 6 weeks."

---

**[0:{duration * 0.90:.0f}-{duration}:00] THE CLOSE**
"[Memorable, inspiring, actionable]"

Script:
- "[Vision statement - where this goes long-term]"
- "[Call to action - what you want them to do]"
- "Thank you."

Example: "We're going to power 1 million buildings with clean, local energy in the next decade. If you want to be part of this revolution, let's talk after. Thank you."

---

**DELIVERY TIPS**:

**Energy & Presence**:
- High energy from first word
- Smile (confidence and passion)
- Make eye contact with judges/audience
- Use hand gestures (but don't overdo)
- Move purposefully (don't pace nervously)
- Project your voice (even with microphone)

**Pacing**:
- Speak clearly (nervous = talk too fast)
- Pause for emphasis (after key points)
- Vary pace (slow down for important stats, speed up for energy)
- Practice with timer (know your splits)

**Slides** (if allowed):
- 1 slide per section maximum ({(duration / 0.5):.0f} slides total)
- More images, less text
- Readable from back of room (huge fonts)
- You are the presentation, not the slides

**Common Mistakes to Avoid**:
- ❌ Spending too long on problem (get to solution fast)
- ❌ Too much technical jargon
- ❌ Burying the traction (lead with strongest metrics)
- ❌ Weak ask (be specific and confident)
- ❌ Going over time (automatic disqualification at many competitions)
- ❌ Reading slides
- ❌ Low energy

**Practice Regimen**:
- Memorize script (but make it sound natural)
- Practice 50+ times before competition
- Practice in front of tough audience
- Record yourself and watch
- Time yourself every time
- Practice with distractions
- Know every second of your {duration} minutes

**Q&A Preparation** (if applicable):
Have crisp answers ready for:
- "What's your competitive advantage?"
- "How do you acquire customers?"
- "What's your biggest risk?"
- "Why you/this team?"
- "What's your exit strategy?"
- "How do you defend against [competitor]?"

**WINNING FORMULA**:
Hook + Problem + Solution + Traction + Ask = Win

The judges are evaluating:
1. Idea (20%) - Is this innovative and valuable?
2. Team (30%) - Can these people execute?
3. Traction (30%) - Is there evidence this works?
4. Presentation (20%) - Can they sell?

Make them believe. Make them excited. Make them want to write a check.

**GOAL**: When you finish, judges should think "I need to talk to them more" and audience should want to work for you or buy from you.

Good luck! 🚀"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def investor_update_template():
    """
    Generate template for monthly/quarterly investor updates.
    """
    
    prompt = """You are creating a template for investor update emails that keep investors engaged and supportive.

**INVESTOR UPDATE EMAIL TEMPLATE**

**Subject Line Options**:
1. "[Company] Update: [Key Metric] → [New Metric] (__% growth)"
2. "[Month] Update: [Exciting Milestone Achieved]"
3. "Q[X] Update: $__M ARR, [Key Win], [Key Hire]"

Choose subject line that leads with your best news.

---

**Hi [Investor Name / Team],**

Hope you're doing well! Here's what's happening at [Company].

---

**📊 KEY METRICS**

| Metric | Last Update | Now | Change |
|--------|-------------|-----|--------|
| Revenue (MRR/ARR) | $__ | $__ | +__% |
| Customers | __ | __ | +__ |
| Pipeline | $__ | $__ | +__% |
| Team size | __ | __ | +__ |
| Runway | __ months | __ months | |
| Burn rate | $__/month | $__/month | |

**Highlights**:
• [Most impressive metric or achievement]
• [Second most impressive]

---

**🎯 PROGRESS ON GOALS** (from last update)

Last update, we said we'd accomplish:
1. ✅ [Goal 1] - [What happened]
2. ✅ [Goal 2] - [What happened]
3. 🔄 [Goal 3] - [Status and why not complete]

---

**🚀 KEY WINS**

**Product**:
• [New feature launched / improvement made]
• [Customer feedback highlight]
• [Technical milestone]

**Sales/Customers**:
• Signed [Company Name] for $__/year
• Expanded with [Company Name] (now $__ contract)
• [Number] new customers in pipeline worth $__

**Team**:
• New hire: [Name, role, background]
• Promotion: [Name to new role]
• Advisor joined: [Name, credentials]

**Partnerships**:
• Partnership with [Company] to [do what]
• [Other notable relationship]

**Press/Recognition**:
• Featured in [Publication]
• Won [Award/Competition]
• Speaking at [Conference]

---

**📉 CHALLENGES** (be honest, investors appreciate transparency)

We're facing a few headwinds:

1. **[Challenge 1]**: [Brief description]
   - Impact: [What this means]
   - Plan: [How we're addressing]

2. **[Challenge 2]**: [Brief description]
   - Impact: [What this means]
   - Plan: [How we're addressing]

Note: Only include real challenges (not humblebrags). If things are going well, you can skip this section or say "Execution is on track across all fronts."

---

**🎯 GOALS FOR NEXT PERIOD**

**Next 30 days**:
1. [Specific, measurable goal]
2. [Specific, measurable goal]
3. [Specific, measurable goal]

**Next 90 days**:
1. [Bigger milestone]
2. [Bigger milestone]

These goals will move us toward [strategic objective].

---

**💡 HOW YOU CAN HELP** (give investors ways to add value)

If you have connections or expertise in these areas, would love your help:

1. **[Specific ask #1]**: [What you need - e.g., "Intro to VP of Ops at [Company]"]
2. **[Specific ask #2]**: [What you need - e.g., "Advice on [topic]"]
3. **[Specific ask #3]**: [What you need - e.g., "Candidate referrals for [role]"]

---

**📅 WHAT'S NEXT**

Upcoming milestones:
• [Date]: [Event/milestone]
• [Date]: [Event/milestone]
• [Date]: [Event/milestone]

Next update: [Date]

---

**Thanks for your continued support!**

Best regards,
[Your Name]
[Title]

P.S. [Personal note, exciting announcement, or invitation to visit/call]

---

**APPENDIX** (optional, for detailed updates)

**Financial Details**:
- Detailed P&L
- Burn analysis
- Cash position
- Fundraising status (if applicable)

**Product Roadmap**:
- Features shipping this quarter
- Engineering priorities

**Customer Pipeline**:
- Top 10 opportunities with status

---

**TEMPLATE NOTES**:

**Frequency**:
- Monthly: For active investors and during rapid growth
- Quarterly: For less active investors or stable growth phase
- Major milestones: Ad hoc updates for big news

**Tone**:
- Confident but honest
- Data-driven but not overwhelming
- Concise (aim for 3-5 minute read)
- Professional but personable

**What to Include**:
- ✅ Quantified progress (numbers, percentages)
- ✅ Specific customer names (when appropriate)
- ✅ Team updates (people matter)
- ✅ Challenges (shows maturity and trust)
- ✅ Clear asks (help investors help you)
- ✅ Forward-looking goals (show vision)

**What to Avoid**:
- ❌ Making excuses
- ❌ Being vague about problems
- ❌ Only sharing good news (lose credibility)
- ❌ Too much detail (save for quarterly board meetings)
- ❌ Inconsistent metrics (pick metrics and stick with them)
- ❌ Asking for help without being specific

**Strategic Value**:
These updates are not just reporting—they:
1. Keep investors engaged and supportive
2. Create advocates (investors forward to their networks)
3. Facilitate warm intros for next fundraise
4. Build trust through transparency
5. Source advice and connections
6. Maintain momentum and accountability

**Pro Tips**:
1. Write updates even when things are hard (especially then)
2. Celebrate wins with your investors (they're on your team)
3. Track metrics consistently month-over-month
4. Save all updates (great fundraising material later)
5. Personalize for different investor tiers (board vs. angels)
6. Use tools like Visible or Carta for distribution
7. Include visuals (charts, product screenshots)

Make your investors feel like insiders who are part of the journey."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Pitch Deck Generator initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python pitch_deck_generator.py <command> [parameters]")
        print("\nCommands:")
        print("  deck <stage> <audience>      - Generate full pitch deck (seed/series_a/series_b/growth)")
        print("  onepager <audience>          - Generate one-page summary (investors/partners/customers)")
        print("  demo <duration>              - Demo day pitch script (3/5/10 minutes)")
        print("  update                       - Investor update email template")
        print("\nExamples:")
        print("  python pitch_deck_generator.py deck seed investors")
        print("  python pitch_deck_generator.py onepager investors")
        print("  python pitch_deck_generator.py demo 3")
        print("  python pitch_deck_generator.py update")
    else:
        command = sys.argv[1].lower()
        
        if command == 'deck':
            stage = sys.argv[2] if len(sys.argv) > 2 else 'seed'
            audience = sys.argv[3] if len(sys.argv) > 3 else 'investors'
            print(f"📊 Generating {stage} pitch deck for {audience}...\n")
            result = generate_deck(stage, audience)
            print(result)
            
        elif command == 'onepager':
            audience = sys.argv[2] if len(sys.argv) > 2 else 'investors'
            print(f"📄 Generating one-pager for {audience}...\n")
            result = one_pager(audience)
            print(result)
            
        elif command == 'demo':
            duration = int(sys.argv[2]) if len(sys.argv) > 2 else 3
            print(f"🎤 Generating {duration}-minute demo day pitch...\n")
            result = demo_day_pitch(duration)
            print(result)
            
        elif command == 'update':
            print("📧 Generating investor update template...\n")
            result = investor_update_template()
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: deck, onepager, demo, update")
