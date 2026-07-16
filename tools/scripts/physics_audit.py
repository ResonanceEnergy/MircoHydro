#!/usr/bin/env python3
"""Independent physics audit of the MicroHydro v2.0 design. Every number recomputed from first principles."""
import math

rho, g = 1000.0, 9.81

print("=" * 70)
print("A. DESIGN POINT vs TARGET OUTPUT")
Q, H = 0.150, 5.0
Pgross = rho * g * Q * H
print(f"Gross hydraulic power @ 150 L/s, 5 m: {Pgross/1000:.2f} kW")
for eta, label in [(0.326, "spec's honest cascade 33%"), (0.485, "claimed quick-win 48.5%"), (0.53, "best realistic 53%")]:
    print(f"  net @ {label}: {Pgross*eta/1000:.2f} kW")
print(f"  Target claimed: 10-15 kW peak / 7-10 kW avg")
need = 12000 / 0.45
print(f"  Q*H needed for 12 kW net @ 45%: {need/(rho*g):.1f} m4/s  (e.g. {need/(rho*g)/10*1000:.0f} L/s @ 10 m)")

print("=" * 70)
print("B. PENSTOCK FRICTION (check spec arithmetic)")
L, f = 50.0, 0.018
for D, label in [(0.273, "ID used in spec friction calc"), (0.300, "ID implied by spec velocity 2.11")]:
    A = math.pi * (D/2)**2
    v = Q / A
    hf = f * (L/D) * v**2 / (2*g)
    print(f"  D={D} m ({label}): v={v:.2f} m/s, hf={hf:.2f} m = {hf/H*100:.0f}% of head")
# DN350
D = 0.350 * 0.91  # approx ID
A = math.pi * (D/2)**2
v = Q / A
hf = f * (L/D) * v**2 / (2*g)
print(f"  DN350 upsize: v={v:.2f} m/s, hf={hf:.2f} m = {hf/H*100:.1f}%")

print("=" * 70)
print("C. CASCADE RECONCILIATION (the five answers in one doc)")
casc = 0.82 * 0.79 * 0.65 * 0.88 * 0.88
print(f"  Honest cascade product: {casc*100:.1f}%  (matches the 33% claim)")
print(f"  Front-matter '81%' = 0.90*0.95*0.95 additive-loss error AND omits turbine+intake+penstock stages")
quick = 0.88 * 0.90 * 0.68 * 0.895 * 0.89   # post quick-win stage estimates
print(f"  Realistic post-quick-win cascade: {quick*100:.1f}% (not 48.5; their point-adding double counts)")

print("=" * 70)
print("D. QUICK-WIN #2 CHECK: DN300->DN350 claimed +7 system points")
base = 0.82 * 0.79 * 0.65 * 0.88 * 0.88
pen350 = 1 - (0.35/5 + 0.06 + 0.01)   # their own hf 0.35m + same fittings
new = 0.82 * pen350 * 0.65 * 0.88 * 0.88
print(f"  penstock stage: 0.79 -> {pen350:.2f}; system {base*100:.1f}% -> {new*100:.1f}%  (+{(new-base)*100:.1f} pts, not +7)")

print("=" * 70)
print("E. RAM PUMP BRANCH ENERGY BALANCE (4 L/s to 55 m head tank)")
q, Hlift, eta_ram, hdrive = 0.004, 55.0, 0.66, 5.0
Qdrive = q * Hlift / (eta_ram * hdrive)
print(f"  Drive flow needed: {Qdrive*1000:.0f} L/s  (architecture diagram says '20%' of ~150 = 30 L/s -- off by 2.2x)")
P_in = rho * g * Qdrive * hdrive
P_tank = rho * g * q * Hlift
P_elec_ram_path = P_tank * 0.80 * 0.88 * 0.88   # Pelton@55m ~80%, gen, PE (no intake/penstock loss; tank feeds directly)
P_elec_direct = P_in * 0.326
print(f"  Stream power consumed: {P_in/1000:.2f} kW -> tank hydraulic {P_tank/1000:.2f} kW")
print(f"  Electricity via ram->tank->Pelton: {P_elec_ram_path/1000:.2f} kW")
print(f"  Electricity if same water ran main turbine: {P_elec_direct/1000:.2f} kW")
print(f"  Net gain: {(P_elec_ram_path-P_elec_direct)/1000:+.2f} kW for ~$8-15k extra capital (ram, 55m pipe, tank, 2nd turbine)")

print("=" * 70)
print("F. HYBRID AVERAGE-POWER BUDGET (Alberta)")
pv = 5.0 * 0.16      # Alberta annual CF for fixed PV ~15-17%
wind = 2.0 * 0.15    # small wind at low hub height, generous
hydro_yr_round = 2.4
hydro_canal = 2.4 * (5.5/12)  # irrigation canal: water May-Oct only
print(f"  PV 5 kW -> avg {pv:.2f} kW;  Wind 2 kW -> avg {wind:.2f} kW")
print(f"  Hydro (year-round stream): avg {hydro_yr_round:.1f} kW;  (irrigation canal, 5.5 mo): {hydro_canal:.2f} kW")
print(f"  System average: {pv+wind+hydro_yr_round:.1f} kW (stream) / {pv+wind+hydro_canal:.1f} kW (canal)")
print(f"  vs claimed 7-10 kW average -- shortfall 2-4x")
print(f"  Peak: hydro 2.4-3.9 + PV 5 + wind 2 = 9.4-10.9 kW, capped by 10 kW inverter (claim: 15 kW)")

print("=" * 70)
print("G. ANNUAL ENERGY & LCOE")
for label, kw, months in [("stream year-round", 3.15, 12), ("irrigation canal", 3.15, 5.5)]:
    E = kw * 8760 * months/12
    capex, om, r, n = 120_000, 2000, 0.05, 25
    crf = r * (1+r)**n / ((1+r)**n - 1)
    lcoe = (capex * crf + om) / E
    print(f"  {label}: {E/1000:.1f} MWh/yr -> LCOE ${lcoe:.2f}/kWh  (claims: $0.05-0.12)")
print(f"  Note: spec annual figures assume 100% capacity factor (no hydrology/seasonality)")

print("=" * 70)
print("H. COST PER KW")
for net, label in [(2.4, "honest net now"), (3.9, "best-case optimized")]:
    print(f"  $110-135k / {net} kW net = ${110000/net/1000:.0f}k-{135000/net/1000:.0f}k per kW  (target claim: $1.5-2.5k/kW)")

print("=" * 70)
print("I. FISH SCREEN AREA")
A_screen = Q / 0.3
print(f"  min net open area @ 0.3 m/s: {A_screen:.2f} m2; with 50% winter blockage: {A_screen*2:.1f} m2")

print("=" * 70)
print("J. BATTERY WINTER CHECK")
print(f"  15 kWh LiFePO4 (front matter) vs 23 kWh (winter section) -- size inconsistency")
print(f"  LiFePO4 charge cutoff 0C: Alberta Nov-Mar REQUIRES heated enclosure (flagged in spec, absent from BOM)")
print(f"  Overnight load 1 kW x 14 h winter night = 14 kWh -> 15 kWh usable ~13.5 kWh: no autonomy margin")
