"""
Relationship Manager - CRM and partner relationship tracking
Division: Partnerships
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

load_dotenv(dotenv_path='../.env')

class RelationshipManager:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ Relationship Manager initialized (Groq - FREE)")
    
    def track_interaction(self, partner_name, interaction_details):
        """Log and analyze partner interaction"""
        prompt = f"""
Track partner interaction and provide analysis.

**PARTNER:** {partner_name}
**INTERACTION:**
{interaction_details}

## INTERACTION ANALYSIS

### Interaction Summary
- **Date:** {datetime.now().strftime('%Y-%m-%d')}
- **Type:** [Email / Call / Meeting / Conference]
- **Participants:** [Names and titles]
- **Duration:** [Time]
- **Location:** [Physical / Virtual]

### Key Points Discussed
1. [Topic 1]
2. [Topic 2]
3. [Topic 3]

### Decisions Made
- [Decision 1]
- [Decision 2]

### Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Task 1] | [Person] | [Date] | Not Started |
| [Task 2] | [Person] | [Date] | Not Started |

### Partner Sentiment
**Interest Level:** Hot 🔥 / Warm 👍 / Cool 😐 / Cold ❄️

**Indicators:**
- [Positive signals observed]
- [Concerns raised]
- [Questions asked]

**Engagement Score:** [1-10]

### Relationship Status
- **Stage:** [Identified / Contacted / Engaged / Proposing / Negotiating / Partner]
- **Health:** [Strong / Good / Fair / At Risk / Lost]
- **Last Contact:** [Date]
- **Days Since Contact:** [Number]

### Next Steps
**Immediate (This Week):**
- [Action 1 with deadline]
- [Action 2 with deadline]

**Short-term (This Month):**
- [Goal 1]
- [Goal 2]

**Follow-up Date:** [Specific date and time]
**Follow-up Action:** [What we'll do]

### Notes & Insights
[Free-form notes about the interaction, partner needs, competitive intel, etc.]

Generate interaction log entry with analysis and next steps.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def pipeline_view(self):
        """Generate partner pipeline dashboard"""
        prompt = """
Generate partnership pipeline view.

## PARTNERSHIP PIPELINE

### Pipeline Overview

| Stage | # Partners | Total Value | Avg Days | Conversion Rate |
|-------|-----------|-------------|----------|-----------------|
| Identified | 0 | - | - | - |
| Contacted | 0 | - | 7 days | 40% |
| Engaged | 0 | - | 14 days | 50% |
| Proposing | 0 | - | 21 days | 50% |
| Negotiating | 0 | - | 30 days | 60% |
| Signed | 0 | $0 | - | - |

### Stage Definitions

**Identified:** Research complete, not yet contacted
**Contacted:** Initial outreach sent, awaiting response
**Engaged:** Active conversations, exploring fit
**Proposing:** Proposal submitted or in development
**Negotiating:** Term sheet discussions, finalizing
**Signed:** Partnership agreement executed

### Top 10 Active Partnerships

| Partner | Stage | Value | Next Action | Due Date | Owner |
|---------|-------|-------|-------------|----------|-------|
| [Partner 1] | [Stage] | $[X] | [Action] | [Date] | [Name] |
| [Partner 2] | [Stage] | $[Y] | [Action] | [Date] | [Name] |
[etc. for all active partners]

### At-Risk Partnerships

Partners that need attention:
- **[Partner Name]:** Last contact [X] days ago, [reason for risk]
- **[Partner Name]:** Stalled at [stage], [blocker]

**Actions:** [Recommended interventions]

### Recent Wins
- **[Partner Name]:** Signed [date], $[value]

### Recent Losses
- **[Partner Name]:** Lost to [competitor/reason]
- **Lesson Learned:** [What to do differently]

### Weekly Activity Summary

**This Week:**
- New prospects identified: [#]
- Outreach emails sent: [#]
- Calls/meetings held: [#]
- Proposals submitted: [#]
- Deals closed: [#]

**Next Week Targets:**
- Outreach: [#] new partners
- Calls: [#] discovery calls
- Proposals: [#] to submit
- Closes: [#] deals to close

### Health Metrics

**Response Rate:** [%] (target: 20%)
**Meeting Conversion:** [%] (target: 50%)
**Proposal Win Rate:** [%] (target: 40%)
**Avg Deal Size:** $[X] (target: $[Y])
**Avg Sales Cycle:** [X] days (target: [Y] days)

Generate pipeline dashboard with current status (start with empty template).
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2500
        )
        return completion.choices[0].message.content
    
    def relationship_health(self, partner_name):
        """Assess partnership relationship health"""
        prompt = f"""
Assess relationship health with: {partner_name}

## RELATIONSHIP HEALTH CHECK

### Partner Profile
- **Company:** {partner_name}
- **Type:** [Manufacturer / Distributor / Developer / etc.]
- **Partnership Since:** [Date or "In discussion"]
- **Current Stage:** [Pipeline stage]

### Health Score (1-10)

**Overall Score:** [X/10]

**Breakdown:**
- **Communication:** [1-10] - Frequency and quality of interactions
- **Responsiveness:** [1-10] - Time to respond to emails/calls
- **Engagement:** [1-10] - Level of interest and enthusiasm
- **Alignment:** [1-10] - Strategic fit and shared goals
- **Trust:** [1-10] - Openness and transparency
- **Progress:** [1-10] - Momentum toward partnership goals

### Positive Indicators ✅
- [Factor 1: e.g., "Quick email responses"]
- [Factor 2: e.g., "Multiple stakeholders engaged"]
- [Factor 3: e.g., "Proactive with ideas"]

### Warning Signs ⚠️
- [Factor 1: e.g., "Slow response times"]
- [Factor 2: e.g., "Vague commitments"]
- [Factor 3: e.g., "Price focus only"]

### Red Flags 🚩
- [Critical issues if any]

### Relationship Trajectory

**Trend:** ↗️ Improving / → Stable / ↘️ Declining

**Recent Changes:**
- [What's changed in last 30 days]
- [Impact on relationship]

### Stakeholder Map

| Name | Title | Role | Influence | Advocate/Neutral/Blocker |
|------|-------|------|-----------|--------------------------|
| [Person 1] | [Title] | [Economic buyer] | High | Advocate |
| [Person 2] | [Title] | [Technical eval] | Medium | Neutral |

### Action Plan

**To Strengthen Relationship:**
1. [Specific action with timeline]
2. [Specific action with timeline]
3. [Specific action with timeline]

**To Address Concerns:**
1. [Issue and mitigation]
2. [Issue and mitigation]

**Communication Frequency:**
- Current: [X contacts/month]
- Recommended: [Y contacts/month]
- Format: [Email / Calls / In-person]

### 30-Day Checkpoints

**Week 1:** [Milestone]
**Week 2:** [Milestone]
**Week 3:** [Milestone]
**Week 4:** [Review and adjust]

Generate relationship health assessment with actionable recommendations.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=2500
        )
        return completion.choices[0].message.content
    
    def meeting_prep(self, partner_name, meeting_type=""):
        """Generate meeting preparation brief"""
        prompt = f"""
Prepare for meeting with: {partner_name}
Meeting type: {meeting_type if meeting_type else "Discovery call"}

## MEETING PREPARATION BRIEF

### Meeting Details
- **Date/Time:** [To be scheduled]
- **Duration:** [30 / 60 minutes]
- **Format:** [Phone / Video / In-person]
- **Attendees:** [Names and roles]

### Meeting Objectives

**Our Goals:**
1. [Primary objective]
2. [Secondary objective]
3. [What we want to learn]

**Expected Outcomes:**
- [Concrete deliverable 1]
- [Concrete deliverable 2]
- [Next step agreed]

### Pre-Meeting Research

**Company Background:**
- Founded: [Year]
- Size: [Revenue/employees]
- Recent news: [Key developments]
- Strategic priorities: [What they care about]

**Key People:**
- [Name, Title]: [Background, interests, LinkedIn insights]

**Competitive Context:**
- Their competitors: [Who they compete with]
- Their challenges: [Pain points we can solve]

### Topics to Cover

**Agenda (Share in advance):**
1. Introductions (5 min)
2. ResonanceEnergy overview (5 min)
3. [Partner] current initiatives (10 min)
4. Partnership opportunity exploration (15 min)
5. Q&A and next steps (5 min)

**Key Points to Make:**
- Our φ-turbine technology (6-12% efficiency gain)
- Patent portfolio ($20M-63M value)
- Market opportunity ($2.8B market, 7% growth)
- Why partner with us (specific benefits for THEM)

**Questions to Ask:**
1. [Discovery question about their business]
2. [Question about their technology needs]
3. [Question about decision-making process]
4. [Question about timeline and budget]
5. [Question about success criteria]

### Value Proposition (Customized)

**For [Partner Name] specifically:**
- **Problem We Solve:** [Their specific pain point]
- **Our Solution:** [How our tech helps them]
- **Unique Advantage:** [Why us vs. alternatives]
- **Proof Points:** [Test results, patents, validations]

### Objection Handling

**Potential Objections:**
- "We already have turbine suppliers"
  → Response: [Differentiation points]
  
- "You're pre-revenue, too risky"
  → Response: [De-risking: patents, test data, no upfront cost model]
  
- "Efficiency gains sound too good"
  → Response: [Test data, physics basis, conservative claims]

### Materials to Bring/Share

- [ ] One-pager (partnership overview)
- [ ] Technical overview (φ-turbine specs)
- [ ] Test results summary
- [ ] Patent portfolio summary
- [ ] Financial projections
- [ ] References/case studies (if any)

### Success Metrics for This Meeting

**Meeting is successful if:**
✅ They agree to next meeting
✅ We identify specific opportunity to pursue
✅ We get introduced to decision maker
✅ Timeline and process clarified

**Red flags to watch for:**
🚩 Vague answers about authority/budget
🚩 Focus only on price, not value
🚩 No willingness to share information
🚩 No clear next steps at end

### Follow-Up Plan

**Within 24 hours:**
- Send thank you email
- Share materials discussed
- Recap action items
- Propose next meeting

**Within 1 week:**
- Complete any commitments made
- Follow up on open questions

**Template email ready to send:**
[Draft thank you/follow-up email]

Generate complete meeting prep brief with talking points and materials.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=3000
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"🤝 RELATIONSHIP MANAGER")
    print(f"{'='*70}\n")
    
    agent = RelationshipManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "log":
            if len(sys.argv) > 3:
                partner = sys.argv[2]
                interaction = " ".join(sys.argv[3:])
                print(f"LOGGING INTERACTION: {partner}\n")
                print(agent.track_interaction(partner, interaction))
            else:
                print("❌ Usage: python relationship_manager.py log '<partner>' '<interaction details>'")
        
        elif command == "pipeline":
            print("PARTNERSHIP PIPELINE\n")
            print(agent.pipeline_view())
        
        elif command == "health":
            if len(sys.argv) > 2:
                partner = " ".join(sys.argv[2:])
                print(f"RELATIONSHIP HEALTH: {partner}\n")
                print(agent.relationship_health(partner))
            else:
                print("❌ Usage: python relationship_manager.py health '<partner name>'")
        
        elif command == "prep":
            if len(sys.argv) > 2:
                partner = sys.argv[2]
                meeting = sys.argv[3] if len(sys.argv) > 3 else ""
                print(f"MEETING PREP: {partner}\n")
                print(agent.meeting_prep(partner, meeting))
            else:
                print("❌ Usage: python relationship_manager.py prep '<partner>' '[meeting type]'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  log '<partner>' '<details>'  - Log interaction")
            print("  pipeline                      - View partnership pipeline")
            print("  health '<partner>'            - Relationship health check")
            print("  prep '<partner>' '[type]'     - Meeting preparation")
    else:
        print("Available commands:")
        print("  log '<partner>' '<details>'  - Log interaction")
        print("  pipeline                      - View partnership pipeline")
        print("  health '<partner>'            - Relationship health check")
        print("  prep '<partner>' '[type]'     - Meeting preparation")
        print("\nQuick start:")
        print('  python relationship_manager.py pipeline')
        print('  python relationship_manager.py prep "Voith Hydro" "Discovery call"')
