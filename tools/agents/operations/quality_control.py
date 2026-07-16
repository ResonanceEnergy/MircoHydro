"""
QUALITY CONTROL AGENT
Standards compliance, inspection protocols, defect tracking, and quality improvement.
Uses Groq (FREE) - llama-3.3-70b-versatile
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def standards_compliance(quality_standards):
    """
    Ensure compliance with quality standards and certifications.
    Args: quality_standards - standards to comply with (ISO 9001, industry standards, etc.)
    """
    prompt = f"""You are a Quality Standards Compliance System. Create comprehensive compliance framework for: {quality_standards}

DEVELOP COMPLETE QUALITY STANDARDS COMPLIANCE PROGRAM:

**STANDARDS OVERVIEW:**

**Applicable Standards:**
- ISO 9001:2015 - Quality Management Systems
- Industry-Specific Standards: [e.g., IEEE, ASME, UL, etc.]
- Customer Requirements: [Contractual quality requirements]
- Regulatory: [OSHA safety, EPA environmental, etc.]
- Internal Standards: [Company quality policies]

**ISO 9001:2015 COMPLIANCE FRAMEWORK:**

**Clause 4: Context of the Organization**

**4.1 Understanding the Organization and Its Context:**
- Internal factors: Strengths, weaknesses, resources, culture
- External factors: Market, competition, regulations, technology
- Analysis: SWOT analysis, stakeholder mapping
- **Compliance Action:** Document organizational context review (annually)

**4.2 Understanding Needs and Expectations of Interested Parties:**
- Customers: Quality, delivery, cost expectations
- Employees: Safe workplace, fair compensation, growth
- Regulators: Compliance with laws
- Shareholders: Profitability, growth
- **Compliance Action:** Stakeholder register with needs documented

**4.3 Determining Scope of QMS:**
- What processes are included? (Design, production, service, support)
- What products/services? (All or specific lines?)
- What locations? (All sites or specific facilities?)
- Exclusions: [If any, with justification]
- **Compliance Action:** Quality manual with defined scope

**4.4 Quality Management System and its Processes:**
- Process map: All QMS processes documented
- Interactions: How processes connect and depend on each other
- Resources: People, equipment, infrastructure needed
- **Compliance Action:** Process map, procedure documents, responsibility matrix

**Clause 5: Leadership**

**5.1 Leadership and Commitment:**
- Top management demonstrates commitment to quality
- Quality policy established and communicated
- QMS requirements integrated into business processes
- Resources provided for QMS
- **Compliance Action:** Management review meetings (quarterly), quality policy statement

**5.2 Quality Policy:**
- Appropriate to purpose and context
- Provides framework for quality objectives
- Commitment to satisfy requirements and continual improvement
- Communicated, understood, applied throughout organization
- **Compliance Action:** Quality policy document, posted in facilities, training

**5.3 Organizational Roles, Responsibilities, and Authorities:**
- Quality Manager: Overall QMS responsibility
- Process Owners: Responsible for individual processes
- Management Representative: Interface with customers and registrars
- All Staff: Responsible for quality in their work
- **Compliance Action:** Organization chart, job descriptions, responsibility matrix

**Clause 6: Planning**

**6.1 Actions to Address Risks and Opportunities:**
- Risk assessment: What could go wrong? What are opportunities?
- Risk mitigation plans
- Review effectiveness of actions
- **Compliance Action:** Risk register, mitigation plans, review schedule

**6.2 Quality Objectives and Planning to Achieve Them:**
- SMART objectives: Specific, Measurable, Achievable, Relevant, Time-bound
- Examples:
  * Reduce defect rate from 2% to <1% by end of year
  * Achieve 98% on-time delivery
  * Improve customer satisfaction score from 7.5 to 8.5
- Action plans: Who, what, when, resources
- **Compliance Action:** Quality objectives document, action plans, quarterly tracking

**6.3 Planning of Changes:**
- Change management process for QMS changes
- Consider implications, resources, responsibilities
- **Compliance Action:** Change request procedure, change log

**Clause 7: Support**

**7.1 Resources:**
- People: Adequate staffing, competence
- Infrastructure: Equipment, facilities, IT systems
- Environment: Work environment conducive to quality
- Monitoring and measuring resources: Calibrated equipment
- Organizational knowledge: Documented, preserved
- **Compliance Action:** Resource plans, equipment lists, calibration schedule, training records

**7.2 Competence:**
- Determine required competencies for each role
- Ensure people are competent (education, training, experience)
- Provide training where gaps exist
- Evaluate effectiveness of training
- Maintain records
- **Compliance Action:** Competency matrix, training plan, training records

**7.3 Awareness:**
- Employees aware of quality policy, objectives, and their role
- Awareness of implications of not conforming
- **Compliance Action:** Training, communication, performance reviews

**7.4 Communication:**
- What to communicate? (Quality performance, objectives, changes)
- When? (Regular meetings, as needed)
- To whom? (Internal: all staff, External: customers, suppliers)
- How? (Meetings, emails, intranet, reports)
- **Compliance Action:** Communication plan, meeting schedule

**7.5 Documented Information:**
- Required by ISO 9001: Quality manual, procedures, records
- Required by organization: Work instructions, forms, templates
- Control of documents: Version control, approval, review
- Control of records: Filing, retention, protection, disposal
- **Compliance Action:** Document control procedure, records retention schedule

**Clause 8: Operation**

**8.1 Operational Planning and Control:**
- Plan production and service delivery
- Define criteria for acceptable output
- Determine resources needed
- Implement controls per requirements
- **Compliance Action:** Production planning, work orders, process controls

**8.2 Requirements for Products and Services:**
- Determine customer requirements (stated, implied, statutory)
- Review orders before acceptance (can we meet requirements?)
- Communicate with customers (inquiries, orders, feedback, changes)
- **Compliance Action:** Sales process, order review, customer communication log

**8.3 Design and Development (if applicable):**
- Design planning: stages, reviews, verification, validation
- Design inputs: Requirements, regulations, standards
- Design controls: Reviews at appropriate stages
- Design outputs: Drawings, specifications, BOMs
- Design verification: Did we design it right? (review, testing)
- Design validation: Did we design the right thing? (customer acceptance)
- Design changes: Controlled, documented, approved
- **Compliance Action:** Design procedure, design files, review records, test reports

**8.4 Control of Externally Provided Processes, Products, and Services:**
- Supplier evaluation and selection criteria
- Supplier performance monitoring
- Incoming inspection
- **Compliance Action:** Approved supplier list, supplier scorecards, receiving inspection procedure

**8.5 Production and Service Provision:**
- Controlled conditions: Documented procedures, competent people, suitable equipment
- Identification and traceability: Label products, track through production
- Property belonging to customers or external providers: Safeguard, identify, protect
- Preservation: Protect product during internal handling and delivery
- Post-delivery activities: Warranty, maintenance, technical support
- Control of changes: Review and authorize changes to production
- **Compliance Action:** Work instructions, traceability system, handling procedures

**8.6 Release of Products and Services:**
- Verify product meets requirements before release
- Inspection and testing at appropriate stages
- Authority to release product
- **Compliance Action:** Inspection and test plan, inspection records, release authority

**8.7 Control of Nonconforming Outputs:**
- Identify nonconforming product (defects, out-of-spec)
- Segregate (prevent unintended use or delivery)
- Disposition: Rework, scrap, use-as-is (with customer concession), return to supplier
- Document nonconformances and actions
- Re-verify after correction
- **Compliance Action:** Nonconformance report procedure, hold tag, disposition authority

**Clause 9: Performance Evaluation**

**9.1 Monitoring, Measurement, Analysis, and Evaluation:**
- Determine what to monitor: Process performance, product conformity, customer satisfaction
- Determine methods and frequency
- Analyze data to evaluate QMS effectiveness
- **Compliance Action:** KPI dashboard, data analysis, reports

**9.1.2 Customer Satisfaction:**
- Monitor customer perceptions (are we meeting their needs?)
- Methods: Surveys, feedback, complaints, reviews, NPS
- **Compliance Action:** Customer satisfaction survey, feedback log, quarterly analysis

**9.1.3 Analysis and Evaluation:**
- Analyze data on: Product conformity, process performance, supplier performance, customer satisfaction, effectiveness of actions
- Use analysis to identify improvement opportunities
- **Compliance Action:** Monthly/quarterly data analysis report

**9.2 Internal Audit:**
- Audit QMS at planned intervals (annually or more frequently)
- Verify conformance to ISO 9001 and internal requirements
- Verify QMS is effectively implemented and maintained
- Audit criteria, scope, frequency, methods
- Auditor independence (don't audit your own work)
- Audit findings: Nonconformances, observations, opportunities
- Corrective actions for nonconformances
- **Compliance Action:** Audit schedule, audit procedures, audit reports, corrective action records

**9.3 Management Review:**
- Top management reviews QMS at planned intervals (quarterly recommended)
- Review inputs: Previous management review actions, changes, performance data, customer feedback, nonconformances, audit results, risks, improvement opportunities
- Review outputs: Decisions on improvements, resource needs, changes to QMS
- **Compliance Action:** Management review meeting agenda, meeting minutes, action items

**Clause 10: Improvement**

**10.1 General:**
- Continually improve suitability, adequacy, effectiveness of QMS
- Consider analysis and evaluation results
- **Compliance Action:** Continuous improvement program

**10.2 Nonconformity and Corrective Action:**
- When nonconformity occurs: React, control, correct
- Evaluate need for corrective action: Determine causes, determine if similar nonconformances exist elsewhere
- Implement corrective action: Actions to eliminate cause, prevent recurrence
- Review effectiveness of corrective action
- Update risks and opportunities if needed
- **Compliance Action:** Corrective action procedure, CAPA log, effectiveness verification

**10.3 Continual Improvement:**
- Proactive improvement (not just reactive)
- Methods: Kaizen events, Six Sigma, Lean, suggestion programs
- **Compliance Action:** Improvement projects, suggestion program, kaizen events

**COMPLIANCE CHECKLIST:**

**Documentation Required:**
- [ ] Quality Manual (scope, processes, procedures)
- [ ] Quality Policy and Objectives
- [ ] Process Maps and Procedures
- [ ] Work Instructions
- [ ] Forms and Templates
- [ ] Organizational chart and responsibilities

**Records Required:**
- [ ] Training records
- [ ] Internal audit reports
- [ ] Management review minutes
- [ ] Nonconformance and corrective action records
- [ ] Inspection and test records
- [ ] Customer feedback
- [ ] Supplier evaluations
- [ ] Calibration records
- [ ] Design records (if applicable)

**Activities Required:**
- [ ] Annual internal audits
- [ ] Quarterly management reviews
- [ ] Annual training plan and execution
- [ ] Ongoing monitoring of KPIs
- [ ] Customer satisfaction surveys
- [ ] Supplier performance reviews
- [ ] Risk assessments
- [ ] Corrective and preventive actions

**CERTIFICATION PROCESS:**

**Step 1: Gap Analysis**
- Compare current practices to ISO 9001 requirements
- Identify gaps (what's missing or inadequate?)
- Prioritize gaps by impact
- Estimated time: 2-4 weeks

**Step 2: Planning**
- Develop implementation plan
- Assign responsibilities
- Allocate resources (time, people, budget)
- Set timeline (typically 6-12 months to certification)

**Step 3: Documentation**
- Write Quality Manual, procedures, work instructions
- Develop forms and templates
- Train document control
- Estimated time: 2-3 months

**Step 4: Implementation**
- Train all staff on QMS
- Begin using procedures and forms
- Conduct internal audits
- Hold management reviews
- Track nonconformances and corrective actions
- Estimated time: 3-6 months (to establish track record)

**Step 5: Pre-Assessment (Optional)**
- Hire consultant or registrar for practice audit
- Identify remaining gaps
- Correct before formal audit
- Estimated time: 1-2 weeks

**Step 6: Certification Audit**
- Stage 1: Document review (off-site or quick on-site)
- Stage 2: Full on-site audit (2-5 days depending on size)
- Auditor reviews documentation, interviews staff, observes processes
- Nonconformances identified (major or minor)
- Estimated time: 1 week for Stage 1, 1 week for Stage 2

**Step 7: Corrective Actions**
- Address nonconformances found in audit
- Provide evidence of correction
- Estimated time: 2-4 weeks

**Step 8: Certification**
- If all requirements met, certificate issued
- Valid for 3 years
- Surveillance audits annually to maintain

**Step 9: Continual Improvement**
- Maintain QMS
- Prepare for annual surveillance audits
- Continually improve

**COSTS:**

**Implementation Costs:**
- Consultant (if used): $15,000-50,000
- Internal labor: 500-2,000 hours
- Training: $5,000-15,000
- Software (document control, etc.): $2,000-10,000/year
**Total Implementation:** $30,000-100,000 (depends on company size and current state)

**Certification Costs:**
- Certification body audit: $5,000-20,000 (depends on company size)
- Annual surveillance audits: $2,000-8,000
**Total First Year:** $7,000-28,000
**Annual Ongoing:** $2,000-8,000

**BENEFITS:**

**Tangible:**
- Fewer defects (reduced rework, scrap, warranty costs): 20-50% reduction
- Improved efficiency (streamlined processes): 10-30% productivity gain
- Better supplier performance (fewer incoming quality issues): 15-25% improvement
- Customer requirement (some customers require ISO 9001)

**Intangible:**
- Improved customer confidence
- Competitive advantage in bidding
- Better employee engagement (clear processes, less chaos)
- Foundation for continuous improvement

**ROI:**
Typical ROI of 2-5x within 2-3 years through defect reduction and efficiency gains.

**RECOMMENDATIONS:**

1. **Commit from the Top:**
   - CEO/senior leadership must champion quality
   - Allocate adequate resources
   - Lead by example

2. **Involve Frontline Staff:**
   - They know the processes best
   - Get their input on procedures
   - Train them well

3. **Start Simple:**
   - Don't over-document
   - Minimum documentation required: Quality Manual + 6 mandatory procedures + records
   - Add more as needed

4. **Use the Standard as Improvement Framework:**
   - ISO 9001 is about good business practice, not just certification
   - Even if you don't certify, the standard provides excellent structure

5. **Integrate with Business:**
   - QMS should be how you run the business, not a separate "quality system"
   - Integrate quality into daily work

This ISO 9001 compliance framework will establish a robust quality management system, improve consistency, reduce defects, and build customer confidence."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def inspection_protocols(inspection_requirements):
    """
    Design comprehensive inspection and testing protocols.
    Args: inspection_requirements - what needs to be inspected and how
    """
    prompt = f"""You are an Inspection Protocol Design System. Create detailed inspection protocols for: {inspection_requirements}

DEVELOP COMPREHENSIVE INSPECTION AND TESTING PROTOCOLS:

**INSPECTION STRATEGY OVERVIEW:**

**Inspection Philosophy:**
- **Prevention** > Detection > Correction (catch issues early)
- **Risk-based approach:** More inspection where risk is higher
- **100% inspection vs. Sampling:** Balance cost and risk
- **In-process inspection:** Don't wait until the end
- **First article inspection:** Verify setup before production run

**Types of Inspection:**
1. **Receiving Inspection** - Incoming materials/components
2. **In-Process Inspection** - During production
3. **Final Inspection** - Before shipment to customer
4. **First Article Inspection** - First unit from new setup/order
5. **Source Inspection** - At supplier's facility
6. **Patrol Inspection** - Random checks by roving inspector

**INSPECTION PROTOCOL TEMPLATE:**

**For Each Critical Product/Process:**

**Protocol ID:** [e.g., IP-001]
**Product/Process:** [Name and description]
**Revision:** [Version number and date]
**Approved By:** [Quality Manager]

**1. SCOPE:**
- What is being inspected? [Product, component, process step]
- When is inspection performed? [Receiving, in-process, final]
- Where? [Location: receiving dock, production line station 3, final assembly]

**2. INSPECTION FREQUENCY:**
- **100% Inspection:** Every unit inspected (for critical characteristics)
- **Sampling:** Inspect ___ units per batch (use sampling plan, e.g., AQL 2.5%, Level II)
- **Frequency:** Every batch / Every shift / Every ___ hours / As needed

**3. INSPECTION CHARACTERISTICS:**

| Characteristic | Specification | Inspection Method | Measurement Tool | Accept/Reject Criteria |
|----------------|---------------|-------------------|------------------|------------------------|
| Dimension A | 10.0 ± 0.1 mm | Measurement | Caliper (±0.01mm) | Accept: 9.9-10.1mm |
| Surface Finish | Ra <1.6 μm | Measurement | Profilometer | Accept: Ra ≤1.6 |
| Visual | No cracks, chips | Visual | Naked eye / 10x mag | Reject: Any crack visible |
| Functional Test | Operates per spec | Functional test | Test fixture | Pass functional test |
| Weight | 100-110 grams | Measurement | Scale (±0.1g) | Accept: 100-110g |
[List all critical characteristics]

**Critical vs. Major vs. Minor Defects:**
- **Critical:** Safety or functionality severely impaired (reject immediately, stop production)
- **Major:** Significant degradation (affects performance, reduces life)
- **Minor:** Cosmetic or slight deviation (document but may accept)

**4. INSPECTION PROCEDURE:**

**Step-by-Step Instructions:**

**Step 1: Preparation**
- Verify measuring equipment is calibrated (check calibration stickers)
- Clean part/product (remove debris, oil)
- Review product specifications and drawings
- Prepare inspection report form

**Step 2: Visual Inspection**
- Inspect for obvious defects: cracks, chips, scratches, dents, discoloration
- Check labeling: Correct labels, legible, properly adhered
- Check packaging: Damaged box, missing components
- Document any visual defects

**Step 3: Dimensional Inspection**
- Measure [Characteristic 1]: [Specific measurement location/method]
  * Tool: [Caliper / Micrometer / CMM]
  * Procedure: [Zero tool, measure at 3 points, record average]
  * Acceptance: [10.0 ± 0.1 mm]
- Measure [Characteristic 2]: [...]
[Continue for all dimensions]

**Step 4: Functional Testing**
- Test [Function 1]: [How to test]
  * Expected result: [...]
  * Pass criteria: [...]
- Test [Function 2]: [...]
[Continue for all functions]

**Step 5: Documentation**
- Record all measurements on inspection report
- Mark part: Pass (green sticker) / Fail (red tag)
- For failures: Complete nonconformance report
- For pass: Release to next operation or ship

**Step 6: Disposition**
- **Accept:** Release to next step or shipping
- **Reject:** Tag with red "HOLD" tag, segregate in rejection area, complete NCR
- **Use-As-Is:** If defect is minor and customer approves (document approval)
- **Rework:** If defect is correctable (re-inspect after rework)
- **Return to Supplier:** If purchased part (RMA process)

**5. SAMPLING PLAN (if not 100%):**

**For Lot/Batch Inspection:**

Use ANSI/ASQ Z1.4 (formerly MIL-STD-105E) sampling tables:

- **Lot Size:** [e.g., 1,000 units]
- **Inspection Level:** II (normal)
- **AQL (Acceptable Quality Level):** 
  * Critical defects: 0% (zero defects allowed)
  * Major defects: 2.5%
  * Minor defects: 4.0%
- **Sample Size:** [From table: e.g., n=80 for lot size 1,000, Level II]
- **Acceptance Number (Ac):** [From table: e.g., Ac=5 for AQL 2.5%]
- **Rejection Number (Re):** [From table: e.g., Re=6]

**Interpretation:**
- Inspect 80 random units from lot of 1,000
- If ≤5 defects found: Accept entire lot
- If ≥6 defects found: Reject entire lot (100% sorting or return to supplier)

**Tightened vs. Normal vs. Reduced Inspection:**
- Start with **Normal** inspection
- Switch to **Tightened** (stricter) if quality degrades (2 out of 5 lots rejected)
- Switch to **Reduced** (less sampling) if quality is consistently good (10 lots accepted)
- This adjusts inspection intensity based on supplier/process performance

**6. CALIBRATION REQUIREMENTS:**

**Equipment Used:**
- Caliper: Calibrate annually (±0.01mm accuracy required)
- Micrometer: Calibrate annually
- Test fixture: Calibrate semi-annually
- Scale: Calibrate annually

**Calibration Procedure:**
- Send to certified calibration lab
- Verify against NIST-traceable standards
- Affix calibration sticker (date, due date, serial number)
- Maintain calibration records

**Out-of-Calibration Action:**
- Immediately remove from service
- Review all inspections performed since last calibration (are results valid?)
- Re-inspect if necessary

**7. TRAINING:**

**Required Training:**
- New inspector: 40 hours (1 week) training + 80 hours (2 weeks) supervised practice
- Annual refresher: 8 hours
- Training on new procedures: As needed

**Training Content:**
- How to use measuring instruments (hands-on)
- How to read drawings and specifications
- Inspection procedure walkthroughs
- Nonconformance reporting
- Safety (handling sharp parts, heavy lifting)

**Competency Verification:**
- Written test (80% passing score)
- Practical test (inspect 10 parts, results must match known good/bad)
- Annual competency check

**8. RECORDS:**

**Inspection Records to Maintain:**
- Inspection report for each lot/batch (or each unit if 100%)
- Nonconformance reports (NCRs) for all rejections
- Corrective action records (for systemic issues)
- Calibration records for all measurement equipment
- Training records for all inspectors

**Retention:**
- Inspection records: 7 years (or per customer requirement)
- Calibration records: Life of equipment + 3 years
- Training records: Duration of employment + 3 years

**9. CONTINUOUS IMPROVEMENT:**

**Data Analysis:**
- Track defect rates by type, supplier, production line
- Pareto analysis: Which defects are most common?
- Trend analysis: Is quality improving or degrading?

**Root Cause Analysis:**
- For recurring defects, conduct root cause investigation (5 Whys, Fishbone)
- Implement corrective actions
- Verify effectiveness

**Process Improvement:**
- Mistake-proofing (poka-yoke): Design processes to prevent defects
- Automation: Automated inspection (vision systems, sensors)
- Supplier development: Help suppliers improve quality

**EXAMPLE INSPECTION PROTOCOLS:**

**Example 1: Micro-Hydro Turbine Runner Inspection**

**Critical Characteristics:**
- Runner diameter: 300 ± 1 mm (affects power output)
- Surface roughness: Ra <0.8 μm (affects efficiency)
- Balance: <5 gram-mm (vibration)
- Material: 316 stainless steel (corrosion resistance)
- No cracks or voids (safety)

**Inspection Method:**
- Receiving inspection (from supplier): 100% inspection
- Dimensional: CMM or manual caliper at 4 points
- Surface: Profilometer at 3 locations
- Balance: Dynamic balancing machine
- Material: Review mill cert, verify hardness spot check
- Visual: 10x magnification for cracks

**Accept/Reject:**
- All dimensions within tolerance: Accept
- Any dimension out of tolerance: Reject, return to supplier
- Any crack detected: Reject immediately

**Example 2: Electrical Panel Final Inspection**

**Critical Characteristics:**
- Wiring per schematic (correct connections)
- Torque on terminals: 35 ± 5 in-lbs
- Insulation resistance: >10 MΩ
- Ground continuity: <1 Ω
- Functional test: All functions operate
- Labeling: All components labeled

**Inspection Method:**
- 100% final inspection before shipment
- Visual: Compare wiring to schematic
- Torque: Torque wrench verification of all terminals
- Insulation: Megohmmeter test
- Ground: Continuity tester
- Functional: Energize and test all functions
- Labels: Visual check

**Example 3: Supplier Receiving Inspection (Sampling)**

**Product:** Bolts (purchased parts)
**Lot Size:** 5,000 bolts
**Critical Characteristics:**
- Length: 50 ± 0.5 mm
- Thread: M10 x 1.5
- Material: Grade 8.8 steel
- No visible defects

**Sampling Plan:**
- Inspection Level: II
- AQL: 1.0% (major defects)
- Sample Size: n=125 (from table for lot size 5,000)
- Acceptance Number: Ac=3
- Rejection Number: Re=4

**Procedure:**
- Randomly select 125 bolts from lot
- Measure length (10 samples): Must be 49.5-50.5 mm
- Check thread with go/no-go gauge: Must pass
- Visual inspection (all 125): No cracks, corrosion, bent threads
- If ≤3 defects in sample: Accept lot
- If ≥4 defects in sample: Reject entire lot, return to supplier

**BEST PRACTICES:**

1. **Clearly Define Accept/Reject Criteria:**
   - No ambiguity (inspector should not guess)
   - Use objective measurements where possible
   - For subjective (visual), use photo standards (good vs. bad examples)

2. **Train Inspectors Well:**
   - Consistent interpretation of standards
   - Proficiency with measurement tools
   - Empowered to stop production if critical defect

3. **Calibrate Equipment:**
   - Measurement validity depends on calibrated equipment
   - Never skip calibration

4. **Document Everything:**
   - If it's not documented, it didn't happen
   - Critical for traceability and liability

5. **Act on Data:**
   - Don't just inspect and forget
   - Analyze trends, implement improvements
   - Close the loop

6. **Balance Inspection Cost vs. Risk:**
   - 100% inspection for critical characteristics (safety, function)
   - Sampling for less critical (cost-effective)
   - As process capability improves, may reduce inspection

This comprehensive inspection protocol framework will ensure consistent quality, catch defects before they reach customers, and provide data for continuous improvement."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def defect_tracking(quality_issues):
    """
    Track defects, analyze patterns, and implement corrective actions.
    Args: quality_issues - description of quality issues to track
    """
    prompt = f"""You are a Defect Tracking and Analysis System. Create comprehensive defect management framework for: {quality_issues}

CREATE COMPLETE DEFECT TRACKING AND CORRECTIVE ACTION SYSTEM:

**DEFECT MANAGEMENT OVERVIEW:**

**Purpose:**
- Capture all nonconformances (defects, deviations, customer complaints)
- Analyze patterns to identify systemic issues
- Implement corrective actions to prevent recurrence
- Track effectiveness of corrective actions
- Drive continuous improvement

**Scope:**
- Internal defects (caught before shipment)
- Customer complaints (escaped defects)
- Supplier nonconformances
- Process deviations
- Documentation errors

**DEFECT TRACKING SYSTEM:**

**Nonconformance Report (NCR) Template:**

**NCR #:** [Auto-generated unique number, e.g., NCR-2026-0001]
**Date Issued:** [Date]
**Reported By:** [Name, Department]
**Priority:** ⚠️ Critical / 🟡 Major / 🔵 Minor

**SECTION 1: DEFECT DESCRIPTION**

**Product/Process Affected:**
- Part Number: [e.g., P/N 12345]
- Description: [Product name]
- Lot/Batch/Serial Number: [For traceability]
- Quantity Affected: [Number of units]
- Location Found: [Receiving / In-Process / Final Inspection / Customer Site]

**Defect Type:**
- [ ] Dimensional (out of tolerance)
- [ ] Visual (scratch, dent, discoloration)
- [ ] Functional (doesn't work as intended)
- [ ] Material (wrong material, contamination)
- [ ] Documentation (missing, incorrect)
- [ ] Other: [Describe]

**Detailed Description:**
[What exactly is wrong? Be specific. Include measurements, photos, etc.]

**Specification/Requirement:**
[What was the requirement? Drawing, spec, customer PO, standard]

**Actual Condition:**
[What did we find? Measurements, observations]

**SECTION 2: CONTAINMENT (Immediate Action)**

**Containment Actions Taken:**
- [ ] Segregate nonconforming product (red tag, hold area)
- [ ] Stop production (if defect is being produced)
- [ ] Notify customer (if already shipped)
- [ ] Inspect similar products (check if issue is widespread)
- [ ] Implement 100% sorting (screen remaining inventory)

**Responsibility:** [Who is responsible for containment?]
**Target Date:** [When must containment be complete?]
**Actual Completion:** [When was it completed?]
**Verified By:** [QA Manager]

**SECTION 3: DISPOSITION (What to do with nonconforming product?)**

**Disposition Decision:**
- [ ] **Scrap** - Product cannot be used, discard
- [ ] **Rework** - Product can be corrected to meet requirements
  * Rework procedure: [Describe what needs to be done]
  * Re-inspection required: Yes
  * Rework completed by: [Name]
  * Re-inspection result: Pass / Fail
- [ ] **Use-As-Is** - Product doesn't meet spec but is acceptable
  * Justification: [Why is it acceptable?]
  * Customer approval required: Yes / No
  * Customer approval obtained: [Date, name]
- [ ] **Return to Supplier** - If purchased part
  * RMA #: [Return authorization number]
  * Supplier notified: [Date]
  * Replacement ETA: [Date]
- [ ] **Sort/Grade** - Segregate good from bad units
  * Number sorted: [___]
  * Good: [___], Bad: [___]
  * Disposition of bad units: Scrap / Rework

**Approved By:** [Quality Manager, Date]
**Customer Approval:** [If required, name and date]

**SECTION 4: ROOT CAUSE ANALYSIS**

**Investigation Required?**
- [ ] Yes - For major/critical defects or recurring issues
- [ ] No - For minor, isolated incidents

**Root Cause Analysis Method:**
- [ ] 5 Whys
- [ ] Fishbone Diagram (Ishikawa)
- [ ] Fault Tree Analysis
- [ ] Other: [Method]

**5 Whys Example:**
1. **Why did the defect occur?** [First-level cause]
2. **Why did that happen?** [Second-level cause]
3. **Why did that happen?** [Third-level cause]
4. **Why did that happen?** [Fourth-level cause]
5. **Why did that happen?** [Root cause - stop when you reach controllable cause]

**Root Cause Identified:**
[Statement of root cause. Should be something the company can control.]

**Contributing Factors:**
[Other factors that contributed, even if not primary root cause]

**SECTION 5: CORRECTIVE ACTION (Prevent Recurrence)**

**Corrective Actions:** (Address root cause)

**Action 1:** [Specific action to prevent recurrence]
- Responsibility: [Who will do it?]
- Target Date: [When?]
- Resources Required: [Budget, equipment, training]
- Status: Open / In Progress / Complete

**Action 2:** [...]

**Action 3:** [...]

**Examples of Corrective Actions:**
- Revise procedure/work instruction
- Provide additional training
- Implement mistake-proofing (poka-yoke)
- Change supplier
- Redesign product/process
- Add inspection point
- Improve maintenance
- Upgrade equipment

**SECTION 6: PREVENTIVE ACTION (Prevent Similar Issues Elsewhere)**

**Are there similar situations where this could happen?**
- Yes / No

**If Yes, Preventive Actions:**
[Apply lessons learned to similar processes, products, or suppliers]

**SECTION 7: VERIFICATION OF EFFECTIVENESS**

**How will we verify corrective action worked?**
- [ ] Monitor defect rate for next ___ weeks (should decrease)
- [ ] Re-audit process
- [ ] Customer feedback (if customer-facing)
- [ ] Statistical analysis (control charts)

**Effectiveness Check:**
- Date Checked: [___]
- Result: Effective / Not Effective / Partially Effective
- If Not Effective: Revise corrective action and repeat

**SECTION 8: COST IMPACT** (Optional but recommended)

**Direct Costs:**
- Scrap cost: $___ (___ units × $___ per unit)
- Rework labor: $___ (___ hours × $___ per hour)
- Rework materials: $___
- Sorting/inspection: $___ (___ hours × $___ per hour)
- Expedited shipping (replacement): $___
- **Total Direct Cost:** $___

**Indirect Costs:**
- Engineering time: $___
- Management time: $___
- Production downtime: $___
- Lost sales/revenue: $___
- **Total Indirect Cost:** $___

**Customer Impact:**
- Warranty cost: $___
- Customer goodwill: $___
- **Total Customer Impact:** $___

**TOTAL COST OF QUALITY ISSUE:** $___

[This cost justifies spending on corrective actions to prevent recurrence]

**SECTION 9: CLOSURE**

**Completed By:** [Name, Title]
**Date Closed:** [Date]
**Approved By:** [Quality Manager]

**Status:**
- [ ] Open (initial report)
- [ ] Containment Complete (immediate actions done)
- [ ] Root Cause Identified (investigation complete)
- [ ] Corrective Action Implemented (actions taken)
- [ ] Effectiveness Verified (confirmed it worked)
- [ ] Closed (issue fully resolved)

---

**DEFECT DATABASE SYSTEM:**

**Fields to Track:**
- NCR Number (unique ID)
- Date Opened
- Date Closed
- Product/Part Number
- Defect Type (category)
- Defect Description (text)
- Quantity Affected
- Location Found (receiving, in-process, final, customer)
- Disposition (scrap, rework, use-as-is, return)
- Root Cause (text)
- Corrective Actions (text)
- Cost ($)
- Status (open, closed)
- Assigned To (owner)
- Priority (critical, major, minor)

**Software Options:**
- **Simple:** Excel spreadsheet or Google Sheets
- **Better:** Database (Access, Filemaker)
- **Best:** QMS software (ETQ, MasterControl, Arena) or custom web app

**DEFECT ANALYSIS AND REPORTING:**

**Weekly Defect Summary:**

**Open NCRs:**
- Total Open: ___
- By Priority: Critical ___, Major ___, Minor ___
- Aging: >30 days ___, >60 days ___ (escalate these!)

**NCRs Closed This Week:** ___

**New NCRs This Week:** ___

**Top 5 Defect Types:** (Pareto Analysis)
1. [Defect Type] - ___ occurrences (___% of total)
2. [Defect Type] - ___ occurrences
3. [Defect Type] - ___ occurrences
4. [Defect Type] - ___ occurrences
5. [Defect Type] - ___ occurrences

**Action Items:**
- Investigate [Defect Type #1] - Most frequent
- Follow up on overdue corrective actions (list)

**Monthly Defect Report:**

**Defect Metrics:**

**Internal Defect Rate:**
- Formula: (Defective Units / Total Units Inspected) × 100%
- This Month: ___%
- Last Month: ___%
- Trend: ↗ Improving / → Stable / ↘ Worsening
- Target: <1%

**Customer Defect Rate (Escaped Defects):**
- Formula: (Customer Complaints / Units Shipped) × 1,000,000 (PPM - parts per million)
- This Month: ___ PPM
- Last Month: ___ PPM
- Trend: ↗ / → / ↘
- Target: <100 PPM (world-class <10 PPM)

**Cost of Quality:**
- Total Cost of Defects This Month: $___
- As % of Revenue: ___%
- Target: <2% of revenue

**First Pass Yield:**
- Formula: (Units Passed First Inspection / Total Units Inspected) × 100%
- This Month: ___%
- Target: >99%

**Defect Pareto Chart:**
[Bar chart showing defect types ranked by frequency]
- Focus improvement efforts on top 2-3 defect types (80/20 rule)

**Defect Trend Analysis:**
[Line chart showing defect rate over time - last 12 months]
- Is defect rate improving? (goal: yes)
- Identify months with spikes (what happened?)

**Defects by Source:**
| Source | Count | % of Total | Action |
|--------|-------|------------|--------|
| Supplier A | 25 | 40% | Supplier quality issue - escalate |
| Internal Process X | 15 | 24% | Process improvement needed |
| Design Issue | 10 | 16% | Engineering review |
| Operator Error | 8 | 13% | Training needed |
| Other | 4 | 7% | |

**Corrective Action Status:**
- Total Open Corrective Actions: ___
- On-Time: ___ (___%)
- Overdue: ___ (___%) [RED FLAG - escalate]
- Target: >95% on-time

**Quarterly Defect Review:**
[Detailed analysis for management review]

- Summary of quarter's performance
- Year-over-year comparison
- Breakthrough issues (what got fixed?)
- Persistent issues (what's not improving?)
- Cost impact (total cost of quality)
- Recommendations for next quarter

**BEST PRACTICES:**

**1. Make It Easy to Report:**
- Simple form (paper or electronic)
- Encourage reporting (no blame culture)
- Anyone can report (operator, inspector, customer service, engineer)
- Acknowledge reports promptly

**2. Respond Quickly:**
- Containment within 24 hours (prevent more defects)
- Root cause within 1 week (for major issues)
- Corrective action within 30 days
- Verify effectiveness within 90 days

**3. Focus on Prevention:**
- Root cause analysis (not just symptoms)
- Permanent corrective actions (not band-aids)
- Preventive actions (apply lessons learned elsewhere)
- Mistake-proofing (design out the possibility of error)

**4. Close the Loop:**
- Verify effectiveness (did corrective action work?)
- Track trends (is defect rate decreasing?)
- Share learnings (educate organization)

**5. Use Data:**
- Pareto analysis (focus on vital few)
- Trend analysis (early warning of problems)
- Cost of quality (justify improvement investments)

**6. Management Engagement:**
- Review defect metrics monthly
- Hold teams accountable for corrective actions
- Celebrate improvements
- Provide resources for quality initiatives

**CORRECTIVE ACTION LIFECYCLE:**

**Stage 1: Detection** (Day 0)
- Defect discovered
- NCR created
- Containment initiated

**Stage 2: Containment** (Day 0-1)
- Immediate actions to prevent more defects
- Segregate bad product
- Stop production if needed

**Stage 3: Disposition** (Day 1-3)
- Decide what to do with nonconforming product
- Scrap, rework, use-as-is, return
- Obtain approvals if needed

**Stage 4: Investigation** (Day 3-10)
- Root cause analysis
- 5 Whys, Fishbone, data analysis
- Identify root cause and contributing factors

**Stage 5: Corrective Action** (Day 10-30)
- Develop and implement corrective actions
- Address root cause (prevent recurrence)
- Document actions taken

**Stage 6: Verification** (Day 30-90)
- Monitor results (is defect rate decreasing?)
- Verify corrective action effectiveness
- Adjust if needed

**Stage 7: Closure** (Day 90)
- Close NCR
- Share lessons learned
- Update procedures/training

**TOOLS AND TEMPLATES:**

**Nonconformance Report Form:**
[8.5" x 11" form or electronic form in QMS software]

**Defect Tracking Spreadsheet:**
[Excel template with all fields listed above]

**Pareto Chart Template:**
[Excel chart showing defect types by frequency]

**Cost of Quality Calculator:**
[Spreadsheet to calculate total cost impact]

**Corrective Action Plan Template:**
[Action, Owner, Due Date, Status format]

**RECOMMENDATIONS:**

1. **Implement NCR System Immediately:**
   - Start capturing all defects (visibility is first step)
   - Train team on how to write NCRs

2. **Weekly Review:**
   - Operations Manager + Quality Manager
   - Review new NCRs, status of corrective actions
   - Escalate overdue items

3. **Monthly Analysis:**
   - Calculate defect metrics
   - Generate Pareto chart
   - Report to management

4. **Focus on Top 3:**
   - Tackle top 3 defect types (biggest impact)
   - Assign project teams
   - Measure results

5. **Target Metrics:**
   - Internal defect rate <1%
   - Customer defect rate <100 PPM
   - First pass yield >99%
   - Cost of quality <2% revenue

This defect tracking and corrective action system will drive systematic quality improvement, reduce costs, and increase customer satisfaction."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


def quality_improvement(improvement_goals):
    """
    Design and implement quality improvement initiatives.
    Args: improvement_goals - quality improvement targets and initiatives
    """
    prompt = f"""You are a Quality Improvement Program Manager. Design comprehensive quality improvement program for: {improvement_goals}

CREATE COMPLETE QUALITY IMPROVEMENT PROGRAM:

**QUALITY IMPROVEMENT FRAMEWORK:**

**Current State Baseline:**
- Current defect rate: ___%
- Current first pass yield: ___%
- Current customer complaints: ___ per month
- Current cost of quality: $___/month (___% of revenue)
- Current customer satisfaction: ___/10

**Target State (12-Month Goals):**
- Target defect rate: <1% (___% improvement)
- Target first pass yield: >99%
- Target customer complaints: <___ per month (___% reduction)
- Target cost of quality: <2% of revenue
- Target customer satisfaction: >8.5/10

**Gap Analysis:**
- Current vs. Target defect rate: ___% gap
- Financial opportunity: $___ per year in defect costs to eliminate
- Customer satisfaction gap: ___ points

**QUALITY IMPROVEMENT METHODOLOGIES:**

**Methodology 1: Six Sigma (DMAIC)**

**Best For:** Data-driven process improvement, reducing variation

**DMAIC Process:**

**D - Define:**
- Define the problem (what are we trying to improve?)
- Define project scope (boundaries)
- Define customer requirements (what do they need?)
- Form project team (who will work on this?)
- Create project charter (1-2 page document)

**M - Measure:**
- Map current process (flowchart)
- Identify key metrics (CTQs - Critical to Quality)
- Establish baseline (how bad is it now?)
- Develop data collection plan
- Measure current performance (collect data for 2-4 weeks)

**A - Analyze:**
- Analyze data (graphs, charts, statistical analysis)
- Identify root causes (5 Whys, Fishbone diagram)
- Validate root causes (test hypotheses)
- Prioritize causes (which have biggest impact?)

**I - Improve:**
- Generate potential solutions (brainstorming)
- Evaluate solutions (feasibility, cost, impact)
- Select best solution(s)
- Pilot test solutions (small scale first)
- Implement full-scale

**C - Control:**
- Develop control plan (how to sustain improvement?)
- Implement process controls (visual management, checklists, mistake-proofing)
- Train staff on new process
- Monitor performance (control charts)
- Document standardized procedure
- Close project and celebrate success

**Timeline:** 3-6 months per project
**Team Size:** 3-6 people
**Tools:** Statistical analysis, process mapping, brainstorming, piloting

**Methodology 2: Lean (Eliminate Waste)**

**Best For:** Reducing waste, improving flow, increasing efficiency

**7 Wastes (TIMWOOD):**
1. **Transportation** - Moving materials/products unnecessarily
2. **Inventory** - Excess stock (ties up cash, hides problems)
3. **Motion** - Unnecessary movement of people (walking, reaching, searching)
4. **Waiting** - Idle time (waiting for approvals, materials, information)
5. **Overproduction** - Making more than needed or before needed
6. **Overprocessing** - Doing more work than customer values
7. **Defects** - Rework, scrap, warranty costs

**Lean Tools:**
- **Value Stream Mapping:** Map entire process, identify waste
- **5S:** Sort, Set in Order, Shine, Standardize, Sustain (workplace organization)
- **Kanban:** Pull system (produce only what's needed when needed)
- **Kaizen:** Continuous improvement events (focused 2-5 day workshops)
- **Poka-Yoke:** Mistake-proofing (design process to prevent errors)
- **SMED:** Single-Minute Exchange of Dies (quick changeovers)

**Methodology 3: Kaizen Events**

**Best For:** Rapid improvement of specific process

**What is Kaizen?**
- Japanese word meaning "continuous improvement"
- Focused improvement event (typically 3-5 days)
- Cross-functional team
- Hands-on, action-oriented
- Measurable results by end of week

**Kaizen Event Structure:**

**Monday: Define and Measure**
- Project kickoff, team introductions
- Define problem and goals
- Map current state process
- Collect baseline data
- Identify waste and opportunities

**Tuesday-Wednesday: Analyze and Improve**
- Root cause analysis
- Brainstorm solutions
- Evaluate and select solutions
- Begin implementation (rearrange workspace, create new forms, etc.)

**Thursday: Implement and Test**
- Complete implementation
- Test new process
- Refine as needed
- Train staff

**Friday: Control and Present**
- Document new standard procedure
- Create control plan
- Calculate results (time saved, quality improved, cost reduced)
- Present to management (celebrate success!)

**Results:**
- Typical cycle time reduction: 30-50%
- Typical defect reduction: 50-70%
- Immediate implementation (not just recommendations)

**Methodology 4: Plan-Do-Check-Act (PDCA)**

**Best For:** Simple, iterative problem-solving

**Plan:**
- Identify problem or opportunity
- Analyze root causes
- Develop action plan

**Do:**
- Implement plan on small scale (pilot)
- Document what happens

**Check:**
- Evaluate results
- Did it work? How well?
- What did we learn?

**Act:**
- If successful: Standardize and implement full-scale
- If unsuccessful: Adjust plan and repeat PDCA cycle
- Either way, start next PDCA cycle (continuous improvement)

**QUALITY IMPROVEMENT PROJECTS:**

**Project Prioritization:**

**High-Impact Projects (Start Here):**

**Project 1: Reduce [Top Defect Type]**
- **Current State:** [Defect type] occurs ___ times per month, costs $___
- **Goal:** Reduce by 80% within 3 months
- **Approach:** Six Sigma DMAIC
- **Team:** Quality Engineer (lead), Production Manager, Operator, Maintenance Tech
- **Timeline:** 3 months
- **Expected Savings:** $___ per year

**Project 2: Improve First Pass Yield at [Process Step]**
- **Current State:** FPY = ___% (___% rework/scrap)
- **Goal:** FPY >95%
- **Approach:** Kaizen event
- **Timeline:** 1 week event + 30 days follow-up
- **Expected Savings:** ___ hours rework eliminated = $___/year

**Project 3: Supplier Quality Improvement**
- **Current State:** Supplier A has ___% defect rate (highest of all suppliers)
- **Goal:** Reduce to <1%
- **Approach:** Supplier audit, corrective actions, monitoring
- **Timeline:** 3 months
- **Expected Savings:** Fewer incoming defects, less sorting = $___/year

[List 5-10 priority projects]

**IMPLEMENTATION ROADMAP:**

**Quarter 1:**
- Launch 2-3 high-impact projects (DMAIC or Kaizen)
- Train 5-10 people on quality improvement tools
- Establish monthly project review meetings
- Target: 30% reduction in top defect type

**Quarter 2:**
- Continue Q1 projects to completion
- Launch 2-3 additional projects
- Conduct 2 Kaizen events
- Target: 50% reduction in defect rate, FPY >97%

**Quarter 3:**
- Implement control plans from completed projects
- Launch 2-3 more projects (address next-tier issues)
- Expand training (15-20 people trained)
- Target: Defect rate <1.5%, FPY >98%

**Quarter 4:**
- Complete all active projects
- Verify sustainability (are improvements holding?)
- Plan next year's projects
- Target: Defect rate <1%, FPY >99%, 50% reduction in cost of quality

**TOOLS AND TRAINING:**

**Training Plan:**
- **Quality Basics (all staff, 4 hours):**
  * Importance of quality
  * How to identify and report defects
  * Everyone's role in quality
- **Quality Tools (supervisors/leads, 16 hours):**
  * Process mapping
  * Root cause analysis (5 Whys, Fishbone)
  * Pareto analysis
  * Control charts
  * Problem solving (PDCA, 8D)
- **Six Sigma Green Belt (quality engineers, 40 hours):**
  * DMAIC methodology
  * Statistical analysis
  * Project management
  * Leading improvement projects
- **Kaizen Facilitation (managers, 16 hours):**
  * How to run a Kaizen event
  * Team facilitation
  * Change management

**Total Training Investment:** ~$20,000-40,000

**Tools/Software:**
- Minitab or Stat graphics (statistical analysis): $1,500/year
- Process mapping software (Visio, Lucidchart): $500/year
- Quality management system (optional but recommended): $5,000-20,000/year

**GOVERNANCE:**

**Quality Council:**
- **Members:** CEO, COO, Quality Manager, Engineering Manager, Operations Manager
- **Frequency:** Monthly
- **Purpose:** 
  * Review quality metrics and trends
  * Approve improvement projects
  * Allocate resources
  * Remove roadblocks
  * Celebrate successes

**Project Review Meetings:**
- **Frequency:** Bi-weekly
- **Attendees:** All project team leads + Quality Manager
- **Purpose:**
  * Status updates (schedule, results)
  * Issue escalation
  * Share learnings
  * Coordinate resources

**CHANGE MANAGEMENT:**

**Communication:**
- Town hall kickoff: Announce quality improvement program
- Monthly newsletter: Project updates, success stories
- Visual management: Metrics posted in production area
- Recognition: Celebrate team successes

**Training:**
- Train everyone on quality basics
- Train project teams on improvement tools
- Just-in-time training (before projects start)

**Engagement:**
- Involve frontline staff (they know the problems best)
- Encourage suggestions (suggestion box, digital forms)
- Respond to all suggestions (even if not implemented, explain why)
- Reward contributions (recognition, small monetary awards)

**Leadership:**
- Management must champion quality (walk the talk)
- Allocate adequate resources (people, time, budget)
- Hold teams accountable (track project progress)
- Remove barriers (bureaucracy, turf wars)

**SUCCESS METRICS:**

**Lagging Indicators (Results):**
- Defect rate: ___% → <1%
- First pass yield: ___% → >99%
- Customer complaints: ___ → <___ per month
- Cost of quality: $___/month → <2% revenue
- Customer satisfaction: ___/10 → >8.5/10

**Leading Indicators (Activities):**
- Number of active improvement projects: ___ (target 5-10)
- Number of people trained: ___ (target 20-30 in year 1)
- Number of improvement ideas submitted: ___ per month
- Percentage of projects on schedule: >80%
- Percentage of corrective actions on-time: >95%

**Financial Metrics:**
- Cost savings from projects: $___/year (target $100k+ in year 1)
- ROI on quality program: ___% (savings / investment)
- Payback period: ___ months (typically 6-12 months)

**CULTURAL TRANSFORMATION:**

**From:** "Quality is Quality Department's job"
**To:** "Quality is everyone's job"

**From:** "We've always done it this way"
**To:** "How can we do it better?"

**From:** "Don't bring me problems"
**To:** "Bring me problems and ideas"

**From:** "Blame culture" (who screwed up?)
**To:** "Learning culture" (what can we learn? how do we prevent it?)

**Actions to Build Quality Culture:**
1. Make quality visible (metrics posted, talked about)
2. Reward quality (not just output)
3. Stop and fix problems (don't just work around them)
4. Learn from mistakes (root cause, not blame)
5. Empower frontline (they can stop production if quality issue)
6. Continuous improvement mindset (always ask "can we do better?")

**BEST PRACTICES:**

1. **Start with Quick Wins:**
   - Build momentum and credibility
   - Show that improvement is possible
   - Demonstrate ROI

2. **Focus on Vital Few:**
   - 80/20 rule: 20% of defect types = 80% of cost
   - Pareto analysis to prioritize
   - Don't try to fix everything at once

3. **Use Data:**
   - Measure baseline (how bad is it?)
   - Track progress (is it improving?)
   - Prove results (show savings, not just activity)

4. **Engage Frontline:**
   - They know where the problems are
   - They have ideas (often overlooked)
   - They must implement solutions (buy-in critical)

5. **Sustain Improvements:**
   - Standardize new procedures
   - Train everyone
   - Monitor compliance
   - Audit periodically

6. **Celebrate Successes:**
   - Recognize teams publicly
   - Share success stories
   - Small rewards (gift cards, lunch, trophy)
   - Build positive momentum

**ROI CALCULATION:**

**Investment:**
- Training: $30,000
- Tools/software: $10,000
- Project team time: 1,000 hours × $50/hr = $50,000
- Consultant (optional): $50,000
**Total Year 1 Investment:** $140,000

**Return:**
- Defect reduction (scrap, rework): $200,000/year
- Efficiency improvement (less touch time): $100,000/year
- Customer retention (fewer complaints): $50,000/year
- Warranty cost reduction: $30,000/year
**Total Annual Benefit:** $380,000/year

**ROI:** ($380k - $140k) / $140k = **171% first year**
**Payback Period:** 5 months

**Years 2-3:** Continued benefits with lower investment (sustain mode) → 300-500% ROI

**RECOMMENDATIONS:**

1. **Commit to Quality:**
   - CEO/leadership must champion
   - Allocate budget and resources
   - Make it strategic priority

2. **Start Now:**
   - Pick 2-3 quick-win projects
   - Form teams and launch
   - Show results in 90 days

3. **Build Capability:**
   - Train 20-30 people in year 1
   - Develop internal expertise
   - Reduce reliance on consultants

4. **Track and Report:**
   - Monthly quality metrics to management
   - Quarterly business review
   - Celebrate wins publicly

5. **Make It Sustainable:**
   - Institutionalize (part of how we work)
   - Continuous improvement, not one-time program
   - Multi-year commitment

**Target Outcome:**
Within 12 months, reduce defects by 75%, improve first pass yield to >99%, reduce cost of quality by 50%, and deliver 150-300% ROI on quality improvement investment. Build a culture of continuous improvement that sustains results for years to come.

This comprehensive quality improvement program will systematically eliminate defects, improve processes, reduce costs, and build a quality-focused culture."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=4000
    )
    
    return response.choices[0].message.content


# CLI Interface
if __name__ == "__main__":
    print("\n✅ Quality Control Agent initialized (Groq - FREE)\n")
    
    import sys
    if len(sys.argv) < 2:
        print("QUALITY CONTROL AGENT")
        print("\nCommands:")
        print("  standards    - Ensure standards compliance (ISO 9001, etc.)")
        print("  inspection   - Design inspection protocols")
        print("  defects      - Track and analyze defects")
        print("  improvement  - Design quality improvement initiatives")
        print("\nUsage: python quality_control.py <command> <parameters>")
        print("Example: python quality_control.py standards 'ISO 9001:2015 compliance'")
        sys.exit(0)
    
    command = sys.argv[1].lower()
    params = sys.argv[2] if len(sys.argv) > 2 else "quality management"
    
    if command == "standards":
        print(standards_compliance(params))
    elif command == "inspection":
        print(inspection_protocols(params))
    elif command == "defects":
        print(defect_tracking(params))
    elif command == "improvement":
        print(quality_improvement(params))
    else:
        print(f"❌ Unknown command: {command}")
        print("Available: standards, inspection, defects, improvement")
