# microhydro_matrix_monitor.py
# MicroHydro Matrix Monitor - Real-time Enterprise Intelligence Platform
# Adapted from AAC Matrix Monitor technology for MicroHydro operations

import streamlit as st
import pandas as pd
import time
import os
import json
from datetime import datetime
from microhydro_site_optimization_engine import SiteOptimizationEngine

# Import design matrix
DESIGN_MATRIX = [
    {"constraint": "Spiral/vortex flow geometry in penstock", "insights": ["#1", "#2", "#7", "#9"], "priority": "H", "acceptance": "Penstock incorporates spiral rifling or helical channels", "impact": "+5-10% efficiency gain", "status": "In Progress"},
    {"constraint": "Temperature compensation in turbine design", "insights": ["#10"], "priority": "H", "acceptance": "System performance stable across -5°C to +30°C water temp", "impact": "Year-round reliability", "status": "Completed"},
    {"constraint": "Coherent flow minimization of turbulence", "insights": ["#9", "#14"], "priority": "H", "acceptance": "All water pathways smooth; Reynolds number >critical value", "impact": "Core efficiency target", "status": "In Progress"},
    {"constraint": "Wide flow range efficiency optimization", "insights": ["#13", "#16", "#30"], "priority": "H", "acceptance": "System maintains ≥70% efficiency from 25% to 100% flow", "impact": "Field viability", "status": "Pending"},
    {"constraint": "Frequency/voltage tight control", "insights": ["#24"], "priority": "H", "acceptance": "Frequency ±0.1 Hz; voltage ±5%; supports sensitive loads", "impact": "Grid-tie + off-grid operation", "status": "Completed"},
    {"constraint": "Simplicity in design & operation", "insights": ["#3", "#4", "#6", "#8"], "priority": "H", "acceptance": "Component count ≤[X]; UI intuitive; manual <30 pages", "impact": "User adoption; maintenance", "status": "In Progress"},
    {"constraint": "Locally-available, standard components", "insights": ["#5"], "priority": "H", "acceptance": "≥90% of BOM available globally; no proprietary parts", "impact": "Field serviceability", "status": "Completed"},
    {"constraint": "Field-validated design", "insights": ["#23"], "priority": "H", "acceptance": "Phase 6 real-customer installations; documented field learning", "impact": "Design refinement", "status": "Pending"},
    {"constraint": "Cost-effectiveness ($/kW target)", "insights": ["#16"], "priority": "H", "acceptance": "Manufacturing cost ≤[X]/kW; customer price ≤[Y]/kW", "impact": "Business viability", "status": "In Progress"},
    {"constraint": "Tank sediment settling design", "insights": ["#21"], "priority": "M", "acceptance": "Settling volume/residence time removes 90% sediment; drain auto-purges", "impact": "Turbine longevity", "status": "Pending"},
    {"constraint": "User training & knowledge transfer", "insights": ["#22"], "priority": "M", "acceptance": "Installation manual illustrated; video training; peer support community", "impact": "Customer satisfaction", "status": "In Progress"},
    {"constraint": "Material selection for water compatibility", "insights": ["#18"], "priority": "M", "acceptance": "Bearings/seals selected for wet environment; corrosion testing completed", "impact": "30-year durability", "status": "Completed"},
    {"constraint": "3-phase AC electrical system", "insights": ["#11"], "priority": "M", "acceptance": "Specify 3-phase generator; transformer ≥98% efficient", "impact": "+10-15% electrical efficiency", "status": "Completed"},
    {"constraint": "Power factor correction capability", "insights": ["#25"], "priority": "M", "acceptance": "ELC includes capacitor bank or electronic correction", "impact": "Grid compatibility", "status": "Pending"},
    {"constraint": "Adaptive operation across load range", "insights": ["#19", "#30"], "priority": "M", "acceptance": "System maintains performance as flow varies ±50% from nominal", "impact": "Field reliability", "status": "In Progress"},
    {"constraint": "Optional grid interconnect architecture", "insights": ["#27"], "priority": "H", "acceptance": "System operates standalone; grid-tie optional via external inverter", "impact": "Distributed resilience", "status": "Completed"},
    {"constraint": "Mechanical governor backup", "insights": ["#20"], "priority": "L", "acceptance": "Optional mechanical backup for critical applications", "impact": "Extreme resilience", "status": "Pending"},
    {"constraint": "Wireless monitoring/control module", "insights": ["#29"], "priority": "L", "acceptance": "Architecture open for future wireless module integration", "impact": "Phase 5+ option", "status": "Pending"}
]

DIVISIONS = [
    "Engineering Division",
    "Funding Division", 
    "Partnership Division",
    "IP/Patent Division",
    "Research Division (EURA)",
    "Operations Division",
    "Quality Control Division"
]

def get_agent_status():
    # Mock agent statuses - in real implementation, check logs or running processes
    return {
        "Dashboard Agent": "Running",
        "Automation Agent": "Running", 
        "QC Agent": "Idle",
        "EURA Research": "Active",
        "Design Matrix Monitor": "Active"
    }

def get_system_health():
    return {
        "CPU Usage": "45%",
        "Memory Usage": "60%",
        "Disk Space": "85% free",
        "Network": "Connected",
        "Last Backup": "2 hours ago"
    }

def main():
    st.set_page_config(page_title="MicroHydro Matrix Monitor", page_icon="🌊", layout="wide")
    
    st.title("🌊 MicroHydro Matrix Monitor")
    st.markdown("**Real-time Enterprise Intelligence Platform for MicroHydro Operations**")
    
    # Sidebar
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Select View", ["Dashboard", "Design Matrix", "Site Optimization", "Divisions", "Agents", "System Health"])
    
    if page == "Dashboard":
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Active Agents", "5", "+2")
        with col2:
            st.metric("Design Constraints Met", "8/18", "+1")
        with col3:
            st.metric("System Uptime", "99.9%", "Stable")
        with col4:
            st.metric("Top Site Score", "0.65", "Mountain Stream B")
        
        st.subheader("Recent Activity")
        activity_df = pd.DataFrame({
            "Time": [datetime.now().strftime("%H:%M:%S") for _ in range(6)],
            "Event": ["Agent execution completed", "Design matrix updated", "EURA research synced", "QC check passed", "Site optimization run", "Backup completed"]
        })
        st.dataframe(activity_df)
        
    elif page == "Design Matrix":
        st.subheader("Design Input Matrix Monitor")
        
        df = pd.DataFrame(DESIGN_MATRIX)
        st.dataframe(df)
        
        # Priority breakdown
        priority_counts = df['priority'].value_counts()
        st.bar_chart(priority_counts)
        
        # Status breakdown
        status_counts = df['status'].value_counts()
        st.bar_chart(status_counts)
        
    elif page == "Site Optimization":
        st.subheader("Site Selection Optimization Engine")
        
        # Sample sites for demo
        candidate_sites = [
            {
                'name': 'River Bend Site A',
                'usgs_id': '12345678',
                'head_m': 25,
                'fish_passage_required': True,
                'wetland_nearby': False,
                'endangered_species': False,
                'permits_required': ['FERC', 'EPA'],
                'estimated_capex': 800000
            },
            {
                'name': 'Mountain Stream Site B',
                'usgs_id': '87654321',
                'head_m': 40,
                'fish_passage_required': False,
                'wetland_nearby': True,
                'endangered_species': False,
                'permits_required': ['State Water', 'Local'],
                'estimated_capex': 600000
            }
        ]
        
        engine = SiteOptimizationEngine()
        optimized_sites = engine.optimize_site_selection(candidate_sites)
        
        # Display results
        for site in optimized_sites:
            with st.expander(f"{site['name']} - Score: {site['viability_score']:.2f}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Potential Power", f"{site.get('potential_kw', 0):.1f} kW")
                    st.metric("Head Height", f"{site['head_m']} m")
                    st.metric("Avg Flow", f"{site.get('avg_flow_cfs', 0):.1f} cfs")
                with col2:
                    st.write("**Component Scores:**")
                    for k, v in site.get('component_scores', {}).items():
                        st.write(f"{k}: {v:.2f}")
                    st.write(f"**Permits Required:** {len(site.get('permits_required', []))}")
                    st.write(f"**Est. CAPEX:** ${site.get('estimated_capex', 0):,}")
        st.subheader("Department Divisions")
        
        for division in DIVISIONS:
            with st.expander(division):
                st.write(f"Status: Active")
                st.write(f"Last Update: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
                st.write("Key Metrics: TBD")
                
    elif page == "Agents":
        st.subheader("Agent Status Monitor")
        
        agent_status = get_agent_status()
        for agent, status in agent_status.items():
            color = "🟢" if status == "Running" or status == "Active" else "🟡" if status == "Idle" else "🔴"
            st.write(f"{color} {agent}: {status}")
            
    elif page == "System Health":
        st.subheader("System Health Dashboard")
        
        health = get_system_health()
        for metric, value in health.items():
            st.metric(metric, value)
    
    # Auto-refresh
    # time.sleep(5)
    # st.rerun()

if __name__ == "__main__":
    main()