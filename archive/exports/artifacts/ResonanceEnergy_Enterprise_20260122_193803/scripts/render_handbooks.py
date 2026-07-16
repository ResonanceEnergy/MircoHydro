#!/usr/bin/env python3
"""
Manual PDF renderer for handbooks.
Reads: 04_Technology/handbooks/HB-*/handbook.md
Expands {{COVER}} and {{DISCLAIMER}} from 04_Technology/handbooks/_shared/
Outputs PDFs into each handbook's exports/ folder.

Run:
  python3 scripts/render_handbooks.py

Requires:
  pip3 install reportlab
(or: python3 -m pip install reportlab)
"""

import json
import datetime
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

ROOT = Path(__file__).resolve().parents[1]
HB_ROOT = ROOT / "04_Technology" / "handbooks"
SHARED = HB_ROOT / "_shared"

def load_style():
    p = SHARED / "handbook_style.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"margins_in": {"left": 0.75, "right": 0.75, "top": 0.75, "bottom": 0.75},
            "fonts": {"h1": 16, "h2": 13, "body": 10},
            "line_spacing": {"body": 13}}

def md_to_story(md: str, style):
    ss = getSampleStyleSheet()
    body = ParagraphStyle("Body", parent=ss["Normal"], fontName="Helvetica",
                          fontSize=style["fonts"]["body"], leading=style["line_spacing"]["body"])
    h1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold",
                        fontSize=style["fonts"]["h1"], leading=style["fonts"]["h1"] + 4, spaceAfter=10)
    h2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold",
                        fontSize=style["fonts"]["h2"], leading=style["fonts"]["h2"] + 3, spaceAfter=8)

    story = []
    for raw in md.splitlines():
        line = raw.rstrip()
        if not line:
            story.append(Spacer(1, 0.12 * inch))
            continue
        if line.strip() == "[[PAGEBREAK]]":
            story.append(PageBreak()); continue
        if line.startswith("# "):
            story.append(Paragraph(line[2:], h1)); continue
        if line.startswith("## "):
            story.append(Paragraph(line[3:], h2)); continue
        if line.startswith("---"):
            story.append(Spacer(1, 0.2 * inch)); continue
        if line.startswith("- "):
            story.append(Paragraph("• " + line[2:], body)); continue

        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        safe = safe.replace("**", "<b>").replace("<b><b>", "</b>")
        story.append(Paragraph(safe, body))

    return story

def expand_templates(md: str, handbook_id: str, title: str, version: str):
    cover = (SHARED / "COVER_TEMPLATE.md").read_text(encoding="utf-8")
    disclaimer = (SHARED / "DISCLAIMER.md").read_text(encoding="utf-8")
    cover = (cover.replace("{{HANDBOOK_ID}}", handbook_id)
                  .replace("{{TITLE}}", title)
                  .replace("{{VERSION}}", version)
                  .replace("{{DATE}}", datetime.date.today().isoformat()))
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
            title = s[2:]; break
    return handbook_id, title, version

def render_handbook(folder: Path, style):
    md_path = folder / "handbook.md"
    if not md_path.exists():
        return
    md = md_path.read_text(encoding="utf-8")
    handbook_id, title, version = parse_meta(md, folder.name)
    md = expand_templates(md, handbook_id, title, version)

    out_dir = folder / "exports"
    out_dir.mkdir(exist_ok=True)
    pdf_path = out_dir / f"{handbook_id}_{title.replace(' ', '_')}.pdf"

    m = style["margins_in"]
    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter,
                            leftMargin=m["left"] * inch, rightMargin=m["right"] * inch,
                            topMargin=m["top"] * inch, bottomMargin=m["bottom"] * inch)

    story = md_to_story(md, style)
    doc.build(story)
    print(f"Rendered: {pdf_path}")

def main():
    style = load_style()
    for hb in HB_ROOT.iterdir():
        if hb.is_dir() and hb.name.startswith("HB-"):
            render_handbook(hb, style)

if __name__ == "__main__":
    main()
