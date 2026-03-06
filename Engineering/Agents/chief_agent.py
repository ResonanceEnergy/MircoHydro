"""
Chief Engineering Agent - Orchestrator
Uses: Groq (free tier) or Ollama (local)
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv()

class ChiefEngineeringAgent:
    def __init__(self, use_local=False):
        self.use_local = use_local
        self.agent_name = "Chief Engineering Agent"
        
        if use_local:
            # Use Ollama (local LLM)
            try:
                from langchain_ollama import OllamaLLM
                self.llm = OllamaLLM(model="llama3.1:8b")
                print("✅ Chief Agent initialized (Local LLM)")
            except:
                print("❌ Ollama not available, falling back to Groq")
                use_local = False
        
        if not use_local:
            # Use Groq (free tier - 14,400 req/day)
            try:
                from groq import Groq
                api_key = os.getenv('GROQ_API_KEY')
                if not api_key:
                    print("❌ GROQ_API_KEY not found in .env")
                    print("Get free key: https://console.groq.com/keys")
                    exit(1)
                self.client = Groq(api_key=api_key)
                print("✅ Chief Agent initialized (Groq - FREE)")
            except Exception as e:
                print(f"❌ Error initializing Groq: {e}")
                exit(1)
    
    def daily_briefing(self):
        """Generate daily status report"""
        prompt = f"""
You are the Chief Engineering Agent for ResonanceEnergy, a micro-hydro startup.

Today is {datetime.now().strftime('%A, %B %d, %Y')}.

Current Focus: Group A (φ-Turbine Patent) - Week 1 of 3

CONTEXT:
- Mission: File Provisional Patent #1 by Week 3 (Feb 16)
- Budget: $3k-8k total
- Current Phase: Desktop test rig build and validation
- Expected Result: Prove 6-12% efficiency improvement (21-blade φ vs 20-blade control)

PRIORITIES (from PATENT_EXECUTION_FOCUS_GROUPS.md):
1. Design 21-blade Fibonacci runner (φ-optimized)
2. Order test rig components (Amazon Prime 2-day)
3. Write test protocol (60 tests planned)
4. Set up data collection pipeline

Generate TODAY'S EXECUTION PLAN:

## 🎯 TOP 3 PRIORITIES
[What are the most critical tasks for today?]

## 👤 HUMAN TASKS (Physical Work)
[What requires hands-on work? E.g., ordering, building, testing]

## 🤖 AGENT TASKS (Autonomous)
[What can agents handle? E.g., CAD design, data analysis, documentation]

## 🚨 BLOCKERS & DECISIONS
[Any issues preventing progress? Decisions needed from human?]

## 📊 PROGRESS METRICS
[How close are we to Week 1 completion? % complete]

Format as clear bullet points. Be specific and actionable.
        """
        
        if self.use_local:
            response = self.llm.invoke(prompt)
        else:
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=2000
            )
            response = completion.choices[0].message.content
        
        return response
    
    def analyze_project_status(self, project_file):
        """Analyze project file and provide recommendations"""
        try:
            with open(project_file, 'r', encoding='utf-8') as f:
                content = f.read()[:15000]  # First 15k chars
        except FileNotFoundError:
            return f"❌ File not found: {project_file}"
        
        prompt = f"""
Analyze this patent execution plan and identify IMMEDIATE actions:

PROJECT EXCERPT:
{content}

Provide:

## 1. NEXT IMMEDIATE ACTION (Do Today)
[Single most important task to do right now]

## 2. QUICK WINS (<2 hours each)
[3-5 tasks that can be completed quickly]

## 3. BLOCKERS
[What's preventing progress? Missing resources?]

## 4. SHOPPING LIST
[Components to order NOW with estimated costs]

## 5. WEEK 1 COMPLETION CHECKLIST
[Tasks to complete by end of this week]

Be specific with part numbers, suppliers, exact tasks.
        """
        
        if self.use_local:
            response = self.llm.invoke(prompt)
        else:
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=2000
            )
            response = completion.choices[0].message.content
        
        return response
    
    def prioritize_tasks(self, task_list):
        """Prioritize a list of tasks using weighted scoring"""
        prompt = f"""
Prioritize these engineering tasks using this framework:

SCORING CRITERIA:
- Patent timeline impact: 30% (critical for Feb 16 deadline)
- Revenue enablement: 25% (does it unlock income?)
- Risk reduction: 20% (does it de-risk the project?)
- Efficiency gain: 15% (does it save time long-term?)
- Cost-effectiveness: 10% (best ROI?)

TASKS:
{task_list}

Return as:

## RANK | TASK | SCORE | REASONING
1. [Task name] - 85/100 - [Why this is #1]
2. [Task name] - 78/100 - [Why this is #2]
...

Start with highest priority first.
        """
        
        if self.use_local:
            response = self.llm.invoke(prompt)
        else:
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=2000
            )
            response = completion.choices[0].message.content
        
        return response
    
    def generate_shopping_list(self):
        """Generate Amazon shopping list for desktop test rig"""
        prompt = """
Generate a complete Amazon shopping list for a desktop turbine test rig:

REQUIREMENTS:
- 3D print turbine runners (need filament)
- Pump water through test rig (need pump, tubing)
- Measure flow, pressure, electrical output
- Desktop scale (100mm runner diameter)
- Budget: $100-300

Return as markdown table:

| Item | Spec | Example Product | Est. Price | Priority |
|------|------|----------------|-----------|----------|
| PLA Filament | 1kg, any color | OVERTURE PLA | $25 | CRITICAL |
| ... | ... | ... | ... | ... |

Include Amazon search terms and alternatives.
        """
        
        if self.use_local:
            response = self.llm.invoke(prompt)
        else:
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=2000
            )
            response = completion.choices[0].message.content
        
        return response

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"🤖 CHIEF ENGINEERING AGENT")
    print(f"{'='*70}\n")
    
    # Check for .env file
    if not os.path.exists('.env'):
        print("⚠️  No .env file found!")
        print("Create Engineering/.env with your API keys:")
        print("  GROQ_API_KEY=your_key_here")
        print("\nGet free Groq key: https://console.groq.com/keys")
        print()
    
    use_local = os.getenv('USE_LOCAL_LLM', 'false').lower() == 'true'
    
    try:
        agent = ChiefEngineeringAgent(use_local=use_local)
    except:
        print("❌ Failed to initialize agent")
        print("Check your .env file and API keys")
        exit(1)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "briefing":
            print("📋 DAILY BRIEFING\n")
            print(agent.daily_briefing())
        
        elif command == "analyze":
            if len(sys.argv) > 2:
                file_path = sys.argv[2]
                print(f"📊 ANALYZING: {file_path}\n")
                print(agent.analyze_project_status(file_path))
            else:
                print("❌ Usage: python chief_agent.py analyze <file_path>")
                print("Example: python chief_agent.py analyze ../PATENT_EXECUTION_FOCUS_GROUPS.md")
        
        elif command == "prioritize":
            tasks = """
- Design 21-blade φ-runner in CAD
- Order test rig components from Amazon
- Write desktop test protocol
- Set up data collection spreadsheet
- Research patent attorney options
- Build Alberta site database
- Configure CFD simulation
- Generate φ-optimization calculator
- Write prior art literature review
- Schedule daily automated reports
            """
            print("🎯 TASK PRIORITIZATION\n")
            print(agent.prioritize_tasks(tasks))
        
        elif command == "shop":
            print("🛒 SHOPPING LIST FOR TEST RIG\n")
            print(agent.generate_shopping_list())
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  briefing   - Daily execution plan")
            print("  analyze    - Analyze project file")
            print("  prioritize - Prioritize task list")
            print("  shop       - Generate shopping list")
    else:
        # Default: Daily briefing
        print("📋 Generating daily briefing...\n")
        print(agent.daily_briefing())
        print("\n" + "="*70)
        print("\n💡 TIP: Run 'python chief_agent.py shop' for test rig shopping list")
        print("💡 TIP: Run 'python chief_agent.py analyze ../PATENT_EXECUTION_FOCUS_GROUPS.md'")
        print()
