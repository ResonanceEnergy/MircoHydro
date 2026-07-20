#!/usr/bin/env python3
"""Flow-duration tool (GAP-6): honest per-site annual energy from an FDC.

Input: a flow-duration curve as (exceedance %, flow L/s) pairs — from WSC
gauge data, a regional regression, or field measurement. Output: how many
rams the site supports through the year, the seasonal output envelope, and
honest annual kWh (with the P75 'marketing floor' the SKU doc mandates).

Model: each tuned 300 mm ram drinks ~15 L/s (knee) and yields P_RAM watts
(SKU_RESTATEMENT). Site environmental flow reserve is subtracted FIRST
(default 30% of instantaneous flow — DFO-conservative placeholder until a
site-specific instream-flow-need is set). Rams come online in integer steps.

Usage:
  python3 flow_duration.py                      # built-in demo (foothills-type FDC)
  python3 flow_duration.py mysite_fdc.csv       # CSV: exceed_pct,flow_Ls
"""
import csv, sys

RAM_APPETITE_LS = 15.0     # tuned knee, Finding 5/6
P_RAM_W = 82.0             # v2 baseline (SKU_RESTATEMENT); use 105 for buildable chain
ENV_RESERVE = 0.30         # fraction of flow left in-stream (placeholder — site IFN overrides)
MAX_RAMS = 6               # B-Standard

# demo FDC: Alberta-foothills-flavoured small stream (synthetic, labeled as such)
DEMO_FDC = [(5, 400), (10, 260), (20, 150), (30, 105), (40, 80), (50, 62),
            (60, 48), (70, 36), (80, 26), (90, 16), (95, 10), (100, 6)]


def site_energy(fdc, max_rams=MAX_RAMS, appetite=RAM_APPETITE_LS,
                p_ram=P_RAM_W, reserve=ENV_RESERVE):
    rows = []
    prev_pct = 0
    annual_wh = 0.0
    for pct, q in fdc:
        usable = q * (1.0 - reserve)
        n = min(max_rams, int(usable // appetite))
        p = n * p_ram
        frac = (pct - prev_pct) / 100.0
        annual_wh += p * frac * 8760.0
        rows.append(dict(exceed_pct=pct, flow_Ls=q, usable_Ls=round(usable, 1),
                         rams_online=n, power_W=p))
        prev_pct = pct
    # P75 floor: power available 75% of the time
    p75 = next((r["power_W"] for r in rows if r["exceed_pct"] >= 75), rows[-1]["power_W"])
    return rows, annual_wh / 1000.0, p75


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fh:
            fdc = [(float(a), float(b)) for a, b in csv.reader(fh)]
        label = sys.argv[1]
    else:
        fdc, label = DEMO_FDC, "DEMO (synthetic foothills-type stream — not a real site)"
    rows, kwh, p75 = site_energy(fdc)
    print(f"# Flow-duration energy audit: {label}")
    print(f"{'exceed%':>8} {'flow L/s':>9} {'usable':>7} {'rams':>5} {'W':>6}")
    for r in rows:
        print(f"{r['exceed_pct']:>8} {r['flow_Ls']:>9.0f} {r['usable_Ls']:>7.1f} "
              f"{r['rams_online']:>5} {r['power_W']:>6.0f}")
    flat = MAX_RAMS * P_RAM_W * 8.76
    print(f"\nHONEST annual energy: {kwh:,.0f} kWh  (naive flat x8760 would claim {flat:,.0f} kWh"
          f" -> overstatement {100*(flat-kwh)/max(kwh,1):.0f}%)")
    print(f"P75 marketing floor: {p75:.0f} W  |  env reserve modeled: {ENV_RESERVE*100:.0f}% instream")


if __name__ == "__main__":
    main()
