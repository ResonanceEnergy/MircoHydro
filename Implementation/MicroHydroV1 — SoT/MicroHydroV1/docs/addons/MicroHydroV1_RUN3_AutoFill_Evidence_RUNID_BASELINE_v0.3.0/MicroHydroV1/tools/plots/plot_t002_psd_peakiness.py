#!/usr/bin/env python3
"""Plot T-002 PSD + Peakiness (LOCKED-IN metric).

Inputs:
- CSV with columns: Time_s, Pressure_Pa

Outputs:
- PNG plot showing time series + PSD + peakiness value in 0.2–20 Hz band.

Usage:
  python tools/plots/plot_t002_psd_peakiness.py --csv tests/raw/RUN3/T002_TankRipple_timeseries.csv --out tests/results/summary/T002_PSD_Peakiness.png

"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PHI_BAND = (0.2, 20.0)


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
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', required=True, help='T-002 timeseries CSV (Time_s, Pressure_Pa)')
    ap.add_argument('--out', required=True, help='Output PNG path')
    ap.add_argument('--time-col', default='Time_s')
    ap.add_argument('--signal-col', default='Pressure_Pa')
    args = ap.parse_args(argv)

    df = pd.read_csv(args.csv)
    if args.time_col not in df.columns or args.signal_col not in df.columns:
        raise SystemExit(f"Missing columns. Need {args.time_col} and {args.signal_col}. Got: {list(df.columns)}")

    t = pd.to_numeric(df[args.time_col], errors='coerce').to_numpy()
    x = pd.to_numeric(df[args.signal_col], errors='coerce').to_numpy()

    m = np.isfinite(t) & np.isfinite(x)
    t, x = t[m], x[m]

    # infer fs from median dt
    dt = np.diff(t)
    dt = dt[np.isfinite(dt) & (dt > 0)]
    fs = 1.0 / float(np.median(dt)) if len(dt) else 100.0

    f, pxx = compute_psd(x, fs)
    f_low, f_high = PHI_BAND
    band = (f >= f_low) & (f <= f_high)
    p = pxx[band]

    peak = float(np.max(p))
    med = float(np.median(p)) if len(p) else float('nan')
    peakiness = peak / max(1e-12, med)

    # dominant frequency in band
    f_dom = float(f[band][np.argmax(p)]) if np.any(band) else float('nan')

    # Plot
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10,6))

    ax1 = plt.subplot(2,1,1)
    ax1.plot(t - t[0], x, linewidth=1)
    ax1.set_title('T-002 Ripple Time Series (Pressure_Pa)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Pressure (Pa)')
    ax1.grid(True, alpha=0.3)

    ax2 = plt.subplot(2,1,2)
    ax2.semilogy(f, pxx, linewidth=1)
    ax2.axvspan(f_low, f_high, color='orange', alpha=0.15, label='0.2–20 Hz band')
    ax2.axvline(f_dom, color='red', linestyle='--', linewidth=1, label=f'Dominant {f_dom:.2f} Hz')
    ax2.set_title(f'PSD + Peakiness (max/median) = {peakiness:.3f}  |  fs≈{fs:.2f} Hz')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('PSD')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    print('Saved:', out_path)


if __name__ == '__main__':
    main()
