#!/usr/bin/env python3
"""
Machine B — coupled ram-pump -> impulse-turbine design solver.

Architecture (per project design): stream -> drive pipe -> hydram -> air chamber
-> pressure line -> fixed nozzle (jet) -> Pelton/Turgo wheel -> PMA -> MPPT -> battery/loads.
No elevated headstock required: the air chamber smooths delivery so the nozzle's
back-pressure IS the delivery head. (Optional tank where terrain provides one.)

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

def eta_ram(r):
    """Hydram D'Aubuisson-style efficiency vs lift ratio r = H_d / F.
    Fit to published hydram data; repo HYDRAM_GUIDE constant E=0.66 sits at r~6."""
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
