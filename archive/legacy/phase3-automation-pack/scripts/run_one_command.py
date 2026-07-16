#!/usr/bin/env python3
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path
import datetime as dt


def run(cmd: list[str]):
    print('[RUN]', ' '.join(cmd))
    subprocess.check_call(cmd)


def main(argv=None):
    ap = argparse.ArgumentParser(description='One-command per-run pipeline wrapper (Phase 3, macOS).')
    ap.add_argument('--root', default='.')
    ap.add_argument('--run-id', required=True)
    ap.add_argument('--version-tag', default=None)
    ap.add_argument('--date', default=None)
    ap.add_argument('--t002', default=None)
    ap.add_argument('--releases-url', default=None, help='Optional. If set (or env MICROHYDRO_RELEASES_URL), opens in browser after release.')
    ap.add_argument('--skip-optimize', action='store_true')
    ap.add_argument('--skip-import', action='store_true')
    ap.add_argument('--skip-evidence', action='store_true')
    ap.add_argument('--skip-release', action='store_true')
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    run_id = args.run_id

    # infer version tag like RUN3 from run-id
    version = args.version_tag
    if not version:
        import re
        m = re.search(r'Run(\d+)', run_id, re.IGNORECASE)
        version = f"RUN{m.group(1)}" if m else 'RUN'

    date = args.date or dt.date.today().isoformat()

    t002 = Path(args.t002) if args.t002 else (root/'tests'/'raw'/run_id/'T002_TankRipple_timeseries.csv')
    if not t002.is_absolute():
        t002 = root/t002

    # Preflight
    preflight = root/'scripts'/'preflight_t002.py'
    if preflight.exists() and t002.exists():
        run(['python3', str(preflight), '--csv', str(t002)])
    else:
        print('[WARN] Preflight skipped (missing scripts/preflight_t002.py or T002 file).')

    # Closed loop wrapper (existing tool)
    closed = root/'tools'/'workflow'/'run_closed_loop.py'
    if not closed.exists():
        print('[ERROR] Missing tools/workflow/run_closed_loop.py — copy MicroHydroV1 tools into this repo root.')
        sys.exit(2)

    cmd = ['python3', str(closed), '--root', str(root), '--version', version, '--date', date]
    if not args.skip_optimize:
        cmd += ['--optimize', '--resonance-csv', str(t002)]
    if not args.skip_import:
        cmd += ['--import']
    if not args.skip_release:
        cmd += ['--release']
    run(cmd)

    # Evidence generation (if scripts exist)
    if not args.skip_evidence:
        plot = root/'tools'/'plots'/'plot_t002_psd_peakiness.py'
        out_plot = root/'tests'/'results'/'summary'/'T002_PSD_Peakiness.png'
        if plot.exists() and t002.exists():
            run(['python3', str(plot), '--csv', str(t002), '--out', str(out_plot)])

        autofill = root/'tools'/'workflow'/'autofill_evidence_doc.py'
        if autofill.exists() and t002.exists():
            import re
            m = re.search(r'Run(\d+)', run_id, re.IGNORECASE)
            run_num = m.group(1) if m else 'X'
            docs_run = root/'docs'/f'run{run_num}'
            docs_run.mkdir(parents=True, exist_ok=True)
            out_doc = docs_run/f'{version}_Evidence_{run_id}.docx'
            wb = root/'automation'/'MicroHydroV1_RnD_Export.xlsx'
            cmd2 = ['python3', str(autofill), '--root', str(root), '--run-id', run_id, '--t002', str(t002), '--out-doc', str(out_doc), '--out-plot', str(out_plot)]
            if wb.exists():
                cmd2 += ['--workbook', str(wb)]
            run(cmd2)

    print('\n[NEXT] Manual CAD build step (as designed):')
    print('  FreeCAD GUI -> Macro -> cad/macros/build_all.FCMacro')
    print('[NEXT] Upload dist/*.zip to SharePoint Releases (per-run).')

    # macOS convenience: open dist folder and Releases URL
    try:
        import os
        dist_dir = root/'dist'
        if dist_dir.exists():
            subprocess.call(['open', str(dist_dir)])
        url = (args.releases_url or os.environ.get('MICROHYDRO_RELEASES_URL','')).strip()
        if url:
            subprocess.call(['open', url])
    except Exception:
        pass


if __name__ == '__main__':
    main()
