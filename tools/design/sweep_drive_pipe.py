#!/usr/bin/env python3
"""Sim queue #1 — drive-pipe length sweep (L/D 50..1000).

Question: does a longer drive pipe recover per-ram appetite (Q_drive) and/or
efficiency at the reference site? Literature window L/D 150-1000, target ~500
(Watt; Fatahi-Alkouhi dimensional analysis). Our default L put us at the
window's BOTTOM edge (L/D=150).

Grid discipline: n_nodes scales with L to hold dx ~= 2 m so valve-dynamics
time resolution stays comparable across the sweep.

Caveat (stated per canon): Kj=125 was calibrated at L=45 m, r=6. Trends across
L are the deliverable; absolutes away from the calibration point carry extra
uncertainty until re-anchored.
"""
import csv, json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ram_moc_sim import RamSim

LD_TARGETS = (50, 100, 150, 250, 350, 500, 750, 1000)


def sweep(F, D, Hd, label):
    rows = []
    for ld in LD_TARGETS:
        L = ld * D
        n = max(16, int(round(L / 2.0)))
        sim = RamSim(F=F, D=D, L=L, Hd_target=Hd, n_nodes=n)
        # keep sampling window proportional to slower cycles on long pipes
        res = sim.run(t_end=60.0, record_from=30.0)
        res.update(LD=ld, label=label, n_nodes=n, dt_ms=sim.dt * 1000)
        rows.append(res)
        print(f"{label} L/D={ld:>4} L={L:>6.1f}m  Q={res['Q_drive_Ls']:>7.2f} L/s  "
              f"q={res['q_deliv_Ls']:>6.3f} L/s  eta={res['eta']:>6.3f}  "
              f"f={res['freq_hz']:>5.2f} Hz  T002={res['T002_psd_peakiness']:>6.1f}  "
              f"T001cov={res['T001_jet_cov']:>6.3f}")
    return rows


def main():
    out = []
    print("# B-Standard scale: D=300 mm, F=1.5 m, Hd=9 m (r=6, calibration site)")
    out += sweep(F=1.5, D=0.30, Hd=9.0, label="B300")
    print("\n# Pico scale (TWO_MODEL site): D=100 mm, F=1.5 m, Hd=9 m (r=6)")
    out += sweep(F=1.5, D=0.10, Hd=9.0, label="B100")

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "..", "engineering", "data", "sweep_drive_pipe_LD.csv")
    path = os.path.normpath(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    keys = ["label", "LD", "L", "D", "F", "a", "n_nodes", "dt_ms",
            "Q_drive_Ls", "q_deliv_Ls", "h_delivery", "r", "eta",
            "freq_hz", "ripple_pct", "T002_psd_peakiness", "T001_jet_cov"]
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        for r in out:
            w.writerow({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items() if k in keys})
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
