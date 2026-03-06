"""
Partnership Division Hub - Unified interface for all partnership agents
Division: Partnerships
Cost: $0/month
"""

import os
import sys

def print_header():
    print("\n" + "="*70)
    print("🤝 PARTNERSHIP DIVISION - AGENT HUB")
    print("="*70)
    print("\n💼 5 Agents Operational | $0/month Cost | $12,000/month Value")
    print("")

def print_menu():
    print("\n📋 AVAILABLE AGENTS:\n")
    print("  1️⃣  Partnership Scout")
    print("      └─ Find partners, research companies, geographic mapping, pipeline")
    print("")
    print("  2️⃣  Outreach Manager")
    print("      └─ Emails, follow-ups, campaigns, response handling")
    print("")
    print("  3️⃣  Proposal Writer")
    print("      └─ Proposals, term sheets, one-pagers, JV agreements")
    print("")
    print("  4️⃣  Relationship Manager")
    print("      └─ Log interactions, pipeline view, health checks, meeting prep")
    print("")
    print("  5️⃣  Deal Optimizer")
    print("      └─ Structure deals, valuations, comparisons, negotiation tactics")
    print("")
    print("  6️⃣  QUICK START - Find 50 partners NOW")
    print("")
    print("  0️⃣  Exit")
    print("\n" + "-"*70)

def quick_start():
    """Run quick start: find partners and generate outreach"""
    print("\n" + "="*70)
    print("⚡ QUICK START - PARTNERSHIP ACCELERATION")
    print("="*70 + "\n")
    
    print("Step 1: Finding partners...")
    os.system("python Agents/partnership_scout.py find")
    
    print("\n" + "-"*70 + "\n")
    print("Step 2: Generating outreach campaign...")
    os.system('python Agents/outreach_manager.py campaign "Micro-hydro manufacturers"')
    
    print("\n" + "="*70)
    print("✅ Quick Start Complete!")
    print("Next: Review partner list, customize emails, start outreach Monday")
    print("="*70)

def run_agent(choice):
    """Execute selected agent"""
    
    if choice == "1":
        print("\n🔹 PARTNERSHIP SCOUT")
        print("\nCommands:")
        print("  find [category]          - Find partners")
        print("  research '<company>'     - Deep research")
        print("  map [region]             - Geographic mapping")
        print("  pipeline                 - View pipeline")
        
        cmd = input("\nEnter command (or press Enter for 'find'): ").strip()
        if not cmd:
            cmd = "find"
        
        os.system(f'python Agents/partnership_scout.py {cmd}')
    
    elif choice == "2":
        print("\n🔹 OUTREACH MANAGER")
        print("\nCommands:")
        print("  email '<company>' '[name]'   - Generate email")
        print("  followup [stage]             - Follow-up sequence")
        print("  campaign '<targets>'         - Build campaign")
        print("  respond '<email>'            - Analyze response")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python Agents/outreach_manager.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "3":
        print("\n🔹 PROPOSAL WRITER")
        print("\nCommands:")
        print("  proposal '<partner>'     - Full proposal")
        print("  termsheet '<deal>'       - Term sheet")
        print("  onepager '<type>'        - One-pager")
        print("  jv '<details>'           - JV agreement")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python Agents/proposal_writer.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "4":
        print("\n🔹 RELATIONSHIP MANAGER")
        print("\nCommands:")
        print("  log '<partner>' '<details>'  - Log interaction")
        print("  pipeline                      - View pipeline")
        print("  health '<partner>'            - Health check")
        print("  prep '<partner>' '[type]'     - Meeting prep")
        
        cmd = input("\nEnter command (or press Enter for 'pipeline'): ").strip()
        if not cmd:
            cmd = "pipeline"
        
        os.system(f'python Agents/relationship_manager.py {cmd}')
    
    elif choice == "5":
        print("\n🔹 DEAL OPTIMIZER")
        print("\nCommands:")
        print("  optimize '<deal>'       - Optimize structure")
        print("  value '<contributions>' - Value contributions")
        print("  compare '<deals>'       - Compare deals")
        print("  negotiate '<context>'   - Negotiation tactics")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python Agents/deal_optimizer.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "6":
        quick_start()
    
    else:
        print("❌ Invalid selection")

def main():
    """Main interactive loop"""
    while True:
        print_header()
        print_menu()
        
        choice = input("Select agent (0-6): ").strip()
        
        if choice == "0":
            print("\n👋 Goodbye! Partnership agents standing by.\n")
            break
        
        if choice in ["1", "2", "3", "4", "5", "6"]:
            run_agent(choice)
            input("\n⏸️  Press Enter to continue...")
        else:
            print("❌ Invalid selection. Please choose 0-6.")
            input("\n⏸️  Press Enter to continue...")

if __name__ == "__main__":
    main()
