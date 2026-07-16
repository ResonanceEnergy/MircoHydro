"""
SALES/MARKETING HUB
Interactive menu for all 6 Sales & Marketing agents
"""

import os
import sys

# Add Agents directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Agents'))

def print_banner():
    print("\n" + "="*70)
    print("  🎯 SALES & MARKETING HUB - 6 AGENTS READY")
    print("="*70)
    print("  Revenue Generation | Lead Management | Brand Building")
    print("  Target: $15k/month value | Build: 45 min | Cost: $0")
    print("="*70 + "\n")

def print_menu():
    print("📋 AVAILABLE AGENTS:\n")
    print("1. ✍️  Content Marketing    - Blog posts, case studies, content calendars")
    print("2. 🔍 SEO Specialist        - Keywords, on-page optimization, rankings")
    print("3. 🎯 Lead Generation       - Prospecting, qualification, nurturing")
    print("4. 💬 Sales Scripts         - Discovery, demos, objections, closing")
    print("5. 🤝 Customer Success      - Onboarding, retention, upsell strategies")
    print("6. 🎨 Brand Strategy        - Positioning, messaging, visual identity")
    print("\n0. ❌ Exit Hub")
    print("\n" + "-"*70 + "\n")

def content_marketing_menu():
    print("\n✍️  CONTENT MARKETING AGENT")
    print("-" * 50)
    print("1. Write blog post")
    print("2. Create case study")
    print("3. Generate content calendar")
    print("4. Design social media campaign")
    print("0. Back to main menu")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == '1':
        topic = input("Blog topic: ")
        from content_marketing import write_blog_post
        print("\n" + write_blog_post(topic))
    elif choice == '2':
        customer = input("Customer name: ")
        results = input("Key results: ")
        from content_marketing import create_case_study
        print("\n" + create_case_study(customer, results))
    elif choice == '3':
        duration = input("Calendar duration (month/quarter/year): ")
        from content_marketing import content_calendar
        print("\n" + content_calendar(duration))
    elif choice == '4':
        goal = input("Campaign goal: ")
        from content_marketing import social_media_campaign
        print("\n" + social_media_campaign(goal))

def seo_specialist_menu():
    print("\n🔍 SEO SPECIALIST AGENT")
    print("-" * 50)
    print("1. Keyword research")
    print("2. On-page optimization")
    print("3. Technical SEO audit")
    print("4. 90-day ranking strategy")
    print("0. Back to main menu")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == '1':
        topic = input("Research topic: ")
        from seo_specialist import keyword_research
        print("\n" + keyword_research(topic))
    elif choice == '2':
        url = input("Page URL: ")
        keyword = input("Target keyword: ")
        from seo_specialist import optimize_page
        print("\n" + optimize_page(url, keyword))
    elif choice == '3':
        from seo_specialist import technical_seo_audit
        print("\n" + technical_seo_audit())
    elif choice == '4':
        keywords = input("Target keywords (comma-separated): ")
        from seo_specialist import ranking_strategy
        print("\n" + ranking_strategy(keywords))

def lead_generation_menu():
    print("\n🎯 LEAD GENERATION AGENT")
    print("-" * 50)
    print("1. Identify prospects")
    print("2. Qualify leads (BANT)")
    print("3. Generate nurture sequence")
    print("4. Lead scoring model")
    print("0. Back to main menu")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == '1':
        industry = input("Target industry: ")
        from lead_generation import identify_prospects
        print("\n" + identify_prospects(industry))
    elif choice == '2':
        info = input("Lead info (company, role, needs): ")
        from lead_generation import qualify_leads
        print("\n" + qualify_leads(info))
    elif choice == '3':
        lead_type = input("Lead type (hot/warm/cool): ")
        from lead_generation import nurture_sequence
        print("\n" + nurture_sequence(lead_type))
    elif choice == '4':
        from lead_generation import lead_scoring_model
        print("\n" + lead_scoring_model())

def sales_scripts_menu():
    print("\n💬 SALES SCRIPTS AGENT")
    print("-" * 50)
    print("1. Discovery call script")
    print("2. Objection handling playbook")
    print("3. Product demo script")
    print("4. Closing techniques")
    print("0. Back to main menu")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == '1':
        from sales_scripts import discovery_call_script
        print("\n" + discovery_call_script())
    elif choice == '2':
        from sales_scripts import objection_handling
        print("\n" + objection_handling())
    elif choice == '3':
        from sales_scripts import demo_script
        print("\n" + demo_script())
    elif choice == '4':
        from sales_scripts import closing_techniques
        print("\n" + closing_techniques())

def customer_success_menu():
    print("\n🤝 CUSTOMER SUCCESS AGENT")
    print("-" * 50)
    print("1. Create onboarding plan")
    print("2. Retention strategy")
    print("3. Identify upsell opportunities")
    print("4. Satisfaction tracking framework")
    print("0. Back to main menu")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == '1':
        customer = input("Customer name: ")
        from customer_success import onboarding_plan
        print("\n" + onboarding_plan(customer))
    elif choice == '2':
        from customer_success import retention_strategy
        print("\n" + retention_strategy())
    elif choice == '3':
        profile = input("Customer profile: ")
        from customer_success import upsell_opportunities
        print("\n" + upsell_opportunities(profile))
    elif choice == '4':
        from customer_success import satisfaction_tracking
        print("\n" + satisfaction_tracking())

def brand_strategy_menu():
    print("\n🎨 BRAND STRATEGY AGENT")
    print("-" * 50)
    print("1. Brand positioning framework")
    print("2. Messaging by audience")
    print("3. Visual identity system")
    print("4. Complete brand guidelines")
    print("0. Back to main menu")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == '1':
        from brand_strategy import brand_positioning
        print("\n" + brand_positioning())
    elif choice == '2':
        from brand_strategy import messaging_framework
        print("\n" + messaging_framework())
    elif choice == '3':
        from brand_strategy import visual_identity
        print("\n" + visual_identity())
    elif choice == '4':
        from brand_strategy import brand_guidelines
        print("\n" + brand_guidelines())

def quick_start():
    """Run a quick demo showing all agents"""
    print("\n🚀 QUICK START DEMO - Testing all 6 agents...\n")
    
    print("1️⃣  CONTENT MARKETING - Generating blog post idea...")
    from content_marketing import write_blog_post
    result = write_blog_post("micro-hydro benefits for manufacturers")
    print(result[:500] + "...\n")
    
    print("\n2️⃣  SEO SPECIALIST - Keyword research sample...")
    from seo_specialist import keyword_research
    result = keyword_research("micro-hydro power")
    print(result[:500] + "...\n")
    
    print("\n3️⃣  LEAD GENERATION - Prospect identification...")
    from lead_generation import identify_prospects
    result = identify_prospects("manufacturing")
    print(result[:500] + "...\n")
    
    print("\n4️⃣  SALES SCRIPTS - Discovery call framework...")
    from sales_scripts import discovery_call_script
    result = discovery_call_script()
    print(result[:500] + "...\n")
    
    print("\n5️⃣  CUSTOMER SUCCESS - Onboarding plan...")
    from customer_success import onboarding_plan
    result = onboarding_plan("New Customer")
    print(result[:500] + "...\n")
    
    print("\n6️⃣  BRAND STRATEGY - Positioning framework...")
    from brand_strategy import brand_positioning
    result = brand_positioning()
    print(result[:500] + "...\n")
    
    print("\n✅ All 6 agents operational!\n")
    input("Press Enter to continue to main menu...")

def main():
    print_banner()
    
    # Check for quick start argument
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'demo':
        quick_start()
    
    while True:
        print_menu()
        choice = input("Select agent (1-6, or 0 to exit): ").strip()
        
        if choice == '0':
            print("\n👋 Sales & Marketing Hub closed. Build revenue. Scale growth.\n")
            break
        elif choice == '1':
            content_marketing_menu()
        elif choice == '2':
            seo_specialist_menu()
        elif choice == '3':
            lead_generation_menu()
        elif choice == '4':
            sales_scripts_menu()
        elif choice == '5':
            customer_success_menu()
        elif choice == '6':
            brand_strategy_menu()
        elif choice.lower() == 'demo':
            quick_start()
        else:
            print("\n❌ Invalid option. Please select 1-6 or 0.")
        
        if choice != '0':
            input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main()
