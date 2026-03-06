"""
FUNDING HUB
Interactive menu to access all funding agents.
"""

import os
import subprocess
import sys

def print_header():
    print("\n" + "="*70)
    print("💰 FUNDING DIVISION HUB")
    print("="*70)
    print("Professional fundraising, grant writing, and financial modeling")
    print("FREE via Groq API - No cost, enterprise-grade intelligence\n")

def print_menu():
    print("SELECT AN AGENT:")
    print()
    print("  1. Grant Scout           - Find grants and funding opportunities")
    print("  2. Grant Writer          - Write grant applications")
    print("  3. Investor Targeting    - Find and profile investors")
    print("  4. Pitch Deck Generator  - Create investor pitch materials")
    print("  5. Financial Modeler     - Build financial models and projections")
    print("  6. Deal Terms Analyst    - Analyze and negotiate term sheets")
    print()
    print("  7. Daily Briefing        - Run all quick checks")
    print()
    print("  0. Exit")
    print()

def run_agent(agent_file, command):
    """Execute an agent with specified command."""
    agent_path = os.path.join(os.path.dirname(__file__), 'Agents', agent_file)
    
    try:
        result = subprocess.run(
            ['python', agent_path] + command.split(),
            capture_output=True,
            text=True,
            cwd=os.path.dirname(__file__)
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"Error running agent: {e}")

def grant_scout_menu():
    """Grant Scout submenu."""
    print("\n📋 GRANT SCOUT")
    print("Commands: find <category> | calendar | check <grant> | strategy <type>")
    print("Categories: federal, state, utility, private, international, all")
    print()
    
    command = input("Enter command (or 'back'): ").strip()
    if command.lower() != 'back':
        run_agent('grant_scout.py', command)

def grant_writer_menu():
    """Grant Writer submenu."""
    print("\n✍️ GRANT WRITER")
    print("Commands: narrative <grant> <description> | budget <type> <amount>")
    print("         letter <recipient> <org> <rel> | evaluation <project> <outcomes>")
    print()
    
    command = input("Enter command (or 'back'): ").strip()
    if command.lower() != 'back':
        run_agent('grant_writer.py', command)

def investor_targeting_menu():
    """Investor Targeting submenu."""
    print("\n🎯 INVESTOR TARGETING")
    print("Commands: find <category> <stage> | profile <investor>")
    print("         strategy <stage> <amount> | intro <investor> <connector> <rel>")
    print("Categories: vc, angel, family_office, corporate, impact, all")
    print("Stages: seed, series_a, series_b, growth")
    print()
    
    command = input("Enter command (or 'back'): ").strip()
    if command.lower() != 'back':
        run_agent('investor_targeting.py', command)

def pitch_deck_menu():
    """Pitch Deck Generator submenu."""
    print("\n📊 PITCH DECK GENERATOR")
    print("Commands: deck <stage> <audience> | onepager <audience>")
    print("         demo <duration> | update")
    print("Stages: seed, series_a, series_b, growth")
    print("Duration: 3, 5, or 10 minutes")
    print()
    
    command = input("Enter command (or 'back'): ").strip()
    if command.lower() != 'back':
        run_agent('pitch_deck_generator.py', command)

def financial_modeler_menu():
    """Financial Modeler submenu."""
    print("\n💹 FINANCIAL MODELER")
    print("Commands: model <type> <years> | economics <model> | valuation <stage> <revenue> <growth>")
    print("Types: hardware, saas, services, hybrid")
    print()
    
    command = input("Enter command (or 'back'): ").strip()
    if command.lower() != 'back':
        run_agent('financial_modeler.py', command)

def deal_terms_menu():
    """Deal Terms Analyst submenu."""
    print("\n⚖️ DEAL TERMS ANALYST")
    print("Commands: analyze <investor> | standards | compare <num>")
    print()
    
    command = input("Enter command (or 'back'): ").strip()
    if command.lower() != 'back':
        run_agent('deal_terms_analyst.py', command)

def daily_briefing():
    """Run daily briefing across all agents."""
    print("\n" + "="*70)
    print("📅 DAILY FUNDING BRIEFING")
    print("="*70 + "\n")
    
    print("1️⃣ GRANT CALENDAR (Next 30 Days)")
    print("-" * 70)
    run_agent('grant_scout.py', 'calendar')
    
    print("\n2️⃣ INVESTOR PIPELINE STATUS")
    print("-" * 70)
    run_agent('investor_targeting.py', 'find vc seed')
    
    print("\n3️⃣ FINANCIAL SNAPSHOT")
    print("-" * 70)
    run_agent('financial_modeler.py', 'economics hardware')
    
    print("\n" + "="*70)
    print("Daily briefing complete!")
    print("="*70 + "\n")

def main():
    while True:
        print_header()
        print_menu()
        
        choice = input("Select option (0-7): ").strip()
        
        if choice == '0':
            print("\n👋 Exiting Funding Hub. Good luck with fundraising!\n")
            break
        elif choice == '1':
            grant_scout_menu()
        elif choice == '2':
            grant_writer_menu()
        elif choice == '3':
            investor_targeting_menu()
        elif choice == '4':
            pitch_deck_menu()
        elif choice == '5':
            financial_modeler_menu()
        elif choice == '6':
            deal_terms_menu()
        elif choice == '7':
            daily_briefing()
        else:
            print("\n❌ Invalid option. Please select 0-7.\n")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
