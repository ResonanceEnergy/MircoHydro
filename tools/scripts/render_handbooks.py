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
