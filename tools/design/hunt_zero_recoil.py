#!/usr/bin/env python3
"""Sim queue #2+#3 combined — valve tuning map + zero-recoil resonance hunt.

Grid: weight x stroke at the new optimum pipe (L/D=100, Finding 4), B300 scale.
Each point reports eta, Q (water appetite), q (delivery), freq, T-002 coherence,
T-001 jet CoV, and the new recoil_mismatch (|column flow| at valve reopen /
mean drive flow — 0 = Young's zero-recoil condition).

Tests two predictions on the same data:
  P1 (Young 1995/96): the efficiency peak coincides with minimum recoil.
  P2 (founder/coherence): the T-002 coherence peak coincides with the eta peak.
Output: engineering/data/tuning_map_zero_recoil.csv + rank correlations.
"""
import csv, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ram_moc_sim import RamSim

WEIGHTS = (0.35, 0.5, 0.65, 0.8, 1.0, 1.25, 1.5)
STROKES = (0.008, 0.015, 0.025)


def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0.0]*len(v)
        for pos, i in enumerate(order):
            rk[i] = pos
        return rk
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    mx, my = sum(rx)/n, sum(ry)/n
    num = sum((rx[i]-mx)*(ry[i]-my) for i in range(n))
    den = math.sqrt(sum((r-mx)**2 for r in rx)*sum((r-my)**2 for r in ry))
    return num/den if den else 0.0


def main():
    F, D, Hd, LD = 1.5, 0.30, 9.0, 100
    L = LD*D
    n = max(16, int(L/3))
    base = RamSim(F=F, D=D, Hd_target=Hd)
    W0 = base.W
    rows = []
    print(f"# B300 L/D={LD} (L={L:.0f} m), weight x stroke grid")
    print(f"{'Wf':>5} {'stroke':>7} {'eta':>7} {'Q':>7} {'q':>7} {'f_Hz':>6} {'recoil':>7} {'T002':>10} {'T001':>7}")
    for st in STROKES:
        for wf in WEIGHTS:
            s = RamSim(F=F, D=D, L=L, Hd_target=Hd, stroke=st, wv_weight=W0*wf, n_nodes=n)
            r = s.run(t_end=60.0, record_from=30.0)
            r.update(weight_factor=wf, stroke_mm=st*1000, LD=LD)
            rows.append(r)
            print(f"{wf:>5.2f} {st*1000:>6.0f}mm {r['eta']:>7.3f} {r['Q_drive_Ls']:>7.1f} "
                  f"{r['q_deliv_Ls']:>7.2f} {r['freq_hz']:>6.2f} {r['recoil_mismatch']:>7.3f} "
                  f"{r['T002_psd_peakiness']:>10.0f} {r['T001_jet_cov']:>7.3f}")

    live = [r for r in rows if r['freq_hz'] > 0.05 and r['n_reopens'] >= 4]
    print(f"\n{len(live)}/{len(rows)} grid points sustain cycling")
    if len(live) >= 6:
        etas = [r['eta'] for r in live]
        rec = [r['recoil_mismatch'] for r in live]
        coh = [r['T002_psd_peakiness'] for r in live]
        print(f"P1 Spearman(eta, recoil_mismatch) = {spearman(etas, rec):+.3f}  (prediction: strongly negative)")
        print(f"P2 Spearman(eta, T002_coherence)  = {spearman(etas, coh):+.3f}  (prediction: strongly positive)")
        best = max(live, key=lambda r: r['eta'])
        minrec = min(live, key=lambda r: r['recoil_mismatch'])
        maxcoh = max(live, key=lambda r: r['T002_psd_peakiness'])
        for tag, r in (("eta peak", best), ("min recoil", minrec), ("max coherence", maxcoh)):
            print(f"{tag:>14}: Wf={r['weight_factor']:.2f} stroke={r['stroke_mm']:.0f}mm "
                  f"eta={r['eta']:.3f} recoil={r['recoil_mismatch']:.3f}")

    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "..", "engineering", "data", "tuning_map_zero_recoil.csv"))
    keys = ["LD", "weight_factor", "stroke_mm", "eta", "Q_drive_Ls", "q_deliv_Ls",
            "freq_hz", "recoil_mismatch", "n_reopens", "T002_psd_peakiness",
            "T001_jet_cov", "ripple_pct"]
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items() if k in keys})
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
