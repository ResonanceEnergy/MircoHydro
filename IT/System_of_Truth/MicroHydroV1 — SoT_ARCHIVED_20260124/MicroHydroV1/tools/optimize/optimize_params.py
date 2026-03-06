#!/usr/bin/env python3
"""MicroHydroV1 - Parameter optimizer (LOCKED-IN resonance metric).

LOCKED-IN resonance metric (v0.3.0):
  Primary resonance metric = T-002 hydraulic ripple PSD peakiness
  Score = max(PSD) / median(PSD) within 0.2-20 Hz (lower is better)

Defaults (LOCKED-IN):
  --signal-col Pressure_Pa
  --time-col Time_s

Usage:
  python tools/optimize/optimize_params.py     --params cad/params/params.json     --config tools/optimize/opt_config.json     --out cad/params/params_optimized.json     --resonance-csv tests/raw/<run>/T002_timeseries.csv

"""

from __future__ import annotations

import argparse, json, math, random
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def safe_float(x) -> float:
    try:
        return float(x)
    except Exception:
        return float('nan')


def get_path(d: Dict[str, Any], path: str) -> Any:
    cur = d
    for k in path.split('.'):
        cur = cur[k]
    return cur


def set_path(d: Dict[str, Any], path: str, value: Any) -> None:
    keys = path.split('.')
    cur = d
    for k in keys[:-1]:
        cur = cur[k]
    cur[keys[-1]] = value


def build_namespace(params: Dict[str, Any]) -> Dict[str, float]:
    ns: Dict[str, float] = {}

    def flatten(prefix: str, obj: Any):
        if isinstance(obj, dict):
            for k, v in obj.items():
                flatten(prefix + k + '.', v)
        else:
            ns[prefix[:-1]] = safe_float(obj)

    flatten('', params)
    return ns


def compute_expr(params: Dict[str, Any], expr: str) -> float:
    ns = build_namespace(params)
    allowed = set('0123456789.+-*/() _abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if any(ch not in allowed for ch in expr):
        raise ValueError('Invalid characters in expression')
    return float(eval(expr, {'__builtins__': {}}, ns))


def read_timeseries_csv(path: Path, signal_col: str, time_col: Optional[str]):
    import csv
    xs, ts = [], []
    with path.open('r', newline='', encoding='utf-8-sig') as f:
        r = csv.DictReader(f)
        for row in r:
            x = safe_float(row.get(signal_col, 'nan'))
            if not math.isfinite(x):
                continue
            xs.append(x)
            if time_col:
                t = safe_float(row.get(time_col, 'nan'))
                ts.append(t)
    x = np.asarray(xs, dtype=float)
    t = np.asarray(ts, dtype=float) if time_col else None
    return t, x


def psd_peakiness(x: np.ndarray, fs: float, f_low: float, f_high: float, normalize: str):
    x = np.asarray(x, dtype=float)
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

    band = (f >= f_low) & (f <= f_high)
    if not np.any(band):
        return float('inf')

    p = pxx[band]
    peak = float(np.max(p))
    if normalize == 'none':
        return peak
    denom = float(np.median(p)) if normalize == 'median' else float(np.mean(p))
    denom = max(1e-12, denom)
    return peak / denom


def resonance_from_data(csv_path: Path, res_cfg: Dict[str, Any], fs: Optional[float], signal_col: str, time_col: Optional[str]):
    f_low, f_high = res_cfg.get('band_hz', [0.2, 20.0])
    normalize = res_cfg.get('normalize', 'median')
    t, x = read_timeseries_csv(csv_path, signal_col, time_col)

    if time_col and t is not None and len(t) > 3:
        dt = np.diff(t)
        dt = dt[np.isfinite(dt) & (dt > 0)]
        fs_use = (1.0 / float(np.median(dt))) if len(dt) else (float(fs) if fs else 100.0)
    else:
        fs_use = float(fs) if fs else 100.0

    return psd_peakiness(x, fs_use, float(f_low), float(f_high), normalize)


def score(params: Dict[str, Any], cfg: Dict[str, Any], resonance_score: Optional[float]):
    phi_err = 0.0
    for t in cfg.get('phi_targets', []):
        r = compute_expr(params, t['expr'])
        w = float(t.get('weight', 1.0))
        phi_err += w * ((r - PHI) / PHI) ** 2

    res_err = 0.0
    if cfg.get('resonance', {}).get('enabled', False) and resonance_score is not None:
        res_err = max(0.0, float(resonance_score) - 1.0) ** 2

    penalty = 0.0
    for c in cfg.get('constraints', []):
        v = compute_expr(params, c['expr'])
        op = c.get('op', '<=')
        bound = float(c.get('bound', 0.0))
        w = float(c.get('weight', 10.0))
        if op == '<=' and v > bound:
            penalty += w * (v - bound) ** 2
        elif op == '>=' and v < bound:
            penalty += w * (bound - v) ** 2

    w_phi = float(cfg.get('weights', {}).get('phi', 1.0))
    w_res = float(cfg.get('weights', {}).get('resonance', 2.0))
    w_pen = float(cfg.get('weights', {}).get('penalty', 5.0))

    total = w_phi * phi_err + w_res * res_err + w_pen * penalty
    return total, {'phi_err': phi_err, 'res_err': res_err, 'penalty': penalty}


def propose(base: Dict[str, Any], bounds: Dict[str, List[float]], step_scale: float):
    cand = json.loads(json.dumps(base))
    for path, (lo, hi) in bounds.items():
        cur = float(get_path(cand, path))
        span = hi - lo
        new = cur + random.gauss(0, step_scale * span)
        new = max(lo, min(hi, new))
        set_path(cand, path, new)
    return cand


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--params', required=True)
    ap.add_argument('--config', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--iters', type=int, default=2000)
    ap.add_argument('--seed', type=int, default=42)

    ap.add_argument('--resonance-csv', default=None)
    ap.add_argument('--signal-col', default='Pressure_Pa')
    ap.add_argument('--time-col', default='Time_s')
    ap.add_argument('--fs', type=float, default=None)

    args = ap.parse_args(argv)

    random.seed(args.seed)
    params = json.loads(Path(args.params).read_text(encoding='utf-8'))
    cfg = json.loads(Path(args.config).read_text(encoding='utf-8'))

    resonance_score = None
    if args.resonance_csv:
        resonance_score = resonance_from_data(Path(args.resonance_csv), cfg.get('resonance', {}), args.fs, args.signal_col, args.time_col)
        print('[RES] peakiness score:', resonance_score)

    bounds = cfg.get('bounds', {})
    best = params
    best_score, best_det = score(best, cfg, resonance_score)

    step = 0.20
    for i in range(args.iters):
        cand = propose(best, bounds, step)
        sc, det = score(cand, cfg, resonance_score)
        if sc < best_score:
            best, best_score, best_det = cand, sc, det
        if (i + 1) % 200 == 0:
            step = max(0.02, step * 0.85)
            print(f'iter={i+1} best={best_score:.6g} {best_det}')

    best.setdefault('Meta', {})
    best['Meta']['Optimized'] = True
    best['Meta']['Optimization'] = {
        'phi': PHI,
        'metric': 'T-002 PSD peakiness',
        'signal_col': args.signal_col,
        'time_col': args.time_col,
        'best_score': best_score,
        'details': best_det,
    }

    Path(args.out).write_text(json.dumps(best, indent=2) + '
', encoding='utf-8')
    print('Wrote:', args.out)


if __name__ == '__main__':
    main()
