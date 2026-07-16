"""
IP Division Agent Hub - Unified interface for all 6 IP agents
Division: IP & Patent Strategy
Cost: $0/month
"""

import os
import sys

def print_header():
    print("\n" + "="*70)
    print("🏛️  IP & PATENT STRATEGY DIVISION - AGENT HUB")
    print("="*70)
    print("\n💼 6 Agents Operational | $0/month Cost | $15,000/month Value")
    print("")

def print_menu():
    print("\n📋 AVAILABLE AGENTS:\n")
    print("  1️⃣  Patent Portfolio Manager")
    print("      └─ Pipeline status, deadlines, valuation, weekly checklist")
    print("")
    print("  2️⃣  Patent Drafting Specialist")
    print("      └─ Claims, specifications, abstracts, figures, filing")
    print("")
    print("  3️⃣  IP Valuation Analyst")
    print("      └─ Patent valuation, licensing strategy, competitive analysis, ROI")
    print("")
    print("  4️⃣  Freedom to Operate (FTO) Checker")
    print("      └─ Prior art search, infringement analysis, clearance, validity")
    print("")
    print("  5️⃣  Licensing Strategist")
    print("      └─ Target licensees, deal structure, negotiation, term sheets")
    print("")
    print("  6️⃣  International Patent Filer")
    print("      └─ PCT strategy, country selection, timeline, translations")
    print("")
    print("  7️⃣  DAILY BRIEFING - Portfolio status + deadlines")
    print("")
    print("  0️⃣  Exit")
    print("\n" + "-"*70)

def daily_briefing():
    """Run automated daily briefing"""
    print("\n" + "="*70)
    print("📊 DAILY IP BRIEFING")
    print("="*70 + "\n")
    
    print("Running Portfolio Manager (status)...")
    os.system("python portfolio_manager.py status")
    
    print("\n" + "-"*70 + "\n")
    print("Running Portfolio Manager (deadlines)...")
    os.system("python portfolio_manager.py deadlines")
    
    print("\n" + "="*70)
    print("✅ Daily Briefing Complete")
    print("="*70)

def run_agent(choice):
    """Execute selected agent"""
    
    if choice == "1":
        print("\n🔹 PATENT PORTFOLIO MANAGER")
        print("\nCommands:")
        print("  status     - Current pipeline status")
        print("  deadlines  - Upcoming deadlines")
        print("  valuation  - Portfolio value")
        print("  checklist  - Weekly execution checklist")
        
        cmd = input("\nEnter command (or press Enter for status): ").strip()
        if not cmd:
            cmd = "status"
        
        os.system(f"python portfolio_manager.py {cmd}")
    
    elif choice == "2":
        print("\n🔹 PATENT DRAFTING SPECIALIST")
        print("\nCommands:")
        print("  claims '<description>'        - Draft patent claims")
        print("  specification '<title>'       - Draft full specification")
        print("  abstract '<summary>'          - Draft abstract")
        print("  figures '<design>'            - Generate figure descriptions")
        print("  filing '<title>'              - Filing checklist")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python patent_drafter.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "3":
        print("\n🔹 IP VALUATION ANALYST")
        print("\nCommands:")
        print("  value '<patent>'         - Value specific patent")
        print("  licensing '<patent>'     - Licensing strategy")
        print("  competitive '<tech>'     - Competitive landscape")
        print("  roi '<investment>'       - ROI analysis")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python ip_valuator.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "4":
        print("\n🔹 FREEDOM TO OPERATE (FTO) CHECKER")
        print("\nCommands:")
        print("  search '<innovation>'        - Prior art search strategy")
        print("  infringement '<ours>' '<theirs>' - Infringement analysis")
        print("  clearance '<product>'        - FTO clearance report")
        print("  challenge '<patent #>'       - Patent validity challenge")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python fto_checker.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "5":
        print("\n🔹 LICENSING STRATEGIST")
        print("\nCommands:")
        print("  targets '<tech>'         - Identify target licensees")
        print("  deal '<profile>'         - Design deal structure")
        print("  negotiate '<company>'    - Negotiation playbook")
        print("  termsheet '<deal>'       - Generate term sheet")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python licensing_strategist.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "6":
        print("\n🔹 INTERNATIONAL PATENT FILER")
        print("\nCommands:")
        print("  pct '<patent>'           - PCT filing strategy")
        print("  countries '<market>'     - Country selection")
        print("  timeline '<date>'        - Filing timeline")
        print("  translation '<countries>' - Translation requirements")
        
        cmd = input("\nEnter command: ").strip()
        if cmd:
            os.system(f'python international_filer.py {cmd}')
        else:
            print("❌ Command required")
    
    elif choice == "7":
        daily_briefing()
    
    else:
        print("❌ Invalid selection")

def main():
    """Main interactive loop"""
    while True:
        print_header()
        print_menu()
        
        choice = input("Select agent (0-7): ").strip()
        
        if choice == "0":
            print("\n👋 Goodbye! IP agents standing by.\n")
            break
        
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            run_agent(choice)
            input("\n⏸️  Press Enter to continue...")
        else:
            print("❌ Invalid selection. Please choose 0-7.")
            input("\n⏸️  Press Enter to continue...")

if __name__ == "__main__":
    main()
