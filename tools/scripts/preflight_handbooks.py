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
