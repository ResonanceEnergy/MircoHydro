"""
Automation Agent - Workflow automation and CI/CD
Uses: Groq (free tier) or Ollama (local)
Cost: $0/month (free tier)
"""

import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class AutomationAgent:
    def __init__(self, use_local=False):
        self.use_local = use_local
        self.agent_name = "Automation Agent"
        
        if not use_local:
            try:
                from groq import Groq
                api_key = os.getenv('GROQ_API_KEY')
                if not api_key:
                    print("❌ GROQ_API_KEY not found in .env")
                    exit(1)
                self.client = Groq(api_key=api_key)
                print("✅ Automation Agent initialized (Groq - FREE)")
            except Exception as e:
                print(f"❌ Error: {e}")
                exit(1)
    
    def generate_daily_automation(self):
        """Create daily automation script"""
        prompt = """
Generate a PowerShell script for daily automation:

TASKS:
1. Run chief_agent.py briefing, save to Reports/daily_briefing_YYYY-MM-DD.md
2. Check for new test data in Data/, analyze if found
3. Update project status dashboard
4. Commit changes to git with automated message
5. Send summary email (if configured)

Include:
- Error handling
- Logging
- Email notification setup
- Scheduled task configuration

Return complete PowerShell script.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=3000
        )
        return completion.choices[0].message.content
    
    def create_test_automation(self, test_type):
        """Generate automated test pipeline"""
        prompt = f"""
Create automation script for: {test_type}

Include:
1. Data collection automation
2. Real-time analysis
3. Alert conditions (outliers, failures)
4. Automatic backup
5. Report generation

Return Python script with error handling.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=2500
        )
        return completion.choices[0].message.content
    
    def generate_ci_pipeline(self):
        """Create CI/CD pipeline configuration"""
        prompt = """
Generate GitHub Actions workflow for:
1. Automated testing on commit
2. CAD file validation
3. Documentation build
4. Release packaging

Return .github/workflows/main.yml
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=2000
        )
        return completion.choices[0].message.content
    
    def create_monitoring_dashboard(self):
        """Generate real-time monitoring dashboard"""
        prompt = """
Create Streamlit dashboard app for:
- Patent timeline tracking
- Test progress monitoring
- Budget tracking
- Task completion status
- Alert notifications

Return complete Python Streamlit app code.
        """
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=3000
        )
        return completion.choices[0].message.content

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print(f"\n{'='*70}")
    print(f"⚙️ AUTOMATION AGENT")
    print(f"{'='*70}\n")
    
    agent = AutomationAgent()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "daily":
            print("# Daily Automation Script\n")
            print(agent.generate_daily_automation())
        
        elif command == "test-pipeline":
            test_type = sys.argv[2] if len(sys.argv) > 2 else "turbine efficiency testing"
            print(f"# Test Automation: {test_type}\n")
            print(agent.create_test_automation(test_type))
        
        elif command == "ci":
            print("# CI/CD Pipeline\n")
            print(agent.generate_ci_pipeline())
        
        elif command == "dashboard":
            print("# Monitoring Dashboard\n")
            print(agent.create_monitoring_dashboard())
        
        else:
            print(f"❌ Unknown command: {command}")
            print("\nCommands: daily | test-pipeline | ci | dashboard")
    else:
        print("Commands:")
        print("  daily          - Daily automation script")
        print("  test-pipeline  - Test automation")
        print("  ci             - CI/CD workflow")
        print("  dashboard      - Monitoring dashboard")
