"""
Outreach Manager - Automated partner outreach campaigns
Division: Partnerships
Uses: Groq (free tier)
Cost: $0/month
"""

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

load_dotenv(dotenv_path='../.env')

class OutreachManager:
    def __init__(self):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in .env")
            exit(1)
        self.client = Groq(api_key=api_key)
        print("✅ Outreach Manager initialized (Groq - FREE)")
    
    def generate_email(self, company_name, contact_name="", context=""):
        """Generate personalized outreach email"""
        prompt = f"""
Write personalized partnership outreach email.

**TO:** {company_name}
**CONTACT:** {contact_name if contact_name else "Business Development / Partnerships Lead"}
**CONTEXT:** {context if context else "Initial cold outreach"}

## EMAIL REQUIREMENTS

### Subject Line (3 options)
- Short, compelling, specific
- Reference their company or recent initiative
- Avoid spam triggers

### Email Body (200-250 words)
- **Opening:** Personalized hook (reference their work/news)
- **Credibility:** Brief intro to ResonanceEnergy
- **Value Prop:** What's in it for them (specific benefits)
- **Social Proof:** Patents, technology validation, market opportunity
- **Ask:** Clear, low-friction next step (15-min call)
- **Close:** Professional, enthusiastic

### Tone
- Professional but warm
- Confident but humble
- Specific but concise
- Value-focused (not feature-focused)

## RESONANCEENERGY VALUE PROPS

**Technology:**
- φ-optimized turbine design (6-12% efficiency improvement)
- Biomimetic principles (Dan Winter, Viktor Schauberger)
- Patent portfolio ($20M-63M valuation)

**Market Opportunity:**
- $2.8B micro-hydro market, 7% growth
- Distributed generation trend
- Rural electrification needs

**Partnership Benefits:**
- Access to patented technology
- Joint product development
- New revenue streams
- Market differentiation

## CALL TO ACTION OPTIONS

**Light touch:**
"Would you be open to a brief 15-minute call to explore potential synergies?"

**Value-first:**
"I'd love to share how our φ-turbine technology could enhance [their product line]. Are you available for a quick call next week?"

**Collaborative:**
"Given your work in [their specialty], I believe there's an interesting opportunity for collaboration. Can we schedule 15 minutes to discuss?"

Generate 3 subject lines and complete email body optimized for response rate.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.6,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def followup_sequence(self, stage="initial_noresponse"):
        """Generate follow-up email sequence"""
        prompt = f"""
Generate follow-up email for stage: {stage}

## FOLLOW-UP STAGES

### Stage 1: Initial No Response (Day 5-7)
After first email, no reply yet

### Stage 2: Second Follow-Up (Day 14)
Still no response

### Stage 3: Final Attempt (Day 30)
Last touchpoint before moving to "cold"

### Stage 4: Post-Call Follow-Up (Day 1)
After initial conversation

### Stage 5: Proposal Sent Follow-Up (Day 3)
After sending proposal

### Stage 6: Negotiation Follow-Up (Day 7)
During term sheet discussions

## FOLLOW-UP PRINCIPLES

✅ **Do:**
- Add new value each time
- Reference previous email briefly
- Make it easy to respond
- Provide alternative options
- Show persistence with respect

❌ **Don't:**
- Sound desperate
- Be pushy or aggressive
- Repeat same message
- Send more than 3 cold follow-ups
- Neglect to provide value

## EMAIL STRUCTURE

**Subject:** [Different from previous, adds new angle]

**Body:**
- Brief reference to previous email
- New information/value (case study, market insight, etc.)
- Updated or simplified ask
- Graceful exit option ("If timing isn't right...")

Generate follow-up email sequence for specified stage.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.6,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def campaign_builder(self, target_list):
        """Build complete outreach campaign"""
        prompt = f"""
Build outreach campaign for: {target_list}

## CAMPAIGN STRUCTURE

### Campaign Name
[Descriptive name for this cohort]

### Target Audience
- Company types
- Decision maker personas
- Geographic focus
- Industry segments

### Campaign Timeline
- **Week 1:** Initial outreach (Day 0)
- **Week 2:** First follow-up (Day 7)
- **Week 3:** Second follow-up (Day 14)
- **Week 4:** Final follow-up (Day 21)

### Email Sequence

**Email 1 (Day 0): Initial Outreach**
- Subject line options (3)
- Email body
- CTA

**Email 2 (Day 7): Value-Add Follow-Up**
- Subject line options (3)
- Email body (add new info: case study, whitepaper, etc.)
- CTA

**Email 3 (Day 14): Alternative Approach**
- Subject line options (3)
- Email body (try different angle)
- CTA

**Email 4 (Day 21): Final Attempt**
- Subject line options (3)
- Email body (graceful exit option)
- CTA

### Success Metrics

**Target Response Rates:**
- Email 1: 15-20% open, 3-5% response
- Email 2: 10-15% open, 2-3% response
- Email 3: 8-10% open, 1-2% response
- **Total Campaign:** 6-10% response rate

**Lead Scoring:**
- Hot (responded immediately, wants meeting): Priority 1
- Warm (responded but timing unclear): Priority 2
- Cold (no response after 3 emails): Archive for 6 months

### Personalization Variables

For each email, include merge fields:
- {{company_name}}
- {{contact_name}}
- {{contact_title}}
- {{recent_news}} (recent company announcement)
- {{specific_product}} (relevant product/service)

### A/B Testing

Test variations:
- Subject line tone (formal vs casual)
- Email length (short vs detailed)
- CTA type (call vs email response vs demo)

Generate complete 4-email campaign sequence with timing.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.6,
            max_tokens=3500
        )
        return completion.choices[0].message.content
    
    def response_handler(self, email_text):
        """Analyze response and suggest reply"""
        prompt = f"""
Analyze partner response and suggest reply.

**PARTNER EMAIL:**
{email_text}

## RESPONSE ANALYSIS

### Interest Level
- **Hot:** Explicitly interested, wants to meet
- **Warm:** Interested but needs more info
- **Cold:** Polite decline or no interest
- **Unclear:** Need clarification

### Key Signals
- Positive indicators (excited language, questions, availability)
- Concerns raised (timing, budget, fit, authority)
- Information requested (more details, case studies, pricing)
- Decision-making timeline

### Next Best Action
Based on their response, what should we do next?
- Schedule call
- Send more information
- Connect with different contact
- Follow up later
- Move to archive

## SUGGESTED REPLY

**Subject:** [Reply subject]

**Email Body:**
- Acknowledge their specific points
- Address any concerns
- Provide requested information
- Propose clear next step
- Make it easy to respond

**Tone:** Match their communication style

## MEETING SCHEDULING

If they're interested in a call:

**Proposed Times:**
[Offer 3 specific time slots]

**Meeting Agenda (send in advance):**
1. Brief intros (5 min)
2. ResonanceEnergy overview (5 min)
3. Partnership opportunity discussion (10 min)
4. Q&A and next steps (10 min)

**Meeting Prep:**
- Research their recent initiatives
- Prepare 3 questions for them
- Have one-pager ready to share

Generate response analysis and suggested reply.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=2000
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"📧 OUTREACH MANAGER")
    print(f"{'='*70}\n")
    
    agent = OutreachManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "email":
            if len(sys.argv) > 2:
                company = sys.argv[2]
                contact = sys.argv[3] if len(sys.argv) > 3 else ""
                print(f"GENERATING EMAIL TO: {company}\n")
                print(agent.generate_email(company, contact))
            else:
                print("❌ Usage: python outreach_manager.py email '<company>' '[contact name]'")
        
        elif command == "followup":
            stage = sys.argv[2] if len(sys.argv) > 2 else "initial_noresponse"
            print(f"FOLLOW-UP: {stage}\n")
            print(agent.followup_sequence(stage))
        
        elif command == "campaign":
            if len(sys.argv) > 2:
                target = " ".join(sys.argv[2:])
                print(f"BUILDING CAMPAIGN FOR: {target}\n")
                print(agent.campaign_builder(target))
            else:
                print("❌ Usage: python outreach_manager.py campaign '<target list>'")
        
        elif command == "respond":
            if len(sys.argv) > 2:
                email = " ".join(sys.argv[2:])
                print("ANALYZING RESPONSE\n")
                print(agent.response_handler(email))
            else:
                print("❌ Usage: python outreach_manager.py respond '<email text>'")
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  email '<company>' '[name]'   - Generate outreach email")
            print("  followup [stage]             - Follow-up email sequence")
            print("  campaign '<targets>'         - Build complete campaign")
            print("  respond '<email>'            - Analyze response, suggest reply")
    else:
        print("Available commands:")
        print("  email '<company>' '[name]'   - Generate outreach email")
        print("  followup [stage]             - Follow-up email sequence")
        print("  campaign '<targets>'         - Build complete campaign")
        print("  respond '<email>'            - Analyze response, suggest reply")
        print("\nQuick start:")
        print('  python outreach_manager.py email "Voith Hydro"')
        print('  python outreach_manager.py campaign "Micro-hydro manufacturers"')
