"""
PROCESS AUTOMATION AGENT
Workflow optimization, task automation, efficiency analysis, and continuous improvement.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def workflow_optimization(current_workflow):
    """
    Analyze and optimize business workflows for efficiency.
    Args: current_workflow - description of current process or workflow
    """
    prompt = f"""You are a Workflow Optimization and Process Engineering System. Analyze and optimize this workflow: {current_workflow}

PERFORM COMPREHENSIVE WORKFLOW ANALYSIS AND OPTIMIZATION:

**CURRENT STATE ANALYSIS:**

**Step 1: Map Current Workflow**

Document the current process end-to-end:
- Process Name: [Name of the workflow]
- Owner: [Who is responsible?]
- Frequency: [How often does this happen? Daily/Weekly/Monthly/Ad-hoc]
- Stakeholders: [Who is involved? Who depends on this?]

**Current Workflow Steps:**

| Step # | Activity | Owner | Time | Systems/Tools | Dependencies | Pain Points |
|--------|----------|-------|------|---------------|--------------|-------------|
| 1 | [Activity description] | [Person/Role] | 30 min | Excel | None | Manual data entry |
| 2 | [Activity description] | [Person/Role] | 15 min | Email | Step 1 | Waiting for approval |
| 3 | [Activity description] | [Person/Role] | 45 min | Database | Step 2 | Complex lookup |
[Create detailed workflow map with 5-15 steps]

**Current State Metrics:**
- Total Process Time: ___ hours (elapsed time start to finish)
- Total Touch Time: ___ hours (actual work time)
- Wait Time: ___ hours (delays between steps)
- Number of Handoffs: ___ (transfers between people/systems)
- Error Rate: ___% (defects, rework needed)
- Cost per Instance: $___ (labor + systems)
- Volume: ___ instances per [period]

**Step 2: Identify Waste (Lean Principles)**

**1. Defects (Errors requiring rework):**
- [Describe errors that occur]
- Frequency: ___ per instance
- Impact: Time to fix ___ hours, Cost $___
- Root cause: [Why do these errors happen?]

**2. Overproduction (Doing more than needed):**
- [Describe unnecessary work]
- Example: Generating reports no one reads
- Impact: ___ hours wasted per [period]

**3. Waiting (Idle time):**
- [Where do things sit idle?]
- Example: Waiting for approvals, waiting for data
- Total wait time: ___ hours (___ % of total process time)

**4. Non-utilized Talent (People doing low-value work):**
- [Skilled people doing manual data entry, etc.]
- Impact: ___ hours of skilled labor on low-value tasks

**5. Transportation (Moving data/materials unnecessarily):**
- [Unnecessary data transfers, file sharing, etc.]
- Example: Exporting from System A, importing to System B
- Impact: ___ minutes per instance

**6. Inventory (Work piling up):**
- [Backlogs, queues]
- Example: 50 pending approvals
- Impact: Delays, rush jobs, lost revenue

**7. Motion (Unnecessary movement/clicks):**
- [Excessive clicks, switching between systems]
- Example: Opening 5 different systems to complete one task
- Impact: ___ minutes wasted per instance

**8. Extra Processing (Doing more than customer requires):**
- [Unnecessary complexity, over-engineering]
- Example: 10-page report when 1-page summary sufficient
- Impact: ___ hours per report

**Total Waste Identified:** ___ hours per instance (___ % of total time)
**Annual Impact:** ___ hours wasted per year = $___ at $___/hour labor rate

**OPTIMIZATION OPPORTUNITIES:**

**Quick Wins (Implement within 1 week):**

1. **Eliminate [specific waste]**
   - Current: [describe wasteful step]
   - Improved: [describe elimination]
   - Time Saved: ___ minutes per instance
   - Implementation: [what needs to happen?]
   - Effort: Low / Medium / High
   - Impact: Low / Medium / High

2. **Simplify [specific step]**
   - Current: [complex process]
   - Improved: [simplified version]
   - Time Saved: ___ minutes
   - Implementation: [actions needed]

3. **Standardize [process variation]**
   - Current: Everyone does it differently
   - Improved: Single standard procedure
   - Benefit: Fewer errors, easier training, faster execution

[List 5-10 quick wins]

**Medium-Term Improvements (1-4 weeks):**

1. **Automate [manual task]**
   - Current: Manual data entry (30 min)
   - Improved: Automated data sync (0 min)
   - Tool: Python script / API integration / RPA
   - Time Saved: 30 min per instance × [frequency] = ___ hours/month
   - ROI: Time saved ___ hours @ $___/hr = $___/month, Implementation cost $___ (payback ___ months)

2. **Integrate systems [A and B]**
   - Current: Export from A, import to B
   - Improved: Direct integration (real-time sync)
   - Tool: API, middleware, or database connection
   - Benefits: Eliminates manual transfer, reduces errors, real-time data

3. **Create dashboard [for visibility]**
   - Current: Status unknown, must ask people
   - Improved: Real-time dashboard
   - Benefits: Self-service, faster decisions, proactive management

[List 3-5 medium-term improvements]

**Long-Term Transformation (1-6 months):**

1. **Redesign end-to-end process**
   - Current: Sequential, many handoffs
   - Improved: Parallel processing, reduced handoffs
   - Example: Approval routing (sequential → concurrent approvals)
   - Impact: Reduce cycle time from ___ days to ___ days

2. **Implement workflow management system**
   - Current: Email and spreadsheet tracking
   - Improved: Dedicated workflow tool (e.g., Monday.com, Asana, custom)
   - Benefits: 
     * Automated task assignment
     * SLA tracking and alerts
     * Audit trail
     * Reporting and analytics
   - Cost: $___ per month
   - ROI: ___ hours saved = $___ per month

3. **Process AI/ML integration**
   - Opportunity: [Predictive analytics, pattern recognition, anomaly detection]
   - Example: Predict maintenance needs based on sensor data
   - Impact: Prevent downtime, optimize scheduling

**OPTIMIZED WORKFLOW DESIGN:**

**Future State Workflow:**

| Step # | Activity | Owner | Time | Systems/Tools | Automation | Improvement |
|--------|----------|-------|------|---------------|------------|-------------|
| 1 | [Automated activity] | System | 0 min | API | Full | Eliminated manual entry |
| 2 | [Simplified activity] | [Role] | 5 min | Dashboard | Partial | Reduced from 30 min |
| 3 | [Parallel activity] | [Role] | 10 min | Workflow tool | None | Parallel not sequential |
[Create optimized workflow - significantly shorter than current]

**Optimized Metrics:**
- Total Process Time: ___ hours (___% reduction from current)
- Total Touch Time: ___ hours (___% reduction)
- Wait Time: ___ hours (___% reduction)
- Number of Handoffs: ___ (reduced from ___)
- Error Rate: ___% (reduced from ___%)
- Cost per Instance: $___ (___% reduction)

**Value Delivered:**
- Time Savings: ___ hours per instance
- Cost Savings: $___ per instance
- Annual Savings: $___ (volume × cost savings)
- Quality Improvement: ___% fewer errors
- Cycle Time Reduction: ___% faster completion
- Customer Satisfaction: Improved (faster, more accurate)

**IMPLEMENTATION ROADMAP:**

**Phase 1: Quick Wins (Week 1-2)**
- Implement quick wins #1-5
- Train team on new procedures
- Measure baseline metrics
- Total Investment: ___ hours effort, $___ cost
- Expected Savings: ___ hours/month

**Phase 2: Medium-Term Improvements (Week 3-8)**
- Develop automation scripts
- Integrate systems
- Create dashboards
- Test and refine
- Total Investment: ___ hours, $___ cost
- Expected Savings: ___ hours/month

**Phase 3: Long-Term Transformation (Month 3-6)**
- Implement workflow management system
- Redesign end-to-end process
- Train organization
- Monitor and optimize
- Total Investment: ___ hours, $___ cost
- Expected Savings: ___ hours/month

**GOVERNANCE & CONTINUOUS IMPROVEMENT:**

**Process Ownership:**
- Process Owner: [Name, Role]
- Accountable for: Performance metrics, continuous improvement
- Authority: Make changes within guidelines

**Performance Monitoring:**
- Track KPIs weekly: Cycle time, error rate, cost
- Review monthly: Trends, issues, opportunities
- Audit quarterly: Compliance with standard procedure

**Continuous Improvement Culture:**
- Encourage ideas from frontline staff
- Monthly kaizen events (focused improvement workshops)
- Reward process improvements
- Document and share best practices

**TECHNOLOGY ENABLERS:**

**Automation Tools:**
- Python scripts for data processing
- Power Automate / Zapier for workflow automation
- RPA (UiPath, Automation Anywhere) for legacy system automation

**Workflow Management:**
- Monday.com, Asana, Jira - Project/task management
- Kissflow, ProcessMaker - BPM platforms
- Custom applications - Full control

**Integration:**
- APIs (RESTful, GraphQL)
- Middleware (Mulesoft, Dell Boomi)
- Database connections (direct queries)

**Analytics:**
- Process mining (Celonis, UiPath Process Mining)
- Dashboards (Power BI, Tableau, Grafana)
- Custom reporting (Python, R)

**BEST PRACTICES:**

1. **Start with highest-impact processes:**
   - High volume × High waste = Biggest opportunity
   - Example: If process runs 100×/month with 2 hours waste = 200 hours/month opportunity

2. **Involve frontline staff:**
   - They know the pain points
   - They'll use the new process
   - Get their buy-in early

3. **Measure before and after:**
   - Baseline current state
   - Track improvements
   - Prove ROI

4. **Iterate:**
   - Don't wait for perfection
   - Implement, measure, refine
   - Small improvements compound

5. **Standardize, then automate:**
   - Automating a bad process = bad process, faster
   - Optimize first, then automate

6. **Change management:**
   - Communicate why (benefits)
   - Train people (how)
   - Support adoption (help desk, champions)
   - Celebrate wins (recognition)

**CASE STUDY EXAMPLE:**

**Process:** Monthly Financial Close

**Before Optimization:**
- 15 steps, 8 handoffs, 5 systems
- Total time: 80 hours (10 business days)
- Touch time: 35 hours (actual work)
- Wait time: 45 hours (approvals, delays)
- Error rate: 12% (requiring rework)

**After Optimization:**
- 8 steps, 3 handoffs, 3 systems (2 eliminated via integration)
- Total time: 32 hours (4 business days) - 60% reduction
- Touch time: 28 hours - 20% reduction in work time
- Wait time: 4 hours - 90% reduction
- Error rate: 2% - 83% reduction
- Automation: 7 hours of work fully automated
- Annual savings: 576 hours = $57,600 at $100/hr labor rate

**RECOMMENDATIONS:**

1. **Immediate Actions:**
   - Map top 3 highest-volume processes
   - Identify quick wins (can implement this week)
   - Assign process owners

2. **This Quarter:**
   - Implement all quick wins
   - Start automation projects for top 2 processes
   - Establish performance dashboards

3. **This Year:**
   - Optimize top 10 processes (80/20 rule: 20% of processes = 80% of work)
   - Implement workflow management system
   - Train organization on process improvement methodology
   - Target: 30% reduction in process cycle times, 50% reduction in errors

This workflow optimization approach will systematically eliminate waste, reduce cycle times, improve quality, and free up your team to focus on high-value activities instead of administrative busywork."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def task_automation(repetitive_task):
    """
    Identify and automate repetitive tasks.
    Args: repetitive_task - description of task to automate
    """
    prompt = f"""You are a Task Automation System Architect. Design automation solution for: {repetitive_task}

CREATE COMPREHENSIVE TASK AUTOMATION PLAN:

**AUTOMATION ASSESSMENT:**

**Task Profile:**
- Task Name: [Name]
- Current Process: [Describe step-by-step what happens now]
- Frequency: [How often? Daily/Weekly/Monthly, ___ times per ___]
- Time per Instance: [___ minutes/hours]
- Who Performs: [Role/person]
- Systems Involved: [List all systems, tools, files]
- Input: [What triggers this? What data is needed?]
- Output: [What is produced?]
- Downstream Impact: [Who/what depends on this?]

**Automation Opportunity Score:**

| Criteria | Score (1-5) | Weight | Weighted Score | Notes |
|----------|-------------|--------|----------------|-------|
| Repetitiveness | ___ | 25% | ___ | 5=Exactly same every time |
| Volume | ___ | 20% | ___ | 5=Very high frequency |
| Time Consuming | ___ | 20% | ___ | 5=>60 min per instance |
| Error Prone | ___ | 15% | ___ | 5=High error rate |
| Rule-Based | ___ | 15% | ___ | 5=Clear rules, no judgment |
| Feasibility | ___ | 5% | ___ | 5=Easy to automate technically |
| **TOTAL** | | 100% | **___** | >3.5 = Strong candidate |

**Current State Metrics:**
- Time per Instance: ___ minutes
- Instances per Month: ___
- Total Monthly Time: ___ hours
- Annual Time: ___ hours
- Labor Cost (@ $___/hr): $___ per year
- Error Rate: ___% (___% require rework)
- Rework Time: ___ hours per year

**Total Opportunity:** ___ hours per year = $___ per year

**AUTOMATION SOLUTION DESIGN:**

**Approach Selection:**

**Option 1: Simple Script Automation**
- **Best For:** File operations, data transformation, scheduled tasks
- **Tools:** Python, PowerShell, Bash
- **Pros:** Low cost, flexible, full control
- **Cons:** Requires coding skills, maintenance
- **Examples:** 
  * Data extraction from PDFs
  * File renaming/organizing
  * Email notifications
  * Report generation
  * Database queries

**Option 2: No-Code Automation (Power Automate, Zapier)**
- **Best For:** Cloud app integration, workflows, notifications
- **Tools:** Power Automate, Zapier, IFTTT, Integromat
- **Pros:** No coding, fast to build, pre-built connectors
- **Cons:** Monthly cost, limited customization
- **Examples:**
  * Email to CRM sync
  * Form submission workflows
  * Social media posting
  * Slack/Teams notifications

**Option 3: RPA (Robotic Process Automation)**
- **Best For:** UI automation, legacy systems, complex workflows
- **Tools:** UiPath, Automation Anywhere, Blue Prism, Power Automate Desktop
- **Pros:** Can automate anything with UI, no system changes
- **Cons:** Expensive, brittle (UI changes break), maintenance
- **Examples:**
  * Legacy system data entry
  * Multi-system workflows
  * PDF/document processing
  * Screen scraping

**Option 4: API Integration**
- **Best For:** System-to-system data sync, real-time integration
- **Tools:** Custom code (Python/Node.js), middleware (Mulesoft)
- **Pros:** Reliable, real-time, scalable
- **Cons:** Requires API access, coding skills
- **Examples:**
  * CRM ↔ Accounting sync
  * Real-time inventory updates
  * Payment processing
  * Webhook-triggered actions

**Recommended Approach for This Task:** [Option __]
**Justification:** [Why this approach is best fit]

**DETAILED AUTOMATION DESIGN:**

**Architecture Overview:**
```
[Trigger] → [Input Processing] → [Core Logic] → [Output Generation] → [Notification]
```

**Component 1: Trigger (What starts the automation?)**
- **Type:** Schedule / Event / Manual
- **Details:**
  * Schedule: Daily at 6 AM
  * Event: When file arrives in folder
  * Manual: User clicks button
- **Implementation:** Cron job / File watcher / UI button

**Component 2: Input Processing**
- **Data Sources:** [List all inputs]
  * File: [location, format]
  * Database: [connection, query]
  * API: [endpoint, authentication]
  * User Input: [parameters]
- **Validation:** [Check for required data, format, completeness]
- **Error Handling:** [What if input missing/invalid?]

**Component 3: Core Logic (The actual task)**

**Step 1:** [Task description]
- Action: [What happens]
- Input: [What's needed]
- Output: [What's produced]
- Code/Tool: [How it's implemented]
- Error Handling: [What if it fails?]

**Step 2:** [Next task]
[Continue for all steps...]

**Component 4: Output Generation**
- **Format:** Excel file / PDF / Database record / Email / Dashboard update
- **Location:** [Where is output saved/sent?]
- **Naming Convention:** [Filename format with date/time]
- **Retention:** [How long to keep? Archive strategy?]

**Component 5: Notification**
- **Success Notification:**
  * To: [Recipients]
  * Method: Email / Slack / Teams / Dashboard
  * Content: "Task completed: [details], [link to output]"
- **Failure Notification:**
  * To: [Support team]
  * Method: Email + SMS (urgent)
  * Content: "Task failed: [error message], [troubleshooting steps]"
- **Summary Reports:** Daily/Weekly summary of all automation runs

**SAMPLE CODE/IMPLEMENTATION:**

```python
# Example Python automation script
import os
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def main():
    try:
        # Step 1: Read input data
        data = pd.read_csv('input_file.csv')
        
        # Step 2: Process data (example: filter, transform)
        processed_data = data[data['status'] == 'active']
        processed_data['calculated_field'] = processed_data['value'] * 1.1
        
        # Step 3: Generate output
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'output_report_{timestamp}.xlsx'
        processed_data.to_excel(output_file, index=False)
        
        # Step 4: Send notification
        send_email_notification(
            subject='Automation Completed Successfully',
            body=f'Report generated: {output_file}\\n{len(processed_data)} records processed.',
            attachment=output_file
        )
        
    except Exception as e:
        # Error handling
        send_email_notification(
            subject='Automation FAILED',
            body=f'Error: {str(e)}\\nPlease investigate.',
            urgent=True
        )
        raise

def send_email_notification(subject, body, attachment=None, urgent=False):
    # Email sending logic
    pass

if __name__ == '__main__':
    main()
```

**TESTING STRATEGY:**

**Unit Testing:**
- Test each component independently
- Test cases: Normal input, edge cases, invalid input
- Verify outputs match expected results

**Integration Testing:**
- Test end-to-end workflow
- Test with real data (or realistic sample)
- Verify all systems communicate correctly

**User Acceptance Testing:**
- Have end users validate output
- Confirm automation meets requirements
- Get sign-off before production deployment

**Error Scenario Testing:**
- Missing input file
- Corrupted data
- System unavailable
- Network timeout
- Partial failure (some records fail)

**DEPLOYMENT PLAN:**

**Phase 1: Parallel Running (2-4 weeks)**
- Run automation alongside manual process
- Compare outputs for accuracy
- Build confidence in automation
- Refine as needed

**Phase 2: Monitored Automation (4 weeks)**
- Automation runs in production
- Human reviews output before use
- Monitor error rates, performance
- Quick rollback if issues

**Phase 3: Full Automation**
- Automation runs independently
- Human spot-checks periodically
- Exception handling for edge cases
- Continuous monitoring

**MONITORING & MAINTENANCE:**

**Monitoring Dashboard:**
- Execution success rate (target >99%)
- Average run time (track performance degradation)
- Error types and frequency
- Resource usage (CPU, memory, storage)

**Alerts:**
- Immediate: Automation failure
- Daily: Summary of all runs
- Weekly: Performance trends
- Monthly: ROI metrics

**Maintenance:**
- Monthly: Review logs, optimize performance
- Quarterly: Update for system changes
- Annually: Comprehensive review and enhancement

**ROI CALCULATION:**

**Benefits:**
- Time Savings: ___ hours per month × $___/hr = $___/month
- Error Reduction: ___ fewer errors × $___ cost per error = $___/month
- Faster Processing: ___ days → ___ hours (improved customer satisfaction)
- Redeployment: Staff freed up for higher-value work

**Total Annual Benefit: $___**

**Costs:**
- Development: ___ hours × $___/hr = $___
- Software/Tools: $___ per month × 12 = $___/year
- Maintenance: ___ hours per year × $___/hr = $___/year

**Total Annual Cost: $___**

**ROI:**
- Net Benefit: $___/year
- Payback Period: ___ months
- ROI: ___% per year

**RISK MITIGATION:**

**Risk 1: Automation Failure**
- Mitigation: Robust error handling, alerts, fallback to manual process
- Contingency: Manual procedure documented and staff trained

**Risk 2: System Changes Break Automation**
- Mitigation: Version control, testing before production, change management process
- Contingency: Monitoring detects issues quickly, rapid fix or rollback

**Risk 3: Data Quality Issues**
- Mitigation: Input validation, data quality checks, reject bad data
- Contingency: Human review of flagged records

**Risk 4: Security/Compliance**
- Mitigation: Credential management (vaults), audit logging, access controls
- Compliance: Review with IT/Security, ensure meets policies

**SCALING STRATEGY:**

Once this automation is successful:

1. **Document the approach** - Create template for future automations
2. **Identify next candidates** - Prioritize by ROI
3. **Build automation pipeline** - Systematically automate top 20 tasks
4. **Develop automation capability** - Train team, establish CoE (Center of Excellence)
5. **Target:** Automate 30-50% of repetitive tasks within 12 months

**RECOMMENDATIONS:**

1. **Start with This Task:**
   - Strong ROI candidate (payback < ___ months)
   - Low technical complexity
   - High impact (frequent, time-consuming)

2. **Implementation Timeline:**
   - Week 1-2: Design and develop
   - Week 3-4: Test and refine
   - Week 5-8: Parallel run and validation
   - Month 3: Full production deployment

3. **Success Criteria:**
   - >99% success rate
   - <5 minutes average runtime
   - Zero critical errors
   - User satisfaction >8/10
   - ROI achieved within 6 months

4. **Next Steps:**
   - Approve automation project
   - Assign developer/team
   - Set up development environment
   - Schedule kickoff meeting

This automation will eliminate tedious manual work, improve accuracy, free up staff for strategic activities, and deliver measurable ROI."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def efficiency_analysis(business_operations):
    """
    Analyze operational efficiency and identify improvement areas.
    Args: business_operations - description of operations to analyze
    """
    prompt = f"""You are an Operational Efficiency Analysis System. Perform comprehensive efficiency analysis for: {business_operations}

CONDUCT DETAILED EFFICIENCY ANALYSIS:

**ANALYSIS FRAMEWORK:**

**Efficiency Definition:**
Efficiency = Output / Input (maximize output while minimizing input)
- Output: Value delivered (revenue, units produced, customers served)
- Input: Resources consumed (time, money, materials, energy)

**STEP 1: BASELINE MEASUREMENT**

**Current Performance Metrics:**

**Productivity Metrics:**
- Revenue per Employee: $___
- Units Produced per Hour: ___
- Customers Served per Day: ___
- Revenue per Labor Hour: $___
- Asset Utilization: ___% (equipment uptime)

**Cost Metrics:**
- Cost of Goods Sold (COGS): $___
- Operating Expense Ratio: ___% (OPEX/Revenue)
- Labor Cost as % of Revenue: ___%
- Overhead Rate: ___% 
- Cost per Unit: $___

**Time Metrics:**
- Average Cycle Time: ___ days (order to delivery)
- Process Throughput: ___ units per day
- Lead Time: ___ days (order to fulfillment)
- Delivery Time: ___ days (to customer)
- Time to Market (for new products): ___ months

**Quality Metrics:**
- Defect Rate: ___% (target <1%)
- First Pass Yield: ___% (% passing without rework)
- Customer Satisfaction (CSAT): ___ / 10
- Net Promoter Score (NPS): ___
- Return/Refund Rate: ___%

**Resource Utilization:**
- Labor Utilization: ___% of available hours
- Equipment Utilization: ___% of available capacity
- Inventory Turnover: ___ times per year
- Space Utilization: ___ sq ft per $___k revenue

**STEP 2: BENCHMARKING**

**Internal Benchmarks (Historical):**
- This Year vs. Last Year: ___% change
- This Quarter vs. Last Quarter: ___% change
- Trend: Improving / Stable / Declining

**External Benchmarks (Industry):**
| Metric | Our Performance | Industry Average | Best-in-Class | Gap to Best |
|--------|-----------------|------------------|---------------|-------------|
| Revenue per Employee | $___ | $___ | $___ | ___% behind |
| OPEX Ratio | ___% | ___% | ___% | ___ pts higher |
| Asset Utilization | ___% | ___% | ___% | ___ pts lower |
| Defect Rate | ___% | ___% | ___% | ___× higher |
| Cycle Time | ___ days | ___ days | ___ days | ___× slower |

**Performance Assessment:**
- Areas of Strength: [Where we exceed industry average]
- Areas for Improvement: [Where we lag industry]
- Biggest Opportunities: [Largest gaps to best-in-class]

**STEP 3: ROOT CAUSE ANALYSIS**

**Why Are We Less Efficient?**

**Analysis Framework: 7 Wastes (Lean Manufacturing)**

**1. Waiting (Idle time):**
- Where: [Processes waiting for approvals, data, materials, people]
- Impact: ___ hours per [period] of idle time
- Root Cause: [Why? Bottlenecks, approval delays, coordination issues]
- Opportunity: Reduce waiting time by ___% = ___ hours saved

**2. Overproduction (Making more than needed):**
- Where: [Producing ahead of demand, creating unused reports]
- Impact: $___ tied up in excess inventory, ___ hours wasted
- Root Cause: [Why? Batch sizes too large, poor demand forecasting]
- Opportunity: Implement just-in-time = $___ freed up

**3. Defects (Rework required):**
- Where: [Quality issues requiring rework]
- Impact: ___% defect rate × ___ units = ___ hours rework
- Root Cause: [Why? Inadequate training, poor process control, lack of QC]
- Opportunity: Implement quality controls = ___% reduction in defects

**4. Non-utilized Talent:**
- Where: [Skilled people doing low-value work]
- Impact: $___/hr talent on $___ /hr tasks = $___ per year waste
- Root Cause: [Why? Lack of automation, poor delegation, no process]
- Opportunity: Automate low-value tasks, redeploy talent

**5. Transportation (Unnecessary movement):**
- Where: [Moving materials, data, products unnecessarily]
- Impact: ___ miles traveled, ___ hours transport time
- Root Cause: [Why? Poor layout, disconnected systems]
- Opportunity: Colocate, integrate systems = ___% reduction

**6. Inventory (Excess stock):**
- Where: [Raw materials, WIP, finished goods sitting idle]
- Impact: $___ tied up, $___/year carrying cost
- Root Cause: [Why? Large batch sizes, poor forecasting, supply chain issues]
- Opportunity: Reduce inventory by ___% = $___ freed up

**7. Motion (Excess movement/steps):**
- Where: [Excessive clicks, walking, searching for info]
- Impact: ___ minutes per instance × ___ instances = ___ hours
- Root Cause: [Why? Poor ergonomics, disorganized, multi-system]
- Opportunity: Redesign workspace, integrate systems

**Total Waste Identified:** 
- Time: ___ hours per [period] (___% of total time)
- Cost: $___ per [period]
- Annual Opportunity: $___ per year

**STEP 4: EFFICIENCY IMPROVEMENT OPPORTUNITIES**

**CATEGORY 1: PROCESS OPTIMIZATION**

**Opportunity 1: Streamline [Process Name]**
- Current: ___ steps, ___ hours, ___% error rate
- Optimized: ___ steps (___% reduction), ___ hours (___% faster), ___% error rate
- How: Eliminate redundant steps, automate manual tasks, parallel processing
- Impact: ___ hours saved per instance × ___ instances = ___ hours/year
- ROI: $___ per year saved

**Opportunity 2: Eliminate Bottlenecks**
- Current Bottleneck: [Describe constraint limiting throughput]
- Impact: Throughput limited to ___ units per day (could be ___ without bottleneck)
- Solution: [Increase capacity, rebalance workload, add resources]
- Impact: Increase throughput by ___% = $___ additional revenue

**Opportunity 3: Reduce Cycle Time**
- Current: ___ days from start to finish
- Target: ___ days (___% reduction)
- How: Eliminate wait time, parallel processing, faster approvals
- Impact: 
  * Faster customer delivery (competitive advantage)
  * Lower WIP inventory ($___freed up)
  * Increased throughput (more units per year)

[List 5-10 process optimization opportunities]

**CATEGORY 2: AUTOMATION & TECHNOLOGY**

**Opportunity 1: Automate [Manual Task]**
- Current: ___ hours per month of manual work
- Automated: ___ hours (___% automated, ___% still manual)
- Tool: [Python script / Power Automate / RPA / Custom app]
- Investment: $___ (development) + $___ per month (software)
- Payback: ___ months
- Annual ROI: $___

**Opportunity 2: Implement [Technology Solution]**
- Current: [Describe manual or inefficient process]
- Improved: [Describe with new technology]
- Examples: CRM, ERP, workflow management, analytics platform
- Investment: $___ (implementation) + $___ per month (subscription)
- Benefit: ___ hours saved + $___better decisions + ___% revenue growth
- Payback: ___ months

[List 3-5 automation opportunities]

**CATEGORY 3: RESOURCE OPTIMIZATION**

**Labor Optimization:**
- Current: ___ FTEs, $___/year labor cost
- Opportunity: Redeploy ___ FTE from low-value to high-value work
- Impact: 
  * Low-value work automated/eliminated
  * High-value work (sales, strategy, innovation) gets more resources
  * Revenue increase: $___
  * No headcount increase needed

**Asset Utilization:**
- Current: Equipment utilized ___% of available time
- Target: ___% (industry best practice)
- How: Reduce downtime (maintenance), increase throughput, add shifts
- Impact: ___% more capacity without capital investment

**Space Optimization:**
- Current: ___ sq ft, $___/sq ft cost = $___ per year
- Opportunity: Consolidate, eliminate storage, go digital
- Potential: Reduce space by ___% = $___ per year savings

[List 3-5 resource optimization opportunities]

**CATEGORY 4: QUALITY IMPROVEMENT**

**Reduce Defects:**
- Current: ___% defect rate
- Target: <1% (world-class)
- How: Root cause analysis, process control, training, inspection
- Impact: 
  * Rework time saved: ___ hours per year
  * Material waste reduced: $___ per year
  * Customer satisfaction improved (fewer returns)

**First Pass Yield:**
- Current: ___% (pass without rework)
- Target: >99%
- Impact: ___% more units first-time-right = ___ hours saved

[List 2-3 quality opportunities]

**STEP 5: PRIORITIZATION MATRIX**

Rank opportunities by Impact (benefit) vs. Effort (difficulty):

**Impact Score:** (1-10, higher is better)
- Financial: How much $ saved/earned?
- Time: How much time freed up?
- Strategic: How important for competitive advantage?

**Effort Score:** (1-10, lower is better)
- Cost: How expensive to implement?
- Time: How long to implement?
- Complexity: How technically difficult?
- Change Management: How disruptive?

| Opportunity | Impact | Effort | Priority | Quick Win? |
|-------------|--------|--------|----------|------------|
| Automate data entry | 8 | 3 | High | Yes |
| Implement ERP | 10 | 10 | Medium | No (long-term) |
| Eliminate approval step | 6 | 2 | High | Yes |
| Reduce inventory | 7 | 5 | Medium | |
| Streamline Process X | 9 | 4 | High | |
[Rank all opportunities]

**High Impact + Low Effort = DO FIRST (Quick Wins)**
**High Impact + High Effort = STRATEGIC PROJECTS (Plan carefully)**
**Low Impact + Low Effort = NICE TO HAVE (Do if time permits)**
**Low Impact + High Effort = DON'T DO (Not worth it)**

**STEP 6: EFFICIENCY IMPROVEMENT ROADMAP**

**Immediate (Next 30 Days):**
1. [Quick Win #1] - ___ hours saved, $___ ROI
2. [Quick Win #2] - ___ hours saved, $___ ROI
3. [Quick Win #3] - ___ hours saved, $___ ROI
**Total:** ___ hours per month, $___ per year

**Short-Term (Next 90 Days):**
1. [Opportunity #1] - Implementation plan, timeline, resources
2. [Opportunity #2]
3. [Opportunity #3]
**Total:** ___ hours per month, $___ per year

**Medium-Term (6-12 Months):**
1. [Strategic Project #1] - Business case, budget, project plan
2. [Strategic Project #2]
**Total:** ___ hours per month, $___ per year

**Long-Term (12+ Months):**
1. [Transformation Initiative] - Long-term vision, multi-year plan
**Total:** ___ hours per month, $___ per year

**Cumulative Impact:**
- Year 1: $___savings + ___% productivity improvement
- Year 2: $___ savings + ___% productivity improvement
- Year 3: $___ savings + ___% productivity improvement

**STEP 7: IMPLEMENTATION FRAMEWORK**

**Governance:**
- Executive Sponsor: [C-level champion]
- Program Manager: [Day-to-day leader]
- Working Team: [Cross-functional representatives]
- Frequency: Bi-weekly meetings, monthly executive review

**Change Management:**
- Communication: Town halls, emails, intranet updates
- Training: Hands-on workshops for new processes/tools
- Support: Help desk, super users, FAQs
- Recognition: Celebrate wins, reward contributions

**Measurement:**
- Track KPIs monthly (before/after comparison)
- Report savings and ROI quarterly
- Adjust plan based on results

**RECOMMENDATIONS:**

1. **Start with Quick Wins:**
   - Build momentum
   - Demonstrate ROI
   - Build credibility for larger initiatives

2. **Focus on Top 3 Opportunities:**
   - Don't boil the ocean
   - 80/20 rule: Top 20% of opportunities = 80% of benefit

3. **Sustain Improvements:**
   - Make new processes standard operating procedure
   - Train all staff
   - Monitor compliance
   - Continuous improvement culture

4. **Scale Successes:**
   - Document what works
   - Replicate across organization
   - Build operational excellence capability

**EFFICIENCY TARGETS:**

**6-Month Targets:**
- Productivity: +15%
- Cycle Time: -20%
- Defect Rate: -50%
- OPEX Ratio: -10%

**12-Month Targets:**
- Productivity: +25%
- Cycle Time: -35%
- Defect Rate: -70%
- OPEX Ratio: -15%

**Best-in-Class (3-Year Vision):**
- Match or exceed industry best-in-class across all metrics
- Operational efficiency as competitive advantage
- Culture of continuous improvement

This efficiency analysis provides a data-driven roadmap to systematically improve performance, reduce waste, and maximize output from available resources."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def automation_recommendations(business_context):
    """
    Provide comprehensive automation recommendations based on business context.
    Args: business_context - description of business operations and goals
    """
    prompt = f"""You are an Automation Strategy Consultant. Provide comprehensive automation recommendations for: {business_context}

CREATE DETAILED AUTOMATION STRATEGY AND RECOMMENDATIONS:

**AUTOMATION ASSESSMENT:**

**Business Context Analysis:**
- Industry: [Industry sector]
- Company Size: [# employees, revenue]
- Current State: [Manual/partially automated/automated]
- Goals: [Efficiency, growth, cost reduction, quality]
- Constraints: [Budget, timeline, technical capability]

**STEP 1: AUTOMATION OPPORTUNITY SCAN**

**Identify All Automatable Tasks:**

**Category 1: Data Entry & Transfer**
- Manual data entry from emails/forms/documents
- Copy-paste between systems
- File downloads and uploads
- Data validation and cleanup
**Automation Potential:** 90-100% (highest ROI tasks)
**Tools:** Python scripts, Power Automate, RPA

**Category 2: Document Processing**
- Invoice processing
- Contract review and extraction
- Report generation
- PDF/Email parsing
**Automation Potential:** 70-90%
**Tools:** OCR (Optical Character Recognition), Document AI, Python

**Category 3: Communication & Notifications**
- Email sending (confirmations, reminders, alerts)
- Status updates
- Meeting scheduling
- Customer follow-ups
**Automation Potential:** 80-95%
**Tools:** Email automation, Slack/Teams bots, Calendly

**Category 4: Reporting & Analytics**
- Data aggregation
- Dashboard updates
- Performance reports
- KPI calculations
**Automation Potential:** 85-95%
**Tools:** Power BI, Python, SQL, automated reporting

**Category 5: Customer Service**
- FAQs and common questions
- Order status inquiries
- Appointment scheduling
- Basic troubleshooting
**Automation Potential:** 40-60% (chatbots handle tier 1)
**Tools:** Chatbots, knowledge bases, IVR systems

**Category 6: Business Workflows**
- Approval workflows
- Onboarding processes
- Procurement processes
- Expense reporting
**Automation Potential:** 60-80%
**Tools:** Workflow management platforms, RPA

**Category 7: Financial Processes**
- Invoice matching (3-way matching)
- Expense reconciliation
- Financial close processes
- Payroll processing
**Automation Potential:** 70-85%
**Tools:** Accounting software integrations, RPA

**Category 8: IT Operations**
- Server monitoring
- Backup processes
- Software deployments
- Incident ticketing
**Automation Potential:** 80-95%
**Tools:** DevOps tools, monitoring platforms, runbooks

**STEP 2: PRIORITIZED AUTOMATION ROADMAP**

**Scoring Methodology:**
Each opportunity scored on 5 criteria (1-5 scale):
1. **ROI:** Time/cost savings potential
2. **Volume:** How frequently does this occur?
3. **Complexity:** How difficult to automate?
4. **Business Impact:** How important to business goals?
5. **Feasibility:** Do we have the skills/tools?

**TOP 10 AUTOMATION OPPORTUNITIES:**

**#1: [Automation Opportunity Name]**
- **Current Process:** [Describe manual process]
- **Time per Instance:** ___ minutes
- **Frequency:** ___ times per [day/week/month]
- **Total Time:** ___ hours per month
- **Error Rate:** ___%
- **Automation Approach:** [Python script / Power Automate / RPA / API]
- **Effort to Implement:** ___ hours development
- **Cost:** $___ (one-time) + $___ per month (ongoing)
- **Time Savings:** ___ hours per month
- **Payback Period:** ___ months
- **Annual ROI:** $___
- **Score:** ___/25 (Top Priority!)

**#2: [Next Opportunity]**
[Same template...]

**#3-10:** [Continue listing top opportunities]

**STEP 3: AUTOMATION TECHNOLOGY STACK**

**Recommended Tools by Use Case:**

**For Simple Automations (80% of opportunities):**

**1. Python + Libraries**
- **Use For:** Data processing, file operations, API calls, web scraping
- **Key Libraries:**
  * pandas - data manipulation
  * requests - API calls
  * openpyxl - Excel files
  * PyPDF2 - PDF processing
  * schedule - task scheduling
  * smtplib - email sending
- **Cost:** FREE (open source)
- **Learning Curve:** Medium (many tutorials available)
- **Pros:** Flexible, powerful, free
- **Cons:** Requires coding skills

**2. Power Automate (Microsoft)**
- **Use For:** Cloud app workflows, approvals, notifications
- **Connectors:** 400+ pre-built (Office 365, SharePoint, Teams, CRM, etc.)
- **Cost:** $15/user/month (or free with Office 365)
- **Learning Curve:** Low (no-code)
- **Pros:** Easy to build, Microsoft ecosystem integration
- **Cons:** Limited customization, can get expensive at scale

**3. Zapier / Make (Integromat)**
- **Use For:** Connecting cloud apps (Gmail, Slack, Salesforce, etc.)
- **Cost:** $20-50/month (depends on volume)
- **Learning Curve:** Low (no-code)
- **Pros:** 5,000+ app integrations, fast to build
- **Cons:** Monthly cost, trigger-based (not real-time)

**For Complex Automations (20% of opportunities):**

**4. RPA Platforms (UiPath, Automation Anywhere, Blue Prism)**
- **Use For:** Legacy UI automation, complex multi-system workflows
- **Cost:** $3,000-15,000 per bot per year
- **Learning Curve:** Medium-High
- **Pros:** Can automate anything with a UI, no system changes
- **Cons:** Expensive, brittle, maintenance-intensive

**5. Custom Application Development**
- **Use For:** Unique requirements, high-volume/high-value processes
- **Technology:** Python/Node.js backend, React/Vue frontend, PostgreSQL database
- **Cost:** $50,000-200,000 (depending on complexity)
- **Learning Curve:** High (requires developers)
- **Pros:** Full control, scalable, tailored to needs
- **Cons:** Expensive, time to build, maintenance

**RECOMMENDED STARTING STACK:**
1. **Python** - Core automation engine (free, flexible)
2. **Power Automate or Zapier** - Quick cloud app integrations (low-code)
3. **Git/GitHub** - Version control for scripts
4. **Server/Cloud VM** - To run scheduled automations (AWS/Azure)
**Total Cost:** ~$50-100/month (cloud hosting + Power Automate/Zapier)

**STEP 4: IMPLEMENTATION PLAN**

**Phase 1: Foundation (Month 1-2)**

**Week 1-2: Setup & Skills**
- Set up development environment (Python, Git, accounts)
- Training: Python fundamentals, automation concepts
- Select 2-3 pilot automation projects (quick wins)
- Assign automation champion/team

**Week 3-4: Pilot Automations**
- Build 2-3 simple automations
- Test and refine
- Deploy to production
- Measure results (time saved, errors eliminated)

**Deliverables:**
- 2-3 automations live
- Proven ROI (showcase time/cost savings)
- Team capability established

**Phase 2: Scale (Month 3-6)**

**Build 10-15 High-Impact Automations:**
- Tackle top opportunities from prioritized list
- Mix of Python scripts and no-code tools
- Standardize approach (templates, best practices)
- Build automation library

**Build Automation Culture:**
- Share wins (showcase time savings)
- Train more team members (democratize automation)
- Establish "Automation CoE" (Center of Excellence)
- Monthly automation pipeline review

**Deliverables:**
- 10-15 automations live
- Measurable productivity improvement
- Scalable automation capability

**Phase 3: Advanced Automation (Month 7-12)**

**Complex Workflows:**
- Multi-system integrations
- Advanced logic (AI/ML if applicable)
- Real-time automations (event-driven)
- RPA for legacy systems (if needed)

**Optimization:**
- Monitor all automations (success rate, performance)
- Refine and enhance existing automations
- Decommission automations that aren't working
- Document lessons learned

**Deliverables:**
- 25-40 automations live (comprehensive coverage)
- 30-50% of repetitive work automated
- Self-sustaining automation program

**STEP 5: GOVERNANCE & BEST PRACTICES**

**Automation Standards:**

**1. Documentation Required:**
- Purpose and scope
- Input/output specification
- Dependencies (systems, files, credentials)
- Error handling and escalation
- Maintenance contact

**2. Code Quality:**
- Version control (Git)
- Meaningful variable names
- Comments explaining logic
- Error logging
- Testing before production

**3. Security:**
- Credential management (use vaults, not hardcoded)
- Access controls (who can run/edit?)
- Audit logging (who ran what when?)
- Data privacy compliance (GDPR, etc.)

**4. Monitoring:**
- Success/failure tracking
- Performance metrics (runtime)
- Alert on failures (SMS/email)
- Dashboard showing all automations

**5. Change Management:**
- Test in non-production first
- Get user approval before deploying
- Communicate changes
- Provide training/support

**STEP 6: ROI PROJECTION**

**Investment Required:**

**Year 1:**
- Tools/Software: $___ per month × 12 = $___
- Development Time: ___ hours × $___/hr = $___
- Training: $___
- Infrastructure (servers): $___
**Total Year 1 Investment:** $___

**Year 2-3:**
- Ongoing tools: $___ per year
- Maintenance: ___ hours × $___/hr = $___
**Total Annual (Steady State):** $___

**Benefits:**

**Year 1:**
- Time Savings: ___ hours per month × 12 = ___ hours/year
- Value of Time: ___ hours × $___/hr = $___
- Error Reduction: ___ fewer errors × $___ per error = $___
- Redeployment: Staff freed up for revenue-generating activities = $___
**Total Year 1 Benefit:** $___

**Year 2-3:**
- Continued time savings: $___
- Additional automations: $___
- Compounding benefits (freed-up staff grows revenue): $___
**Total Annual Benefit (Steady State):** $___

**ROI Calculation:**
- Year 1 ROI: ($___benefit - $___investment) / $___investment = ___%
- Payback Period: ___ months
- 3-Year NPV: $___

**STEP 7: SUCCESS METRICS**

**Track These KPIs:**

**Automation Coverage:**
- % of repetitive tasks automated (target: 40-60% by year 1)
- # of automations live and working
- % of staff using/benefiting from automations

**Time Savings:**
- Hours saved per month (track by automation)
- Cumulative hours saved (year-to-date)
- Value of time saved ($)

**Quality Improvement:**
- Error rate reduction (before vs. after automation)
- % of processes with zero defects

**Business Impact:**
- Productivity increase (%% more output with same staff)
- Cost reduction (lower OPEX)
- Revenue growth (staff redeployed to sales/strategy)
- Employee satisfaction (less tedious work)

**RECOMMENDATIONS:**

**1. Start Small, Think Big:**
- Don't try to automate everything at once
- Start with 2-3 quick wins to prove value
- Build momentum and capability
- Scale systematically

**2. Focus on High-Impact, Low-Complexity First:**
- Highest ROI = High volume × High time × Low complexity
- Examples: Data entry, report generation, file processing

**3. Build Internal Capability:**
- Don't outsource all automation (expensive, not sustainable)
- Train 2-3 internal "automation champions"
- Target: 50-80% of automations built in-house

**4. Measure and Communicate:**
- Track time saved (and celebrate it!)
- Monthly "Automation Wins" newsletter
- Make heroes of automation champions

**5. Iterate and Improve:**
- Automations aren't "set and forget"
- Monitor performance
- Refine based on feedback
- Decommission what doesn't work

**Next Steps:**
1. Approve automation program and budget
2. Identify automation champion/team (2-4 people)
3. Set up tools and training (Month 1)
4. Start pilot projects (Month 1-2)
5. Review results and scale (Month 3+)

**Target Outcome:**
Within 12 months, automate 40-60% of repetitive manual work, saving 500-2,000 hours per year and delivering 300-500% ROI on automation investment.

This automation strategy will systematically eliminate tedious work, improve accuracy, free up staff for strategic initiatives, and create a sustainable competitive advantage through operational excellence."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


# CLI Interface
if __name__ == "__main__":
    print("\n✅ Process Automation Agent initialized (Groq - FREE)\n")
    
    import sys
    if len(sys.argv) < 2:
        print("PROCESS AUTOMATION AGENT")
        print("\nCommands:")
        print("  workflow    - Optimize business workflows")
        print("  automate    - Design task automation")
        print("  efficiency  - Analyze operational efficiency")
        print("  recommend   - Get automation recommendations")
        print("\nUsage: python process_automation.py <command> <parameters>")
        print("Example: python process_automation.py workflow 'monthly reporting process'")
        sys.exit(0)
    
    command = sys.argv[1].lower()
    params = sys.argv[2] if len(sys.argv) > 2 else "business operations"
    
    if command == "workflow":
        print(workflow_optimization(params))
    elif command == "automate":
        print(task_automation(params))
    elif command == "efficiency":
        print(efficiency_analysis(params))
    elif command == "recommend":
        print(automation_recommendations(params))
    else:
        print(f"❌ Unknown command: {command}")
        print("Available: workflow, automate, efficiency, recommend")
