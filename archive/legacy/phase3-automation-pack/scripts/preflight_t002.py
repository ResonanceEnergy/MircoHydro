#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import json
import numpy as np
import pandas as pd

BAND_LOW = 0.2
BAND_HIGH = 20.0

def compute_psd(x: np.ndarray, fs: float):
    x = x - np.nanmean(x)
    try:
        from scipy.signal import welch
        f, pxx = welch(x, fs=fs, nperseg=min(2048, len(x)))
    except Exception:
        n = len(x)
        win = np.hanning(n)
        xf = np.fft.rfft(x * win)
        pxx = (np.abs(xf) ** 2) / (fs * np.sum(win ** 2))
        f = np.fft.rfftfreq(n, d=1.0/fs)
    return f, pxx

def main(argv=None):
    ap = argparse.ArgumentParser(description='Preflight T-002 timeseries (Time_s, Pressure_Pa).')
    ap.add_argument('--csv', required=True)
    ap.add_argument('--time-col', default='Time_s')
    ap.add_argument('--signal-col', default='Pressure_Pa')
    ap.add_argument('--no-write', action='store_true')
    args = ap.parse_args(argv)

    p = Path(args.csv)
    df = pd.read_csv(p)
    if args.time_col not in df.columns or args.signal_col not in df.columns:
        raise SystemExit(f"Missing columns. Need {args.time_col} and {args.signal_col}. Got: {list(df.columns)}")

    t = pd.to_numeric(df[args.time_col], errors='coerce').to_numpy()
    x = pd.to_numeric(df[args.signal_col], errors='coerce').to_numpy()
    m = np.isfinite(t) & np.isfinite(x)
    t, x = t[m], x[m]

    report = {
        'file': str(p.as_posix()),
        'n_rows': int(len(df)),
        'n_valid': int(len(t)),
        'time_monotonic': None,
        'fs_est_hz': None,
        'band_hz': [BAND_LOW, BAND_HIGH],
        'peakiness': None,
        'dominant_hz': None,
        'warnings': [],
    }

    if len(t) < 10:
        report['warnings'].append('Not enough valid samples after cleaning.')
        print(json.dumps(report, indent=2))
        raise SystemExit(2)

    dt = np.diff(t)
    dt_pos = dt[np.isfinite(dt) & (dt > 0)]
    report['time_monotonic'] = bool(len(dt_pos) == len(dt) and np.all(dt > 0))
    if not report['time_monotonic']:
        report['warnings'].append('Time_s is not strictly monotonic. Check logger export.')

    fs = 1.0 / float(np.median(dt_pos)) if len(dt_pos) else 100.0
    report['fs_est_hz'] = float(fs)

    f, pxx = compute_psd(x, fs)
    band = (f >= BAND_LOW) & (f <= BAND_HIGH)
    if not np.any(band):
        report['warnings'].append('No PSD bins in 0.2–20 Hz band. Check sampling/timebase.')
        print(json.dumps(report, indent=2))
        raise SystemExit(2)

    pband = pxx[band]
    peak = float(np.max(pband))
    med = float(np.median(pband))
    report['peakiness'] = float(peak / max(1e-12, med))
    report['dominant_hz'] = float(f[band][np.argmax(pband)])

    print(json.dumps(report, indent=2))

    if not args.no_write:
        out = p.with_suffix('.preflight.json')
        out.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
