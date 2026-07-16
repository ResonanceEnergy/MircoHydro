"""
GRANT SCOUT AGENT
Identifies government grants, private foundations, and funding opportunities for micro-hydro projects.
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

def find_grants(category='all'):
    """
    Find government and private grants for micro-hydro projects.
    
    Categories: federal, state, utility, private, international, all
    """
    
    prompt = f"""You are a grant research specialist finding funding opportunities for micro-hydro renewable energy projects.

SEARCH CATEGORY: {category}

Find and list 15-20 ACTIVE grants/funding opportunities in these categories:

FEDERAL GRANTS (if applicable):
- DOE Water Power Technologies Office
- USDA Rural Energy for America Program (REAP)
- EPA Environmental Justice Grants
- NSF Engineering Research
- DOC Economic Development Administration

STATE GRANTS (if applicable):
- State energy offices renewable energy programs
- State water resources development funds
- Agricultural energy efficiency programs
- Rural electrification programs

UTILITY PROGRAMS:
- Green tariff programs
- Distributed generation incentives
- Net metering programs
- Renewable energy credits (REC) programs

PRIVATE FOUNDATIONS:
- Environmental foundations (e.g., Kresge, Packard, MacArthur)
- Community development foundations
- Technology innovation funds
- Impact investment funds

INTERNATIONAL (if applicable):
- World Bank renewable energy programs
- UN Development Programme (UNDP)
- Asian Development Bank
- Inter-American Development Bank

For each grant, provide:
1. **Name**: Full program name
2. **Agency/Foundation**: Issuing organization
3. **Amount**: Typical grant size (range)
4. **Deadline**: Next application deadline
5. **Eligibility**: Who can apply
6. **Focus**: Specific project types funded
7. **Match Required**: Yes/No and percentage
8. **Competitiveness**: Low/Medium/High
9. **Success Tips**: 3 tips for winning applications
10. **Contact**: Website and program officer if available

FOCUS ON:
- Active programs with upcoming deadlines
- Realistic matches for micro-hydro projects (10kW-1MW range)
- Mix of small ($25k-100k) and large ($500k-5M) opportunities
- Geographic diversity (federal, state, regional)
- Combination of capital grants and R&D grants

Prioritize grants with:
- Upcoming deadlines in next 90 days
- High probability of success for new companies
- Lower match requirements
- Faster award timelines

FORMAT: Clear sections by category, ranked by deadline urgency."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def grant_calendar():
    """
    Generate 12-month grant application calendar with deadlines and prep timelines.
    """
    
    prompt = """You are a grant planning specialist creating a strategic 12-month grant application calendar for a micro-hydro renewable energy company.

Create a comprehensive grant calendar with:

MONTHLY BREAKDOWN (Next 12 months):
For each month, list:

1. **Grants Due This Month**:
   - Grant name and agency
   - Typical amount
   - Application complexity (Simple/Medium/Complex)
   - Prep time needed (2 weeks, 1 month, 3 months)
   - Key requirements

2. **Prep Work Needed Next Month**:
   - Which grants to start preparing
   - What materials to gather
   - Who to contact
   - Partnerships to establish

3. **Success Probability**:
   - High/Medium/Low for each grant
   - Why (track record, fit, competition level)

STRATEGIC CALENDAR PLANNING:

**Q1 (Jan-Mar)**:
- Focus: Quick-turnaround state grants, utility programs
- Goal: $100k-250k in applications submitted
- Key activities: Complete eligibility checks, gather baseline materials

**Q2 (Apr-Jun)**:
- Focus: Federal grants (DOE, USDA), foundation grants
- Goal: $500k-2M in applications submitted
- Key activities: Develop detailed technical plans, secure letters of support

**Q3 (Jul-Sep)**:
- Focus: International programs, R&D grants, pilot project grants
- Goal: $250k-1M in applications submitted
- Key activities: Refine past applications, follow up on Q1/Q2 submissions

**Q4 (Oct-Dec)**:
- Focus: Annual foundation grants, state fiscal year programs
- Goal: $300k-750k in applications submitted
- Key activities: Year-end reporting, plan next year's calendar

CRITICAL PREP CHECKLIST:
- [ ] 501(c)(3) status or fiscal sponsor identified
- [ ] DUNS number and SAM.gov registration
- [ ] Audited financial statements (or CPA review)
- [ ] Board of directors list and bios
- [ ] Letters of support from 5-10 stakeholders
- [ ] Detailed project budget template
- [ ] Environmental assessment documentation
- [ ] Technical specifications and engineering reports
- [ ] Community engagement documentation
- [ ] Impact measurement framework

BUNDLING STRATEGY:
- Materials you create for one grant can be reused for 5-10 others
- Group similar deadlines to batch prep work
- Prioritize grants with highest ROI (award amount / prep time)

RESOURCE ALLOCATION:
- Month 1-2: 10 hours/week grant prep (building foundation)
- Month 3-6: 20 hours/week grant prep (peak application season)
- Month 7-12: 15 hours/week grant prep (sustained momentum)

Expected first-year results:
- Applications submitted: 15-25 grants
- Total requested: $3M-8M
- Expected awards: 20-30% success rate
- Actual funding: $600k-2.4M in Year 1"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def eligibility_checker(grant_name):
    """
    Check eligibility requirements and readiness for specific grant.
    """
    
    prompt = f"""You are a grant eligibility specialist analyzing requirements for: {grant_name}

Provide comprehensive eligibility analysis:

1. **BASIC ELIGIBILITY**:
   - Organization type requirements (LLC, Corp, Non-profit, etc.)
   - Geographic restrictions
   - Project size/scale requirements
   - Technology requirements
   - Timeline requirements

2. **TECHNICAL REQUIREMENTS**:
   - Environmental permits needed
   - Engineering documentation required
   - Site control requirements
   - Grid interconnection status
   - Technology readiness level (TRL)

3. **FINANCIAL REQUIREMENTS**:
   - Match requirements (cash vs. in-kind)
   - Financial statements needed
   - Audit requirements
   - Budget restrictions
   - Allowable costs

4. **ADMINISTRATIVE REQUIREMENTS**:
   - Registration systems (SAM.gov, Grants.gov, etc.)
   - Certifications needed
   - Insurance requirements
   - Bonding requirements
   - Reporting obligations

5. **COMPETITIVE FACTORS**:
   - Evaluation criteria and weighting
   - Past award patterns
   - Typical applicant profile
   - Success rates by category

6. **READINESS CHECKLIST**:
   Rate your readiness (1-10) for:
   - [ ] Legal entity structure
   - [ ] Project development stage
   - [ ] Technical documentation
   - [ ] Financial capacity
   - [ ] Team qualifications
   - [ ] Community support
   - [ ] Environmental compliance
   - [ ] Economic justification

7. **GAP ANALYSIS**:
   What's missing? Priority order:
   - Critical (must-have to apply)
   - Important (significantly affects score)
   - Helpful (marginal benefit)

8. **PREP TIMELINE**:
   If starting today:
   - Week 1-2: [Actions]
   - Week 3-4: [Actions]
   - Week 5-6: [Actions]
   - Week 7-8: [Final prep]
   
   Realistic submission date: [X weeks from now]

9. **STRATEGIC RECOMMENDATION**:
   - Apply now / Wait 3 months / Wait 6 months / Skip this grant
   - Reasoning
   - Alternative grants to consider

Provide brutally honest assessment - better to skip a grant than waste 40 hours on low-probability application."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def success_strategy(grant_type):
    """
    Generate winning strategies for different grant types.
    
    Types: federal, state, utility, foundation, international
    """
    
    prompt = f"""You are a grant strategy consultant who has helped clients win $50M+ in grants. Create a comprehensive winning strategy for {grant_type} grants in renewable energy.

WINNING STRATEGY FRAMEWORK:

1. **WHAT REVIEWERS ACTUALLY WANT** (insider perspective):
   - Stated criteria vs. actual priorities
   - Red flags that kill applications
   - Green flags that win applications
   - Common mistakes to avoid

2. **NARRATIVE STRUCTURE** (storytelling that wins):
   - Opening hook (first paragraph that grabs attention)
   - Problem statement (make it urgent and relevant)
   - Solution approach (innovative yet credible)
   - Impact statement (quantified benefits)
   - Closing argument (why fund YOU specifically)

3. **TECHNICAL CREDIBILITY**:
   - How much detail is enough (not too much, not too little)
   - Which credentials matter most
   - How to demonstrate feasibility
   - How to address risk without looking risky

4. **BUDGET PSYCHOLOGY**:
   - What budget size wins most often
   - How to justify overhead vs. direct costs
   - Match strategies (cash vs. in-kind positioning)
   - Cost-sharing that impresses reviewers

5. **COMPETITIVE DIFFERENTIATION**:
   - How to stand out in a pool of 200 applications
   - Unique angles for micro-hydro projects
   - Partnerships that add credibility
   - Innovation claims that are believable

6. **COMMON WINNING PATTERNS**:
   - Profile of recent awardees
   - Geographic strategies (underserved areas score higher)
   - Economic development angles
   - Environmental justice positioning
   - Community engagement approaches

7. **REVIEW PANEL INSIGHTS**:
   - Who actually reviews these grants
   - What they're looking for (technical vs. programmatic reviewers)
   - How to write for non-experts
   - How to impress experts

8. **REAL EXAMPLES** (anonymized case studies):
   - Winning application structure
   - Scoring breakdown (why it won)
   - Losing application mistakes
   - Before/after rewrites

9. **TIMING TACTICS**:
   - Early vs. late submission pros/cons
   - Pre-submission consultation strategy
   - Resubmission approach (if not funded first time)

10. **RELATIONSHIP BUILDING**:
    - How to contact program officers (do's and don'ts)
    - Questions that show sophistication
    - Follow-up strategies
    - Building rapport for future cycles

GRANT TYPE SPECIFIC INSIGHTS:
Provide 10 specific tactical tips for {grant_type} grants that most applicants don't know.

SUCCESS PROBABILITY CALCULATOR:
Rate these factors (1-10) and estimate overall success probability:
- Project fit with grant goals: __/10
- Team qualifications: __/10
- Technical readiness: __/10
- Budget realism: __/10
- Innovation level: __/10
- Community support: __/10
- Writing quality: __/10
- Strategic partnerships: __/10

Formula: Overall probability = (Sum of factors / 80) × Base success rate

FINAL RECOMMENDATION:
Should you pursue this grant category? Why or why not?"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Grant Scout initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python grant_scout.py <command> [category/name/type]")
        print("\nCommands:")
        print("  find <category>     - Find grants (federal/state/utility/private/international/all)")
        print("  calendar            - Generate 12-month grant calendar")
        print("  check <grant_name>  - Check eligibility for specific grant")
        print("  strategy <type>     - Winning strategies (federal/state/utility/foundation/international)")
        print("\nExamples:")
        print("  python grant_scout.py find federal")
        print("  python grant_scout.py calendar")
        print("  python grant_scout.py check 'DOE Water Power'")
        print("  python grant_scout.py strategy foundation")
    else:
        command = sys.argv[1].lower()
        
        if command == 'find':
            category = sys.argv[2] if len(sys.argv) > 2 else 'all'
            print(f"🔍 Finding {category} grants for micro-hydro projects...\n")
            result = find_grants(category)
            print(result)
            
        elif command == 'calendar':
            print("📅 Generating 12-month grant application calendar...\n")
            result = grant_calendar()
            print(result)
            
        elif command == 'check':
            grant_name = sys.argv[2] if len(sys.argv) > 2 else 'DOE Water Power Technologies Office'
            print(f"✓ Checking eligibility for: {grant_name}...\n")
            result = eligibility_checker(grant_name)
            print(result)
            
        elif command == 'strategy':
            grant_type = sys.argv[2] if len(sys.argv) > 2 else 'federal'
            print(f"🎯 Generating winning strategy for {grant_type} grants...\n")
            result = success_strategy(grant_type)
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: find, calendar, check, strategy")
