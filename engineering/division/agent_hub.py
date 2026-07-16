"""
Agent Hub - Launch and coordinate all engineering agents
Free tier operation using Groq API
"""

import os
import sys
from pathlib import Path

# Add Agents directory to path
sys.path.append(str(Path(__file__).parent / 'Agents'))

def show_menu():
    print(f"\n{'='*70}")
    print(f"🤖 ENGINEERING AGENT HUB")
    print(f"{'='*70}\n")
    print("ALL AGENTS: $0/month (Groq Free Tier)")
    print()
    print("1.  Chief Agent       - Daily briefing & orchestration")
    print("2.  Tool Builder      - Generate engineering calculators")
    print("3.  Research Agent    - Patents, literature, protocols")
    print("4.  Data Analysis     - Statistics & visualization")
    print("5.  Documentation     - Reports, patents, manuals")
    print("6.  Automation        - CI/CD, workflows, dashboards")
    print("7.  Testing/QA        - Test plans, validation, QA")
    print("8.  CFD/FEA Sim       - Fluid dynamics & structural analysis")
    print("9.  Optimization      - Design optimization, φ-analysis")
    print()
    print("10. Run All Daily Tasks")
    print("0.  Exit")
    print()

def run_chief_agent():
    """Chief Agent commands"""
    print("\n📊 CHIEF AGENT")
    print("1. Daily briefing")
    print("2. Analyze project")
    print("3. Prioritize tasks")
    print("4. Shopping list")
    choice = input("\nChoice: ")
    
    if choice == "1":
        os.system("python Agents/chief_agent.py briefing")
    elif choice == "2":
        file = input("File to analyze: ")
        os.system(f"python Agents/chief_agent.py analyze {file}")
    elif choice == "3":
        os.system("python Agents/chief_agent.py prioritize")
    elif choice == "4":
        os.system("python Agents/chief_agent.py shop")

def run_tool_builder():
    """Tool Builder commands"""
    print("\n🔧 TOOL BUILDER AGENT")
    print("1. φ-optimization calculator")
    print("2. Efficiency calculator")
    print("3. Site assessment tool")
    print("4. Data logger")
    print("5. All tools")
    choice = input("\nChoice: ")
    
    if choice == "1":
        os.system("python Agents/tool_builder_agent.py phi")
    elif choice == "2":
        os.system("python Agents/tool_builder_agent.py efficiency")
    elif choice == "3":
        os.system("python Agents/tool_builder_agent.py site")
    elif choice == "4":
        os.system("python Agents/tool_builder_agent.py logger")
    elif choice == "5":
        os.system("python Agents/tool_builder_agent.py all")

def run_research_agent():
    """Research Agent commands"""
    print("\n🔬 RESEARCH AGENT")
    print("1. Patent search")
    print("2. Prior art analysis")
    print("3. Literature review")
    print("4. Protocol generation")
    choice = input("\nChoice: ")
    
    if choice == "1":
        query = input("Patent search query: ")
        os.system(f'python Agents/research_agent.py patents "{query}"')
    elif choice == "2":
        query = input("Technology to analyze: ")
        os.system(f'python Agents/research_agent.py prior-art "{query}"')
    elif choice == "3":
        topic = input("Literature topic: ")
        os.system(f'python Agents/research_agent.py literature "{topic}"')
    elif choice == "4":
        name = input("Test name: ")
        hypothesis = input("Hypothesis: ")
        os.system(f'python Agents/research_agent.py protocol "{name}" "{hypothesis}"')

def run_data_agent():
    """Data Analysis Agent commands"""
    print("\n📊 DATA ANALYSIS AGENT")
    print("1. Analyze test data (CSV)")
    print("2. Generate visualization code")
    print("3. Calculate sample size")
    choice = input("\nChoice: ")
    
    if choice == "1":
        file = input("CSV file path: ")
        os.system(f'python Agents/data_agent.py analyze "{file}"')
    elif choice == "2":
        data_type = input("Data type: ")
        os.system(f'python Agents/data_agent.py visualize "{data_type}"')
    elif choice == "3":
        effect = input("Expected effect size (%): ")
        os.system(f'python Agents/data_agent.py sample-size {effect}')

def run_documentation_agent():
    """Documentation Agent commands"""
    print("\n📝 DOCUMENTATION AGENT")
    print("1. Generate test report")
    print("2. Draft patent claims")
    print("3. Create user manual")
    print("4. Technical specification")
    choice = input("\nChoice: ")
    
    if choice == "1":
        summary = input("Test summary: ")
        os.system(f'python Agents/documentation_agent.py test-report "{summary}"')
    elif choice == "2":
        innovation = input("Innovation description: ")
        os.system(f'python Agents/documentation_agent.py patent-claims "{innovation}"')
    elif choice == "3":
        product = input("Product name: ")
        os.system(f'python Agents/documentation_agent.py manual "{product}"')
    elif choice == "4":
        system = input("System name: ")
        os.system(f'python Agents/documentation_agent.py spec "{system}"')

def run_automation_agent():
    """Automation Agent commands"""
    print("\n⚙️ AUTOMATION AGENT")
    print("1. Daily automation script")
    print("2. Test automation pipeline")
    print("3. CI/CD workflow")
    print("4. Monitoring dashboard")
    choice = input("\nChoice: ")
    
    if choice == "1":
        os.system("python Agents/automation_agent.py daily")
    elif choice == "2":
        test_type = input("Test type: ")
        os.system(f'python Agents/automation_agent.py test-pipeline "{test_type}"')
    elif choice == "3":
        os.system("python Agents/automation_agent.py ci")
    elif choice == "4":
        os.system("python Agents/automation_agent.py dashboard")

def run_testing_agent():
    """Testing/QA Agent commands"""
    print("\n🧪 TESTING/QA AGENT")
    print("1. Generate test plan")
    print("2. Validate test data")
    print("3. Calibration procedure")
    print("4. Failure analysis")
    choice = input("\nChoice: ")
    
    if choice == "1":
        system = input("System to test: ")
        os.system(f'python Agents/testing_agent.py test-plan "{system}"')
    elif choice == "2":
        data = input("Data description: ")
        os.system(f'python Agents/testing_agent.py validate "{data}"')
    elif choice == "3":
        equipment = input("Equipment list: ")
        os.system(f'python Agents/testing_agent.py calibration "{equipment}"')
    elif choice == "4":
        description = input("Failure description: ")
        os.system(f'python Agents/testing_agent.py failure "{description}"')

def run_simulation_agent():
    """CFD/FEA Agent commands"""
    print("\n🌊 CFD/FEA SIMULATION AGENT")
    print("1. Generate OpenFOAM case")
    print("2. CFD Python script")
    print("3. Interpret CFD results")
    print("4. FEA analysis plan")
    choice = input("\nChoice: ")
    
    if choice == "1":
        geometry = input("Geometry description: ")
        os.system(f'python Agents/simulation_agent.py openfoam "{geometry}"')
    elif choice == "2":
        analysis = input("Analysis type: ")
        os.system(f'python Agents/simulation_agent.py cfd-script "{analysis}"')
    elif choice == "3":
        results = input("Results summary: ")
        os.system(f'python Agents/simulation_agent.py interpret "{results}"')
    elif choice == "4":
        structure = input("Structure description: ")
        os.system(f'python Agents/simulation_agent.py fea "{structure}"')

def run_optimization_agent():
    """Optimization Agent commands"""
    print("\n🎯 OPTIMIZATION AGENT")
    print("1. Optimize blade geometry")
    print("2. φ (golden ratio) optimization")
    print("3. Cost-benefit analysis")
    print("4. Multi-objective optimization")
    choice = input("\nChoice: ")
    
    if choice == "1":
        constraints = input("Design constraints: ")
        os.system(f'python Agents/optimization_agent.py blade "{constraints}"')
    elif choice == "2":
        parameter = input("Parameter to optimize: ")
        os.system(f'python Agents/optimization_agent.py phi "{parameter}"')
    elif choice == "3":
        decision = input("Decision to analyze: ")
        os.system(f'python Agents/optimization_agent.py cost-benefit "{decision}"')
    elif choice == "4":
        objectives = input("Objectives (comma-separated): ")
        os.system(f'python Agents/optimization_agent.py multi-objective "{objectives}"')

def run_all_daily_tasks():
    """Execute daily automation"""
    print("\n🚀 RUNNING DAILY TASKS...\n")
    print("1. Daily briefing...")
    os.system("python Agents/chief_agent.py briefing > Reports/daily_briefing.txt")
    print("\n2. Shopping list...")
    os.system("python Agents/chief_agent.py shop > Reports/shopping_list.txt")
    print("\n3. Task prioritization...")
    os.system("python Agents/chief_agent.py prioritize > Reports/priorities.txt")
    print("\n✅ Daily tasks complete! Check Reports/ folder")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select agent (0-10): ").strip()
        
        if choice == "0":
            print("\n👋 Goodbye!")
            break
        elif choice == "1":
            run_chief_agent()
        elif choice == "2":
            run_tool_builder()
        elif choice == "3":
            run_research_agent()
        elif choice == "4":
            run_data_agent()
        elif choice == "5":
            run_documentation_agent()
        elif choice == "6":
            run_automation_agent()
        elif choice == "7":
            run_testing_agent()
        elif choice == "8":
            run_simulation_agent()
        elif choice == "9":
            run_optimization_agent()
        elif choice == "10":
            run_all_daily_tasks()
        else:
            print("❌ Invalid choice")
        
        input("\nPress Enter to continue...")
