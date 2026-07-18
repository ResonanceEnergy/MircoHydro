#!/usr/bin/env python3
"""Sim queue #3 — air chamber + rise-pipe sizing for delivery smoothness.

Grid: air-chamber gas volume V_air0 x rise-pipe conductance G_del at the tuned
B300 operating point (L/D=100, Wf=0.65, 8 mm stroke — Finding 6 knee).

Metrics: T-001 CoV of rise-pipe delivery flow (the chamber's smoothing job —
note the headstock adds further smoothing downstream before the jet), eta,
delivery, chamber pressure ripple.

Regulatory hook (REQ-S1): CSA B51's pressure-vessel scope has a small-vessel
exemption class around 42.5 L (1.5 ft^3) internal volume [VERIFY against
current B51/ABSA Pressure Equipment Safety Regulation before relying on it].
Design question: does a <=40 L chamber deliver acceptable smoothing, letting
the design exit vessel scope entirely? The 150 L PN10 spec'd in the legacy
HYBRID docs is in-scope and unengineered — smaller may be both legal AND
sufficient.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ram_moc_sim import RamSim

V_AIRS = (0.015, 0.030, 0.060, 0.120)      # m^3 gas volume (15-120 L)
G_DELS = (0.004, 0.008, 0.016, 0.032)      # m^3/s per m head (rise-pipe class)


def main():
    base = RamSim(F=1.5, D=0.30, Hd_target=9.0)
    W0 = base.W
    rows = []
    print(f"{'V_air(L)':>9} {'G_del':>7} {'eta':>7} {'q(L/s)':>7} {'T001cov':>8} {'ripple%':>8} {'f_Hz':>6}")
    for V in V_AIRS:
        for Gd in G_DELS:
            s = RamSim(F=1.5, D=0.30, L=30.0, Hd_target=9.0, stroke=0.008,
                       wv_weight=W0*0.65, V_air0=V, n_nodes=16)
            s.G_del = Gd
            r = s.run(t_end=60.0, record_from=30.0)
            r.update(V_air_L=V*1000, G_del=Gd)
            rows.append(r)
            print(f"{V*1000:>9.0f} {Gd:>7.3f} {r['eta']:>7.3f} {r['q_deliv_Ls']:>7.2f} "
                  f"{r['T001_jet_cov']:>8.3f} {r['ripple_pct']:>8.1f} {r['freq_hz']:>6.2f}")
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "..", "engineering", "data", "sweep_chamber_sizing.csv"))
    keys = ["V_air_L", "G_del", "eta", "Q_drive_Ls", "q_deliv_Ls", "freq_hz",
            "ripple_pct", "T001_jet_cov", "T002_psd_peakiness", "recoil_mismatch"]
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items() if k in keys})
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
