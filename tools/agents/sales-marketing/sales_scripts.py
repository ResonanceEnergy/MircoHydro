"""
SALES SCRIPTS AGENT
Discovery calls, demo scripts, objection handling, closing techniques.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def discovery_call_script():
    """Generate discovery call framework"""
    
    prompt = """Create a discovery call script for micro-hydro sales:

**DISCOVERY CALL SCRIPT** (45-60 minutes)

---

**PRE-CALL PREPARATION:**

**Research Checklist:**
- [ ] Company website reviewed
- [ ] Recent news/press releases
- [ ] LinkedIn profiles of attendees
- [ ] Industry trends affecting them
- [ ] Competitor intelligence
- [ ] Similar customer case studies

**Call Objective:**
- Uncover pain points and needs
- Establish budget and timeline
- Identify decision-makers
- Build rapport and trust
- Qualify or disqualify
- Set next steps

---

**OPENING (5 minutes)**

**"Thank you for taking the time today. I'm [Name] from [Company]. Before we dive in, I want to make sure we use your time well."**

**Agenda Setting:**
"Here's what I'd like to cover in the next 45 minutes:
- Learn about your current energy situation and challenges
- Understand your goals and what success looks like
- Share some relevant examples from similar companies
- Discuss if and how we might be able to help
- Determine logical next steps

Does that work for you? Anything else you'd like to make sure we cover?"

**Permission to Ask Questions:**
"I'll probably ask a lot of questions - that's how I can best understand if we're a fit. Is that okay?"

---

**DISCOVERY QUESTIONS (25-30 minutes)**

**SECTION 1: CURRENT STATE**

"Tell me about your current energy setup..."

1. **"What's your current energy source?"** (Grid, diesel, solar, hybrid)
   - Listen for: Reliability issues, cost concerns

2. **"What does your operation consume monthly?"** (kWh, cost)
   - Listen for: Scale, budget capacity

3. **"Walk me through a typical energy bill..."**
   - Listen for: Peak demand charges, time-of-use rates

4. **"Have you had any power issues recently?"** (Outages, brownouts, surges)
   - Listen for: Pain severity, business impact

5. **"What does downtime cost your business?"** (Revenue, productivity, customer impact)
   - Listen for: Quantifiable pain

**SECTION 2: GOALS & PRIORITIES**

"Help me understand what you're trying to achieve..."

6. **"What prompted you to explore alternative energy?"** (Cost, sustainability, reliability)
   - Listen for: True motivation

7. **"If we're sitting here 12 months from now, what has to happen for you to feel this was a success?"**
   - Listen for: Success criteria, KPIs

8. **"What's most important: cost savings, sustainability goals, or energy independence?"**
   - Listen for: Priority ranking

9. **"Do you have specific sustainability commitments or targets?"** (Net-zero, carbon reduction %)
   - Listen for: External drivers, deadlines

**SECTION 3: DECISION-MAKING PROCESS**

"Let's talk about how decisions like this get made..."

10. **"Who else besides you is involved in this decision?"**
    - Listen for: Committee, CFO, Board, facilities manager

11. **"What's the typical approval process for a capital investment like this?"**
    - Listen for: Bureaucracy, timeline

12. **"Have you allocated budget for this, or would it need to be approved?"**
    - Listen for: Budget authority

13. **"What's your ideal timeline for implementation?"**
    - Listen for: Urgency, constraints

14. **"Are you evaluating other solutions or providers?"**
    - Listen for: Competitive landscape

**SECTION 4: CONSTRAINTS & CONCERNS**

"Let's discuss potential challenges..."

15. **"What concerns do you have about renewable energy projects?"**
    - Listen for: Objections to address

16. **"Have you done any renewable energy projects before? How did they go?"**
    - Listen for: Past experience (good or bad)

17. **"What would prevent you from moving forward with a project like this?"**
    - Listen for: Deal-breakers, risks

18. **"Is there anything about your site or operations that might make installation challenging?"**
    - Listen for: Technical barriers

---

**SOLUTION PREVIEW (10 minutes)**

**Only if good fit - don't pitch if not qualified**

"Based on what you've shared, let me tell you how we've helped similar companies..."

**Relevance Bridge:**
"You mentioned [specific pain point]. We worked with [similar company] who had the exact same challenge..."

**Brief Case Study:**
- Their situation (mirror prospect's)
- Solution we provided
- Specific results (numbers, timeline)

**Soft Trial Close:**
"Does something like that make sense for you?"

---

**QUALIFICATION SUMMARY (5 minutes)**

**BANT Recap (Internal Mental Checklist):**
- ✅ Budget: Do they have money?
- ✅ Authority: Is this the buyer?
- ✅ Need: Do they have pain?
- ✅ Timeline: When will they buy?

**Red Flags:**
- Vague answers
- No urgency
- Can't identify pain
- No budget discussion
- Not decision-maker and won't introduce us

**Green Flags:**
- Specific pain points
- Quantified impact
- Engaged multiple stakeholders
- Clear timeline
- Budget allocated

---

**CLOSING & NEXT STEPS (5 minutes)**

**If Qualified (Hot Lead):**
"Based on our conversation, I think we can definitely help. Here's what I'd suggest for next steps:

1. I'll send you a detailed ROI analysis based on your numbers
2. Let's schedule a site assessment for [specific dates]
3. I'll prepare a preliminary proposal for your team
4. We can present to your full committee on [date]

How does that sound?"

**If Warm Lead:**
"I think there's potential here. Let me send you:
1. Case study from [similar industry]
2. Our ROI calculator
3. Some dates for a site visit

Can we reconnect next week after you've reviewed?"

**If Not Qualified:**
"Thanks for the transparency. Based on what you've shared, I don't think we're the right fit right now because [specific reason]. 

However, I'd love to stay in touch. Can I add you to our quarterly newsletter? And if your situation changes, don't hesitate to reach out."

**Action Items:**
"Let me recap what we agreed to:
- I'm sending [X, Y, Z] by [date]
- You're going to [action] by [date]
- We'll reconnect on [specific date/time]

Did I miss anything?"

---

**POST-CALL:**

**Immediate Actions:**
- [ ] Send calendar invite for next meeting
- [ ] Email recap and promised materials
- [ ] Update CRM with notes and score
- [ ] Create tasks for follow-up items
- [ ] Flag for manager if hot lead

**CRM Notes Template:**
```
DISCOVERY CALL SUMMARY
Date: [Date]
Attendees: [Names, titles]

PAIN POINTS:
1. [Primary pain]
2. [Secondary pain]

GOALS:
- [What success looks like]

BANT SCORE: __/100
- Budget: [Y/N] - [Details]
- Authority: [Y/N] - [Who decides]
- Need: [High/Med/Low] - [Urgency]
- Timeline: [Date/Quarter]

DECISION PROCESS:
[Who's involved, steps, timeline]

COMPETITORS:
[Who else they're evaluating]

NEXT STEPS:
- I'm doing: [Actions by date]
- They're doing: [Actions by date]
- Next meeting: [Date/time]

DEAL PROBABILITY: [High/Med/Low]
NOTES: [Key insights]
```

---

**TIPS FOR SUCCESS:**

**Do:**
- Listen 70%, talk 30%
- Ask follow-up questions
- Take detailed notes
- Confirm understanding ("So what I'm hearing is...")
- Stay curious
- Build rapport
- Respect their time

**Don't:**
- Jump to solutions before understanding
- Pitch features (focus on outcomes)
- Talk over them
- Make assumptions
- Be pushy
- Ignore red flags
- Over-promise

**Magic Questions:**

- "Tell me more about that..."
- "What do you mean by...?"
- "Can you quantify that?"
- "What happens if you don't solve this?"
- "What's the cost of doing nothing?"
- "Help me understand..."

Remember: Discovery is about THEM, not you. Your job is to uncover truth, not sell."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def objection_handling():
    """Generate objection handling playbook"""
    
    prompt = """Create objection handling scripts for common sales objections:

**OBJECTION HANDLING PLAYBOOK**

---

**FRAMEWORK: Feel, Felt, Found**

"I understand how you FEEL. Other customers have FELT the same way. Here's what they FOUND..."

**Or: Acknowledge, Isolate, Resolve**

1. Acknowledge the concern
2. Isolate it ("Is this the only thing holding you back?")
3. Resolve with evidence and confidence

---

**OBJECTION #1: "It's too expensive"**

**Bad Response:** "We're actually very competitive..." (defensive)

**Good Response:**

"I understand the investment feels significant. Can I ask - too expensive compared to what?"

[Listen]

"Let me show you how [Company X] looked at it. They were paying $15k/month in energy costs. Our system was $300k, which felt expensive. But their payback was 18 months. After that, it's $180k/year in savings.

Over 25 years, that's $4.5 million. So the question isn't 'Can we afford it?' but 'Can we afford NOT to do it?'

Would it help if I ran those numbers specific to your situation?"

**Key**: Reframe from cost to investment and ROI

---

**OBJECTION #2: "We need to think about it"**

**Bad Response:** "Okay, let me know!" (passive)

**Good Response:**

"Absolutely, this is a big decision. Let me ask - what specifically do you need to think about? Is it budget, timing, technical feasibility, or something else?"

[Listen for real objection]

"Okay, so it's [real concern]. Let's address that right now. [Handle specific concern]

What else would you need to see to feel confident moving forward?"

**Key**: Uncover the real objection, don't accept smokescreens

---

**OBJECTION #3: "We're already talking to [Competitor]"**

**Bad Response:** "We're better than them..." (trash-talking)

**Good Response:**

"That's great - they're a solid company. Many of our customers evaluated them too.

Can I ask what you like about their proposal?"

[Listen]

"Those are good points. Here's how we're different: [unique value props without bashing]

At the end of the day, you'll make the right choice for your needs. I just want to make sure you have all the information to compare apples to apples.

What's most important to you in making this decision?"

**Key**: Differentiate on value, not price

---

**OBJECTION #4: "We don't have budget right now"**

**Bad Response:** "We can wait..." (gives up)

**Good Response:**

"I appreciate your honesty. Let me ask - is there no budget at all, or is it allocated elsewhere right now?"

**If no budget:**
"Okay. When does your next budget cycle start?"
[Get specific date]
"Let's do this: I'll put together a budget proposal you can submit. What information do you need to justify it?"

**If budget allocated elsewhere:**
"Got it. Help me understand the priority. What project has the budget?"
[Listen]
"How does the ROI on that compare to energy savings? I only ask because if we can show a faster payback, it might make sense to reprioritize."

**Key**: Find when budget comes, or help create business case

---

**OBJECTION #5: "The payback is too long"**

**Bad Response:** "18 months is actually fast..." (defensive)

**Good Response:**

"I hear you. What payback period would feel comfortable for you?"

[Listen - typically they'll say 12-24 months]

"Okay, so [their number]. Let me ask - what other capital investments are you making, and what's the payback on those?"

[Most business investments have 3-5 year paybacks or longer]

"Here's the thing: unlike most capital expenditures that depreciate, this one GENERATES cash flow starting day one. 

After payback, it's pure profit for 20+ more years. How many investments can say that?"

**Key**: Compare to alternative uses of capital

---

**OBJECTION #6: "We're worried about maintenance / reliability"**

**Bad Response:** "It's very reliable..." (vague reassurance)

**Good Response:**

"That's a smart concern. Let me address it with data:

1. **Reliability**: Our systems have 99.7% uptime over 10 years. Compare that to grid power at 99.9% - nearly identical, but you control it.

2. **Maintenance**: Scheduled maintenance is twice per year, about 4 hours total. Annual cost is typically $2-3k.

3. **Warranty**: 10-year comprehensive warranty. Any issues, we fix at no cost.

4. **Track Record**: [Customer X] has run for 8 years with zero downtime.

Would it help to talk to one of our customers about their experience?"

**Key**: Evidence and data, plus customer references

---

**OBJECTION #7: "We need to get other quotes"**

**Bad Response:** "We can beat any price..." (race to bottom)

**Good Response:**

"Absolutely, you should get multiple quotes. This is a major investment.

Can I give you some questions to ask other vendors? This way you're comparing apples to apples:

1. What's included in the price? (Installation, permits, interconnection?)
2. What's the warranty coverage and duration?
3. What's the expected annual maintenance cost?
4. Can they provide references from similar installations?
5. What's their average project timeline?

Also, keep in mind: cheapest isn't always best. [Example of customer who went cheap, had problems]

Whatever you decide, I want you to be successful. How about this: get your other quotes, and let's compare them together. I'll help you evaluate them objectively.

Sound fair?"

**Key**: Position as advisor, not just vendor

---

**OBJECTION #8: "This isn't a priority right now"**

**Bad Response:** "Okay, maybe later..." (gives up)

**Good Response:**

"I understand you have competing priorities. Let me ask - what IS the priority right now?"

[Listen]

"Got it. And what happens if energy costs keep rising while you're focused on [other priority]? 

I only ask because [Customer Y] thought the same thing. They waited 2 years. In that time, they spent $360k on energy they could have saved.

What if we could get this started without it becoming a distraction? We handle everything: permits, installation, interconnection. You'd be in and out of a few meetings.

Would it be worth 2 hours of your time to explore that?"

**Key**: Show cost of inaction, make it easy

---

**OBJECTION #9: "We need board/committee approval"**

**Bad Response:** "Let me know when they approve..." (loses control)

**Good Response:**

"That makes sense for an investment this size. 

Help me understand the approval process:
- Who's on the board/committee?
- When do they meet?
- What information do they need to make a decision?
- What typically causes them to say yes or no?

Here's what I'd suggest: Let me help you build the business case. I'll provide:
1. Executive summary (1-pager)
2. Detailed ROI analysis
3. Risk mitigation plan
4. Implementation timeline
5. Customer references

Would it help if I presented to the board directly? I've done it dozens of times and know the questions they'll ask."

**Key**: Help them sell internally, offer to present

---

**OBJECTION #10: "We've had bad experiences with contractors"**

**Bad Response:** "We're different..." (everyone says this)

**Good Response:**

"I'm sorry to hear that. What happened?"

[Listen empathetically]

"That's frustrating. Here's how we're different:

1. **Transparent Pricing**: Fixed price contract, no surprises
2. **Project Management**: Dedicated PM with weekly updates
3. **Timeline Commitments**: On-time completion guarantee or we pay you $X/day
4. **Quality Standards**: [Certifications, insurance, bonding]
5. **References**: Here's 10 customers - call any of them

But most importantly: I'm your single point of contact. If anything goes wrong, call me directly: [personal cell].

What would it take for you to trust us with this project?"

**Key**: Acknowledge pain, provide evidence, personal accountability

---

**OBJECTION #11: "We're not sure our site is suitable"**

**Bad Response:** "It probably is..." (assumption)

**Good Response:**

"That's a great question, and you're right to ask it up front.

Here's what we need for a viable site:
- [Water flow rate]
- [Head height]
- [Distance from building]
- [Grid interconnection access]

Good news: We offer a FREE site assessment (no obligation). Our engineer will:
1. Measure flow and head
2. Calculate generation potential
3. Provide preliminary ROI estimate
4. Identify any deal-breakers

Takes about 2 hours, and you'll know for sure if it makes sense.

I have availability next [day] or [day]. Which works better for you?"

**Key**: Remove uncertainty with risk-free next step

---

**OBJECTION #12: "Let me talk to my [spouse/partner/boss]"**

**Bad Response:** "Sure, call me after..." (loses momentum)

**Good Response:**

"Of course, that's smart. They should be part of this decision.

What concerns do you think they'll have?"

[Listen - this reveals THEIR concerns]

"Okay, so they'll want to know about [concern]. Let me give you materials to share:

Would it make sense for all of us to talk together? I can explain the details, and they can ask questions directly. That way nothing gets lost in translation.

How about we schedule a brief call with all of you? 20 minutes. Would [day/time] work?"

**Key**: Include decision-makers, don't let lead lose control

---

**FINAL TIPS:**

**Never:**
- Argue with the prospect
- Get defensive
- Trash competitors
- Make excuses
- Give up easily

**Always:**
- Acknowledge their concern
- Ask clarifying questions
- Provide evidence (data, references)
- Offer next step
- Stay confident and helpful

**Remember:** Objections mean they're interested. No objections means no engagement. Welcome objections as buying signals!"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def demo_script():
    """Generate product demo presentation script"""
    
    prompt = """Create a compelling product demo script:

**PRODUCT DEMO SCRIPT** (30-45 minutes)

---

**PRE-DEMO PREP:**

- [ ] Test all technology (screen share, video, audio)
- [ ] Customize demo with their company name/logo if possible
- [ ] Prepare 2-3 relevant case studies
- [ ] Review discovery notes (their pain points)
- [ ] Set up ROI calculator with their numbers

---

**OPENING (5 min)**

"Thanks for joining today. Before I show you the system, let me make sure we're on the same page.

**Recap Their Needs:**
From our last conversation, you mentioned:
1. [Pain point #1]
2. [Pain point #2]  
3. [Goal they want to achieve]

Is that still accurate? Anything else we should cover today?"

[Let them add or adjust]

"Perfect. Here's how I'll structure the next 30 minutes:
1. I'll show you the system and how it works (10 min)
2. Walk through a real installation similar to yours (5 min)
3. Show you the ROI specific to your numbers (10 min)
4. Answer any questions (5 min)
5. Discuss next steps

Feel free to interrupt with questions anytime."

---

**SYSTEM OVERVIEW (10 min)**

**Visual: System diagram**

"Let me show you how the system works at a high level..."

**Key Components:**
1. **Intake & Turbine** - "Water enters here, spins the turbine..."
2. **Generator** - "Converts mechanical energy to electrical..."
3. **Power Conditioning** - "Clean, grid-quality electricity..."
4. **Control System** - "Monitors and optimizes 24/7..."
5. **Grid Interconnection** - "Integrates with your existing power..."

**Not a technical lecture - focus on benefits:**
- "This means you generate power 24/7, not just when it's sunny or windy"
- "This component ensures grid-quality power - no flicker, no issues"
- "This part is completely automated - set it and forget it"

**Visual: Installation photos**

"Here's what it looks like installed. Notice how compact it is - about the size of [familiar object]."

**Pause for questions**

---

**CASE STUDY WALKTHROUGH (5 min)**

"Let me show you a real example that's similar to your situation..."

**Visual: Case study slides**

**CUSTOMER: [Similar company in their industry]**

**Their Challenge:**
- $20k/month energy bills
- Unreliable grid power causing downtime
- Sustainability goals

**Our Solution:**
- 150kW micro-hydro system
- Installed in 6 weeks
- Integrated with existing electrical

**Results:**
- 60% energy cost reduction ($12k/month savings)
- $144k/year in savings
- 22-month payback
- Zero downtime in 3 years
- Offset 800 tons CO2 annually

**Visual: Customer testimonial (video or quote)**

"Here's what their CFO said: [Testimonial]"

"Does this resonate with what you're trying to achieve?"

---

**CUSTOMIZED ROI (10 min)**

"Now let's run the numbers specific to YOUR situation..."

**Visual: ROI calculator / spreadsheet**

**Input Their Numbers:**
- Current monthly energy cost: $___
- Annual consumption: ___ kWh
- Current rate per kWh: $___ 

**Recommended System:**
- Size: ___kW
- Estimated generation: ___ kWh/year
- System cost: $___

**ROI Calculation:**
- Annual savings: $___
- Payback period: ___ months
- 10-year savings: $___
- 25-year savings: $___
- ROI: ___% (compare to S&P 500: 10%)

**Visual: Savings graph over time**

"Here's what it looks like visually. This red line is your current trajectory - spending $X per year on energy.

This green line is with our system. You cross break-even at month [X], then it's pure cash flow.

Over 25 years, you're looking at $[X] million in total savings."

**Pause - let that sink in**

"How does that compare to your expectations?"

---

**IMPLEMENTATION TIMELINE (3 min)**

"If you decided to move forward, here's what the timeline looks like:"

**Visual: Gantt chart or timeline graphic**

- **Week 1-2**: Site assessment, engineering
- **Week 3-4**: Permits and approvals
- **Week 5-8**: Equipment manufacturing
- **Week 9-10**: Installation
- **Week 11**: Testing and commissioning
- **Week 12**: Go-live and training

**Total: 12 weeks from contract to operation**

"What would be your ideal timeline?"

---

**RISK MITIGATION (2 min)**

"Let me address the common concerns I hear..."

**Concern: Reliability**
"99.7% uptime over our 10-year dataset. Plus 10-year comprehensive warranty."

**Concern: Maintenance**
"Twice per year, ~$2-3k annually. We provide or you can self-perform."

**Concern: Technical complexity**
"Fully automated. You'll check the monitoring app occasionally, but no daily management needed."

**Concern: What if it breaks?**
"Warranty covers parts and labor. Average response time: 48 hours."

---

**Q&A (5 min)**

"What questions do you have?"

**Common Questions:**

**Q: "How long will it last?"**
A: "25-30 years typical lifespan. Turbines have been running for 50+ years with maintenance."

**Q: "What about winter/freezing?"**
A: "System designed for [your climate]. Water flow prevents freezing, plus optional heating."

**Q: "Can we expand later?"**
A: "Yes, modular design. Start with [X]kW, add more capacity if needed."

**Q: "What happens if water flow decreases?"**
A: "We design for minimum flow conditions. Plus, weather variability is baked into ROI calc."

**Q: "Do we need special insurance?"**
A: "Usually no change to existing policy, but we'll help you verify with your carrier."

---

**CLOSING & NEXT STEPS (5 min)**

**Trial Close:**
"Based on what you've seen, does this solution make sense for your needs?"

**If YES:**
"Great! Here's what I suggest for next steps:

1. **Site Assessment** (this week)
   - Our engineer visits your site
   - Confirms feasibility and sizing
   - Refines ROI estimate
   - No cost, no obligation

2. **Detailed Proposal** (next week)
   - Engineering drawings
   - Exact pricing
   - Financing options if needed
   - Implementation plan

3. **Stakeholder Presentation** (following week)
   - Present to your team/board
   - Answer technical questions
   - Move to contract

Sound like a plan?"

**If HESITANT:**
"I sense some hesitation. What concerns do you still have?"

[Address concerns]

"Would it help to talk to one of our customers? I can connect you with [Similar Company] - they were in your exact position."

---

**POST-DEMO FOLLOW-UP**

**Send Within 1 Hour:**
- Recording of demo (if recorded)
- ROI analysis shown
- Case study PDF
- Customer references
- Calendar invite for next meeting

**Email Template:**
```
Subject: [Company Name] - Micro-Hydro Demo Recap & ROI

Hi [Name],

Thanks for your time today. As discussed, here's a summary:

📊 YOUR ROI:
- Investment: $[X]
- Annual Savings: $[X]
- Payback: [X] months
- 25-year total: $[X]M

📄 ATTACHED:
- ROI calculator
- [Industry] case study
- Implementation timeline
- Customer references

NEXT STEPS:
1. Site assessment - [proposed dates]
2. Detailed proposal - [target date]
3. Team presentation - [tentative date]

Let me know if you have any questions!

[Signature]
```

---

**DEMO DO'S:**

✅ Show, don't tell
✅ Use their specific numbers
✅ Tell stories (case studies)
✅ Check for understanding frequently
✅ Handle objections confidently
✅ Clear call to action
✅ Fast follow-up

**DEMO DON'TS:**

❌ Feature dump (boring!)
❌ Too technical (unless they want it)
❌ Talk too much (they should talk 30-40%)
❌ Skip their pain points
❌ Assume the sale
❌ End without clear next steps
❌ Forget to follow up

Remember: Demo should feel like a consultation, not a presentation. Make it about THEM."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

def closing_techniques():
    """Generate closing strategies and techniques"""
    
    prompt = """Create a guide to closing sales effectively:

**CLOSING TECHNIQUES PLAYBOOK**

---

**CLOSING MINDSET:**

Closing isn't a trick or manipulation. It's helping a qualified buyer make a decision that's in their best interest.

**If you've done your job:**
- Identified real pain
- Presented viable solution
- Demonstrated ROI
- Addressed concerns
- Built trust

**Then closing is simply:** "Are you ready to move forward?"

---

**TRIAL CLOSES** (Use throughout conversation)

Trial closes test the temperature without asking for the sale directly.

**Examples:**
- "Does this make sense so far?"
- "Can you see this working for your operation?"
- "How does this compare to what you expected?"
- "On a scale of 1-10, how interested are you?"
- "What would it take for you to feel confident moving forward?"

**If positive response:** Move toward close
**If hesitant:** Uncover objections

---

**ASSUMPTIVE CLOSE**

Act as if they've already decided (use cautiously).

**Examples:**
- "When would you like us to start the installation?"
- "Should we schedule the site assessment for Tuesday or Thursday?"
- "I'll get the contract drafted - do you prefer email or DocuSign?"

**Works when:** Strong buying signals, hot lead, good rapport

**Doesn't work when:** They're still in evaluation mode

---

**SUMMARY CLOSE**

Recap all the benefits and ROI, then ask.

**Script:**
"Let me summarize what we've covered:
- You're spending $20k/month on energy
- Our system will cut that by 60% - saving $12k/month
- Payback in 22 months
- After that, $144k/year in pure savings for 20+ years
- Plus, you hit your sustainability targets

We've addressed [objections they had], and you've seen it work for [similar customer].

Does it make sense to move forward?"

---

**ALTERNATIVE CLOSE**

Give two choices, both of which are "yes."

**Examples:**
- "Would you prefer the 100kW or 150kW system?"
- "Does a spring or fall installation work better for you?"
- "Should we include the extended warranty, or standard is fine?"

**Works when:** They're decided but need a nudge

---

**NOW OR NEVER CLOSE**

Create urgency (must be genuine, not manipulative).

**Examples:**
- "We have installation capacity in March, but April is filling up fast. Should I hold a spot?"
- "Utility rates are expected to increase 15% next month. If we start now, you lock in current savings."
- "Federal tax credit decreases from 30% to 26% after this year. That's $50k difference for you."

**Only use with:** Real, legitimate urgency

**Never:** Make up fake scarcity (destroys trust)

---

**PUPPY DOG CLOSE**

Let them "try before they buy" (hard with capital equipment, but creative solutions exist).

**Examples:**
- "How about we do the site assessment first - no cost, no obligation. You'll see exact numbers for your site."
- "Let's install a temporary flow meter for a month. You'll see real generation potential before committing."
- "Talk to 3 of our customers. If you're not convinced after that, no hard feelings."

**Works when:** Uncertainty or risk aversion

---

**QUESTION CLOSE**

Ask a closing question that reveals true objections.

**Examples:**
- "Is there anything preventing you from moving forward today?"
- "What would you need to see to feel comfortable signing?"
- "If we could [address concern], would you be ready to proceed?"

**Then:** Address whatever they say, and ask again

---

**TAKE-AWAY CLOSE**

Reverse psychology - suggest it might not be a fit.

**Script:**
"You know, based on our conversation, I'm not sure this is the right fit for you right now because [reason].

Maybe it makes sense to revisit this in 6 months when [condition changes]?"

**Two outcomes:**
1. They agree (good - you saved time on a bad prospect)
2. They object and convince YOU why they should buy (golden)

**Use when:** Sensing hesitation or tire-kicking

---

**DIRECT CLOSE**

Just ask for the business. Simple and honest.

**Examples:**
- "Are you ready to move forward?"
- "Should we get the paperwork started?"
- "Can I send over the contract?"

**Works when:** Strong relationship, clear need, obvious fit

**Why it works:** People appreciate directness

---

**BEN FRANKLIN CLOSE**

List pros and cons together, then show pros outweigh cons.

**Script:**
"Let's do what Benjamin Franklin did with big decisions. Draw a line down the middle.

**Pros:**
- $144k/year savings
- Hit sustainability goals
- Energy independence
- Increase property value
- 10-year warranty
- Proven technology

**Cons:**
- Upfront investment
- [Whatever concerns they have]

Looking at this objectively, do the pros outweigh the cons?"

**Works when:** Analytical buyers, need rational justification

---

**SHARP ANGLE CLOSE**

They ask for concession, you agree IF they sign.

**Examples:**

**Them:** "Can you include free maintenance for year 1?"
**You:** "If I can do that, are you ready to sign today?"

**Them:** "Can you do better on price?"
**You:** "If I can get you 5% off, will you give me a deposit today?"

**Rules:**
1. Only offer if they close now
2. Don't discount unless you get something
3. Get commitment before offering concession

---

**FEAR OF LOSS CLOSE**

Highlight what they lose by NOT moving forward.

**Script:**
"I understand you want to think about it. Let me ask - what's the cost of waiting another quarter?

That's $36k in energy costs you'll never get back. 

Plus, every month you wait, that's a month later you reach payback. Waiting 3 months means 3 extra months at the end before you're cash-flow positive.

Sometimes the cost of inaction is higher than the cost of action. Does that make sense?"

---

**REDUCE TO RIDICULOUS CLOSE**

Break large number into small, daily amount.

**Script:**
"I know $300k sounds like a big number. But let's break it down:

Over 25 years, that's $12,000 per year. Or $1,000 per month. Or $33 per day.

You'll save $400 per day in energy costs.

So you're investing $33/day to save $400/day. That's a no-brainer, right?"

---

**HIGHER AUTHORITY CLOSE**

Introduce executive/owner to show importance and urgency.

**Script:**
"Given the size of this project, I'd love to have our CEO join our next call. She only does this for our most important partnerships, but I think you two should meet.

She can answer any strategic questions and discuss our long-term vision.

Plus, she has authority to work out custom terms if needed. Sound good?"

**When:** Large deal, stuck in negotiation, need to elevate

---

**CLOSING SIGNALS TO WATCH FOR:**

**Strong Buying Signals:**
- Asking about implementation timeline
- Asking about financing/payment terms
- Introducing other decision-makers
- Asking detailed technical questions
- Asking "what happens after we sign?"
- Discussing contingencies or concerns about logistics
- Already mentally "owning" it ("When we install this...")

**When you see these:** Move to close immediately

---

**POST-CLOSE:**

**Once They Say Yes:**

1. **Confirm verbally:**
   "Excellent! Let me make sure I'm clear on next steps..."

2. **Send contract immediately:**
   "I'll send the contract in the next hour. Can you review and sign by [date]?"

3. **Stay engaged:**
   Don't disappear after they sign. Maintain momentum through implementation.

4. **Ask for referrals:**
   "By the way, who else do you know that might benefit from this?"

---

**WHEN THEY SAY NO:**

**Qualify the "No":**
- "Is this a 'no' or a 'not right now'?"
- "What would need to change for this to be a yes?"
- "Is it the solution itself, or something else?"

**If genuine no:**
- "I appreciate your honesty. Can I ask what led to that decision?"
- Learn from it
- Stay in touch (newsletter)
- Ask for referrals anyway

**If 'not now':**
- "When should we reconnect?"
- "What needs to happen first?"
- Set specific follow-up date

---

**CARDINAL RULES:**

1. **Never lie or manipulate** - Trust is everything
2. **Know when to walk away** - Bad deals hurt both parties
3. **Confidence, not arrogance** - Believe in your solution
4. **Silence is golden** - After asking for the sale, SHUT UP. First person to talk loses.
5. **ABC: Always Be Closing** - Not pushy, but always moving forward
6. **Close on value, not price** - If price is the issue, you didn't sell value
7. **Ask early and often** - Don't wait until "the right moment"

---

**PRACTICE EXERCISE:**

Role-play these scenarios with your team:

1. Prospect says "I need to think about it"
2. Prospect loves it but has no budget
3. Prospect is comparing you to cheaper competitor
4. Prospect keeps delaying decision
5. Prospect says "yes" then ghosts on contract

Remember: Every great closer started as a terrible closer. Practice, practice, practice!"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=4000
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    print("✅ Sales Scripts Agent initialized (Groq - FREE)\n")
    
    if len(sys.argv) < 2:
        print("Commands: discovery, objections, demo, closing")
    else:
        cmd = sys.argv[1].lower()
        
        if cmd == 'discovery':
            print(discovery_call_script())
        elif cmd == 'objections':
            print(objection_handling())
        elif cmd == 'demo':
            print(demo_script())
        elif cmd == 'closing':
            print(closing_techniques())
