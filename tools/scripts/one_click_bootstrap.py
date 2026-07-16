#!/usr/bin/env python3
"""
FULL BOOTSTRAP LOGIC — HYBRID MODE
Creates and updates:
- governance structure (00_MASTER_PLAN/*)
- branding files
- company files
- RND annex structure
Preserves:
- all HB-* content
- any custom operational docs
"""

from __future__ import annotations
import argparse, datetime, subprocess
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.date.today().isoformat()
ART = ROOT / "artifacts"
ART.mkdir(exist_ok=True)

def write(path: Path, content: str, force: bool = False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return f"SKIP (exists): {path}"
    path.write_text(content, encoding="utf-8")
    return f"WROTE: {path}"

def section(title): return f"\n# --- {title} ---\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    force = args.force

    report = [f"# Bootstrap Report — {datetime.datetime.now()}"]

    # -----------------------------
    # 00_MASTER_PLAN (always overwritten)
    # -----------------------------
    report.append(section("Master Plan"))
    report.append(write(ROOT/"00_MASTER_PLAN"/"MASTER_PLAN.md", f"# Master Plan\n\nGenerated: {TODAY}\n", force=True))
    report.append(write(ROOT/"00_MASTER_PLAN"/"FILE_STRUCTURE_MAP.md", "# File Structure Map\n", force=True))
    report.append(write(ROOT/"00_MASTER_PLAN"/"POPULATION_ROADMAP.md", "# Population Roadmap\n", force=True))
    report.append(write(ROOT/"00_MASTER_PLAN"/"DECISION_LOG.md", f"# Decision Log\n\nCreated {TODAY}\n", force=True))

    # -----------------------------
    # Branding (always overwritten)
    # -----------------------------
    report.append(section("Branding"))
    report.append(write(ROOT/"branding"/"DECISIONS_AND_TODOS.md", "# Branding Decisions & TODOs\n", force=True))
    report.append(write(ROOT/"branding"/"taglines"/"TAGLINES_MASTER.md", "# Taglines Master\n", force=True))

    # -----------------------------
    # Company (always overwritten)
    # -----------------------------
    report.append(section("Company"))
    report.append(write(ROOT/"01_Company"/"FOUNDING_STATEMENT.md", "# Founding Statement\n", force=True))
    report.append(write(ROOT/"01_Company"/"VISION_MISSION_VALUES.md", "# Vision, Mission, Values\n", force=True))
    report.append(write(ROOT/"01_Company"/"NORTH_STAR_METRICS.md", "# North Star Metrics\n", force=True))

    # -----------------------------
    # RND Annex (always overwritten)
    # -----------------------------
    report.append(section("RND Annex"))
    report.append(write(ROOT/"05_RND"/"annex_winter_phase_coherence"/"DISCLAIMER.md", "# Winter Phase Coherence Annex\n", force=True))
    report.append(write(ROOT/"05_RND"/"experiment_registry"/"EXP-000_TEMPLATE.md", "# Experiment Template\n", force=True))

    # -----------------------------
    # Bootstrap done
    # -----------------------------
    out_path = ART/"bootstrap_report.md"
    out_path.write_text("\n".join(report), encoding="utf-8")
    print("BOOTSTRAP COMPLETE — report written:", out_path)

if __name__ == "__main__":
    main()
