"""
OPERATIONS DASHBOARD AGENT
Real-time monitoring, KPI tracking, alerts, and operational reporting.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def real_time_monitoring(systems_data):
    """
    Monitor all operational systems in real-time.
    Args: systems_data - description of systems to monitor
    """
    prompt = f"""You are an Operations Dashboard Monitoring System. Create a comprehensive real-time monitoring dashboard for: {systems_data}

GENERATE A DETAILED REAL-TIME OPERATIONS MONITORING DASHBOARD:

**DASHBOARD OVERVIEW:**
- Dashboard Name and Purpose
- Refresh Rate (real-time, 1-min, 5-min updates)
- Data Sources (SCADA, sensors, meters, databases)
- User Roles (who has access to what)

**SECTION 1: GENERATION MONITORING**

**Active Projects Status:**
| Project | Status | Capacity | Current Output | Capacity Factor | Uptime | Alerts |
|---------|--------|----------|----------------|-----------------|--------|--------|
| Site A  | Online | 100 kW   | 85 kW          | 85%             | 99.2%  | None   |
| Site B  | Online | 75 kW    | 60 kW          | 80%             | 98.5%  | Low Flow Warning |
| Site C  | Offline| 50 kW    | 0 kW           | 0%              | 0%     | ⚠️ MAINTENANCE |
[Create realistic table for 5-10 sites]

**Real-Time Metrics:**
- Total Installed Capacity: ___ kW
- Current Generation: ___ kW
- Fleet Capacity Factor: ___% (target >75%)
- Fleet Availability: ___% (target >95%)
- Today's Energy: ___ kWh
- Month-to-Date: ___ MWh
- Year-to-Date: ___ MWh

**SECTION 2: OPERATIONAL HEALTH**

**Critical Parameters (Color-coded: Green=Normal, Yellow=Warning, Red=Critical):**

**Site A - 100 kW Hydro:**
- Flow Rate: 150 GPM ✅ (target 120-200 GPM)
- Head Pressure: 42 psi ✅ (target 40-45 psi)
- Generator Temp: 155°F ✅ (normal <175°F)
- Bearing Vibration: 0.3 in/sec ✅ (alarm >0.5)
- Oil Pressure: 35 psi ✅ (normal 30-40 psi)
- Voltage: 480V ✅ (±5%)
- Frequency: 60.0 Hz ✅ (±0.1 Hz)

**Site B - 75 kW Hydro:**
- Flow Rate: 100 GPM ⚠️ (target 120-180 GPM) - LOW FLOW WARNING
- Head Pressure: 38 psi ✅
- Generator Temp: 168°F ⚠️ (warning >165°F)
- Bearing Vibration: 0.45 in/sec ⚠️ (approaching alarm threshold)
- Oil Pressure: 32 psi ✅
- Voltage: 475V ✅
- Frequency: 59.95 Hz ✅

[Create similar for each monitored site]

**SECTION 3: ALERT MANAGEMENT**

**Active Alerts (Last 24 Hours):**

| Time | Site | Severity | Alert | Status | Actions Taken |
|------|------|----------|-------|--------|---------------|
| 08:30 | Site B | ⚠️ Warning | Low Flow Detected | Open | Monitoring - seasonal variation expected |
| 07:15 | Site C | 🔴 Critical | Turbine Shutdown | Resolved | Maintenance team dispatched, fixed bearing issue |
| 22:00 | Site A | ⚠️ Warning | High Generator Temp | Resolved | Cooling system cleaned, normal operation restored |
[List 5-10 recent alerts]

**Alert Categories:**
- Critical (Immediate Action): ___ active
- Warning (Monitor Closely): ___ active
- Informational: ___ today
- Total Alerts (30 days): ___
- Mean Time to Acknowledge: ___ minutes (target <15 min)
- Mean Time to Resolve: ___ hours (target <4 hours)

**SECTION 4: PERFORMANCE METRICS**

**Today's Performance:**
- Peak Generation: ___ kW at [time]
- Minimum Generation: ___ kW at [time]
- Average Generation: ___ kW
- Energy Delivered: ___ kWh
- Revenue: $___ (at $0.10/kWh)
- CO2 Avoided: ___ lbs

**This Month:**
- Energy Target: ___ MWh
- Actual Generation: ___ MWh
- Target Achievement: ___% (on pace for ___)
- Capacity Factor: ___% (target >75%)
- Availability: ___% (target >95%)
- Forced Outage Hours: ___
- Planned Outage Hours: ___

**This Year:**
- Annual Target: ___ MWh
- YTD Generation: ___ MWh
- Projected Annual: ___ MWh (based on current pace)
- Target Achievement: ___% (on/ahead/behind schedule)

**SECTION 5: EQUIPMENT STATUS**

**Turbines:**
- Online: ___ units
- Offline (Scheduled Maintenance): ___ units
- Offline (Unscheduled): ___ units
- Total Runtime (Fleet): ___ hours
- Next Scheduled Service: [Site X - Date]

**Generators:**
- Operating Hours (by unit): [list]
- Maintenance Due: [Site Y in 50 hours]
- Last Inspection: [dates by site]

**Protective Relays:**
- All Functional: ✅ / ⚠️
- Last Test Date: [dates]
- Next Test Required: [dates]

**SECTION 6: FINANCIAL TRACKING**

**Revenue Dashboard:**
- Today: $___ 
- MTD: $___
- YTD: $___
- Projected Annual: $___
- Revenue by Site: [breakdown]

**Operating Costs (MTD):**
- Maintenance: $___
- Insurance: $___
- Property Lease: $___
- Repairs: $___
- Total OPEX: $___
- OPEX per kWh: $___ (target <$0.02/kWh)

**Profitability:**
- Net Income (MTD): $___
- Profit Margin: ___% (target >70%)
- EBITDA: $___

**SECTION 7: ENVIRONMENTAL COMPLIANCE**

**Water Management:**
- Bypass Flow (Site A): ___ GPM ✅ (required minimum: ___ GPM)
- Bypass Flow (Site B): ___ GPM ✅
- Stream Temperature (downstream): ___°F ✅ (limit <18°C/64°F)
- Dissolved Oxygen: ___ mg/L ✅ (target >6 mg/L)

**Fish Passage (if applicable):**
- Ladder Flow: ___ GPM ✅
- Velocity: ___ ft/sec ✅ (limit <4 ft/sec for salmon)
- Last Fish Count: [date] - ___ fish observed

**Compliance Status:**
- Water Rights Compliance: ✅ In Compliance
- Environmental Permit: ✅ In Compliance
- FERC/State Requirements: ✅ In Compliance
- Days Since Last Violation: ___

**SECTION 8: MAINTENANCE TRACKING**

**Scheduled Maintenance (Next 30 Days):**
| Date | Site | Task | Duration | Outage | Tech Assigned |
|------|------|------|----------|--------|---------------|
| Feb 5 | Site A | Quarterly Inspection | 4 hrs | Yes | Tech 1 |
| Feb 12 | Site B | Oil Change | 2 hrs | Yes | Tech 2 |
| Feb 20 | Site C | Bearing Replacement | 8 hrs | Yes | Tech 1 + Tech 3 |
[List upcoming maintenance]

**Maintenance Metrics:**
- Preventive Maintenance Completion: ___% (target >95%)
- Average PM Duration: ___ hours
- Overdue Maintenance Items: ___ (target = 0)
- Work Order Backlog: ___ items

**SECTION 9: WEATHER & HYDROLOGY**

**Current Conditions:**
- Precipitation (24hr): ___ inches
- Stream Flow (gauge): ___ CFS (normal for this date: ___ CFS)
- Snowpack (upstream): ___% of normal
- Reservoir Level (if applicable): ___ feet (% of capacity)

**7-Day Forecast:**
- Precipitation Expected: ___ inches
- Flow Projection: Increasing / Stable / Decreasing
- Generation Impact: ___% change expected
- Alerts: Spring runoff / Drought conditions / Normal

**SECTION 10: SYSTEM INTEGRATIONS**

**Data Sources Status:**
- SCADA System: ✅ Connected (last update: 5 seconds ago)
- Revenue Meters: ✅ All reporting
- Weather API: ✅ Connected
- USGS Stream Gauges: ✅ Connected
- Financial System: ✅ Synced
- Utility Billing: ✅ Connected

**SECTION 11: USER ACTIONS**

**Quick Actions:**
[ ] Acknowledge All Alerts
[ ] Export Daily Report
[ ] Schedule Maintenance
[ ] Contact Tech Support
[ ] View Historical Trends
[ ] Generate Financial Report

**Support:**
- Operations Hotline: [phone]
- Technical Support Email: [email]
- On-Call Engineer: [name, phone]

**RECOMMENDATIONS:**

1. **Immediate Actions:**
   - Investigate Site B low flow condition (seasonal? upstream issue?)
   - Monitor Site B generator temperature (trend increasing? cooling system?)
   - Schedule Site B bearing inspection (vibration approaching limit)

2. **Short-Term (This Week):**
   - Complete scheduled maintenance on [dates]
   - Review and update alert thresholds (reduce false alarms)
   - Conduct weekly ops meeting to review performance

3. **Medium-Term (This Month):**
   - Analyze capacity factor trends (opportunities for optimization?)
   - Review maintenance schedule (any adjustments needed?)
   - Financial review (on track to meet budget?)

4. **Dashboard Improvements:**
   - Add predictive analytics (forecast generation based on weather/hydrology)
   - Implement mobile app for field techs
   - Integrate drone inspection imagery
   - Add benchmarking against industry standards

**NOTES:**
- Dashboard should auto-refresh every 60 seconds for real-time data
- Historical data archive: [location]
- Export options: PDF, Excel, CSV, API
- Mobile responsive design for field access
- Role-based permissions (operator, manager, executive views)

This dashboard provides complete operational visibility, enabling proactive management, rapid issue resolution, and data-driven decision making."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def kpi_tracking(business_metrics):
    """
    Track key performance indicators across all operations.
    Args: business_metrics - description of KPIs to track
    """
    prompt = f"""You are a KPI Tracking and Analytics System. Create a comprehensive KPI tracking framework for: {business_metrics}

DEVELOP A COMPLETE KPI TRACKING SYSTEM:

**KPI FRAMEWORK OVERVIEW:**
- Measurement Period: Daily, Weekly, Monthly, Quarterly, Annual
- Data Collection Methods
- Reporting Frequency
- Stakeholders (who sees which KPIs)

**CATEGORY 1: GENERATION & PRODUCTION KPIs**

**Primary Metrics:**

1. **Capacity Factor**
   - Definition: (Actual Generation / Maximum Possible Generation) × 100%
   - Target: >75% (excellent), 60-75% (good), <60% (needs improvement)
   - Current: ___%
   - Trend: ↗ Improving / → Stable / ↘ Declining
   - Benchmark: Industry average 70-80% for run-of-river hydro
   - Analysis: [What's driving performance? Seasonal? Maintenance? Equipment?]

2. **Availability**
   - Definition: (Hours Available / Total Hours) × 100%
   - Target: >95% (excellent), 90-95% (acceptable), <90% (poor)
   - Current: ___%
   - Forced Outages: ___ hours (target <2% annually)
   - Planned Outages: ___ hours
   - MTBF (Mean Time Between Failures): ___ hours

3. **Energy Generation**
   - Daily Average: ___ kWh/day
   - Monthly Total: ___ MWh
   - YTD Total: ___ MWh
   - Annual Target: ___ MWh
   - Progress to Target: ___%
   - Variance from Forecast: +/- ___%

4. **Specific Generation**
   - kWh per kW installed (annual): ___ kWh/kW
   - Target: >6,500 kWh/kW/year (excellent for 75% CF)
   - This measures how effectively installed capacity is utilized

**CATEGORY 2: FINANCIAL KPIs**

**Revenue Metrics:**

5. **Revenue per kWh**
   - Current Rate: $___/kWh
   - Weighted Average (multiple revenue streams): $___/kWh
   - Target: >$0.08/kWh (good), >$0.12/kWh (excellent)
   - Revenue Sources: Net metering ___%, PPA ___%, RECs ___%

6. **Monthly Revenue**
   - Current Month: $___
   - Target: $___
   - Achievement: ___%
   - Annual Run-Rate: $___
   - Year-over-Year Growth: +/- ___%

7. **EBITDA Margin**
   - EBITDA: $___
   - Revenue: $___
   - Margin: ___%
   - Target: >75% (excellent), 60-75% (good), <60% (needs improvement)
   - Industry benchmark: 70-85% for hydro

**Cost Metrics:**

8. **OPEX per kWh**
   - Total OPEX: $___
   - Generation: ___ kWh
   - Cost per kWh: $___
   - Target: <$0.02/kWh (excellent), $0.02-0.04 (acceptable), >$0.04 (high)
   - Breakdown: Maintenance ___%, Insurance ___%, Lease ___%, Other ___%

9. **Maintenance Cost as % of Revenue**
   - Maintenance Spend: $___
   - Revenue: $___
   - Percentage: ___%
   - Target: <15% (excellent), 15-25% (acceptable), >25% (high)

10. **All-In Costs**
    - OPEX: $___
    - Debt Service: $___
    - Depreciation: $___
    - Total Cost per kWh: $___
    - Profitability: Revenue $___/kWh - Cost $___/kWh = $___ margin

**Return Metrics:**

11. **Cash-on-Cash Return**
    - Annual Cash Flow: $___
    - Equity Invested: $___
    - Return: ___%
    - Target: >12% (excellent), 8-12% (good), <8% (poor)

12. **Project IRR (to date)**
    - IRR: ___%
    - Target: >12% (excellent)
    - On track to meet proforma projections? Yes/No

**CATEGORY 3: OPERATIONAL EFFICIENCY KPIs**

**Reliability Metrics:**

13. **Equivalent Availability Factor (EAF)**
    - Definition: Accounts for both outages and derates
    - Current: ___%
    - Target: >95%
    - Best-in-class: >98%

14. **Mean Time Between Failures (MTBF)**
    - Current: ___ hours
    - Target: >8,760 hours (1 year)
    - Trend: Improving / Stable / Declining

15. **Mean Time to Repair (MTTR)**
    - Average: ___ hours
    - Target: <4 hours for minor issues, <24 hours for major
    - Fastest repair: ___ hours
    - Longest repair: ___ hours

**Maintenance Metrics:**

16. **Preventive Maintenance Compliance**
    - Scheduled PM Tasks: ___
    - Completed On-Time: ___
    - Compliance Rate: ___%
    - Target: >95%

17. **Reactive vs. Preventive Maintenance Ratio**
    - Reactive (unplanned): ___% 
    - Preventive (planned): ___%
    - Target: <20% reactive, >80% preventive (proactive = cost effective)

18. **Maintenance Cost per Operating Hour**
    - Total Maintenance Cost: $___
    - Total Operating Hours: ___
    - Cost per Hour: $___
    - Trend: Increasing / Stable / Decreasing

**CATEGORY 4: ENVIRONMENTAL & COMPLIANCE KPIs**

**Compliance Metrics:**

19. **Environmental Compliance Rate**
    - Permit Conditions: ___ total
    - In Compliance: ___
    - Rate: 100% (target)
    - Violations (12 months): ___ (target = 0)
    - Days Since Last Violation: ___

20. **Bypass Flow Compliance**
    - Required Minimum: ___ GPM
    - Actual (average): ___ GPM
    - Compliance: ___%
    - Violations: ___ incidents

21. **Water Quality Compliance**
    - Temperature Limit: <18°C (64°F)
    - Actual (max): ___°C
    - Dissolved Oxygen Target: >6 mg/L
    - Actual (avg): ___ mg/L
    - Compliance: ✅ / ⚠️

**Sustainability Metrics:**

22. **CO2 Emissions Avoided**
    - Annual Generation: ___ MWh
    - Grid Emission Factor: ___ lbs CO2/MWh (regional grid mix)
    - Total Avoided: ___ tons CO2
    - Equivalent: ___ cars off road for 1 year

23. **Renewable Energy Certificates (RECs)**
    - RECs Generated: ___ (1 per MWh)
    - RECs Sold: ___
    - Average Price: $___ per REC
    - Revenue: $___

**CATEGORY 5: SAFETY KPIs**

**Safety Metrics:**

24. **Total Recordable Incident Rate (TRIR)**
    - Incidents: ___ (target = 0)
    - Hours Worked: ___
    - TRIR: ___ per 200,000 hours worked
    - Industry benchmark: <2.0

25. **Days Since Last Incident**
    - Current: ___ days
    - Record: ___ days
    - Goal: Continuous improvement

26. **Safety Training Compliance**
    - Required Training Hours: ___
    - Completed: ___
    - Compliance: ___%
    - Target: 100%

**CATEGORY 6: PROJECT DEVELOPMENT KPIs** (For Growing Portfolio)

**Pipeline Metrics:**

27. **Sites in Development**
    - Identified: ___ sites
    - Feasibility Phase: ___ sites
    - Permitting Phase: ___ sites
    - Construction: ___ sites
    - Total Pipeline Capacity: ___ MW

28. **Permitting Success Rate**
    - Applications Submitted: ___
    - Approvals Received: ___
    - Success Rate: ___%
    - Average Timeline: ___ months

29. **Development Cost per kW**
    - Total Development Cost: $___
    - Capacity Developed: ___ kW
    - Cost per kW: $___/kW
    - Target: <$5,000/kW all-in CAPEX

**CATEGORY 7: CUSTOMER/STAKEHOLDER KPIs**

**Stakeholder Satisfaction:**

30. **Landowner Satisfaction**
    - Survey Score: ___ / 10
    - Issues Reported: ___
    - Resolution Rate: ___%
    - Target: >8/10 satisfaction

31. **Utility Relationship Score**
    - Interconnection Issues: ___ (target = 0)
    - Payment Timeliness: ___ days average
    - Communication Rating: ___ / 10

32. **Community Engagement**
    - Public Events: ___ per year
    - Site Tours: ___ visitors
    - Educational Outreach: ___ students
    - Media Coverage: ___ articles

**KPI DASHBOARD DESIGN:**

**Executive Dashboard (CEO/Board):**
- Capacity Factor (monthly)
- Revenue vs. Target
- EBITDA Margin
- Project IRR
- Safety (days without incident)
- Development pipeline

**Operations Dashboard (COO/Operations Manager):**
- Availability
- Generation vs. Forecast
- OPEX per kWh
- Maintenance compliance
- Active alerts
- Environmental compliance

**Financial Dashboard (CFO):**
- Revenue (monthly, YTD)
- EBITDA
- Cash flow
- OPEX breakdown
- Cost per kWh
- Accounts receivable aging

**Technical Dashboard (Engineering Manager):**
- Capacity factor by site
- Equipment performance
- MTBF/MTTR
- Maintenance schedule adherence
- Reliability metrics

**KPI REPORTING CADENCE:**

**Daily:**
- Generation (kWh)
- Availability (%)
- Active alerts
- Safety incidents

**Weekly:**
- Generation vs. forecast
- Maintenance completed
- Cost tracking
- Issues log

**Monthly:**
- All financial KPIs
- Capacity factor
- OPEX analysis
- Compliance status
- Board report package

**Quarterly:**
- Strategic KPIs (IRR, pipeline, growth)
- Trend analysis
- Benchmarking vs. industry
- Budget vs. actual review

**Annually:**
- Annual performance review
- Compensation tied to KPIs
- Strategic planning
- Asset valuation

**KPI IMPROVEMENT ACTIONS:**

**For Underperforming KPIs:**
1. Root cause analysis (5 Whys, fishbone diagram)
2. Set improvement target and timeline
3. Assign owner and resources
4. Weekly progress review
5. Document lessons learned

**For Meeting/Exceeding KPIs:**
1. Document best practices
2. Share across sites (if portfolio)
3. Benchmark externally
4. Set stretch goals

**KPI SOFTWARE/TOOLS:**

- Real-time data: SCADA system
- Analytics: Power BI, Tableau, Excel
- Maintenance: CMMS software
- Financial: QuickBooks, Xero
- Automated reporting: Python/R scripts
- Mobile access: Custom dashboard app

**RECOMMENDATIONS:**

1. Establish baseline for all KPIs (first 6 months)
2. Set realistic targets based on industry benchmarks
3. Review and adjust KPIs quarterly (are we measuring what matters?)
4. Tie compensation to key KPIs (alignment)
5. Automate data collection and reporting (reduce manual effort)
6. Benchmark against industry (how do we compare?)
7. Focus on 5-7 critical KPIs per role (avoid information overload)

This KPI framework enables data-driven management, continuous improvement, and accountability across the organization."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def alerts_management(alert_parameters):
    """
    Configure and manage operational alerts and notifications.
    Args: alert_parameters - alert conditions and response protocols
    """
    prompt = f"""You are an Alert Management and Notification System. Design a comprehensive alert management framework for: {alert_parameters}

CREATE A COMPLETE ALERT MANAGEMENT SYSTEM:

**ALERT SYSTEM ARCHITECTURE:**

**Alert Severity Levels:**
1. 🔴 **CRITICAL** - Immediate action required, potential revenue loss/safety issue
2. ⚠️ **WARNING** - Monitor closely, may escalate to critical
3. ℹ️ **INFORMATIONAL** - FYI only, no action needed
4. ✅ **CLEARED** - Previous alert resolved

**Alert Categories:**
- Equipment Performance
- Generation/Production
- Environmental/Compliance
- Safety
- Financial
- Maintenance
- Security
- Weather/Hydrology

**ALERT RULES ENGINE:**

**CATEGORY 1: CRITICAL EQUIPMENT ALERTS** (Immediate Response)

**Alert 1: Turbine Shutdown**
- Trigger: Power output drops to 0 kW while flow available
- Data Sources: SCADA, power meter
- Check Interval: Real-time (5 seconds)
- Notification: SMS + Email + Phone Call to on-call engineer
- Recipients: On-call tech (immediate), Operations Manager (immediate), CEO (if >4 hours)
- Auto-Actions: 
  * Log incident timestamp
  * Capture all parameters at time of shutdown
  * Check protective relay status
  * Initiate remote restart procedure (if safe)
- Response Protocol:
  1. Verify alert (check cameras, SCADA data)
  2. Attempt remote restart if protective relay did NOT trip
  3. If restart fails, dispatch tech (ETA < 2 hours)
  4. Update status every 30 minutes until resolved
- SLA: Tech on-site within 2 hours

**Alert 2: Generator Overheat**
- Trigger: Generator temperature >180°F (critical threshold)
- Warning Threshold: >165°F (gives advance notice)
- Check Interval: Every 60 seconds
- Notification: SMS + Email + Dashboard Pop-up
- Recipients: On-call tech, Operations Manager
- Auto-Actions:
  * Reduce load by 20% (if possible)
  * Increase cooling system (if available)
  * Log temperature trend (last 4 hours)
- Response Protocol:
  1. Verify cooling system operating
  2. Check for obstructions (debris, dirt)
  3. Monitor temperature trend (increasing? stable? decreasing?)
  4. If >190°F, initiate controlled shutdown to prevent damage
  5. Schedule inspection within 24 hours
- SLA: Temperature <175°F within 2 hours or shutdown

**Alert 3: Low Oil Pressure**
- Trigger: Oil pressure <25 psi (critical), <28 psi (warning)
- Normal Range: 30-40 psi
- Check Interval: Every 30 seconds
- Notification: SMS + Email
- Auto-Actions:
  * If <20 psi, automatic shutdown (prevent bearing damage)
  * Log oil pressure history
  * Check oil level sensor
- Response Protocol:
  1. Check oil level (low? leak?)
  2. Inspect for leaks (visual inspection)
  3. Check oil filter (clogged?)
  4. Check oil pump (failed?)
  5. Do NOT restart until pressure >30 psi
- SLA: Diagnose cause within 4 hours

**Alert 4: High Vibration**
- Trigger: Vibration >0.5 in/sec (critical), >0.4 in/sec (warning)
- Normal Range: <0.3 in/sec
- Check Interval: Continuous monitoring
- Notification: SMS + Email
- Auto-Actions:
  * If >0.7 in/sec, automatic shutdown (bearing failure imminent)
  * Capture vibration spectrum (frequency analysis)
  * Log trend (sudden? gradual?)
- Response Protocol:
  1. Analyze vibration spectrum (bearing? imbalance? misalignment?)
  2. If sudden, shutdown immediately (bearing failure?)
  3. If gradual, schedule inspection within 48 hours
  4. Perform vibration analysis (handheld analyzer)
  5. Replace bearings if needed
- SLA: Inspection within 48 hours, replacement within 1 week

**Alert 5: Electrical Fault**
- Trigger: Protective relay trip (overvoltage, undervoltage, frequency, ground fault)
- Check Interval: Real-time
- Notification: SMS + Email + Phone Call
- Recipients: On-call tech, Operations Manager, Utility (if grid issue)
- Auto-Actions:
  * Log fault type and timestamp
  * Capture waveform data (if available)
  * Do NOT auto-restart (investigate cause first)
- Response Protocol:
  1. Identify fault type (what relay tripped?)
  2. Check for external causes (grid disturbance? lightning?)
  3. Inspect equipment (damage? burned components?)
  4. Reset relay only after cause identified and corrected
  5. Monitor closely after restart (recurrence?)
- SLA: Cause identified within 4 hours

**CATEGORY 2: GENERATION/PRODUCTION ALERTS**

**Alert 6: Low Generation**
- Trigger: Power output <50% of expected (based on flow/head)
- Check Interval: Every 5 minutes
- Notification: Email + Dashboard Alert
- Recipients: Operations Manager
- Auto-Actions:
  * Check flow rate (inadequate water?)
  * Check head pressure (intake clog? penstock leak?)
  * Compare to historical performance (degradation?)
- Response Protocol:
  1. Verify flow and head measurements
  2. Inspect intake (debris screen clogged?)
  3. Check penstock (air lock? leak?)
  4. Inspect turbine (nozzle wear? runner damage?)
  5. Schedule maintenance if performance degraded
- SLA: Investigate within 24 hours

**Alert 7: Zero Generation During Normal Flow**
- Trigger: Power = 0 kW but stream flow >minimum threshold
- Check Interval: Every 15 minutes
- Notification: SMS + Email
- Auto-Actions:
  * Check if shutdown was manual or automatic
  * Verify grid connection (interconnection issue?)
  * Log downtime start
- Response Protocol:
  1. Check for manual shutdown (maintenance? testing?)
  2. Check grid connection (utility outage? breaker open?)
  3. Check turbine (jammed? frozen? debris?)
  4. Check generator (offline? tripped?)
  5. Dispatch tech if not manual shutdown
- SLA: Restart within 4 hours (if safe)

**Alert 8: Capacity Factor Below Target**
- Trigger: Monthly capacity factor <70% (below target)
- Check Interval: Daily calculation
- Notification: Email + Monthly Report
- Recipients: Operations Manager, CEO
- Auto-Actions:
  * Analyze downtime log (what caused low CF?)
  * Compare to previous months (trend? seasonal?)
  * Identify improvement opportunities
- Response Protocol:
  1. Categorize downtime (forced outage? planned maintenance? low flow?)
  2. Analyze root causes (equipment reliability? hydrology? operations?)
  3. Develop improvement plan
  4. Set target for next month
- SLA: Improvement plan within 30 days

**CATEGORY 3: ENVIRONMENTAL/COMPLIANCE ALERTS**

**Alert 9: Bypass Flow Below Minimum**
- Trigger: Bypass flow <required minimum (e.g., <10 GPM if 10 GPM required)
- Check Interval: Every 15 minutes
- Notification: SMS + Email + Regulatory Report
- Recipients: Operations Manager, Environmental Compliance Officer
- Auto-Actions:
  * Reduce water intake (increase bypass)
  * Log violation (duration, severity)
  * Capture data for regulatory report
- Response Protocol:
  1. Verify bypass flow sensor accuracy
  2. Adjust intake gate to increase bypass
  3. Investigate cause (sensor failure? operator error? design issue?)
  4. Report to regulatory agency (within 24 hours per permit)
  5. Implement corrective actions
- SLA: Restore compliance within 1 hour, report within 24 hours

**Alert 10: Stream Temperature Exceedance**
- Trigger: Downstream temperature >18°C (64°F) limit
- Check Interval: Every 30 minutes during warm months
- Notification: Email + SMS (if >0.5°C over limit)
- Recipients: Environmental Compliance Officer
- Auto-Actions:
  * Log temperature and conditions
  * Check if project-caused or ambient
  * Increase bypass flow (if reduces temperature)
- Response Protocol:
  1. Verify temperature sensor
  2. Compare to upstream temperature (project impact?)
  3. Check bypass flow (adequate?)
  4. If project-caused, implement mitigation (increase bypass, reduce intake)
  5. Report if required by permit
- SLA: Mitigation within 2 hours, report within 24 hours

**Alert 11: Fish Passage Issue**
- Trigger: Fish ladder flow <required OR velocity >limit
- Check Interval: Every hour during migration season
- Notification: Email
- Recipients: Environmental Compliance Officer
- Auto-Actions:
  * Log conditions
  * Adjust ladder flow valve
  * Capture camera footage (if available)
- Response Protocol:
  1. Verify ladder flow rate
  2. Adjust attraction flow (5-10% of river flow)
  3. Inspect ladder (debris? damage?)
  4. Monitor fish use (video, visual observation)
  5. Report to fisheries agency if required
- SLA: Restore proper operation within 4 hours

**CATEGORY 4: SAFETY ALERTS**

**Alert 12: Personnel Safety**
- Trigger: Emergency button pressed OR motion detected after-hours OR safety sensor tripped
- Check Interval: Real-time
- Notification: SMS + Phone Call + 911 (if emergency button)
- Recipients: On-call tech, Operations Manager, Emergency Services (if warranted)
- Auto-Actions:
  * Log incident
  * Activate site alarm (if intruder)
  * Check cameras (if available)
  * Shutdown equipment (if safety risk)
- Response Protocol:
  1. Contact person on-site (if known)
  2. Dispatch emergency services if no response
  3. Send tech to investigate (with backup)
  4. Document incident
  5. Review safety procedures
- SLA: Response within 15 minutes

**CATEGORY 5: FINANCIAL ALERTS**

**Alert 13: Revenue Below Forecast**
- Trigger: Monthly revenue <85% of forecast
- Check Interval: Daily
- Notification: Email + Monthly Report
- Recipients: CFO, CEO
- Auto-Actions:
  * Analyze generation vs. forecast
  * Check electricity rates (changed?)
  * Review invoice status (payment delay?)
- Response Protocol:
  1. Determine cause (low generation? lower rates? billing issue?)
  2. Update financial forecast
  3. Implement corrective actions (improve generation, renegotiate PPA, etc.)
- SLA: Analysis within 1 week

**Alert 14: OPEX Overrun**
- Trigger: Monthly OPEX >125% of budget
- Check Interval: Weekly
- Notification: Email
- Recipients: Operations Manager, CFO
- Auto-Actions:
  * Generate expense report
  * Identify largest variances
- Response Protocol:
  1. Categorize overrun (maintenance? repairs? unexpected costs?)
  2. Determine if one-time or recurring
  3. Adjust budget or reduce costs
  4. Approve additional spending or defer non-critical items
- SLA: Budget review within 2 weeks

**ALERT NOTIFICATION MATRIX:**

| Alert Type | Critical | Warning | Info | SMS | Email | Call | Dashboard |
|------------|----------|---------|------|-----|-------|------|-----------|
| Turbine Shutdown | ✅ | - | - | ✅ | ✅ | ✅ | ✅ |
| Generator Overheat | ✅ | ✅ | - | ✅ | ✅ | ⚠️ | ✅ |
| Low Oil Pressure | ✅ | ✅ | - | ✅ | ✅ | - | ✅ |
| High Vibration | ✅ | ✅ | - | ✅ | ✅ | - | ✅ |
| Electrical Fault | ✅ | - | - | ✅ | ✅ | ✅ | ✅ |
| Low Generation | - | ✅ | - | - | ✅ | - | ✅ |
| Compliance Issue | ✅ | ✅ | - | ✅ | ✅ | - | ✅ |
| Safety Emergency | ✅ | - | - | ✅ | ✅ | ✅ | ✅ |
| Financial Variance | - | - | ✅ | - | ✅ | - | ✅ |

**ALERT ESCALATION PROCEDURES:**

**Level 1: On-Call Technician** (Initial Response - 0-2 hours)
- Receives all critical alerts immediately
- Responds within 30 minutes (acknowledge alert)
- On-site within 2 hours (if required)
- Authority to shutdown equipment if safety concern

**Level 2: Operations Manager** (If Unresolved - 2-4 hours)
- Escalates if tech hasn't resolved within 2 hours
- Can authorize overtime, emergency repairs
- Updates stakeholders (CEO, landowner, utility)

**Level 3: CEO/Executive** (Major Issues - >4 hours)
- Escalates if outage >4 hours or major safety/compliance issue
- Authorizes major expenses
- Handles regulatory/media communication

**ALERT REPORTING:**

**Daily Alert Summary:** (Sent every morning at 7 AM)
- Alerts in last 24 hours
- Critical alerts still active
- Top 3 issues requiring attention
- Yesterday's performance summary

**Weekly Alert Report:** (Sent Monday mornings)
- Total alerts by category
- Response time metrics (average time to acknowledge, time to resolve)
- Most frequent alerts (opportunities for prevention?)
- Alert trends (increasing? decreasing?)

**Monthly Alert Analysis:** (Executive Summary)
- Alert volume trends
- Impact on availability/generation
- Root cause analysis of recurring alerts
- Recommended improvements (alert thresholds, equipment upgrades, training)

**ALERT SYSTEM BEST PRACTICES:**

1. **Minimize False Alarms:**
   - Set appropriate thresholds (not too sensitive)
   - Use rate-of-change alerts (sudden change more important than absolute value)
   - Implement alarm delays (transient vs. persistent conditions)
   - Review and adjust thresholds quarterly

2. **Prevent Alert Fatigue:**
   - Limit to truly important alerts (don't cry wolf)
   - Use severity levels appropriately
   - Consolidate related alerts (don't send 5 alerts for same issue)
   - Auto-clear alerts when condition returns to normal

3. **Ensure Response:**
   - Require acknowledgement (did someone see it?)
   - Track response times (are SLAs being met?)
   - Escalate if no response (don't let alerts go ignored)
   - Test alert system monthly (does it work? do people respond?)

4. **Continuous Improvement:**
   - Review alerts quarterly (are thresholds right?)
   - Analyze recurring alerts (can we prevent them?)
   - Update response procedures (lessons learned?)
   - Train staff (do they know what to do?)

**ALERT TECHNOLOGY STACK:**

- Alert Engine: SCADA system, custom Python scripts
- Notification Platform: Twilio (SMS), SendGrid (email), PagerDuty
- Monitoring: Datadog, Grafana, custom dashboards
- Escalation: PagerDuty, VictorOps
- Documentation: Wiki, Standard Operating Procedures

This comprehensive alert management system ensures rapid response to issues, minimizes downtime, maintains compliance, and protects assets."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def reporting(report_requirements):
    """
    Generate operational reports for stakeholders.
    Args: report_requirements - report type, frequency, recipients
    """
    prompt = f"""You are an Operational Reporting System. Create comprehensive reporting framework for: {report_requirements}

DESIGN A COMPLETE OPERATIONAL REPORTING SYSTEM:

**REPORTING FRAMEWORK OVERVIEW:**

**Report Types:**
1. Daily Operations Report (Operations team)
2. Weekly Performance Summary (Management)
3. Monthly Executive Dashboard (C-Suite/Board)
4. Quarterly Business Review (Investors/Board)
5. Annual Performance Report (All stakeholders)
6. Incident Reports (As needed)
7. Compliance Reports (Regulatory agencies)

**Report Distribution:**
- Automated generation and distribution
- Role-based access (who sees what)
- Secure portal for sensitive data
- Archive for historical reference

---

**REPORT 1: DAILY OPERATIONS REPORT**

**Audience:** Operations Manager, Site Technicians, On-Call Engineer
**Frequency:** Every morning at 7:00 AM
**Delivery:** Email + Dashboard

**DAILY OPERATIONS REPORT - [Date]**

**EXECUTIVE SUMMARY:**
- Yesterday's Generation: ___ kWh (___% of forecast)
- Fleet Capacity Factor (yesterday): ___%
- Fleet Availability: ___%
- Critical Alerts: ___ (describe if any)
- Maintenance Activities: ___ (list)
- Revenue (yesterday): $___ 

**GENERATION PERFORMANCE:**

| Site | Capacity | Generation (kWh) | CF (%) | Avail (%) | Status | Notes |
|------|----------|------------------|--------|-----------|--------|-------|
| Site A | 100 kW | 1,800 | 75% | 100% | Online | Normal ops |
| Site B | 75 kW | 0 | 0% | 0% | Offline | Scheduled maintenance |
| Site C | 50 kW | 900 | 75% | 100% | Online | Normal ops |
| TOTAL | 225 kW | 2,700 | 50% | 67% | - | - |

**ALERT SUMMARY (Last 24 Hours):**
- Critical: ___ (describe each)
- Warning: ___ (top 3 listed)
- Informational: ___ 
- All Cleared: ✅ / ⚠️ Open alerts remain

**WEATHER & HYDROLOGY:**
- Precipitation (24hr): ___ inches
- Stream Flow: ___ CFS (___% of normal)
- Today's Forecast: [conditions, impact on generation]

**MAINTENANCE ACTIVITIES COMPLETED:**
1. [Site A - Oil change - 2 hours - Completed - Tech 1]
2. [Site C - Monthly inspection - 1 hour - Completed - Tech 2]

**SCHEDULED FOR TODAY:**
1. [Site B - Continue scheduled maintenance - 4 hours - Tech 1]
2. [Site A - Quarterly electrical testing - 2 hours - Tech 3]

**ACTION ITEMS:**
- [ ] Complete Site B maintenance and return to service (ETA 3 PM)
- [ ] Monitor Site A generator temperature (trending up yesterday)
- [ ] Schedule bearing replacement for Site C (vibration increasing)

**COMPLIANCE STATUS:**
- Environmental: ✅ In Compliance
- Safety: ✅ No incidents
- Water Rights: ✅ Bypass flows adequate

**NOTES:**
[Any notable events, issues, or observations]

**Prepared by:** [Automated System / Operations Manager]
**Next Report:** Tomorrow 7:00 AM

---

**REPORT 2: WEEKLY PERFORMANCE SUMMARY**

**Audience:** Operations Manager, Engineering Manager, CFO, CEO
**Frequency:** Every Monday morning
**Delivery:** Email + Dashboard + PDF

**WEEKLY PERFORMANCE SUMMARY - Week of [Date]**

**HIGHLIGHTS:**
- ✅ Strong generation: 18,900 kWh (95% of forecast)
- ⚠️ Site B offline for 16 hours (scheduled maintenance)
- ✅ No environmental compliance issues
- ⚠️ Site C vibration trending up - bearing replacement scheduled

**GENERATION PERFORMANCE:**

**Weekly Totals:**
- Total Generation: 18,900 kWh
- Forecast: 19,900 kWh
- Achievement: 95%
- Fleet Capacity Factor: 72% (target >75%)
- Fleet Availability: 92% (target >95%)

**By Site:**
| Site | Capacity | Gen (kWh) | CF (%) | Avail (%) | Trend | YTD CF (%) |
|------|----------|-----------|--------|-----------|-------|------------|
| Site A | 100 kW | 12,600 | 75% | 100% | → | 76% |
| Site B | 75 kW | 3,600 | 48% | 90% | ↘ | 74% |
| Site C | 50 kW | 2,700 | 45% | 75% | ↘ | 73% |

**OPERATIONAL HIGHLIGHTS:**

**Availability Analysis:**
- Planned Outages: 16 hours (Site B maintenance)
- Unplanned Outages: 12 hours (Site C vibration issue)
- Total Downtime: 28 hours
- Availability Impact: -8% from target

**Top Alerts (This Week):**
1. Site C - High vibration (⚠️ Warning - bearing replacement scheduled)
2. Site A - Generator temp spike (✅ Resolved - cooling system cleaned)
3. Site B - Scheduled maintenance (✅ Completed - back online)

**MAINTENANCE SUMMARY:**

**Completed:**
- Site B quarterly maintenance (16 hours, $2,500)
- Site A cooling system cleaning (2 hours, $200)
- All sites monthly inspections (6 hours total)

**Scheduled Next Week:**
- Site C bearing replacement (8 hours, $3,500)
- Site A electrical testing (2 hours, $500)

**FINANCIAL SUMMARY:**

**Revenue:**
- Generation: 18,900 kWh
- Rate: $0.10/kWh
- Revenue: $1,890
- Monthly Pace: $8,100 (target $9,000)

**OPEX (This Week):**
- Maintenance: $2,700
- Labor: $1,200
- Other: $300
- Total: $4,200

**ENVIRONMENTAL & COMPLIANCE:**
- Bypass Flows: ✅ All sites compliant
- Water Quality: ✅ All parameters within limits
- Permit Compliance: ✅ 100%
- Incidents: 0

**SAFETY:**
- Incidents: 0
- Near Misses: 0
- Safety Training: 2 hours (electrical safety refresher)
- Days Since Last Incident: 180

**WEATHER & HYDROLOGY:**
- Precipitation: 1.2 inches (above normal)
- Stream Flows: 115% of normal (good for generation)
- Forecast: Normal precipitation next week

**ACTION ITEMS FOR NEXT WEEK:**
1. Complete Site C bearing replacement
2. Monitor Site B performance post-maintenance
3. Analyze Site C vibration trend (other issues?)
4. Review monthly capacity factor (how to improve?)

**KEY METRICS DASHBOARD:**
[Visual charts showing weekly trends]
- Generation (kWh/day)
- Capacity Factor (%)
- Availability (%)
- Revenue ($/day)

**Prepared by:** Operations Manager
**Distribution:** Management Team
**Next Report:** Next Monday

---

**REPORT 3: MONTHLY EXECUTIVE DASHBOARD**

**Audience:** CEO, CFO, COO, Board of Directors
**Frequency:** First Monday of each month
**Delivery:** Email + PDF + Board Portal

**MONTHLY EXECUTIVE DASHBOARD - [Month, Year]**

**EXECUTIVE SUMMARY:**

**Performance vs. Target:**
- ✅ Generation: 85,000 kWh (95% of target)
- ⚠️ Capacity Factor: 73% (target 75%)
- ✅ Revenue: $8,500 (target $8,000)
- ✅ OPEX: $1,200 (budget $1,500)
- ✅ Net Income: $7,300 (86% margin)

**Key Highlights:**
- Strong financial performance (profit margin >85%)
- Capacity factor slightly below target (weather/maintenance)
- No safety or compliance issues
- Site C needs attention (equipment aging)

**SECTION 1: GENERATION & PRODUCTION**

**Monthly Performance:**
- Total Generation: 85,000 kWh
- Target: 90,000 kWh
- Achievement: 94%
- Fleet Capacity Factor: 73%
- Fleet Availability: 93%

**By Site Performance:**
| Site | Capacity | Gen (MWh) | CF (%) | Target | Variance | Trend (3mo) |
|------|----------|-----------|--------|--------|----------|-------------|
| Site A | 100 kW | 55 | 76% | 75% | +1% | ↗ |
| Site B | 75 kW | 20 | 74% | 75% | -1% | → |
| Site C | 50 kW | 10 | 69% | 75% | -6% | ↘ |

**Downtime Analysis:**
- Planned Outages: 32 hours (quarterly maintenance)
- Unplanned Outages: 24 hours (equipment issues)
- Total Downtime: 56 hours (7% of month)

**Year-to-Date:**
- YTD Generation: 255 MWh
- Annual Target: 1,200 MWh
- Pace: On track for 1,020 MWh (85% of target)

**SECTION 2: FINANCIAL PERFORMANCE**

**Revenue:**
- Energy Sales: $8,000 (85 MWh @ $0.094/kWh weighted avg)
- REC Sales: $500 (85 RECs @ $5.88 each)
- Total Revenue: $8,500
- Monthly Target: $8,000
- Variance: +6%

**Operating Expenses:**
- Maintenance: $600
- Insurance: $300
- Property Lease: $200
- Utilities: $50
- Administrative: $50
- Total OPEX: $1,200
- Budget: $1,500
- Variance: -20% (favorable)

**Profitability:**
- Revenue: $8,500
- OPEX: $1,200
- EBITDA: $7,300
- Margin: 86%
- Target Margin: >75%

**Year-to-Date Financial:**
- YTD Revenue: $25,500
- YTD OPEX: $3,600
- YTD EBITDA: $21,900
- Annual Forecast: $102,000 revenue, $90,000 EBITDA

**SECTION 3: KEY PERFORMANCE INDICATORS**

**Operational KPIs:**
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Capacity Factor | 73% | 75% | ⚠️ |
| Availability | 93% | 95% | ⚠️ |
| OPEX per kWh | $0.014 | <$0.020 | ✅ |
| EBITDA Margin | 86% | >75% | ✅ |
| MTBF | 6,500 hr | >8,760 | ⚠️ |

**Financial KPIs:**
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Revenue/kWh | $0.10 | >$0.08 | ✅ |
| Cash-on-Cash | 11% | >10% | ✅ |
| Project IRR | 13% | >12% | ✅ |

**SECTION 4: OPERATIONAL EXCELLENCE**

**Reliability:**
- Equivalent Availability: 93%
- Forced Outage Rate: 3% (target <2%)
- Planned Outage Rate: 4%

**Maintenance:**
- PM Completion: 100% (all scheduled maintenance completed on time)
- Reactive/Preventive Ratio: 25/75 (target <20/80)
- Maintenance Cost: $600 (within budget)

**SECTION 5: COMPLIANCE & SAFETY**

**Environmental:**
- Permit Compliance: 100%
- Bypass Flow Compliance: 100%
- Water Quality: All parameters within limits
- Violations: 0

**Safety:**
- Incidents: 0
- TRIR: 0.0
- Days Since Last Incident: 210
- Safety Training Hours: 8

**SECTION 6: STRATEGIC INITIATIVES**

**Current Projects:**
1. Site C Equipment Upgrade (in progress, complete next month)
2. SCADA System Enhancement (planning phase)
3. Site D Development (permitting phase)

**Pipeline:**
- Sites in Development: 3
- Total Pipeline Capacity: 150 kW
- Expected Completion: 18-24 months

**SECTION 7: RISKS & MITIGATION**

**Top Risks:**
1. **Site C Equipment Aging** - Increasing maintenance needs
   - Mitigation: Upgrade plan in progress, budget approved
2. **Below-Target Capacity Factor** - Weather + maintenance
   - Mitigation: Optimize maintenance scheduling, monitor weather forecasts
3. **Permit Renewal (Site A)** - Due in 6 months
   - Mitigation: Application preparation underway

**SECTION 8: OUTLOOK & RECOMMENDATIONS**

**Next Month Forecast:**
- Generation: 90,000 kWh (normal weather, Site C improved)
- Revenue: $9,000
- OPEX: $1,400
- EBITDA: $7,600

**Recommendations:**
1. Approve Site C equipment upgrade ($15k investment, payback 18 months)
2. Continue focus on preventive maintenance (reduce unplanned outages)
3. Explore additional revenue opportunities (REC price optimization)
4. Begin permit renewal process for Site A

**Prepared by:** CFO/COO
**Approved by:** CEO
**Distribution:** Board of Directors, Investors
**Next Report:** First Monday next month

---

**REPORT 4: QUARTERLY BUSINESS REVIEW (QBR)**

**Audience:** Board of Directors, Investors, Senior Management
**Frequency:** Quarterly (15 days after quarter end)
**Delivery:** In-person presentation + detailed report package

[Create 25-30 page comprehensive report covering:]

**Section 1: Executive Summary** (2 pages)
- Quarter highlights
- Financial summary
- Operational performance
- Strategic progress
- Outlook

**Section 2: Financial Performance** (5 pages)
- Income statement (quarterly + YTD)
- Cash flow statement
- Balance sheet highlights
- KPI dashboard
- Budget variance analysis
- Forecast update

**Section 3: Operational Performance** (5 pages)
- Generation analysis (by site, trends)
- Availability and reliability
- Maintenance summary
- Equipment health
- Efficiency improvements

**Section 4: Strategic Initiatives** (5 pages)
- Project development pipeline
- Capital projects status
- Technology upgrades
- Market expansion

**Section 5: Risk Management** (3 pages)
- Risk register review
- Mitigation progress
- New risks identified
- Insurance and compliance

**Section 6: Stakeholder Relations** (2 pages)
- Landowner relations
- Utility coordination
- Community engagement
- Regulatory updates

**Section 7: Outlook & Guidance** (3 pages)
- Next quarter forecast
- Annual projection update
- Strategic priorities
- Capital allocation

**Appendices:**
- Detailed financial statements
- Site-by-site performance data
- Compliance certifications
- Organizational chart

---

**REPORT 5: ANNUAL PERFORMANCE REPORT**

**Audience:** All stakeholders (Board, Investors, Lenders, Regulators)
**Frequency:** Annually (60 days after year-end)
**Delivery:** Professional bound report + PDF + Executive presentation

[Create comprehensive 50+ page annual report covering full year performance, strategy, and outlook]

---

**REPORT 6: INCIDENT REPORT**

**Audience:** Management, Safety Officer, Insurance (if claim)
**Frequency:** As needed (within 24 hours of incident)
**Delivery:** Email + formal documentation

**INCIDENT REPORT - [Date, Time]**

**Incident Summary:**
- Date/Time: [timestamp]
- Site: [location]
- Type: Equipment Failure / Safety / Environmental / Other
- Severity: Minor / Moderate / Severe / Critical
- Injuries: Yes/No
- Property Damage: Yes/No ($___ estimated)
- Environmental Impact: Yes/No

**Description:**
[Detailed narrative of what happened]

**Root Cause Analysis:**
[5 Whys, Fishbone diagram, investigation findings]

**Corrective Actions:**
1. [Immediate actions taken]
2. [Short-term corrective actions]
3. [Long-term preventive actions]

**Lessons Learned:**
[What can we learn to prevent recurrence?]

**Follow-up:**
- Action Item Owner: [name]
- Completion Date: [date]
- Verification: [how will we verify effectiveness?]

---

**REPORT 7: COMPLIANCE REPORTS**

**Audience:** Regulatory agencies (FERC, State, EPA, etc.)
**Frequency:** As required by permits (monthly, quarterly, annual)
**Delivery:** Formal submission per permit requirements

**Annual Environmental Compliance Report:**
- Generation summary
- Bypass flow compliance
- Water quality monitoring results
- Fish passage effectiveness (if applicable)
- Incident log (any violations)
- Photos and documentation
- Certification statement

---

**REPORTING BEST PRACTICES:**

1. **Automate Where Possible:**
   - Daily/weekly reports fully automated
   - Monthly reports semi-automated (manual review)
   - Quarterly/annual reports manual but template-driven

2. **Visualize Data:**
   - Charts and graphs (trends, comparisons)
   - Color-coding (green/yellow/red status)
   - Dashboards (interactive for digital delivery)

3. **Tailor to Audience:**
   - Executives: High-level summary, key metrics, strategic
   - Operations: Detailed technical data, action items
   - Investors: Financial focus, returns, risks
   - Regulators: Compliance data, certifications

4. **Timeliness:**
   - Daily reports: 7 AM
   - Weekly reports: Monday AM
   - Monthly reports: Within 5 business days
   - Quarterly reports: Within 15 days
   - Annual reports: Within 60 days

5. **Archive and Access:**
   - Maintain report library (5+ years)
   - Searchable database
   - Secure access (role-based permissions)

This comprehensive reporting framework ensures all stakeholders have the information they need, when they need it, in the format that's most useful."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


# CLI Interface
if __name__ == "__main__":
    print("\n✅ Operations Dashboard Agent initialized (Groq - FREE)\n")
    
    import sys
    if len(sys.argv) < 2:
        print("OPERATIONS DASHBOARD AGENT")
        print("\nCommands:")
        print("  monitor   - Real-time system monitoring")
        print("  kpi       - Track key performance indicators")
        print("  alerts    - Configure alert management")
        print("  report    - Generate operational reports")
        print("\nUsage: python operations_dashboard.py <command> <parameters>")
        print("Example: python operations_dashboard.py monitor '3 micro-hydro sites'")
        sys.exit(0)
    
    command = sys.argv[1].lower()
    params = sys.argv[2] if len(sys.argv) > 2 else "micro-hydro operations"
    
    if command == "monitor":
        print(real_time_monitoring(params))
    elif command == "kpi":
        print(kpi_tracking(params))
    elif command == "alerts":
        print(alerts_management(params))
    elif command == "report":
        print(reporting(params))
    else:
        print(f"❌ Unknown command: {command}")
        print("Available: monitor, kpi, alerts, report")
