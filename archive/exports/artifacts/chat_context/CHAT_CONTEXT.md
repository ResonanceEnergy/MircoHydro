# Resonance Energy Systems — Chat Context Pack
**Generated:** 2026-01-22 20:29:30
**Repo root:** `/Users/gripandripphdd/Desktop/ResonanceEnergy_Enterprise_POPULATED`

> Paste this entire file into a new chat to restore full context.
> Source-of-truth policy: repo contents override chat assumptions.


---

## Core Truth Set (Key Files)

### MISSING: `branding/DECISIONS_AND_TODOS.md`
### MISSING: `branding/taglines/TAGLINES_MASTER.md`
### `04_Technology/handbooks/README.md`

```text
# Doctrine Handbooks (Mini Handbooks — 4–8 pages)

Last updated: 2026-01-22

Render PDFs (manual):
```bash
python3 scripts/render_handbooks.py
```

## Handbooks

- **HB-01** — Turbine Selection Doctrine (Crossflow-first)  \
  Folder: `HB-01_Turbine_Selection/`  \
  Status: **Draft**
- **HB-02** — Intake & Debris Management (Run-of-River, Water-kind)  \
  Folder: `HB-02_Intake_Debris/`  \
  Status: **Draft**
- **HB-03** — Penstock & Headloss Design (≤10% Loss Standard)  \
  Folder: `HB-03_Penstock_Headloss/`  \
  Status: **Draft**
- **HB-04** — Hydraulic Ram Pump Design & Tuning  \
  Folder: `HB-04_Hydram_Tuning/`  \
  Status: **Draft**
- **HB-05** — Controls, Blackstart & SCADA (Microgrid Backbone)  \
  Folder: `HB-05_Controls_SCADA/`  \
  Status: **Draft**
- **HB-06** — Commissioning & Acceptance Testing (FAT → SAT)  \
  Folder: `HB-06_Commissioning_FAT_SAT/`  \
  Status: **Draft**

## Tagline
Tagline is TBD (see branding/taglines/TAGLINES_MASTER.md).

```
### `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`

```text
# Default Deployment Contexts (All Three)

Last updated: 2026-01-22

Resonance Energy Systems handbooks support three default deployment contexts:

1) **[CREEK]** Creek / Foothills Run-of-River (Cold + Debris)
2) **[CANAL]** Irrigation Canal Drop (High Flow + Operations Crew)
3) **[OUTFALL]** Industrial Outfall / Water-Works (24/7 + Compliance + Corrosion)

Each handbook should include:
- Core Doctrine (applies everywhere)
- Context Overlays (Creek/Canal/Outfall)

Checklist items should be tagged: [CREEK], [CANAL], [OUTFALL].

```
### `04_Technology/handbooks/_shared/CONTEXT_MATRIX.md`

```text
# Context Matrix (Handbooks × Deployment Contexts)

Last updated: 2026-01-22

Labels:
- [CREEK] Creek / foothills
- [CANAL] Irrigation canal
- [OUTFALL] Industrial outfall

Use this file to track per-handbook requirements across all three contexts.

```
### `04_Technology/handbooks/_shared/COVER_TEMPLATE.md`

```text
# Resonance Energy Systems

> **Tagline:** *(TBD — see `branding/taglines/TAGLINES_MASTER.md`)*

**Document:** {{HANDBOOK_ID}} — {{TITLE}}

**Version:** {{VERSION}}

**Date:** {{DATE}}

**Applicable contexts:** Creek / Canal / Outfall (default)  
See `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`

---

```
### `04_Technology/handbooks/_shared/DISCLAIMER.md`

```text
## Disclaimer & Positioning

- This handbook is engineering doctrine for deployment and operations.
- Performance claims must be supported by measured head, flow, losses, and efficiency.
- Visionary inspirations may influence design heuristics but do not replace validated physics.

```
### `04_Technology/handbooks/_shared/handbook_style.json`

```text
{
  "page_size": "LETTER",
  "margins_in": {
    "left": 0.75,
    "right": 0.75,
    "top": 0.75,
    "bottom": 0.75
  },
  "fonts": {
    "title": 18,
    "h1": 16,
    "h2": 13,
    "body": 10,
    "mono": 9
  },
  "line_spacing": {
    "body": 13,
    "tight": 11
  },
  "footer": {
    "show": true,
    "text": "Resonance Energy Systems \u2014 Internal Doctrine (Draft)"
  }
}
```
### `11_References/MASTER_REFERENCES.md`

```text
# Master References (curated) — 2026-01-23

## NRCan (Canada)
- NRCan: *Micro-Hydropower Systems — An Introduction* (PDF). citeturn2search1
- NRCan archived page: *Micro-Hydro Systems — A Buyer’s Guide* (overview + download). citeturn2search6

## Hydram (Hydraulic Ram Pump)
- Life4Water Guide (references USAID Water for the World technical note; includes delivered-volume formula and efficiency factors). citeturn2search20
- “Designing a Hydraulic Ram Pump” (USAID-derived PDF copy). citeturn2search22

## Crossflow turbines
- Adhikari & Wood (2018): *Design of High Efficiency Crossflow Hydro Turbines: A Review and Extension* (UCalgary). citeturn2search7
- Adhikari & Wood (2017): nozzle redesign improving efficiency 69%→87%. citeturn2search11

## Pipe headloss methods
- Hazen-Williams vs Darcy-Weisbach comparisons. citeturn2search31 citeturn2search35
- Engineering Toolbox Hazen-Williams C coefficients by material. citeturn2search32

## Batteries / PV cost anchors
- BloombergNEF 2025 battery price survey press release ($108/kWh average; $70/kWh stationary storage). citeturn2search43
- PVPS Task 1 Canada 2024 report (PV price ranges). citeturn2search25

## IAHR vortex-flow intakes
- IAHR Water Monograph Series: *Vortex-Flow Intakes* (2023). citeturn2search13

## Dan Winter sources (non-mainstream; R&D annex)
- goldenmean.info index. citeturn2search37
- fractalfield conjugate gravity article. citeturn2search38
- Winter & Jones paper. citeturn2search39


```
### MISSING: `scripts/README.md`
### `scripts/automate_handbooks.py`

```text
#!/usr/bin/env python3
"""
Idempotently enforces the Resonance Energy Systems handbook structure:
- Shared doctrine files in 04_Technology/handbooks/_shared/
- Ensures each HB-* folder has: diagrams/, checklists/, exports/, contexts/
- Ensures contexts/CONTEXT_OVERLAYS.md exists
- Ensures each handbook.md contains a Deployment Contexts section (CREEK/CANAL/OUTFALL)
- Adds a small context-tag note to checklist files
- Updates 04_Technology/handbooks/README.md

Run:
  python3 scripts/automate_handbooks.py --report artifacts/handbook_automation_report.md
"""

from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB_ROOT = ROOT / "04_Technology" / "handbooks"
SHARED = HB_ROOT / "_shared"
TODAY = datetime.date.today().isoformat()

DEFAULT_HBS = [
    ("HB-01_Turbine_Selection", "HB-01", "Turbine Selection Doctrine (Crossflow-first)"),
    ("HB-02_Intake_Debris", "HB-02", "Intake & Debris Management (Run-of-River, Water-kind)"),
    ("HB-03_Penstock_Headloss", "HB-03", "Penstock & Headloss Design (≤10% Loss Standard)"),
    ("HB-04_Hydram_Tuning", "HB-04", "Hydraulic Ram Pump Design & Tuning"),
    ("HB-05_Controls_SCADA", "HB-05", "Controls, Blackstart & SCADA (Microgrid Backbone)"),
    ("HB-06_Commissioning_FAT_SAT", "HB-06", "Commissioning & Acceptance Testing (FAT → SAT)"),
]

def ensure_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")

def ensure_dirs(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def upsert_context_block(md: str) -> str:
    header = "## Deployment Contexts (Default: All Three)"
    if header in md:
        return md

    block = (
        "## Deployment Contexts (Default: All Three)\n"
        "This handbook is written to be valid for three default deployment environments:\n"
        "- **[CREEK]** Creek / foothills run-of-river (cold + debris)\n"
        "- **[CANAL]** Irrigation canal drop (high flow + ops crew)\n"
        "- **[OUTFALL]** Industrial outfall / water-works (24/7 + compliance + corrosion)\n\n"
        "Context overlays live in: `contexts/CONTEXT_OVERLAYS.md`.  \n"
        "Shared definitions: `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`.\n"
    )

    # Insert after first '---' separator if present, else append
    if "---" in md:
        before, after = md.split("---", 1)
        return before + "---\n\n" + block + "\n---\n" + after
    return md + "\n\n" + block

def ensure_shared():
    ensure_dirs(SHARED)

    ensure_text(
        SHARED / "DEFAULT_CONTEXTS.md",
        f"""# Default Deployment Contexts (All Three)

Last updated: {TODAY}

Resonance Energy Systems handbooks support three default deployment contexts:

1) **[CREEK]** Creek / Foothills Run-of-River (Cold + Debris)
2) **[CANAL]** Irrigation Canal Drop (High Flow + Operations Crew)
3) **[OUTFALL]** Industrial Outfall / Water-Works (24/7 + Compliance + Corrosion)

Each handbook should include:
- Core Doctrine (applies everywhere)
- Context Overlays (Creek/Canal/Outfall)

Checklist items should be tagged: [CREEK], [CANAL], [OUTFALL].
""",
    )

    ensure_text(
        SHARED / "CONTEXT_MATRIX.md",
        f"""# Context Matrix (Handbooks × Deployment Contexts)

Last updated: {TODAY}

Labels:
- [CREEK] Creek / foothills
- [CANAL] Irrigation canal
- [OUTFALL] Industrial outfall

Use this file to track per-handbook requirements across all three contexts.
""",
    )

    ensure_text(
        SHARED / "DISCLAIMER.md",
        """## Disclaimer & Positioning

- This handbook is engineering doctrine for deployment and operations.
- Performance claims must be supported by measured head, flow, losses, and efficiency.
- Visionary inspirations may influence design heuristics but do not replace validated physics.
""",
    )

    ensure_text(
        SHARED / "COVER_TEMPLATE.md",
        """# Resonance Energy Systems

> **Tagline:** *(TBD — see `branding/taglines/TAGLINES_MASTER.md`)*

**Document:** {{HANDBOOK_ID}} — {{TITLE}}

**Version:** {{VERSION}}

**Date:** {{DATE}}

**Applicable contexts:** Creek / Canal / Outfall (default)  
See `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`

---
""",
    )

    style_path = SHARED / "handbook_style.json"
    if not style_path.exists():
        style = {
            "page_size": "LETTER",
            "margins_in": {"left": 0.75, "right": 0.75, "top": 0.75, "bottom": 0.75},
            "fonts": {"title": 18, "h1": 16, "h2": 13, "body": 10, "mono": 9},
            "line_spacing": {"body": 13, "tight": 11},
            "footer": {"show": True, "text": "Resonance Energy Systems — Internal Doctrine (Draft)"},
        }
        style_path.write_text(json.dumps(style, indent=2), encoding="utf-8")

def ensure_handbook_folder(folder_name: str, hb_id: str, title: str):
    hb = HB_ROOT / folder_name
    ensure_dirs(hb)

    for sub in ["diagrams", "checklists", "exports", "contexts"]:
        ensure_dirs(hb / sub)

    ensure_text(
        hb / "contexts" / "CONTEXT_OVERLAYS.md",
        """# Context Overlays

## [CREEK] Creek / Foothills Run-of-River
- (Add creek-specific requirements)

## [CANAL] Irrigation Canal Drop
- (Add canal-specific requirements)

## [OUTFALL] Industrial Outfall / Water-Works
- (Add outfall-specific requirements)
""",
    )

    ensure_text(
        hb / "handbook.md",
        f"""{{{{COVER}}}}

{{{{DISCLAIMER}}}}

# {title}

**Handbook ID:** {hb_id}  
**Version:** 0.1 (Draft)

---

## Table of Contents
1. Overview
2. Key Principles
3. Deployment Contexts (Default: All Three)
4. Procedures
5. Failure Modes & Red Flags
6. Checklists
7. References

---

## 1) Overview
(Draft)

---

## 2) Key Principles
(Draft)

---

## 3) Deployment Contexts (Default: All Three)
(This section will be inserted automatically if missing.)

---

## 4) Procedures
(Draft)

---

## 5) Failure Modes & Red Flags
(Draft)

---

## 6) Checklists
See `checklists/`.

---

## 7) References
See `11_References/MASTER_REFERENCES.md`.
""",
    )

    # Ensure context section exists in handbook.md
    hb_md = hb / "handbook.md"
    md = hb_md.read_text(encoding="utf-8")
    md2 = upsert_context_block(md)
    if md2 != md:
        hb_md.write_text(md2, encoding="utf-8")

    # Add context tag note to checklist md files
    for chk in (hb / "checklists").glob("*.md"):
        txt = chk.read_text(encoding="utf-8")
        if "Context tags:" not in txt:
            chk.write_text(
                txt.rstrip()
                + "\n\n> Context tags: use [CREEK], [CANAL], [OUTFALL] on context-specific checklist items.\n",
                encoding="utf-8",
            )

def update_index():
    readme = HB_ROOT / "README.md"
    hb_dirs = sorted([p for p in HB_ROOT.iterdir() if p.is_dir() and p.name.startswith("HB-")])

    lines = [
        "# Doctrine Handbooks (Mini Handbooks — 4–8 pages)",
        "",
        f"Last updated: {TODAY}",
        "",
        "Render PDFs (manual):",
        "```bash",
        "python3 scripts/render_handbooks.py",
        "```",
        "",
        "## Handbooks",
        "",
    ]

    for hb in hb_dirs:
        hid = hb.name.split("_")[0]
        title = "(unknown)"
        md_path = hb / "handbook.md"
        if md_path.exists():
            for ln in md_path.read_text(encoding="utf-8").splitlines():
                if ln.startswith("# "):
                    title = ln[2:].strip()
                    break
        lines.append(f"- **{hid}** — {title}  \\\n  Folder: `{hb.name}/`  \\\n  Status: **Draft**")

    lines += ["", "## Tagline", "Tagline is TBD (see branding/taglines/TAGLINES_MASTER.md).", ""]
    readme.write_text("\n".join(lines), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", type=str, default=None)
    args = ap.parse_args()

    ensure_dirs(HB_ROOT)
    ensure_shared()

    # Ensure the default HB folders exist
    for folder_name, hb_id, title in DEFAULT_HBS:
        ensure_handbook_folder(folder_name, hb_id, title)

    update_index()

    if args.report:
        report_path = ROOT / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            f"# Handbook Automation Report\n\nDate: {TODAY}\n\nCompleted.\n",
            encoding="utf-8",
        )
        print(f"Wrote report: {report_path}")

    print("Handbook automation completed.")

if __name__ == "__main__":
    main()

```
### `scripts/preflight_handbooks.py`

```text
#!/usr/bin/env python3
"""
Preflight validator for Resonance Energy Systems handbooks.

Run:
  python3 scripts/preflight_handbooks.py --report artifacts/preflight_report.md

Exit:
  0 = pass
  1 = fail (one or more FAIL)
"""

import argparse
import datetime
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB_ROOT = ROOT / "04_Technology" / "handbooks"
SHARED = HB_ROOT / "_shared"

TODAY = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

CONTEXT_HEADER = "## Deployment Contexts (Default: All Three)"
REQUIRED_CONTEXT_TAGS = ["[CREEK]", "[CANAL]", "[OUTFALL]"]
REQUIRED_OVERLAY_HEADERS = ["## [CREEK]", "## [CANAL]", "## [OUTFALL]"]
CHECKLIST_NOTE = "Context tags: use [CREEK], [CANAL], [OUTFALL]"

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def escape_html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def convert_inline(md_line: str) -> str:
    s = escape_html(md_line)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s

def expand_templates(md: str) -> str:
    cover = read_text(SHARED / "COVER_TEMPLATE.md") if (SHARED / "COVER_TEMPLATE.md").exists() else ""
    disclaimer = read_text(SHARED / "DISCLAIMER.md") if (SHARED / "DISCLAIMER.md").exists() else ""
    return md.replace("{{COVER}}", cover).replace("{{DISCLAIMER}}", disclaimer)

def validate_handbook(hb_dir: Path):
    findings = []
    hb_md = hb_dir / "handbook.md"
    if not hb_md.exists():
        return [("FAIL", "Missing handbook.md")]

    md = read_text(hb_md)
    expanded = expand_templates(md)

    # Context section must exist and mention all tags
    if CONTEXT_HEADER not in expanded:
        findings.append(("FAIL", f"Missing required header: {CONTEXT_HEADER}"))
    else:
        for t in REQUIRED_CONTEXT_TAGS:
            if t not in expanded:
                findings.append(("FAIL", f"Missing required context tag: {t}"))

    # Overlay file must exist with required headers
    overlays = hb_dir / "contexts" / "CONTEXT_OVERLAYS.md"
    if not overlays.exists():
        findings.append(("FAIL", "Missing contexts/CONTEXT_OVERLAYS.md"))
    else:
        o = read_text(overlays)
        for h in REQUIRED_OVERLAY_HEADERS:
            if h not in o:
                findings.append(("FAIL", f"Overlay missing section: {h}"))

    # Balanced ** markers
    if expanded.count("**") % 2 != 0:
        findings.append(("FAIL", "Unbalanced '**' markers (odd count)."))

    # Simulate inline conversion and check tag balance totals
    b_open = b_close = i_open = i_close = 0
    for line in expanded.splitlines():
        if line.startswith("> "):
            converted = "<i>" + convert_inline(line[2:]) + "</i>"
        else:
            converted = convert_inline(line)
        b_open += converted.count("<b>")
        b_close += converted.count("</b>")
        i_open += converted.count("<i>")
        i_close += converted.count("</i>")

    if b_open != b_close:
        findings.append(("FAIL", f"Unbalanced <b> tags after conversion: <b>={b_open}, </b>={b_close}"))
    if i_open != i_close:
        findings.append(("FAIL", f"Unbalanced <i> tags after conversion: <i>={i_open}, </i>={i_close}"))

    # Checklist note is recommended (warn if missing)
    chk_dir = hb_dir / "checklists"
    if chk_dir.exists():
        for cf in chk_dir.glob("*.md"):
            if CHECKLIST_NOTE not in read_text(cf):
                findings.append(("WARN", f"Checklist missing context tag note: checklists/{cf.name}"))

    if not findings:
        findings.append(("PASS", "OK"))

    return findings

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", default="artifacts/preflight_report.md")
    args = ap.parse_args()

    hb_dirs = [p for p in HB_ROOT.iterdir() if p.is_dir() and p.name.startswith("HB-")] if HB_ROOT.exists() else []
    if not hb_dirs:
        print("No HB-* folders found under 04_Technology/handbooks/")
        raise SystemExit(1)

    any_fail = False
    report_lines = [
        "# Preflight Handbook Report",
        "",
        f"- Generated: {TODAY}",
        f"- Repo root: `{ROOT}`",
        "",
        "## Results",
        ""
    ]

    for hb in sorted(hb_dirs, key=lambda p: p.name):
        report_lines.append(f"### {hb.name}")
        findings = validate_handbook(hb)
        for level, msg in findings:
            report_lines.append(f"- **{level}**: {msg}")
            if level == "FAIL":
                any_fail = True
        report_lines.append("")

    out = ROOT / args.report
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Preflight report written: {out}")

    if any_fail:
        print("Preflight FAILED — fix issues before rendering PDFs.")
        raise SystemExit(1)

    print("Preflight PASSED — safe to render PDFs.")
    raise SystemExit(0)

if __name__ == "__main__":
    main()

```
### `scripts/render_handbooks.py`

```text
#!/usr/bin/env python3
"""
Manual PDF renderer for handbooks (Markdown -> PDF).

Reads:
  04_Technology/handbooks/HB-*/handbook.md

Expands:
  {{COVER}} and {{DISCLAIMER}} using templates in:
  04_Technology/handbooks/_shared/

Outputs:
  PDFs into each handbook's exports/ folder

Run:
  python3 scripts/render_handbooks.py

Requires:
  python3 -m pip install --user reportlab
"""

import json
import datetime
import re
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

ROOT = Path(__file__).resolve().parents[1]
HB_ROOT = ROOT / "04_Technology" / "handbooks"
SHARED = HB_ROOT / "_shared"


def load_style():
    style_path = SHARED / "handbook_style.json"
    if style_path.exists():
        return json.loads(style_path.read_text(encoding="utf-8"))
    return {
        "margins_in": {"left": 0.75, "right": 0.75, "top": 0.75, "bottom": 0.75},
        "fonts": {"h1": 16, "h2": 13, "body": 10},
        "line_spacing": {"body": 13},
    }


def escape_html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def md_inline_to_rl_html(s: str) -> str:
    """
    Minimal inline markdown conversion for ReportLab:
    - escape HTML
    - **bold** -> <b>bold</b>
    """
    s = escape_html(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s


def md_to_story(md: str, style: dict, source_label: str = ""):
    """
    Minimal markdown subset:
    - # Heading
    - ## Subheading
    - - bullet
    - --- separator -> spacing
    - [[PAGEBREAK]] -> PageBreak
    - > blockquote -> italic paragraph
    - Inline **bold** supported safely
    """
    ss = getSampleStyleSheet()

    body = ParagraphStyle(
        "Body",
        parent=ss["Normal"],
        fontName="Helvetica",
        fontSize=style["fonts"]["body"],
        leading=style["line_spacing"]["body"],
    )
    quote = ParagraphStyle(
        "Quote",
        parent=body,
        leftIndent=12,
        textColor="#374151",
        italic=True,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=ss["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=style["fonts"]["h1"],
        leading=style["fonts"]["h1"] + 4,
        spaceAfter=10,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=ss["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=style["fonts"]["h2"],
        leading=style["fonts"]["h2"] + 3,
        spaceAfter=8,
    )

    story = []
    lines = md.splitlines()

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip()

        if not line:
            story.append(Spacer(1, 0.12 * inch))
            continue

        if line.strip() == "[[PAGEBREAK]]":
            story.append(PageBreak())
            continue

        if line.startswith("# "):
            story.append(Paragraph(escape_html(line[2:]), h1))
            continue

        if line.startswith("## "):
            story.append(Paragraph(escape_html(line[3:]), h2))
            continue

        if line.startswith("---"):
            story.append(Spacer(1, 0.2 * inch))
            continue

        if line.startswith("- "):
            safe = md_inline_to_rl_html(line[2:])
            try:
                story.append(Paragraph("• " + safe, body))
            except Exception as e:
                raise RuntimeError(f"{source_label}: bullet parse error on line {i}: {raw}\n{e}")
            continue

        if line.startswith("> "):
            safe = md_inline_to_rl_html(line[2:])
            try:
                story.append(Paragraph(safe, quote))
            except Exception as e:
                raise RuntimeError(f"{source_label}: quote parse error on line {i}: {raw}\n{e}")
            continue

        safe = md_inline_to_rl_html(line)
        try:
            story.append(Paragraph(safe, body))
        except Exception as e:
            raise RuntimeError(f"{source_label}: paragraph parse error on line {i}: {raw}\n{e}")

    return story


def expand_templates(md: str, handbook_id: str, title: str, version: str) -> str:
    cover_path = SHARED / "COVER_TEMPLATE.md"
    disclaimer_path = SHARED / "DISCLAIMER.md"

    cover = cover_path.read_text(encoding="utf-8") if cover_path.exists() else ""
    disclaimer = disclaimer_path.read_text(encoding="utf-8") if disclaimer_path.exists() else ""

    cover = (
        cover.replace("{{HANDBOOK_ID}}", handbook_id)
        .replace("{{TITLE}}", title)
        .replace("{{VERSION}}", version)
        .replace("{{DATE}}", datetime.date.today().isoformat())
    )
    return md.replace("{{COVER}}", cover).replace("{{DISCLAIMER}}", disclaimer)


def parse_meta(md: str, folder_name: str):
    handbook_id = folder_name.split("_")[0]
    title = folder_name.replace("_", " ")
    version = "0.1"

    for line in md.splitlines():
        s = line.strip()
        if s.startswith("**Handbook ID:**"):
            handbook_id = s.split("**Handbook ID:**", 1)[1].strip()
        if s.startswith("**Version:**"):
            version = s.split("**Version:**", 1)[1].strip().split()[0]
        if s.startswith("# "):
            title = s[2:]
            break

    return handbook_id, title, version


def render_handbook(folder: Path, style: dict):
    md_path = folder / "handbook.md"
    if not md_path.exists():
        return False, f"Missing handbook.md in {folder}"

    md = md_path.read_text(encoding="utf-8", errors="replace")
    handbook_id, title, version = parse_meta(md, folder.name)
    md = expand_templates(md, handbook_id, title, version)

    out_dir = folder / "exports"
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = out_dir / f"{handbook_id}_{title.replace(' ', '_')}.pdf"

    m = style["margins_in"]
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        leftMargin=m["left"] * inch,
        rightMargin=m["right"] * inch,
        topMargin=m["top"] * inch,
        bottomMargin=m["bottom"] * inch,
    )

    story = md_to_story(md, style, source_label=str(md_path))
    doc.build(story)
    return True, f"Rendered: {pdf_path}"


def main():
    style = load_style()

    if not HB_ROOT.exists():
        print("No handbooks folder found at 04_Technology/handbooks/")
        raise SystemExit(1)

    hb_dirs = [p for p in HB_ROOT.iterdir() if p.is_dir() and p.name.startswith("HB-")]
    if not hb_dirs:
        print("No HB-* folders found under 04_Technology/handbooks/")
        raise SystemExit(1)

    errors = 0
    for hb in sorted(hb_dirs, key=lambda p: p.name):
        try:
            ok, msg = render_handbook(hb, style)
            print(msg)
            if not ok:
                errors += 1
        except Exception as e:
            errors += 1
            print(f"[ERROR] {hb.name}: {e}")

    if errors:
        print(f"\nRender finished with {errors} error(s). Fix the above and re-run.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

```
### `scripts/zip_repo_safe.py`

```text
#!/usr/bin/env python3
"""
Safe zipper for the repo:
- Run from repo root
- Avoids ZIP pre-1980 timestamp errors by clamping to 1980-01-01
- Skips .zip files and common junk folders

Run:
  python3 scripts/zip_repo_safe.py
"""
from pathlib import Path
import zipfile
import datetime

REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = REPO_ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

MIN_DT = (1980, 1, 1, 0, 0, 0)
EXCLUDE_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "dist", "build"}

def should_skip(p: Path) -> bool:
    parts = set(p.parts)
    if any(d in parts for d in EXCLUDE_DIRS):
        return True
    if p.suffix.lower() == ".zip":
        return True
    return False

def add_file(z: zipfile.ZipFile, file_path: Path, arcname: str):
    st = file_path.stat()
    dt = datetime.datetime.fromtimestamp(st.st_mtime).timetuple()[:6]
    if dt < MIN_DT:
        dt = MIN_DT
    zi = zipfile.ZipInfo(arcname)
    zi.date_time = dt
    zi.compress_type = zipfile.ZIP_DEFLATED
    with open(file_path, "rb") as f:
        z.writestr(zi, f.read())

def main():
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = ARTIFACTS / f"ResonanceEnergy_Enterprise_{stamp}.zip"
    with zipfile.ZipFile(out, "w") as z:
        for p in REPO_ROOT.rglob("*"):
            if not p.is_file():
                continue
            if should_skip(p):
                continue
            arc = p.relative_to(REPO_ROOT).as_posix()
            add_file(z, p, arc)
    print(f"Created: {out}")

if __name__ == "__main__":
    main()

```


---

## Handbooks (HB-01..HB-06)

### `HB-01_Turbine_Selection`
**Overlay:** `04_Technology/handbooks/HB-01_Turbine_Selection/contexts/CONTEXT_OVERLAYS.md`

```text
# Context Overlays

## [CREEK] Creek / Foothills Run-of-River
- (Add creek-specific requirements)

## [CANAL] Irrigation Canal Drop
- (Add canal-specific requirements)

## [OUTFALL] Industrial Outfall / Water-Works
- (Add outfall-specific requirements)

```
**Body:** `04_Technology/handbooks/HB-01_Turbine_Selection/handbook.md`

```text
{{COVER}}

{{DISCLAIMER}}

# Turbine Selection Doctrine (Crossflow-first)

**Handbook ID:** HB-01  
**Version:** 0.1 (Draft)

---

## Deployment Contexts (Default: All Three)
This handbook is written to be valid for three default deployment environments:
- **[CREEK]** Creek / foothills run-of-river (cold + debris)
- **[CANAL]** Irrigation canal drop (high flow + ops crew)
- **[OUTFALL]** Industrial outfall / water-works (24/7 + compliance + corrosion)

Context overlays live in: `contexts/CONTEXT_OVERLAYS.md`.  
Shared definitions: `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`.

---


## Table of Contents
1. Overview
2. Key Principles
3. Deployment Contexts (Default: All Three)
4. Procedures
5. Failure Modes & Red Flags
6. Checklists
7. References

---

## 1) Overview
(Draft)

---

## 2) Key Principles
(Draft)

---

## 3) Deployment Contexts (Default: All Three)
(This section will be inserted automatically if missing.)

---

## 4) Procedures
(Draft)

---

## 5) Failure Modes & Red Flags
(Draft)

---

## 6) Checklists
See `checklists/`.

---

## 7) References
See `11_References/MASTER_REFERENCES.md`.

```
### `HB-02_Intake_Debris`
**Overlay:** `04_Technology/handbooks/HB-02_Intake_Debris/contexts/CONTEXT_OVERLAYS.md`

```text
# Context Overlays

## [CREEK] Creek / Foothills Run-of-River
- (Add creek-specific requirements)

## [CANAL] Irrigation Canal Drop
- (Add canal-specific requirements)

## [OUTFALL] Industrial Outfall / Water-Works
- (Add outfall-specific requirements)

```
**Body:** `04_Technology/handbooks/HB-02_Intake_Debris/handbook.md`

```text
{{COVER}}

{{DISCLAIMER}}

# Intake & Debris Management (Run-of-River, Water-kind)

**Handbook ID:** HB-02  
**Version:** 0.1 (Draft)

---

## Deployment Contexts (Default: All Three)
This handbook is written to be valid for three default deployment environments:
- **[CREEK]** Creek / foothills run-of-river (cold + debris)
- **[CANAL]** Irrigation canal drop (high flow + ops crew)
- **[OUTFALL]** Industrial outfall / water-works (24/7 + compliance + corrosion)

Context overlays live in: `contexts/CONTEXT_OVERLAYS.md`.  
Shared definitions: `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`.

---


## Table of Contents
1. Overview
2. Key Principles
3. Deployment Contexts (Default: All Three)
4. Procedures
5. Failure Modes & Red Flags
6. Checklists
7. References

---

## 1) Overview
(Draft)

---

## 2) Key Principles
(Draft)

---

## 3) Deployment Contexts (Default: All Three)
(This section will be inserted automatically if missing.)

---

## 4) Procedures
(Draft)

---

## 5) Failure Modes & Red Flags
(Draft)

---

## 6) Checklists
See `checklists/`.

---

## 7) References
See `11_References/MASTER_REFERENCES.md`.

```
### `HB-03_Penstock_Headloss`
**Overlay:** `04_Technology/handbooks/HB-03_Penstock_Headloss/contexts/CONTEXT_OVERLAYS.md`

```text
# Context Overlays

## [CREEK] Creek / Foothills Run-of-River
- (Add creek-specific requirements)

## [CANAL] Irrigation Canal Drop
- (Add canal-specific requirements)

## [OUTFALL] Industrial Outfall / Water-Works
- (Add outfall-specific requirements)

```
**Body:** `04_Technology/handbooks/HB-03_Penstock_Headloss/handbook.md`

```text
{{COVER}}

{{DISCLAIMER}}

# Penstock & Headloss Design (≤10% Loss Standard)

**Handbook ID:** HB-03  
**Version:** 0.1 (Draft)

---

## Deployment Contexts (Default: All Three)
This handbook is written to be valid for three default deployment environments:
- **[CREEK]** Creek / foothills run-of-river (cold + debris)
- **[CANAL]** Irrigation canal drop (high flow + ops crew)
- **[OUTFALL]** Industrial outfall / water-works (24/7 + compliance + corrosion)

Context overlays live in: `contexts/CONTEXT_OVERLAYS.md`.  
Shared definitions: `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`.

---


## Table of Contents
1. Overview
2. Key Principles
3. Deployment Contexts (Default: All Three)
4. Procedures
5. Failure Modes & Red Flags
6. Checklists
7. References

---

## 1) Overview
(Draft)

---

## 2) Key Principles
(Draft)

---

## 3) Deployment Contexts (Default: All Three)
(This section will be inserted automatically if missing.)

---

## 4) Procedures
(Draft)

---

## 5) Failure Modes & Red Flags
(Draft)

---

## 6) Checklists
See `checklists/`.

---

## 7) References
See `11_References/MASTER_REFERENCES.md`.

```
### `HB-04_Hydram_Tuning`
**Overlay:** `04_Technology/handbooks/HB-04_Hydram_Tuning/contexts/CONTEXT_OVERLAYS.md`

```text
# Context Overlays

## [CREEK] Creek / Foothills Run-of-River
- (Add creek-specific requirements)

## [CANAL] Irrigation Canal Drop
- (Add canal-specific requirements)

## [OUTFALL] Industrial Outfall / Water-Works
- (Add outfall-specific requirements)

```
**Body:** `04_Technology/handbooks/HB-04_Hydram_Tuning/handbook.md`

```text
{{COVER}}

{{DISCLAIMER}}

# Hydraulic Ram Pump Design & Tuning

**Handbook ID:** HB-04  
**Version:** 0.1 (Draft)

---

## Deployment Contexts (Default: All Three)
This handbook is written to be valid for three default deployment environments:
- **[CREEK]** Creek / foothills run-of-river (cold + debris)
- **[CANAL]** Irrigation canal drop (high flow + ops crew)
- **[OUTFALL]** Industrial outfall / water-works (24/7 + compliance + corrosion)

Context overlays live in: `contexts/CONTEXT_OVERLAYS.md`.  
Shared definitions: `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`.

---


## Table of Contents
1. Overview
2. Key Principles
3. Deployment Contexts (Default: All Three)
4. Procedures
5. Failure Modes & Red Flags
6. Checklists
7. References

---

## 1) Overview
(Draft)

---

## 2) Key Principles
(Draft)

---

## 3) Deployment Contexts (Default: All Three)
(This section will be inserted automatically if missing.)

---

## 4) Procedures
(Draft)

---

## 5) Failure Modes & Red Flags
(Draft)

---

## 6) Checklists
See `checklists/`.

---

## 7) References
See `11_References/MASTER_REFERENCES.md`.

```
### `HB-05_Controls_SCADA`
**Overlay:** `04_Technology/handbooks/HB-05_Controls_SCADA/contexts/CONTEXT_OVERLAYS.md`

```text
# Context Overlays

## [CREEK] Creek / Foothills Run-of-River
- (Add creek-specific requirements)

## [CANAL] Irrigation Canal Drop
- (Add canal-specific requirements)

## [OUTFALL] Industrial Outfall / Water-Works
- (Add outfall-specific requirements)

```
**Body:** `04_Technology/handbooks/HB-05_Controls_SCADA/handbook.md`

```text
{{COVER}}

{{DISCLAIMER}}

# Controls, Blackstart & SCADA (Microgrid Backbone)

**Handbook ID:** HB-05  
**Version:** 0.1 (Draft)

---

## Deployment Contexts (Default: All Three)
This handbook is written to be valid for three default deployment environments:
- **[CREEK]** Creek / foothills run-of-river (cold + debris)
- **[CANAL]** Irrigation canal drop (high flow + ops crew)
- **[OUTFALL]** Industrial outfall / water-works (24/7 + compliance + corrosion)

Context overlays live in: `contexts/CONTEXT_OVERLAYS.md`.  
Shared definitions: `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`.

---


## Table of Contents
1. Overview
2. Key Principles
3. Deployment Contexts (Default: All Three)
4. Procedures
5. Failure Modes & Red Flags
6. Checklists
7. References

---

## 1) Overview
(Draft)

---

## 2) Key Principles
(Draft)

---

## 3) Deployment Contexts (Default: All Three)
(This section will be inserted automatically if missing.)

---

## 4) Procedures
(Draft)

---

## 5) Failure Modes & Red Flags
(Draft)

---

## 6) Checklists
See `checklists/`.

---

## 7) References
See `11_References/MASTER_REFERENCES.md`.

```
### `HB-06_Commissioning_FAT_SAT`
**Overlay:** `04_Technology/handbooks/HB-06_Commissioning_FAT_SAT/contexts/CONTEXT_OVERLAYS.md`

```text
# Context Overlays

## [CREEK] Creek / Foothills Run-of-River
- (Add creek-specific requirements)

## [CANAL] Irrigation Canal Drop
- (Add canal-specific requirements)

## [OUTFALL] Industrial Outfall / Water-Works
- (Add outfall-specific requirements)

```
**Body:** `04_Technology/handbooks/HB-06_Commissioning_FAT_SAT/handbook.md`

```text
{{COVER}}

{{DISCLAIMER}}

# Commissioning & Acceptance Testing (FAT → SAT)

**Handbook ID:** HB-06  
**Version:** 0.1 (Draft)

---

## Deployment Contexts (Default: All Three)
This handbook is written to be valid for three default deployment environments:
- **[CREEK]** Creek / foothills run-of-river (cold + debris)
- **[CANAL]** Irrigation canal drop (high flow + ops crew)
- **[OUTFALL]** Industrial outfall / water-works (24/7 + compliance + corrosion)

Context overlays live in: `contexts/CONTEXT_OVERLAYS.md`.  
Shared definitions: `04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md`.

---


## Table of Contents
1. Overview
2. Key Principles
3. Deployment Contexts (Default: All Three)
4. Procedures
5. Failure Modes & Red Flags
6. Checklists
7. References

---

## 1) Overview
(Draft)

---

## 2) Key Principles
(Draft)

---

## 3) Deployment Contexts (Default: All Three)
(This section will be inserted automatically if missing.)

---

## 4) Procedures
(Draft)

---

## 5) Failure Modes & Red Flags
(Draft)

---

## 6) Checklists
See `checklists/`.

---

## 7) References
See `11_References/MASTER_REFERENCES.md`.

```
