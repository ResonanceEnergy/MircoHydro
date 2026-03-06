"""
SITE SCOUTING HUB
Interactive menu system for all 7 Site Scouting agents.
"""

import os
import sys

# Add Agents directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Agents'))

def print_header():
    print("\n" + "="*80)
    print(" 🗺️  SITE SCOUTING DIVISION - Agent Hub")
    print("="*80)
    print("\n💰 VALUE: $18,000/month equivalent")
    print("🎯 MISSION: Identify and qualify optimal micro-hydro sites\n")

def main_menu():
    while True:
        print_header()
        print("SELECT AGENT:")
        print()
        print("  1. 🗺️  Hydro Mapper       - Resource mapping, site identification, flow analysis")
        print("  2. 📋 Regulatory Scout    - Permits, water rights, compliance strategy")
        print("  3. 💰 Economic Analyst    - Financial modeling, ROI, incentives")
        print("  4. 🌿 Environmental       - Impact assessment, fish passage, mitigation")
        print("  5. 🏡 Land Access         - Property rights, easements, negotiations")
        print("  6. ⚡ Grid Connection     - Utility interconnection, net metering, PPA")
        print("  7. 📊 Report Generator    - Comprehensive reports, presentations")
        print()
        print("  8. 🚀 Quick Demo (run sample from each agent)")
        print("  0. Exit")
        print()
        
        choice = input("Enter selection (0-8): ").strip()
        
        if choice == '0':
            print("\n✅ Site Scouting Hub closed.\n")
            break
        elif choice == '1':
            hydro_mapper_menu()
        elif choice == '2':
            regulatory_scout_menu()
        elif choice == '3':
            economic_analyst_menu()
        elif choice == '4':
            environmental_menu()
        elif choice == '5':
            land_access_menu()
        elif choice == '6':
            grid_connection_menu()
        elif choice == '7':
            report_generator_menu()
        elif choice == '8':
            quick_demo()
        else:
            print("❌ Invalid selection")

def hydro_mapper_menu():
    from hydro_mapper import map_water_resources, assess_site_potential, flow_analysis, site_comparison
    
    while True:
        print("\n" + "="*60)
        print(" 🗺️  HYDRO MAPPER AGENT")
        print("="*60)
        print("\n  1. Map Water Resources (identify sites in region)")
        print("  2. Assess Site Potential (detailed feasibility)")
        print("  3. Flow Analysis (hydrologic assessment)")
        print("  4. Site Comparison (rank multiple sites)")
        print("  0. Back to Main Menu")
        print()
        
        choice = input("Enter selection: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            region = input("Enter region (e.g., 'Pacific Northwest'): ") or 'Pacific Northwest'
            print("\n🔍 Mapping water resources...\n")
            print(map_water_resources(region))
            input("\nPress Enter to continue...")
        elif choice == '2':
            site = input("Enter site data (e.g., '150 GPM flow, 40 ft head'): ") or '150 GPM flow, 40 ft head'
            print("\n📊 Assessing site potential...\n")
            print(assess_site_potential(site))
            input("\nPress Enter to continue...")
        elif choice == '3':
            location = input("Enter location: ") or 'Mountain stream'
            print("\n💧 Analyzing flow...\n")
            print(flow_analysis(location))
            input("\nPress Enter to continue...")
        elif choice == '4':
            sites = input("Enter sites to compare: ") or 'Site A (100GPM, 50ft), Site B (200GPM, 30ft)'
            print("\n📈 Comparing sites...\n")
            print(site_comparison(sites))
            input("\nPress Enter to continue...")

def regulatory_scout_menu():
    from regulatory_scout import permit_requirements, water_rights_analysis, environmental_compliance, compliance_calendar
    
    while True:
        print("\n" + "="*60)
        print(" 📋 REGULATORY SCOUT AGENT")
        print("="*60)
        print("\n  1. Permit Requirements (complete permit roadmap)")
        print("  2. Water Rights Analysis (state-specific)")
        print("  3. Environmental Compliance (ESA, CWA, etc.)")
        print("  4. Compliance Calendar (integrated timeline)")
        print("  0. Back to Main Menu")
        print()
        
        choice = input("Enter selection: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            location = input("Location (e.g., 'Washington State'): ") or 'Washington State'
            size = input("Project size (e.g., '75 kW'): ") or '75 kW'
            print("\n📋 Researching permits...\n")
            print(permit_requirements(location, size))
            input("\nPress Enter to continue...")
        elif choice == '2':
            state = input("State: ") or 'Oregon'
            source = input("Water source: ") or 'Small creek'
            print("\n💧 Analyzing water rights...\n")
            print(water_rights_analysis(state, source))
            input("\nPress Enter to continue...")
        elif choice == '3':
            details = input("Project details: ") or '100 kW, salmon stream'
            print("\n🌿 Analyzing environmental compliance...\n")
            print(environmental_compliance(details))
            input("\nPress Enter to continue...")
        elif choice == '4':
            timeline = input("Project timeline: ") or '36-month project'
            print("\n📅 Creating compliance calendar...\n")
            print(compliance_calendar(timeline))
            input("\nPress Enter to continue...")

def economic_analyst_menu():
    from economic_analyst import project_economics, cost_estimate, roi_scenarios, incentive_analysis
    
    while True:
        print("\n" + "="*60)
        print(" 💰 ECONOMIC ANALYST AGENT")
        print("="*60)
        print("\n  1. Project Economics (complete financial analysis)")
        print("  2. Cost Estimate (detailed CAPEX breakdown)")
        print("  3. ROI Scenarios (best/base/worst case)")
        print("  4. Incentive Analysis (federal, state, local)")
        print("  0. Back to Main Menu")
        print()
        
        choice = input("Enter selection: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            specs = input("Project specs (e.g., '100 kW, 75% CF, $0.10/kWh'): ") or '100 kW, 75% CF, $0.10/kWh'
            print("\n💰 Analyzing economics...\n")
            print(project_economics(specs))
            input("\nPress Enter to continue...")
        elif choice == '2':
            specs = input("System specs: ") or '75 kW Pelton turbine'
            print("\n💵 Estimating costs...\n")
            print(cost_estimate(specs))
            input("\nPress Enter to continue...")
        elif choice == '3':
            assumptions = input("Financial assumptions: ") or '$500k CAPEX, $50k annual revenue'
            print("\n📊 Calculating ROI scenarios...\n")
            print(roi_scenarios(assumptions))
            input("\nPress Enter to continue...")
        elif choice == '4':
            location = input("Location: ") or 'Oregon'
            size = input("Project size: ") or '100 kW'
            print("\n🎁 Researching incentives...\n")
            print(incentive_analysis(location, size))
            input("\nPress Enter to continue...")

def environmental_menu():
    from environmental_assessor import environmental_impact, fish_passage_design, mitigation_plan, environmental_monitoring_protocol
    
    while True:
        print("\n" + "="*60)
        print(" 🌿 ENVIRONMENTAL ASSESSOR AGENT")
        print("="*60)
        print("\n  1. Environmental Impact (comprehensive EIA)")
        print("  2. Fish Passage Design (ladders, screens)")
        print("  3. Mitigation Plan (compensatory mitigation)")
        print("  4. Monitoring Protocol (compliance monitoring)")
        print("  0. Back to Main Menu")
        print()
        
        choice = input("Enter selection: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            info = input("Project info: ") or '100 kW, salmon stream, 500ft dewatered reach'
            print("\n🌿 Assessing environmental impact...\n")
            print(environmental_impact(info))
            input("\nPress Enter to continue...")
        elif choice == '2':
            species = input("Species present: ") or 'Chinook salmon, Steelhead'
            print("\n🐟 Designing fish passage...\n")
            print(fish_passage_design(species))
            input("\nPress Enter to continue...")
        elif choice == '3':
            summary = input("Impact summary: ") or '0.5 acre wetland, 500ft dewatered reach'
            print("\n🔧 Developing mitigation plan...\n")
            print(mitigation_plan(summary))
            input("\nPress Enter to continue...")
        elif choice == '4':
            details = input("Project details: ") or '75 kW, ESA consultation required'
            print("\n📋 Creating monitoring protocol...\n")
            print(environmental_monitoring_protocol(details))
            input("\nPress Enter to continue...")

def land_access_menu():
    from land_access import property_analysis, easement_negotiation, lease_vs_purchase, access_road_requirements
    
    while True:
        print("\n" + "="*60)
        print(" 🏡 LAND ACCESS SPECIALIST AGENT")
        print("="*60)
        print("\n  1. Property Analysis (ownership, rights needed)")
        print("  2. Easement Negotiation (strategy & tactics)")
        print("  3. Lease vs Purchase (financial comparison)")
        print("  4. Access Road Requirements (improvements needed)")
        print("  0. Back to Main Menu")
        print()
        
        choice = input("Enter selection: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            location = input("Site location: ") or 'Rural site, 3 parcels'
            print("\n🏡 Analyzing property...\n")
            print(property_analysis(location))
            input("\nPress Enter to continue...")
        elif choice == '2':
            profile = input("Landowner profile: ") or 'Farmer, 65 yrs old'
            rights = input("Rights needed: ") or 'Penstock easement'
            print("\n🤝 Developing negotiation strategy...\n")
            print(easement_negotiation(profile, rights))
            input("\nPress Enter to continue...")
        elif choice == '3':
            characteristics = input("Site characteristics: ") or '5 acres needed'
            constraints = input("Financial constraints: ") or '$500k budget'
            print("\n💵 Comparing lease vs purchase...\n")
            print(lease_vs_purchase(characteristics, constraints))
            input("\nPress Enter to continue...")
        elif choice == '4':
            conditions = input("Current conditions: ") or 'Gravel road, narrow, 1 mile from highway'
            print("\n🛣️  Analyzing access road...\n")
            print(access_road_requirements(conditions))
            input("\nPress Enter to continue...")

def grid_connection_menu():
    from grid_connection import interconnection_analysis, net_metering_analysis, ppa_structure, utility_tariff_research
    
    while True:
        print("\n" + "="*60)
        print(" ⚡ GRID CONNECTION ANALYST AGENT")
        print("="*60)
        print("\n  1. Interconnection Analysis (utility process & costs)")
        print("  2. Net Metering Analysis (state policies)")
        print("  3. PPA Structure (power purchase agreement)")
        print("  4. Utility Tariff Research (rates & programs)")
        print("  0. Back to Main Menu")
        print()
        
        choice = input("Enter selection: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            specs = input("Project specs: ") or '100 kW, rural location'
            utility = input("Utility: ") or 'Pacific Power'
            print("\n⚡ Analyzing interconnection...\n")
            print(interconnection_analysis(specs, utility))
            input("\nPress Enter to continue...")
        elif choice == '2':
            state = input("State: ") or 'Oregon'
            size = input("Project size: ") or '75 kW'
            print("\n🔌 Analyzing net metering...\n")
            print(net_metering_analysis(state, size))
            input("\nPress Enter to continue...")
        elif choice == '3':
            generation = input("Annual generation: ") or '800 MWh/year'
            rates = input("Market rates: ") or 'Wholesale $0.05/kWh'
            print("\n📄 Structuring PPA...\n")
            print(ppa_structure(generation, rates))
            input("\nPress Enter to continue...")
        elif choice == '4':
            utility = input("Utility name: ") or 'Seattle City Light'
            print("\n🔍 Researching utility tariffs...\n")
            print(utility_tariff_research(utility))
            input("\nPress Enter to continue...")

def report_generator_menu():
    from report_generator import site_assessment_report, executive_summary, investor_presentation, comparative_analysis
    
    while True:
        print("\n" + "="*60)
        print(" 📊 REPORT GENERATOR AGENT")
        print("="*60)
        print("\n  1. Site Assessment Report (comprehensive)")
        print("  2. Executive Summary (2-3 pages)")
        print("  3. Investor Presentation (pitch deck)")
        print("  4. Comparative Analysis (multi-site ranking)")
        print("  0. Back to Main Menu")
        print()
        
        choice = input("Enter selection: ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            data = input("Site data: ") or '100 kW site, good flow'
            print("\n📊 Generating full report...\n")
            print(site_assessment_report(data))
            input("\nPress Enter to continue...")
        elif choice == '2':
            assessment = input("Assessment data: ") or 'Detailed assessment'
            print("\n📝 Creating executive summary...\n")
            print(executive_summary(assessment))
            input("\nPress Enter to continue...")
        elif choice == '3':
            summary = input("Project summary: ") or '75 kW, 15% IRR'
            print("\n🎯 Generating investor presentation...\n")
            print(investor_presentation(summary))
            input("\nPress Enter to continue...")
        elif choice == '4':
            sites = input("Sites to compare: ") or 'Site A (100kW, $600k), Site B (75kW, $400k)'
            print("\n📈 Comparing sites...\n")
            print(comparative_analysis(sites))
            input("\nPress Enter to continue...")

def quick_demo():
    """Run quick sample from each agent"""
    from hydro_mapper import map_water_resources
    from regulatory_scout import permit_requirements
    from economic_analyst import project_economics
    from environmental_assessor import environmental_impact
    from land_access import property_analysis
    from grid_connection import interconnection_analysis
    from report_generator import executive_summary
    
    print("\n" + "="*80)
    print(" 🚀 QUICK DEMO - Site Scouting Division")
    print("="*80 + "\n")
    
    print("Running quick sample from each of 7 agents...\n")
    
    print("="*60)
    print("1. HYDRO MAPPER - Pacific Northwest Water Resources")
    print("="*60)
    print(map_water_resources('Pacific Northwest')[:500] + "...\n")
    input("Press Enter to continue...")
    
    print("\n" + "="*60)
    print("2. REGULATORY SCOUT - Washington State Permits")
    print("="*60)
    print(permit_requirements('Washington State', '75 kW')[:500] + "...\n")
    input("Press Enter to continue...")
    
    print("\n" + "="*60)
    print("3. ECONOMIC ANALYST - Project Economics")
    print("="*60)
    print(project_economics('100 kW, 75% CF, $0.10/kWh')[:500] + "...\n")
    input("Press Enter to continue...")
    
    print("\n" + "="*60)
    print("4. ENVIRONMENTAL ASSESSOR - Impact Assessment")
    print("="*60)
    print(environmental_impact('100 kW, salmon stream')[:500] + "...\n")
    input("Press Enter to continue...")
    
    print("\n" + "="*60)
    print("5. LAND ACCESS - Property Analysis")
    print("="*60)
    print(property_analysis('Rural site, 3 parcels')[:500] + "...\n")
    input("Press Enter to continue...")
    
    print("\n" + "="*60)
    print("6. GRID CONNECTION - Interconnection Analysis")
    print("="*60)
    print(interconnection_analysis('100 kW, rural', 'Pacific Power')[:500] + "...\n")
    input("Press Enter to continue...")
    
    print("\n" + "="*60)
    print("7. REPORT GENERATOR - Executive Summary")
    print("="*60)
    print(executive_summary('100 kW site assessment')[:500] + "...\n")
    
    print("\n✅ Quick demo complete! All 7 agents operational.\n")
    input("Press Enter to return to main menu...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n✅ Site Scouting Hub closed.\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
