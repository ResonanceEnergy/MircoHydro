"""
INVESTOR TARGETING AGENT
Identifies and profiles potential investors for micro-hydro projects.
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

def find_investors(category='all', stage='seed'):
    """
    Find investors interested in renewable energy and micro-hydro.
    
    Categories: vc, angel, family_office, corporate, impact, all
    Stages: seed, series_a, series_b, growth, all
    """
    
    prompt = f"""You are an investor research specialist focusing on renewable energy financing.

SEARCH: {category} investors | Stage: {stage}

Find and profile 15-20 investors/firms matching criteria:

**VENTURE CAPITAL FIRMS**:
- Clean energy focused VCs
- Infrastructure VCs
- Climate tech VCs
- Hardware/deeptech VCs

**ANGEL INVESTORS**:
- Renewable energy angels
- Climate action angels
- Cleantech syndicate members
- Geographic focus angels

**FAMILY OFFICES**:
- Sustainability-focused family offices
- Infrastructure investment offices
- Impact-oriented family offices

**CORPORATE INVESTORS**:
- Utility company venture arms
- Energy equipment manufacturers
- Engineering firms
- Technology companies

**IMPACT INVESTORS**:
- Community development financial institutions (CDFIs)
- Impact investment funds
- ESG-focused funds
- Mission-driven capital

For each investor, provide:

1. **Name & Type**: Firm name, investor category
2. **Investment Thesis**: What they look for
3. **Sweet Spot**: Typical check size and stage
4. **Portfolio**: Relevant companies they've funded
5. **Geography**: Regional focus or restrictions
6. **Decision Makers**: Key partners/individuals
7. **Recent Activity**: Latest deals (past 12 months)
8. **Fit Score** (1-10): Match with micro-hydro projects
9. **Contact Strategy**: Best approach (warm intro, cold email, conference, pitch competition)
10. **Red Flags**: Deal-breakers or concerns to address

PRIORITIZATION CRITERIA:
- Active in renewable energy (not just talking about it)
- Track record in early-stage or infrastructure
- Geographic alignment (North America focus)
- Check size: ${stage=='seed' ? '100k-2M' : stage=='series_a' ? '2M-10M' : '10M+'}
- Decision speed (some firms take 12 months, others 6 weeks)
- Value-add beyond capital (industry connections, technical expertise)

CATEGORIZE BY LIKELIHOOD:
**Tier 1 - Highly Likely** (3-5 investors):
- Perfect fit, active in space, easy to reach

**Tier 2 - Good Potential** (5-8 investors):
- Strong fit, may need warm introduction

**Tier 3 - Worth Exploring** (5-8 investors):
- Adjacent focus, could be convinced with right story

FORMAT: Rank by Fit Score, highest first. Include contact information and specific outreach recommendations."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def investor_profile(investor_name):
    """
    Deep dive profile of specific investor with outreach strategy.
    """
    
    prompt = f"""You are an investor intelligence analyst. Create comprehensive profile for: {investor_name}

COMPLETE INVESTOR PROFILE:

1. **BASIC INFORMATION**:
   - Full legal name
   - Type (VC, angel, family office, corporate, impact fund)
   - Founded / Active since
   - Headquarters location
   - AUM (Assets Under Management)
   - Website and social media

2. **INVESTMENT THESIS**:
   - Stated focus areas
   - Actual investment patterns (may differ from stated)
   - Geographic preferences
   - Stage preferences
   - Sector preferences
   - Technology preferences

3. **DECISION MAKERS**:
   | Name | Title | Background | Focus Areas | LinkedIn | Twitter |
   |------|-------|------------|-------------|----------|---------|
   | | | | | | |
   
   For each key person:
   - Career history
   - Education
   - Board seats
   - Speaking engagements
   - Publications/thought leadership
   - Personal interests relevant to pitch

4. **PORTFOLIO ANALYSIS**:
   **Relevant Investments** (similar to micro-hydro):
   - Company name, sector, stage, amount
   - Why they invested (thesis validation)
   - Current status (success/struggle/exit)
   
   **Portfolio Patterns**:
   - Average check size: $__
   - Follow-on rate: __%
   - Typical ownership: __%
   - Co-investors (who they like to work with)
   - Time from first meeting to investment: __ months

5. **INVESTMENT CRITERIA** (what they actually fund):
   ✅ Must-Haves:
   - [List 5-7 non-negotiables based on portfolio analysis]
   
   ⚠️ Preferences:
   - [List 5-7 things that help but aren't required]
   
   ❌ Red Flags:
   - [List 3-5 things that kill deals for this investor]

6. **DEAL STRUCTURE PREFERENCES**:
   - Typical valuation range
   - Preferred instruments (SAFE, convertible, equity)
   - Board seat expectations
   - Governance requirements
   - Reporting expectations
   - Value-add provided (beyond capital)

7. **RECENT ACTIVITY** (past 12 months):
   - New investments made
   - Portfolio updates
   - Fund announcements
   - Speaking engagements
   - Published thought leadership
   - Notable exits

8. **OUTREACH INTELLIGENCE**:
   **Best Approach**:
   - Cold email success rate: __% (estimated)
   - Best path: [Warm intro / Conference / Pitch event / Cold outreach]
   - Warm intro sources: [Who can introduce you]
   - Decision timeline: __ months typical
   
   **Pitch Customization**:
   - What to emphasize (based on their thesis)
   - What to de-emphasize (doesn't resonate with them)
   - Comparisons they'll appreciate (similar to their portfolio companies)
   - Concerns to address proactively
   
   **Email Strategy**:
   - Subject line that gets opened
   - Hook for first paragraph
   - Key metrics to include
   - Call to action

9. **COMPETITIVE INTELLIGENCE**:
   - Who else might be pitching them
   - Their competitive set (similar investors)
   - Why choose them vs. alternatives
   - Negotiation leverage

10. **RELATIONSHIP BUILDING**:
    **Quick Wins** (before the pitch):
    - Follow them on Twitter, engage thoughtfully
    - Attend events they're speaking at
    - Read and reference their blog posts
    - Connect with their portfolio founders
    
    **Long-term Cultivation**:
    - Quarterly update emails (even before fundraising)
    - Invite to visit project sites
    - Seek advice (not just money initially)
    - Demonstrate coachability

11. **PROBABILITY ASSESSMENT**:
    Rate likelihood of investment (1-10): __/10
    
    Rationale:
    - Fit with thesis: __/10
    - Stage alignment: __/10
    - Geography fit: __/10
    - Technology fit: __/10
    - Team fit: __/10
    - Timing fit: __/10
    
    Overall: HIGH / MEDIUM / LOW priority
    
12. **ACTION PLAN**:
    **Week 1-2**:
    - [ ] Research complete
    - [ ] Identify warm intro path
    - [ ] Customize pitch deck
    
    **Week 3-4**:
    - [ ] Reach out for introduction
    - [ ] Send customized email
    - [ ] Follow up strategically
    
    **Week 5-8**:
    - [ ] Initial meeting
    - [ ] Provide requested materials
    - [ ] Partner meeting (if interested)
    
    **Expected Timeline**: First check in __ months

Make this profile actionable - specific enough to craft a winning approach."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def fundraising_strategy(stage, amount):
    """
    Generate comprehensive fundraising strategy and timeline.
    
    Stages: seed, series_a, series_b, growth, debt
    """
    
    prompt = f"""You are a fundraising strategist. Create comprehensive fundraising plan for {stage} round raising ${amount}.

FUNDRAISING STRATEGIC PLAN:

1. **ROUND STRUCTURE**:
   - Total raise target: ${amount}
   - Structure: [Equity / Convertible / SAFE / Debt]
   - Valuation range: $__ - $__
   - Dilution target: __%
   - Use of funds breakdown (% allocations):
     * Product development: __%
     * Sales & marketing: __%
     * Operations: __%
     * Team expansion: __%
     * Working capital: __%
   
2. **INVESTOR MIX**:
   Target cap table composition:
   - Lead investor: $__ (__%) [Name type of investor]
   - Co-investors: $__ (__%) [2-3 co-investors]
   - Strategic investors: $__ (__%) [Industry players]
   - Angels/advisors: $__ (__%) [5-10 individuals]
   
   Why this mix works:
   - [Strategic reasoning for each category]

3. **FUNDRAISING TIMELINE** (6-9 months):
   
   **Month 1-2: PREPARATION**
   - [ ] Update financial model (3-year projections)
   - [ ] Create/refresh pitch deck
   - [ ] Prepare data room
   - [ ] Identify 50-100 target investors
   - [ ] Secure 3-5 warm introductions to top targets
   - [ ] Practice pitch (20+ times)
   - [ ] Get house in order (clean cap table, legal docs)
   
   **Month 3-4: OUTREACH**
   - [ ] First wave: 20-30 investors contacted
   - [ ] Initial meetings: 10-15 scheduled
   - [ ] Refine pitch based on feedback
   - [ ] Second wave: 20-30 more investors
   - [ ] Partner meetings: 5-8 firms interested
   
   **Month 5-6: NEGOTIATION**
   - [ ] Term sheets received: 2-4 competitive offers
   - [ ] Due diligence (45-60 days)
   - [ ] Reference checks (both ways)
   - [ ] Negotiate terms
   - [ ] Select lead investor
   
   **Month 7-8: CLOSING**
   - [ ] Legal documentation
   - [ ] Final due diligence
   - [ ] Closing conditions satisfied
   - [ ] Wire transfers
   - [ ] Announcements
   
   **Month 9: POST-CLOSE**
   - [ ] Board formation
   - [ ] Investor onboarding
   - [ ] Deploy capital according to plan
   - [ ] Begin quarterly updates

4. **PITCH STRATEGY**:
   **The Hook** (first 30 seconds):
   - Problem so big it demands attention
   - Your unique insight
   - Traction that proves momentum
   
   **The Story** (15 minutes):
   - Slide 1-2: Problem (make it visceral)
   - Slide 3-4: Solution (show the innovation)
   - Slide 5-6: Market (show the opportunity)
   - Slide 7-8: Product (prove it works)
   - Slide 9-10: Traction (show momentum)
   - Slide 11-12: Business model (path to profit)
   - Slide 13-14: Competition (why you win)
   - Slide 15-16: Team (why you)
   - Slide 17-18: Financials (where you're going)
   - Slide 19-20: Ask (what you need)
   
   **The Close** (Q&A):
   - Anticipated objections and responses
   - Follow-up materials to send

5. **TRACTION MILESTONES** (to raise from strength):
   Before starting fundraise, achieve:
   - [ ] Revenue: $__ MRR or $__ in pipeline
   - [ ] Customers: __ signed or __ LOIs
   - [ ] Product: [Milestone - prototype, pilot, production]
   - [ ] Team: [Key hires completed]
   - [ ] Partnerships: [1-2 strategic partnerships signed]

6. **COMPETITIVE POSITIONING**:
   How to differentiate vs. other fundraising companies:
   - Technical moat
   - Market timing
   - Team pedigree
   - Traction metrics
   - Unit economics
   - Capital efficiency

7. **RISK MITIGATION**:
   Address these concerns proactively:
   - Technology risk: [How you've de-risked]
   - Market risk: [How you've validated demand]
   - Execution risk: [Track record, team]
   - Competitive risk: [Sustainable advantages]
   - Financial risk: [Path to profitability]

8. **VALUATION STRATEGY**:
   **Comparable Analysis**:
   - Similar companies at similar stage: [Valuations]
   - Recent transactions in sector: [Multiples]
   
   **Your Range**:
   - Floor (walk away): $__M
   - Target: $__M
   - Ceiling (take it): $__M
   
   **Justification**:
   - Revenue multiple: [If applicable]
   - User/customer multiple: [If applicable]
   - Asset value: [For infrastructure plays]
   - Discounted cash flow: [Long-term model]

9. **INVESTOR OUTREACH PLAN**:
   **Tier 1 - Dream Investors** (5-10):
   - [Specific firms/individuals]
   - Outreach method for each
   - Timeline for each
   
   **Tier 2 - Excellent Fits** (15-20):
   - [Specific firms/individuals]
   - Parallel outreach strategy
   
   **Tier 3 - Good Backups** (30-40):
   - [Categories of investors]
   - Batch outreach approach

10. **FUNDRAISING METRICS** (track weekly):
    - Investors contacted: __
    - Response rate: __%
    - Meetings scheduled: __
    - Meetings held: __
    - Follow-up meetings: __
    - Partner meetings: __
    - Term sheets: __
    - Conversion rate: __%
    
    **Velocity Targets**:
    - 10 new investor conversations per week
    - 3-5 first meetings per week
    - 1-2 partner meetings per week (once pipeline is full)

11. **BUDGET FOR FUNDRAISING**:
    - Legal (term sheet review): $5k-10k
    - Legal (closing): $25k-50k
    - Travel: $5k-10k
    - Materials (data room, etc.): $2k-5k
    - Advisors/consultants: $10k-25k
    - **Total**: $50k-100k (budget this before starting)

12. **PLAN B** (if fundraising struggles):
    - Revenue financing / venture debt
    - Strategic partnership with investment
    - Grant funding to extend runway
    - Down round considerations
    - Bridge financing from existing investors

13. **SUCCESS CRITERIA**:
    Fundraise is successful if:
    - ✅ Raised full amount (or 80%+)
    - ✅ From high-quality, value-add investors
    - ✅ At acceptable valuation and terms
    - ✅ Closed within timeline (9 months max)
    - ✅ Team not burned out from process
    - ✅ Business didn't stall during fundraise

Make this plan realistic, aggressive, and achievable. Fundraising is a full-time job - plan accordingly."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def warm_intro_request(investor_name, connector_name, relationship):
    """
    Generate email requesting warm introduction to investor.
    """
    
    prompt = f"""You are a fundraising consultant crafting a warm introduction request email.

TARGET INVESTOR: {investor_name}
CONNECTOR: {connector_name}
YOUR RELATIONSHIP: {relationship}

Write a concise, effective email requesting introduction:

**Subject Line Options** (choose one):
1. [Most direct]
2. [Most compelling]
3. [Most personal]

**Email Body**:

Hi {connector_name},

[Opening - personal connection, gratitude, brief catch-up]

[The ask - clear and specific]:
- What you're building (2 sentences max)
- Why [investor_name] specifically
- Why now
- What you're asking for (intro, not investment yet)

[Make it easy]:
- Forwardable blurb (3-4 sentences they can send directly)
- Your availability
- No pressure

[Close - gratitude and next step]

Best regards,
[Your name]

---

**FORWARDABLE BLURB** (connector sends this):
```
[Investor name],

I wanted to introduce you to [Your name], founder of [Company]. They're building [one-sentence description] and have [impressive traction metric].

[Why this is interesting - 2 sentences max connecting to investor's thesis]

Worth a conversation if you're taking meetings. I'll let [Your name] take it from here.

Best,
[Connector name]
```

**YOUR FOLLOW-UP EMAIL** (you send to investor after intro):
```
Hi [Investor name],

Thanks to [Connector] for the introduction!

[30-second pitch]:
- Problem
- Solution
- Traction
- Why now
- The ask (20-min call)

I've attached our deck. Would love to get 20 minutes on your calendar in the next couple weeks.

[Link to Calendly or propose specific times]

Thanks,
[Your name]
[Title]
[Phone]
```

TONE GUIDELINES:
- Respectful but confident
- Brief but informative
- Specific but not overwhelming
- Professional but personable

WHAT NOT TO DO:
- ❌ Don't oversell in the intro request (save it for pitch)
- ❌ Don't attach deck to intro request (wait for follow-up)
- ❌ Don't make connector do too much work
- ❌ Don't be vague about what you're building
- ❌ Don't use jargon or hype

Make this easy for connector to say yes and easy for investor to be interested."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Investor Targeting initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python investor_targeting.py <command> [parameters]")
        print("\nCommands:")
        print("  find <category> <stage>       - Find investors (vc/angel/family_office/corporate/impact/all)")
        print("  profile <investor_name>       - Deep dive investor profile")
        print("  strategy <stage> <amount>     - Fundraising strategy (seed/series_a/etc)")
        print("  intro <investor> <connector> <relationship>  - Warm intro request")
        print("\nExamples:")
        print("  python investor_targeting.py find vc seed")
        print("  python investor_targeting.py profile 'Breakthrough Energy Ventures'")
        print("  python investor_targeting.py strategy seed 2000000")
        print("  python investor_targeting.py intro 'Investor Name' 'John Smith' 'former colleague'")
    else:
        command = sys.argv[1].lower()
        
        if command == 'find':
            category = sys.argv[2] if len(sys.argv) > 2 else 'all'
            stage = sys.argv[3] if len(sys.argv) > 3 else 'seed'
            print(f"🔍 Finding {category} investors for {stage} stage...\n")
            result = find_investors(category, stage)
            print(result)
            
        elif command == 'profile':
            investor = sys.argv[2] if len(sys.argv) > 2 else 'Clean Energy Ventures'
            print(f"📊 Profiling {investor}...\n")
            result = investor_profile(investor)
            print(result)
            
        elif command == 'strategy':
            stage = sys.argv[2] if len(sys.argv) > 2 else 'seed'
            amount = int(sys.argv[3]) if len(sys.argv) > 3 else 2000000
            print(f"🎯 Creating {stage} fundraising strategy for ${amount:,}...\n")
            result = fundraising_strategy(stage, amount)
            print(result)
            
        elif command == 'intro':
            investor = sys.argv[2] if len(sys.argv) > 2 else 'Investor Name'
            connector = sys.argv[3] if len(sys.argv) > 3 else 'Connector Name'
            relationship = sys.argv[4] if len(sys.argv) > 4 else 'colleague'
            print(f"📧 Generating warm intro request to {investor}...\n")
            result = warm_intro_request(investor, connector, relationship)
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: find, profile, strategy, intro")
