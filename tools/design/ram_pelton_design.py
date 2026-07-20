#!/usr/bin/env python3
"""
Machine B — coupled ram-pump -> impulse-turbine design solver.

RATIFIED architecture (canon; no-silent-substitution rule): stream -> drive pipe
-> hydram -> air chamber -> rise pipe -> ELEVATED HEADSTOCK -> penstock -> twin
nozzles -> Pelton/Turgo wheel -> PMA -> MPPT -> battery/loads. The headstock is
a founder design element and doubles as the open surge tank (COMPONENT_TECH_SCAN
section 3). An earlier draft of this docstring described a headstock-less
direct-coupled variant; that text was doc drift, corrected 2026-07-18. The
operating-point math (nozzle back-pressure = delivery head) applies unchanged
with the headstock providing that head.

SUPERSESSION NOTE (D-5): the eta_ram(r) fit below is retired as a source of
truth — the MOC transient simulator (ram_moc_sim.py) supersedes it, including
the per-ram appetite cap (SIM_RESULTS Findings 1, 4-6). The fit remains only
until queue #4 (solver ingestion of sim-derived curves) lands.

Grounding in repo docs:
  - engineering/specs/technology/02_Hydram/HYDRAM_GUIDE.md — USAID relation:
    delivered volume q = E * Q * F / L, E ~ 0.66 commercial, 0.33 home-built.
  - research/reference-library/.../Volume_G — energy bounded by rho*g*Q*F; bench-first ladder.
  - engineering/GAP_ANALYSIS.md section 3 — ram is redundant above ~3 m natural head.

Beyond the constant-E USAID relation, published hydram test data (Watt 1975;
manufacturer tables) show efficiency FALLING with lift ratio r = H_d/F.
We fit: eta_ram(r) = clamp(0.85 - 0.03*r, 0.20, 0.72), valid 3 <= r <= 24.
(Check vs USAID: r=6 -> 0.67 ~ 0.66 commercial figure. Conservative beyond r=12.)

The design question this file answers: for a site (F, Q), what lift ratio r,
nozzle bore, wheel size, and speed maximize electric watts subject to the
turbine being small, fast, and clog-resistant? Electric power:
  P(r) = rho*g*Q*F * eta_ram(r) * eta_turb * eta_pma * eta_mppt
is monotone-decreasing in r, so the optimum is the LOWEST r the impulse wheel
tolerates -> constraints, not efficiency, set the operating point:
  - nozzle bore >= 6 mm   (debris/clog floor)
  - wheel PCD <= 300 mm and PCD >= 9 * nozzle bore (Pelton bucket rule)
  - shaft speed within PMA band 300-2000 rpm
  - jet head H_d >= 6 m (impulse wheel practicality floor; below -> flag Turgo)
"""
import math

RHO, G = 1000.0, 9.81
CV = 0.97                 # nozzle velocity coefficient
ETA_TURB = 0.75           # small Pelton/Turgo, matched jet
ETA_PMA = 0.85            # permanent-magnet alternator
ETA_ELEC = 0.92           # rectifier + MPPT
SPEED_RATIO = 0.46        # bucket speed / jet speed
PMA_RPM = (300.0, 2000.0)
PCD_MAX = 0.300           # m
NOZZLE_MIN = 0.006        # m
HD_MIN = 6.0              # m — practical impulse floor

# ---- SIM INGESTION (queue #4, done 2026-07-19) ----------------------------
# Per-ram performance from the calibrated MOC digital bench, model v2
# (Kj=100, leak=0.3%; SIM_RESULTS Findings 4-6, 10). Interpolate on r.
# Columns: r, eta_DAubuisson, q_deliv_Ls (per 300mm ram, tuned-knee class site)
SIM_TABLE_300 = [
    (6.0, 0.693, 1.74),    # knee config, v2
    (8.0, 0.664, 1.46),
    (12.0, 0.624, 1.01),
    (16.0, 0.622, 0.68),
    (20.0, 0.633, 0.56),   # envelope: min(sim, published decline) applies >r=9
]
PUBLISHED_DECLINE = [(6.0, 0.66), (10.0, 0.55), (14.0, 0.45), (20.0, 0.32)]

def _interp(table, r):
    if r <= table[0][0]: return table[0][1:]
    if r >= table[-1][0]: return table[-1][1:]
    for (r1, *v1), (r2, *v2) in zip(table, table[1:]):
        if r1 <= r <= r2:
            f = (r - r1)/(r2 - r1)
            return tuple(a + f*(b - a) for a, b in zip(v1, v2))
    return table[-1][1:]

def eta_ram_sim(r):
    """LIVE per-ram efficiency: conservative envelope min(sim v2, published)."""
    eta_s = _interp(SIM_TABLE_300, r)[0]
    eta_p = _interp(PUBLISHED_DECLINE, r)[0]
    return min(eta_s, eta_p)

def q_per_ram_300(r):
    """Delivered L/s per tuned 300 mm ram (sim v2)."""
    return _interp(SIM_TABLE_300, r)[1]

def eta_ram(r):
    """RETIRED fallback (D-5). Use eta_ram_sim() — kept only for old callers."""
    return max(0.20, min(0.72, 0.85 - 0.03 * r))

def drive_pipe(Q, F):
    """Rigid (steel) drive pipe: velocity ~1.5 m/s sizing, length 6x fall,
    checked against classic L/D 150-1000 window."""
    A = Q / 1.5
    D = math.sqrt(4 * A / math.pi)
    stds = [0.050, 0.065, 0.080, 0.100, 0.125, 0.150, 0.200, 0.250, 0.300, 0.400]
    D = next((s for s in stds if s >= D), stds[-1])
    L = max(6 * F, 150 * D)          # at least 6x fall and L/D >= 150
    L = min(L, 1000 * D)
    return D, L

def solve_site(F, Q, r_lo=3.0, r_hi=24.0):
    """Sweep lift ratio, keep feasible operating points, return the max-power one."""
    best, rows = None, []
    r = r_lo
    while r <= r_hi + 1e-9:
        Hd = r * F
        eta_r = eta_ram(r)
        q = eta_r * Q / r                          # delivered flow (USAID form: q = E*Q*F/Hd)
        Vj = CV * math.sqrt(2 * G * Hd)
        An = q / Vj
        dn = math.sqrt(4 * An / math.pi)
        PCD = max(9 * dn, 0.075)                   # bucket rule, 75 mm floor
        U = SPEED_RATIO * Vj
        rpm = 60 * U / (math.pi * PCD)
        P = RHO * G * Q * F * eta_r * ETA_TURB * ETA_PMA * ETA_ELEC
        feasible = (dn >= NOZZLE_MIN and PCD <= PCD_MAX
                    and PMA_RPM[0] <= rpm <= PMA_RPM[1] and Hd >= HD_MIN)
        row = dict(r=r, Hd=Hd, eta_ram=eta_r, q_Ls=q * 1000, Vj=Vj,
                   dn_mm=dn * 1000, PCD_mm=PCD * 1000, rpm=rpm,
                   P_W=P, feasible=feasible)
        rows.append(row)
        if feasible and (best is None or P > best["P_W"]):
            best = row
        r += 0.5
    return best, rows

def report(sites):
    Dp_note = []
    print(f"{'F(m)':>5} {'Q(L/s)':>7} | {'r*':>4} {'Hd(m)':>6} {'eta_ram':>7} "
          f"{'q(L/s)':>7} {'jet(mm)':>8} {'PCD(mm)':>8} {'rpm':>6} {'W out':>7} "
          f"{'kWh/day':>8} {'drivepipe':>12}")
    for F, Q in sites:
        best, _ = solve_site(F, Q)
        D, L = drive_pipe(Q, F)
        dp = f"{D*1000:.0f}mm x {L:.0f}m"
        if best is None:
            print(f"{F:>5} {Q*1000:>7.0f} |  -- no feasible impulse operating point "
                  f"(fall too small: Hd_min={HD_MIN} m needs r={HD_MIN/F:.0f}) {dp:>12}")
            continue
        wtw = best['P_W'] / (RHO * G * Q * F)
        print(f"{F:>5} {Q*1000:>7.0f} | {best['r']:>4.1f} {best['Hd']:>6.1f} "
              f"{best['eta_ram']:>7.2f} {best['q_Ls']:>7.2f} {best['dn_mm']:>8.1f} "
              f"{best['PCD_mm']:>8.0f} {best['rpm']:>6.0f} {best['P_W']:>7.0f} "
              f"{best['P_W']*24/1000:>8.1f} {dp:>12}   [{wtw*100:.0f}% w2w]")

if __name__ == "__main__":
    print("MACHINE B - ram->jet->impulse coupled operating points (max-W feasible)")
    print("chain: eta_ram(r) x 0.75 turb x 0.85 PMA x 0.92 elec\n")
    sites = [(0.5, 0.030), (0.5, 0.060), (0.5, 0.100),
             (0.75, 0.060), (0.75, 0.100),
             (1.0, 0.030), (1.0, 0.060), (1.0, 0.100), (1.0, 0.200),
             (1.5, 0.060), (1.5, 0.100), (1.5, 0.200),
             (2.0, 0.060), (2.0, 0.100), (2.0, 0.200)]
    report(sites)
    print("\nNotes: r* lands at the LOWEST feasible lift ratio (power falls as r rises);")
    print("what blocks lower r is the 6 mm nozzle floor / 300 mm wheel cap / Hd floor.")
    print("Below F~0.4 m no impulse point exists -> different machine or skip site.")
