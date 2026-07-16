#!/usr/bin/env python3
"""Resonance Energy — One‑Click FULL BUILD

Single button pipeline:
- Update docs (Master Plan + Vision)
- Regenerate CLICKABLE_INDEX.md + CONTEXT_PACK.md
- Preflight handbooks
- Render handbook PDFs
- Zip repo safely
- Write run log

Idempotent + backup behavior.

Run:
  python3 RUN_FULL_BUILD.py
"""

from __future__ import annotations

import datetime
import os
import subprocess
import sys
from pathlib import Path

STAMP = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# ---------------- Repo root discovery ----------------

def find_repo_root(start: Path) -> Path:
    cur = start.resolve()
    for _ in range(15):
        if (cur / '00_MASTER_PLAN' / 'MASTER_PLAN.md').exists() and (cur / '02_Vision_Ethics_Founders' / 'VISION_FOUNDATION.md').exists():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    raise RuntimeError('Repo root not found. Run from inside the repo folder.')

ROOT = find_repo_root(Path.cwd())

# ---------------- Paths ----------------
MASTER_PLAN = ROOT / '00_MASTER_PLAN' / 'MASTER_PLAN.md'
VISION_FOUNDATION = ROOT / '02_Vision_Ethics_Founders' / 'VISION_FOUNDATION.md'
CLICKABLE_INDEX = ROOT / 'CLICKABLE_INDEX.md'
CONTEXT_PACK = ROOT / 'CONTEXT_PACK.md'
ARTIFACTS = ROOT / 'artifacts'
RUN_LOGS = ARTIFACTS / 'run_logs'
RUN_LOGS.mkdir(parents=True, exist_ok=True)
REPORT = RUN_LOGS / f'FULL_BUILD_REPORT_{STAMP}.md'

MP_MARKER = '## Program Phases (R&D First'
VF_MARKER = '## Development Doctrine (How We Build)'

# ---------------- Content blocks (same as prior) ----------------
MP_BLOCK = """

## Program Phases (R&D First → Analysis → Recommendations → Validation → Prototype → Sourceable Build)

### Phase 0 — R&D Knowledge Base (Truth Accumulation)
**Objective:** Build a structured, evidence-anchored R&D library that becomes the internal design authority.
**Outputs:**
- R&D knowledge base index (topics, findings, confidence level, citations, experiments)
- Experiment registry entries (hypothesis → method → results → interpretation → next test)
- Measurement standards: head, flow, losses, power, efficiency, uncertainty
- Safety/controls baseline assumptions (fail-safe behavior, logging, alarms)

**Gate to Phase 1:** We can reproduce baseline measurements and quantify uncertainty.

---

### Phase 1 — Analysis & Interpretation (Turning Data into Engineering Understanding)
**Objective:** Convert R&D results into models, ranges, constraints, and failure modes.
**Outputs:**
- Parameter envelopes (head, flow, losses, efficiency contributors)
- Failure modes catalog (debris, air entrainment, water hammer, cavitation risk, freeze risk, corrosion)
- Constraint list (must/should/may) and “unknowns to test” list

**Gate to Phase 2:** We can explain performance limits using measured or defensible physics-first analysis.

---

### Phase 2 — Design Recommendations (Doctrine → Design Inputs)
**Objective:** Produce design targets and architecture choices derived from R&D.
**Outputs:**
- Recommended architecture modules (see: Modular System Architecture below)
- Target headloss budgets and acceptance thresholds (draft)
- Testable design hypotheses for the prototype (what should improve efficiency and why)

**Gate to Phase 3:** Every recommendation maps to (a) R&D evidence or (b) a clearly labeled assumption to be tested.

---

### Phase 3 — Component-by-Component Validation (Against the R&D Base)
**Objective:** Evaluate each component design against the R&D knowledge base and doctrine.
**Scope components:**
- Intake / inlet diaphragm option
- Debris management & screening
- Penstock/headloss
- Multi-ram pump bank(s) (hydram) and/or helper pumps
- Turbine/nozzle/runner
- Generator and power electronics
- Controls / SCADA / telemetry
- Battery banks (local + grid tie/storage)
- Solar array + wind turbine integration
- Backup/contingency systems
- Commissioning (FAT → SAT) and maintenance doctrine

**Outputs:**
- Component scorecards: “Meets / Deviates / Unknown (test needed)”
- Risk register per component + mitigation test plan
- Updated handbook doctrine reflecting validated decisions

**Gate to Phase 4:** No component enters prototype design unless it passes validation OR has a defined test plan.

---

### Phase 4 — Digital Prototype + CAD + Blueprints
**Objective:** Produce a working digital prototype and build-ready drawings.
**Outputs:**
- System architecture + interface definitions
- CAD drawings & dimensioned blueprints
- Draft BOM: (A) lab-grade version and (B) sourceable version
- Instrumentation & test plan embedded into design

**Gate to Phase 5:** Digital prototype is buildable; interfaces are defined; test instrumentation plan is complete.

---

### Phase 5A — Lab Prototype (“Perfect Version”)
**Objective:** Build the highest-performance instrumented unit to validate efficiency drivers and loss contributors.
**Outputs:**
- Lab build with controlled test harness
- Repeatable efficiency test protocol
- Iteration log: what changed, why, measured deltas, reproducibility

**Gate to Phase 5B:** Efficiency/loss results are repeatable and uncertainty is known.

---

### Phase 5B — Sourceable Prototype (“Off-the-Shelf Good Enough”)
**Objective:** Build a version using readily available parts that matches the lab prototype as closely as practical.
**Outputs:**
- Sourceable BOM + suppliers
- Fit/Function equivalence map vs lab prototype
- Performance delta analysis (losses, reliability tradeoffs, cost tradeoffs)

**Gate to Deployment Concept:** We can explain, accept, and document the delta between lab and sourceable builds.

---

## Modular System Architecture (Base + Options)

### Base Hydro Module (Core)
A repeatable containerized plant built around:
- Intake + screening (with optional inlet diaphragm concept)
- Head management (head tank / hydraulic stabilization as applicable)
- Turbine-generator set
- Power electronics
- Controls + telemetry

### Hydraulic Augmentation Options
- Multi-ram pump bank(s) (multiple hydrams in parallel/series strategies where justified by R&D)
- Helper pumps powered from local generation (only where R&D shows net benefit and reliability)
- Bypass / dump / relief / priming strategies to handle off-nominal conditions

### Hybrid Energy Options (Local Generation + Storage)
- Solar array integration
- Wind turbine integration
- Dual battery banks:
  - **Bank A (Local Machine Bank):** ensures control power, blackstart, local loads, instrument stability
  - **Bank B (Grid-Tie / Storage Bank):** export smoothing, storage, grid or microgrid stabilization
- Inverter/charger strategy and protection scheme (validated in controls doctrine)

### Backup & Contingency
- Redundancy strategy (critical sensors, control power, comms, bypass valves, safe shutdown)
- Fail-safe behaviors (debris jam, freeze event, sensor fault, overcurrent, undervoltage)
- Maintenance access and swap strategy for components (modularity emphasis)

---

## Continuous Policy — Validation Gate (Non-Negotiable)
No design choice or performance claim moves forward unless it:
1) Improves measured performance (efficiency, headloss reduction, reliability), and
2) Does not introduce safety/EMI/operational hazards, and
3) Is reproducible.
"""

VF_BLOCK = """

## Development Doctrine (How We Build)

### R&D-First Sequence
We will proceed in strict order:
1) R&D knowledge base
2) Analysis & interpretation
3) Design recommendations
4) Component-by-component validation against R&D
5) Digital prototype + CAD + blueprints
6) Lab Prototype (“Perfect Version”)
7) Sourceable Prototype (“Off-the-Shelf Good Enough”)

### Two Builds, One Truth
We will build two versions of the system:

**A) Lab Prototype (Perfect / Efficiency-Truth Unit)**
- Purpose: discover and validate true efficiency drivers and loss contributors.
- Requirement: instrumented, repeatable tests, uncertainty known.

**B) Sourceable Prototype (Deployable / Supply-Truth Unit)**
- Purpose: match the lab version as closely as practical using commercially available parts.
- Requirement: document equivalence mapping and measure performance deltas.

**Rule:** Lab unit defines performance truth; sourceable unit defines deployability. Differences must be measured, documented, and accepted intentionally.

### Modular Platform Identity
Our system is modular by design:
- Base hydro module (intake → head management → turbine-generator → controls)
- Optional inlet diaphragm concept (R&D gated)
- Optional hydraulic augmentation: multi-ram pumps and/or helper pumps (R&D gated)
- Hybrid energy options: solar, wind, dual battery banks (local machine bank + grid-tie/storage bank)
- Backup and contingency planning as a core requirement, not an add-on

### Priority Decisions After R&D
We will not prematurely lock priorities (e.g., maximum efficiency vs maximum reliability vs simplest instrumentation).
Those priorities will be chosen after R&D reveals:
- which variables dominate efficiency,
- what risks dominate reliability,
- what constraints dominate deployability.
"""

# ---------------- File helpers ----------------

def rtext(p: Path) -> str:
    return p.read_text(encoding='utf-8', errors='replace')


def wtext(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding='utf-8')


def backup(p: Path) -> Path:
    b = p.with_suffix(p.suffix + f'.bak_{STAMP}')
    wtext(b, rtext(p))
    return b


def upsert(p: Path, marker: str, block: str) -> bool:
    txt = rtext(p)
    if marker in txt:
        return False
    backup(p)
    wtext(p, txt.rstrip() + block + '\n')
    return True


def build_clickable_index() -> None:
    pdfs = sorted((ROOT / '04_Technology' / 'handbooks').rglob('exports/*.pdf'))
    lines = [
        '# Resonance Energy Systems — Clickable Local Index',
        '',
        'Open this file in your editor (VS Code/Obsidian/GitHub Desktop) to click through the repo locally.',
        '',
        '## Key Documents',
        '- [Executive Summary](01_Executive_Summary/EXEC_SUMMARY.md)',
        '- [Master Plan](00_MASTER_PLAN/MASTER_PLAN.md)',
        '- [Vision Foundation](02_Vision_Ethics_Founders/VISION_FOUNDATION.md)',
        '- [Doctrine Handbooks Index](04_Technology/handbooks/README.md)',
        '- [Market Scenarios](03_Market_Scenarios/)',
        '- [Master References](11_References/MASTER_REFERENCES.md)',
        '- [Board Charter](12_Admin_Governance/BOARD_CHARTER.md)',
        '',
        '## Rendered Handbook PDFs',
    ]
    for p in pdfs:
        rel = p.relative_to(ROOT).as_posix()
        lines.append(f'- [{p.name}]({rel})')
    lines += ['', '## Notes', '- If PDF links don’t open from your viewer, open the handbook folder and the `exports/` directory.']
    wtext(CLICKABLE_INDEX, '\n'.join(lines) + '\n')


def build_context_pack() -> None:
    summary = [
        '# Resonance Energy Systems — CONTEXT PACK (Paste into a new chat)',
        '',
        f'Generated: {datetime.date.today().isoformat()}  (local)',
        '',
        '## Source of truth',
        '- This repo is source-of-truth. Refer to files by relative path.',
        '',
        '## Current development doctrine (R&D-first)',
        '- R&D knowledge base → Analysis/Interpretation → Recommendations → Component Validation → Digital Prototype/CAD → Lab Prototype → Sourceable Prototype',
        '- Two builds: Lab “perfect” efficiency truth unit + Sourceable off-the-shelf close-match unit.',
        '',
        '## Modular platform scope (options)',
        '- Inlet diaphragm option',
        '- Solar + wind integration',
        '- Helper pumps powered by local generation',
        '- Dual battery banks (local machine bank + grid-tie/storage bank)',
        '- Multiple ram pumps',
        '- Backup systems + contingencies',
        '',
        '## Key files to open',
        '- 00_MASTER_PLAN/MASTER_PLAN.md',
        '- 02_Vision_Ethics_Founders/VISION_FOUNDATION.md',
        '- 04_Technology/handbooks/README.md',
        '- 11_References/MASTER_REFERENCES.md',
    ]
    wtext(CONTEXT_PACK, '\n'.join(summary) + '\n')

# ---------------- Pipeline runners ----------------

def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    out = (p.stdout or '') + ('\n' + p.stderr if p.stderr else '')
    return p.returncode, out


def ensure_reportlab() -> bool:
    try:
        import reportlab  # noqa: F401
        return True
    except Exception:
        return False


def main() -> int:
    lines = []
    def log(s: str):
        print(s)
        lines.append(s)

    log('# Full Build Report')
    log('')
    log(f'- Timestamp: {STAMP}')
    log(f'- Repo root: `{ROOT}`')
    log('')

    # 1) Update docs
    changed_mp = upsert(MASTER_PLAN, MP_MARKER, MP_BLOCK)
    changed_vf = upsert(VISION_FOUNDATION, VF_MARKER, VF_BLOCK)
    build_clickable_index()
    build_context_pack()

    log('## Step 1 — Docs / Index / Context')
    log(f'- Master Plan updated: **{changed_mp}**')
    log(f'- Vision updated: **{changed_vf}**')
    log(f'- Wrote: `{CLICKABLE_INDEX.relative_to(ROOT)}`')
    log(f'- Wrote: `{CONTEXT_PACK.relative_to(ROOT)}`')
    log('')

    # 2) Preflight
    preflight = ROOT / 'scripts' / 'preflight_handbooks.py'
    if preflight.exists():
        log('## Step 2 — Preflight Handbooks')
        rc, out = run([sys.executable, str(preflight), '--report', 'artifacts/preflight_report.md'], ROOT)
        log(f'- Return code: **{rc}**')
        if out.strip():
            log('```')
            log(out.strip()[:8000])
            log('```')
        log('')
        if rc != 0:
            wtext(REPORT, '\n'.join(lines) + '\n')
            log(f'❌ Stopping: Preflight failed. See `{REPORT.relative_to(ROOT)}`')
            return rc
    else:
        log('## Step 2 — Preflight Handbooks')
        log('- SKIPPED: scripts/preflight_handbooks.py not found')
        log('')

    # 3) Render PDFs
    render = ROOT / 'scripts' / 'render_handbooks.py'
    log('## Step 3 — Render Handbook PDFs')
    if not ensure_reportlab():
        log('- FAIL: Python package `reportlab` not installed.')
        log('- Install: `python3 -m pip install --user reportlab`')
        wtext(REPORT, '\n'.join(lines) + '\n')
        return 3

    if render.exists():
        rc, out = run([sys.executable, str(render)], ROOT)
        log(f'- Return code: **{rc}**')
        if out.strip():
            log('```')
            log(out.strip()[:8000])
            log('```')
        log('')
        if rc != 0:
            wtext(REPORT, '\n'.join(lines) + '\n')
            log(f'❌ Stopping: Render failed. See `{REPORT.relative_to(ROOT)}`')
            return rc
    else:
        log('- SKIPPED: scripts/render_handbooks.py not found')
        log('')

    # 4) Zip repo safely
    zip_safe = ROOT / 'scripts' / 'zip_repo_safe.py'
    log('## Step 4 — Package Repo (Safe ZIP)')
    if zip_safe.exists():
        rc, out = run([sys.executable, str(zip_safe)], ROOT)
        log(f'- Return code: **{rc}**')
        if out.strip():
            log('```')
            log(out.strip()[:8000])
            log('```')
        log('')
        if rc != 0:
            wtext(REPORT, '\n'.join(lines) + '\n')
            log(f'❌ Stopping: ZIP failed. See `{REPORT.relative_to(ROOT)}`')
            return rc
    else:
        log('- SKIPPED: scripts/zip_repo_safe.py not found')
        log('')

    # Refresh index after PDFs
    build_clickable_index()

    log('## Done')
    log('- ✅ Full build completed successfully.')

    wtext(REPORT, '\n'.join(lines) + '\n')
    log(f'- Report: `{REPORT.relative_to(ROOT)}`')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
