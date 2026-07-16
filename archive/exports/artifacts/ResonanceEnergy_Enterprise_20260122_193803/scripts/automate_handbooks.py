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
