"""
GRANT WRITER AGENT
Writes professional grant applications, narratives, and supporting materials.
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

def write_narrative(grant_name, project_description, word_limit=2000):
    """
    Write compelling grant narrative/project description.
    """
    
    prompt = f"""You are an expert grant writer who has won $50M+ in funding. Write a compelling narrative for this grant application.

GRANT: {grant_name}
PROJECT: {project_description}
WORD LIMIT: {word_limit} words

Write a professional grant narrative with these sections:

1. **EXECUTIVE SUMMARY** (10% of words):
   - Hook that captures attention in first sentence
   - Clear problem statement
   - Your solution in 2-3 sentences
   - Expected impact in quantified terms
   - Funding request and timeline

2. **NEED STATEMENT** (20% of words):
   - Urgent problem requiring solution
   - Who is affected and how severely
   - Current gaps in solutions
   - Why existing approaches fall short
   - Cost of inaction
   - Support with data and citations

3. **PROJECT DESCRIPTION** (30% of words):
   - Detailed approach and methodology
   - Innovation and technical approach
   - Project phases and milestones
   - Team qualifications and roles
   - Partnerships and collaborations
   - Risk mitigation strategies
   
4. **IMPACT & OUTCOMES** (20% of words):
   - Quantified benefits (energy, economic, environmental, social)
   - Short-term outputs (Year 1-2)
   - Long-term outcomes (Year 3-5)
   - Sustainability and scalability
   - Measurement and evaluation plan
   - Broader implications

5. **ORGANIZATIONAL CAPACITY** (10% of words):
   - Track record and relevant experience
   - Key personnel qualifications
   - Technical capabilities
   - Financial stability
   - Past grant performance

6. **BUDGET JUSTIFICATION** (10% of words):
   - Why this budget is necessary and reasonable
   - Cost-effectiveness compared to alternatives
   - Leverage and matching funds
   - Value proposition

WRITING GUIDELINES:
- Clear, direct language (avoid jargon unless necessary)
- Active voice
- Specific, quantified claims with evidence
- Confident but not arrogant tone
- Balance technical detail with accessibility
- Show passion and commitment
- Address potential concerns proactively

PERSUASION TECHNIQUES:
- Lead with strongest points
- Use strategic repetition of key themes
- Create urgency without desperation
- Demonstrate innovation while showing feasibility
- Position as strategic investment, not charity

Make this narrative IMPOSSIBLE to say no to. The reviewer should finish reading and think "we have to fund this."

TARGET WORD COUNT: {word_limit} words (±5%)"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def budget_template(project_type, grant_amount):
    """
    Generate detailed grant budget with justifications.
    
    Types: pilot_project, demonstration, commercialization, research
    """
    
    prompt = f"""You are a grant budget specialist. Create a detailed, realistic budget for a {project_type} project requesting ${grant_amount}.

Create comprehensive budget with:

1. **BUDGET SUMMARY TABLE**:
   | Category | Year 1 | Year 2 | Year 3 | Total | % of Budget |
   |----------|--------|--------|--------|-------|-------------|
   | Personnel | $__ | $__ | $__ | $__ | __% |
   | Equipment | $__ | $__ | $__ | $__ | __% |
   | Materials | $__ | $__ | $__ | $__ | __% |
   | Travel | $__ | $__ | $__ | $__ | __% |
   | Subcontracts | $__ | $__ | $__ | $__ | __% |
   | Other Direct | $__ | $__ | $__ | $__ | __% |
   | Indirect (15%) | $__ | $__ | $__ | $__ | __% |
   | **TOTAL** | **$__** | **$__** | **$__** | **${grant_amount}** | **100%** |

2. **DETAILED LINE ITEMS**:

**PERSONNEL** ($__):
- Project Director (20% FTE, $120k salary) = $__
  Justification: Overall project leadership, funder reporting
- Lead Engineer (100% FTE, $95k salary) = $__
  Justification: Technical design, implementation oversight
- Technician (50% FTE, $55k salary) = $__
  Justification: Installation, testing, maintenance
- Grant Administrator (10% FTE, $70k salary) = $__
  Justification: Financial management, compliance
- Fringe Benefits (30% of salaries) = $__

**EQUIPMENT** ($__):
- Turbine system (specify model/capacity) = $__
- Generator and controls = $__
- Penstock and intake structures = $__
- Electrical interconnection equipment = $__
- Monitoring and data acquisition = $__
- Tools and installation equipment = $__

**MATERIALS & SUPPLIES** ($__):
- Civil construction materials = $__
- Electrical wiring and components = $__
- Piping and fittings = $__
- Environmental monitoring equipment = $__
- Office supplies and software = $__

**TRAVEL** ($__):
- Site visits (12 trips × $500) = $__
- Conference presentation (2 trips × $1,500) = $__
- Partner meetings (4 trips × $800) = $__

**SUBCONTRACTS** ($__):
- Environmental permitting consultant = $__
- Structural engineering analysis = $__
- Legal and regulatory compliance = $__
- Community engagement specialist = $__

**OTHER DIRECT COSTS** ($__):
- Permits and regulatory fees = $__
- Insurance = $__
- Testing and commissioning = $__
- Publication and outreach = $__

**INDIRECT COSTS** (15% of MTDC) = $__
Negotiated rate with [organization]

3. **BUDGET NARRATIVE** (2-3 sentences per major line item):
Explain necessity, basis for estimate, and reasonableness

4. **COST SHARING** (if required):
   | Source | Cash | In-Kind | Total |
   |--------|------|---------|-------|
   | Organization | $__ | $__ | $__ |
   | Partners | $__ | $__ | $__ |
   | Other | $__ | $__ | $__ |
   | **TOTAL MATCH** | **$__** | **$__** | **$__** |

5. **COST-EFFECTIVENESS ANALYSIS**:
   - Cost per kW installed: $__
   - Cost per kWh over 25-year life: $__
   - Comparison to alternatives (grid, solar, diesel)
   - Return on grant investment

6. **BUDGET REASONABLENESS**:
   - Comparison to industry standards
   - Competitive bids obtained
   - Market research conducted
   - Value engineering applied

7. **FINANCIAL MANAGEMENT**:
   - Accounting system description
   - Internal controls
   - Audit procedures
   - Reporting frequency

Make this budget defendable, realistic, and aligned with programmatic goals. Every dollar should have clear justification."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def support_letter(recipient_name, organization, relationship):
    """
    Generate letter of support from partner organizations.
    """
    
    prompt = f"""You are a grant writer crafting a strong letter of support for a micro-hydro project.

LETTER FROM: {organization}
TO: {recipient_name}
RELATIONSHIP: {relationship}

Write a compelling 1-2 page letter of support that includes:

1. **OPENING** (1-2 paragraphs):
   - Who we are and our credentials
   - How we know the applicant organization
   - Enthusiastic statement of support
   - Our stake in project success

2. **PROJECT VALUE** (2-3 paragraphs):
   - Why this project is important
   - Alignment with our mission/goals
   - Gap this project fills
   - Unique qualifications of applicant team

3. **OUR COMMITMENT** (2-3 paragraphs):
   - Specific support we are providing:
     * Financial contribution ($__ or __% in-kind)
     * Technical expertise (__ hours of engineering support)
     * Access to resources (equipment, facilities, data)
     * Staff time (__ FTE during project)
     * Letters of introduction to key stakeholders
     * Promotional support through our channels
   - Timeline of our involvement
   - Why we're committing these resources

4. **IMPACT STATEMENT** (1-2 paragraphs):
   - Expected benefits to our organization/community
   - Broader significance
   - Alignment with regional/national priorities

5. **CONFIDENCE & TRACK RECORD** (1 paragraph):
   - Past successful collaborations
   - Why we believe this team will deliver
   - Risk mitigation

6. **CLOSING** (1 paragraph):
   - Strong endorsement
   - Urge funding
   - Contact information for follow-up

TONE: Professional, enthusiastic, credible
FORMAT: Official letterhead format
SIGNATURE LEVEL: Executive Director or higher

Make this letter add real value - not just a generic endorsement. Show genuine partnership and shared investment in success.

[Organization Letterhead]
[Date]

[Recipient Name]
[Grant Program]
[Address]

Dear [Recipient Name]:

[Write full letter here...]

Sincerely,

[Signature]
[Name, Title]
[Organization]
[Contact Information]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=3000
    )
    
    return response.choices[0].message.content

def evaluation_plan(project_description, outcomes):
    """
    Create evaluation and measurement plan for grant outcomes.
    """
    
    prompt = f"""You are a program evaluation specialist. Create a rigorous evaluation plan for this grant project.

PROJECT: {project_description}
EXPECTED OUTCOMES: {outcomes}

Develop comprehensive evaluation framework:

1. **LOGIC MODEL**:
   ```
   INPUTS → ACTIVITIES → OUTPUTS → SHORT-TERM OUTCOMES → LONG-TERM OUTCOMES → IMPACT
   
   Inputs:
   - [List resources: funding, staff, equipment, partnerships]
   
   Activities:
   - [What we will do]
   
   Outputs:
   - [What we will produce - tangible deliverables]
   
   Short-term Outcomes (Year 1-2):
   - [Changes in knowledge, skills, behavior]
   
   Long-term Outcomes (Year 3-5):
   - [Changes in conditions, status]
   
   Impact (Year 5+):
   - [Fundamental changes in systems, communities]
   ```

2. **EVALUATION QUESTIONS**:
   List 5-8 key questions the evaluation will answer:
   - Did we implement as planned? (Process evaluation)
   - Did we achieve intended outcomes? (Outcome evaluation)
   - Was it cost-effective? (Efficiency evaluation)
   - Are results sustainable? (Sustainability evaluation)

3. **PERFORMANCE METRICS** (SMART goals):
   
   **Technical Performance**:
   | Metric | Baseline | Year 1 Target | Year 2 Target | Year 3 Target | Measurement Method |
   |--------|----------|---------------|---------------|---------------|-------------------|
   | Energy production (kWh) | 0 | __ | __ | __ | Smart meter data |
   | System efficiency (%) | N/A | __% | __% | __% | Performance testing |
   | Capacity factor (%) | N/A | __% | __% | __% | Annual analysis |
   | Uptime (%) | N/A | __% | __% | __% | SCADA monitoring |
   
   **Economic Impact**:
   | Metric | Baseline | Year 1 Target | Year 2 Target | Year 3 Target | Measurement Method |
   |--------|----------|---------------|---------------|---------------|-------------------|
   | Energy cost savings ($) | $0 | $__ | $__ | $__ | Utility bill analysis |
   | Jobs created (#) | 0 | __ | __ | __ | Employment records |
   | Local procurement ($) | $0 | $__ | $__ | $__ | Contract tracking |
   | Revenue generated ($) | $0 | $__ | $__ | $__ | Financial statements |
   
   **Environmental Impact**:
   | Metric | Baseline | Year 1 Target | Year 2 Target | Year 3 Target | Measurement Method |
   |--------|----------|---------------|---------------|---------------|-------------------|
   | CO2 avoided (tons) | 0 | __ | __ | __ | EPA calculator |
   | Water quality (index) | __ | __ | __ | __ | Lab testing |
   | Habitat restored (acres) | 0 | __ | __ | __ | Site assessment |
   
   **Social Impact**:
   | Metric | Baseline | Year 1 Target | Year 2 Target | Year 3 Target | Measurement Method |
   |--------|----------|---------------|---------------|---------------|-------------------|
   | Community awareness (%) | __% | __% | __% | __% | Survey (n=100) |
   | Students educated (#) | 0 | __ | __ | __ | Program records |
   | Stakeholder satisfaction | N/A | __/10 | __/10 | __/10 | Annual survey |

4. **DATA COLLECTION PLAN**:
   For each metric:
   - Data source
   - Collection frequency
   - Responsible party
   - Data storage location
   - Quality assurance procedures

5. **ANALYSIS PLAN**:
   - Quantitative methods (statistical analysis)
   - Qualitative methods (interviews, case studies)
   - Comparative analysis (before/after, with/without)
   - Cost-benefit analysis

6. **REPORTING TIMELINE**:
   - Monthly: Internal dashboard review
   - Quarterly: Funder progress reports
   - Annually: Comprehensive evaluation report
   - Final: Summative evaluation and lessons learned

7. **EVALUATION TEAM**:
   - Internal evaluator: [Role, % FTE]
   - External evaluator: [Organization, scope]
   - Data analyst: [Role, % FTE]

8. **BUDGET FOR EVALUATION**:
   Allocate 10-15% of total project budget:
   - Personnel: $__
   - Data collection tools: $__
   - External evaluation: $__
   - Analysis software: $__
   - Reporting and dissemination: $__
   Total: $__

9. **DISSEMINATION PLAN**:
   - Technical reports to funder
   - Conference presentations
   - Peer-reviewed publications
   - Community presentations
   - Website and social media
   - Practitioner briefs

10. **CONTINUOUS IMPROVEMENT**:
    - How evaluation data informs adaptive management
    - Decision points for course correction
    - Learning agenda

This evaluation plan demonstrates rigor, accountability, and commitment to learning."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Grant Writer initialized successfully (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Usage: python grant_writer.py <command> [parameters]")
        print("\nCommands:")
        print("  narrative <grant> <description>  - Write grant narrative")
        print("  budget <type> <amount>           - Create detailed budget")
        print("  letter <recipient> <org> <rel>   - Generate support letter")
        print("  evaluation <project> <outcomes>  - Create evaluation plan")
        print("\nExamples:")
        print("  python grant_writer.py narrative 'DOE Grant' 'φ-spiral turbine pilot'")
        print("  python grant_writer.py budget pilot_project 500000")
        print("  python grant_writer.py letter 'DOE' 'Local Utility' 'Grid partner'")
        print("  python grant_writer.py evaluation '50kW system' 'Energy independence'")
    else:
        command = sys.argv[1].lower()
        
        if command == 'narrative':
            grant = sys.argv[2] if len(sys.argv) > 2 else 'Federal Grant'
            description = sys.argv[3] if len(sys.argv) > 3 else 'Micro-hydro demonstration project'
            print(f"✍️ Writing narrative for {grant}...\n")
            result = write_narrative(grant, description)
            print(result)
            
        elif command == 'budget':
            project_type = sys.argv[2] if len(sys.argv) > 2 else 'pilot_project'
            amount = int(sys.argv[3]) if len(sys.argv) > 3 else 500000
            print(f"💰 Creating budget for {project_type} (${amount:,})...\n")
            result = budget_template(project_type, amount)
            print(result)
            
        elif command == 'letter':
            recipient = sys.argv[2] if len(sys.argv) > 2 else 'Grant Program'
            org = sys.argv[3] if len(sys.argv) > 3 else 'Partner Organization'
            rel = sys.argv[4] if len(sys.argv) > 4 else 'Strategic partner'
            print(f"📧 Generating support letter from {org}...\n")
            result = support_letter(recipient, org, rel)
            print(result)
            
        elif command == 'evaluation':
            project = sys.argv[2] if len(sys.argv) > 2 else 'Micro-hydro project'
            outcomes = sys.argv[3] if len(sys.argv) > 3 else 'Clean energy production'
            print(f"📊 Creating evaluation plan...\n")
            result = evaluation_plan(project, outcomes)
            print(result)
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Valid commands: narrative, budget, letter, evaluation")
