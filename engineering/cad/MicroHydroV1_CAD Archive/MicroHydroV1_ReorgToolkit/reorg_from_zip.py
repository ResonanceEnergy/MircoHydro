#!/usr/bin/env python3
import os, sys, zipfile, shutil, re, hashlib, json
from pathlib import Path
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print('Usage: python reorg_from_zip.py "/absolute/path/to/MICRO HYDRO.zip"')
        sys.exit(1)
    src = Path(sys.argv[1]).expanduser()
    if not src.exists():
        print('ERROR: zip not found:', src)
        sys.exit(2)

    work = Path.cwd()
    stage = work / 'stage_extract'
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    with zipfile.ZipFile(src, 'r') as z:
        z.extractall(stage)

    root = work / 'MicroHydroV1'
    if root.exists():
        shutil.rmtree(root)
    skeleton = [
        '01_CAD/macros','01_CAD/params','01_CAD/exports',
        '02_Testing/procedures','02_Testing/runbooks','02_Testing/fixtures','02_Testing/risk',
        '03_Data/intake_raw','03_Data/processed','03_Data/synthetic','03_Data/RnD_Workbook','03_Data/reports_cache',
        '04_Analysis/notebooks','04_Analysis/scripts','04_Analysis/models',
        '05_Outputs/StageA','05_Outputs/StageB','05_Outputs/StageC','05_Outputs/StageD','05_Outputs/archive',
        '06_Docs/requirements','06_Docs/design_readouts','06_Docs/governance'
    ]
    for d in skeleton:
        (root / d).mkdir(parents=True, exist_ok=True)

    re_rnd_any = re.compile(r'MicroHydroV1_RnD_Export.*\.xlsx$', re.I)
    re_rnd_synth = re.compile(r'.*SYNTH.*\.xlsx$', re.I)
    re_importer = re.compile(r'import_measurements\.py$', re.I)
    re_stageB_nb = re.compile(r'StageB_Analysis\.ipynb$', re.I)
    re_cad_zip = re.compile(r'MicroHydroV1_CAD.*\.zip$', re.I)
    re_cad_macro = re.compile(r'.*\.FCMacro$', re.I)
    re_params_json = re.compile(r'params\.json$', re.I)

    all_files = [p for p in stage.rglob('*') if p.is_file() and '__MACOSX' not in p.as_posix() and not p.name.startswith('._')]
    rnd_candidates, rnd_synth = [], []
    importer_file = None
    notebooks = []
    procedures = []
    risk_files = []
    runbooks_files = []
    fixtures = []
    models = []
    stage_reports = []
    intake_csvs = []
    synthetic_csvs = []
    macros = []
    params_files = []
    cad_zips = []
    decks = []
    gonogo = []
    stw = []
    readouts = []
    reqs = []

    for f in all_files:
        n = f.name; low = n.lower()
        if re_rnd_any.search(n):
            if re_rnd_synth.search(n) or '(1' in n or 'fullupgrade' in low:
                rnd_synth.append(f)
            else:
                rnd_candidates.append(f)
            continue
        if re_importer.search(n):
            importer_file = f; continue
        if re_stageB_nb.search(n):
            notebooks.append(f); continue
        if n.lower().endswith('.csv'):
            (synthetic_csvs if 'synt' in low else intake_csvs).append(f); continue
        if n.endswith('.docx'):
            if 'procedure' in low or 'test plan' in low or 'tank_ripple' in low or 'jet_coherence' in low:
                procedures.append(f); continue
            if 'risk' in low:
                risk_files.append(f); continue
            if 'run-of' in low or 'run_of' in low:
                runbooks_files.append(f); continue
            if 'layout' in low or 'mounting' in low:
                fixtures.append(f); continue
            if 'readout' in low:
                readouts.append(f); continue
            if 'requirements' in low or 'acceptance' in low:
                reqs.append(f); continue
            if 'gono' in low or 'go/no-go' in low or 'go-no-go' in low:
                gonogo.append(f); continue
            if 'stw' in low:
                stw.append(f); continue
            if 'pass a' in low or 'stage b' in low or 'stageb' in low:
                stage_reports.append(f); continue
            continue
        if n.endswith('.pptx'):
            if 'stakeholder' in low or 'progress' in low:
                decks.append(f); continue
            if 'layout' in low:
                fixtures.append(f); continue
        if n.endswith('.xlsx'):
            if any(k in low for k in ['frequency','model','run2','penstock','tank_ripple','nozzle_data']):
                models.append(f); continue
        if re_cad_zip.search(n): cad_zips.append(f); continue
        if re_cad_macro.search(n): macros.append(f); continue
        if re_params_json.search(n): params_files.append(f); continue

    # Canonical RnD workbook
    if rnd_candidates:
        rnd_candidates.sort(key=lambda p: (len(p.as_posix()), p.as_posix()))
        canonical = rnd_candidates[0]
        shutil.copy2(canonical, root / '03_Data/RnD_Workbook/MicroHydroV1_RnD_Export.xlsx')
    for f in rnd_synth:
        shutil.copy2(f, root / '03_Data/synthetic' / f.name)

    # Importer patch
    if importer_file:
        txt = importer_file.read_text(encoding='utf-8', errors='ignore')
        txt = re.sub(r"EXCEL_NAME\s*=\s*'MicroHydroV1_RnD_Export.xlsx'",
                     "# Patched to repo structure\nEXCEL_NAME = 'MicroHydroV1_RnD_Export.xlsx'\nWORKBOOK_DIR = Path(__file__).resolve().parents[2] / '03_Data' / 'RnD_Workbook'\nEXCEL_PATH = WORKBOOK_DIR / EXCEL_NAME",
                     txt)
        txt = txt.replace('load_workbook(EXCEL_NAME)', 'load_workbook(EXCEL_PATH)')
        txt = txt.replace('wb.save(EXCEL_NAME)', 'wb.save(EXCEL_PATH)')
        txt = txt.replace("Path('.')", "Path(__file__).resolve().parents[2] / '03_Data' / 'intake_raw'")
        (root / '04_Analysis/scripts').mkdir(parents=True, exist_ok=True)
        (root / '04_Analysis/scripts/import_measurements.py').write_text(txt, encoding='utf-8')

    # Move notebooks
    for nb in notebooks:
        shutil.copy2(nb, root / '04_Analysis/notebooks' / nb.name)

    # CAD
    cad_zips.sort(key=lambda p: ('fixed' not in p.name.lower(), len(p.as_posix())))
    if cad_zips:
        with zipfile.ZipFile(cad_zips[0], 'r') as z:
            z.extractall(root / '01_CAD')
    for m in macros:
        try:
            shutil.copy2(m, root / '01_CAD/macros' / m.name)
        except:
            pass
    if params_files:
        params_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        shutil.copy2(params_files[0], root / '01_CAD/params/params.json')

    # Patch build_all
    for b in (root / '01_CAD').rglob('build_all.FCMacro'):
        try:
            t = b.read_text(encoding='utf-8', errors='ignore')
            t = re.sub(r"CAD_ROOT\s*=\s*r?'.*'",
                       "CAD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))",
                       t)
            if 'def load_params' in t:
                t = re.sub(r"def load_params\(\):[\s\S]*?return json.load\(f\)",
                           "def load_params():\n    p = os.path.join(CAD_ROOT, 'params', 'params.json')\n    with open(p, 'r') as f:\n        return json.load(f)", t)
            b.write_text(t, encoding='utf-8')
        except:
            pass

    # Procedures, risk, etc.
    for p in procedures: shutil.copy2(p, root / '02_Testing/procedures' / p.name)
    for r in risk_files: shutil.copy2(r, root / '02_Testing/risk' / r.name)
    for rb in runbooks_files: shutil.copy2(rb, root / '02_Testing/runbooks' / rb.name)
    for fx in fixtures: shutil.copy2(fx, root / '02_Testing/fixtures' / fx.name)
    for mdl in models: shutil.copy2(mdl, root / '04_Analysis/models' / mdl.name)
    for s in stage_reports: shutil.copy2(s, root / '05_Outputs/StageA' / s.name)
    for d in decks: shutil.copy2(d, root / '05_Outputs/StageD' / d.name)
    for g in gonogo: shutil.copy2(g, root / '05_Outputs/StageD' / g.name)
    for st in stw: shutil.copy2(st, root / '05_Outputs/StageD' / st.name)
    for dr in readouts: shutil.copy2(dr, root / '06_Docs/design_readouts' / dr.name)
    for rq in reqs: shutil.copy2(rq, root / '06_Docs/requirements' / rq.name)

    for c in intake_csvs: shutil.copy2(c, root / '03_Data/intake_raw' / c.name)
    for sc in synthetic_csvs: shutil.copy2(sc, root / '03_Data/synthetic' / sc.name)

    # READMEs
    (root / '01_CAD/README.md').write_text('# CAD\nRun FreeCAD macros from macros/build_all.FCMacro.', encoding='utf-8')
    (root / '03_Data/README.md').write_text('# Data\nReal CSVs → intake_raw; Synthetic → synthetic; Workbook → RnD_Workbook.', encoding='utf-8')

    # Makefile
    (root / 'Makefile').write_text('DATE := $(shell date +%Y%m%d_%H%M)\n\nimport:\n\tpython 04_Analysis/scripts/import_measurements.py\n\n bundle:\n\tzip -r 05_Outputs/archive/MicroHydroV1_$(DATE).zip 05_Outputs/ 02_Testing/runbooks/ 06_Docs/requirements/ 01_CAD/exports/\n', encoding='utf-8')

    # Manifest
    manifest = {'generated': datetime.utcnow().isoformat()+'Z', 'files': [], 'duplicates': []}
    seen = {}
    for p in root.rglob('*'):
        if p.is_file():
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            manifest['files'].append({'path': p.as_posix(), 'sha256': h, 'bytes': p.stat().st_size})
            if h in seen:
                manifest['duplicates'].append({'a': seen[h], 'b': p.as_posix()})
            else:
                seen[h] = p.as_posix()
    (root / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')

    # Master zip
    master = f"MicroHydroV1_Rebuilt_Clean_Repo_{datetime.utcnow().strftime('%Y%m%d_%H%M%SZ')}.zip"
    with zipfile.ZipFile(master, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in root.rglob('*'):
            z.write(p, p.relative_to(root.parent))

    print('DONE. Clean repo at:', root)
    print('Master zip:', master)

if __name__ == '__main__':
    main()
