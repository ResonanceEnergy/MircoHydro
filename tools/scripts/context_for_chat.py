
#!/usr/bin/env python3
"""
context_for_chat.py — Build a single Markdown "Context Pack" from the repo for pasting into a new chat.

DEFAULTS (Nathan's choice = A):
- Includes FULL handbook bodies for HB-01..HB-06 by default.

Usage:
  python3 scripts/context_for_chat.py
  python3 scripts/context_for_chat.py --out artifacts/chat_context/CHAT_CONTEXT.md
  python3 scripts/context_for_chat.py --max-chars 55000
  python3 scripts/context_for_chat.py --per-file-chars 12000
  python3 scripts/context_for_chat.py --include-hb-body false
"""

from __future__ import annotations
import argparse
import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "artifacts" / "chat_context" / "CHAT_CONTEXT.md"

# Core files we want for continuity
TRUTH_SET = [
    "branding/DECISIONS_AND_TODOS.md",
    "branding/taglines/TAGLINES_MASTER.md",

    "04_Technology/handbooks/README.md",
    "04_Technology/handbooks/_shared/DEFAULT_CONTEXTS.md",
    "04_Technology/handbooks/_shared/CONTEXT_MATRIX.md",
    "04_Technology/handbooks/_shared/COVER_TEMPLATE.md",
    "04_Technology/handbooks/_shared/DISCLAIMER.md",
    "04_Technology/handbooks/_shared/handbook_style.json",

    "11_References/MASTER_REFERENCES.md",

    "scripts/README.md",
    "scripts/automate_handbooks.py",
    "scripts/preflight_handbooks.py",
    "scripts/render_handbooks.py",
    "scripts/zip_repo_safe.py",
]

HB_FOLDERS = [
    "HB-01_Turbine_Selection",
    "HB-02_Intake_Debris",
    "HB-03_Penstock_Headloss",
    "HB-04_Hydram_Tuning",
    "HB-05_Controls_SCADA",
    "HB-06_Commissioning_FAT_SAT",
]

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n\n[TRUNCATED: {len(text)-limit} chars omitted]\n"

def section(title: str) -> str:
    return f"\n\n---\n\n## {title}\n\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=str, default=str(DEFAULT_OUTPUT))
    ap.add_argument("--max-chars", type=int, default=55000, help="Total max characters in output")
    ap.add_argument("--per-file-chars", type=int, default=12000, help="Max characters per included file")
    ap.add_argument("--include-hb-body", type=str, default="true", help="Include handbook.md bodies (true/false)")
    args = ap.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    include_hb = args.include_hb_body.lower() in ("true", "1", "yes", "y")

    pieces = []
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    pieces.append("# Resonance Energy Systems — Chat Context Pack\n")
    pieces.append(f"**Generated:** {ts}\n")
    pieces.append(f"**Repo root:** `{REPO_ROOT}`\n")
    pieces.append("\n> Paste this entire file into a new chat to restore full context.\n")
    pieces.append("> Source-of-truth policy: repo contents override chat assumptions.\n")

    # 1) Truth set files
    pieces.append(section("Core Truth Set (Key Files)"))
    for rel in TRUTH_SET:
        p = REPO_ROOT / rel
        if not p.exists():
            pieces.append(f"### MISSING: `{rel}`\n")
            continue
        content = truncate(read_text(p), args.per_file_chars)
        pieces.append(f"### `{rel}`\n\n```text\n{content}\n```\n")

    # 2) Handbooks (Overlays + Body)
    pieces.append(section("Handbooks (HB-01..HB-06)"))
    hb_root = REPO_ROOT / "04_Technology" / "handbooks"

    for hb in HB_FOLDERS:
        hb_dir = hb_root / hb
        pieces.append(f"### `{hb}`\n")

        if not hb_dir.exists():
            pieces.append(f"- MISSING folder: `{hb_dir}`\n")
            continue

        overlay = hb_dir / "contexts" / "CONTEXT_OVERLAYS.md"
        if overlay.exists():
            pieces.append(f"**Overlay:** `{overlay.relative_to(REPO_ROOT)}`\n\n```text\n{truncate(read_text(overlay), args.per_file_chars)}\n```\n")
        else:
            pieces.append(f"- MISSING overlay: `{overlay.relative_to(REPO_ROOT)}`\n")

        hb_md = hb_dir / "handbook.md"
        if include_hb and hb_md.exists():
            pieces.append(f"**Body:** `{hb_md.relative_to(REPO_ROOT)}`\n\n```text\n{truncate(read_text(hb_md), args.per_file_chars)}\n```\n")
        elif include_hb:
            pieces.append(f"- MISSING handbook: `{hb_md.relative_to(REPO_ROOT)}`\n")

    # Final size clamp (protect against chat limits)
    joined = "".join(pieces)
    joined = truncate(joined, args.max_chars)

    out_path.write_text(joined, encoding="utf-8")
    print(f"Created Context Pack: {out_path}")

if __name__ == "__main__":
    main()

