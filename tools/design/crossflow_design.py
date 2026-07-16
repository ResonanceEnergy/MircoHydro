#!/usr/bin/env python3
"""
Crossflow (Banki-Michell) turbine parametric design model — first principles.

Every number derives from (Q, H_gross) plus stated assumptions. No inherited claims.

Design method: classical Banki/Mockmore & Merryfield correlations
  - Jet velocity        V1 = Cv * sqrt(2 g Hn),           Cv = 0.98
  - Attack angle        alpha = 16 deg (classic optimum)
  - Blade inlet angle   beta1 = 30 deg  (tan(beta1) = 2 tan(alpha))
  - Speed ratio         U1/V1 = cos(alpha)/2  ≈ 0.48  (max-efficiency condition)
  - Jet thickness       s0 = 0.087 * D1
  - Inner diameter      D2 = 0.66 * D1
  - Blade radius        rb = 0.163 * D1
  - Blade count         Nb = 26 (test range 20-30; PROTOCOL_001 A/B slot)
  - Realistic peak component efficiency: 0.70 (well-built small unit;
    theoretical Banki maximum ≈ 0.878, lab bests ≈ 0.80-0.85)

Penstock: Darcy-Weisbach with Swamee-Jain friction factor, HDPE roughness.
Usage:
  python3 crossflow_design.py --Q 0.150 --H 5.0 --L 50           # field unit
  python3 crossflow_design.py --Q 0.00185 --H 1.5 --bench       # bench rig
"""
import argparse, json, math

RHO, G, NU = 1000.0, 9.81, 1.004e-6   # water @ 20 C
E_HDPE = 1.5e-6                        # pipe roughness [m]

def swamee_jain(Re, e_D):
    if Re < 2300:
        return 64.0 / max(Re, 1.0)
    return 0.25 / (math.log10(e_D / 3.7 + 5.74 / Re**0.9))**2

def penstock(Q, H_gross, L, v_target=2.0, K_minor=1.7):
    """Size penstock for ~v_target; return dict incl. net head. K_minor: entrance 0.5 + 2 LR bends 0.6 + valve 0.6."""
    D = math.sqrt(4*Q/(math.pi*v_target))
    # round UP to a standard HDPE ID (m)
    stds = [0.055,0.070,0.090,0.110,0.136,0.163,0.204,0.257,0.290,0.327,0.368,0.409,0.460]
    D = next((s for s in stds if s >= D), stds[-1])
    A = math.pi*D*D/4; v = Q/A
    Re = v*D/NU
    f = swamee_jain(Re, E_HDPE/D)
    hf = f*(L/D)*v*v/(2*G) + K_minor*v*v/(2*G)
    return dict(D_id=D, v=v, Re=Re, f=f, h_loss=hf, h_net=H_gross-hf, loss_frac=hf/H_gross)

def runner(Q, Hn, D1=None, Cv=0.98, alpha_deg=16.0, Nb=26):
    V1 = Cv*math.sqrt(2*G*Hn)
    alpha = math.radians(alpha_deg)
    U1 = 0.5*V1*math.cos(alpha)
    if D1 is None:
        # choose D1 for a direct-drive-friendly speed (target 200-450 rpm field scale)
        # N = 60 U1/(pi D1)  ->  D1 = 60 U1/(pi N_target)
        N_target = 300.0
        D1 = 60*U1/(math.pi*N_target)
        D1 = max(0.06, round(D1/0.02)*0.02)     # snap to 20 mm steps, min 60 mm
    N = 60*U1/(math.pi*D1)
    s0 = 0.087*D1                                # jet (nozzle throat) thickness
    b  = Q/(V1*s0)                               # runner/jet width from continuity
    return dict(V1=V1, U1=U1, D1=D1, D2=0.66*D1, r_blade=0.163*D1, N_rpm=N,
                N_runaway=1.8*N, s0=s0, b=b, Nb=Nb,
                beta1_deg=math.degrees(math.atan(2*math.tan(alpha))), alpha_deg=alpha_deg)

def power_chain(Q, Hn, eta_turb=0.70, eta_gen=0.90, eta_pe=0.90, eta_intake=0.95):
    P_gross_gross = RHO*G*Q*Hn
    P_shaft = P_gross_gross*eta_intake*eta_turb
    P_elec  = P_shaft*eta_gen*eta_pe
    return dict(P_hydraulic_net_head=P_gross_gross, P_shaft=P_shaft, P_electric=P_elec,
                eta_water_to_wire_at_net_head=P_elec/P_gross_gross)

def annual(P_elec_W, capacity_factor):
    return P_elec_W*8760*capacity_factor/1000.0   # kWh/yr

def lcoe(capex, om_yr, E_kwh_yr, r=0.05, n=25):
    crf = r*(1+r)**n/((1+r)**n-1)
    return (capex*crf+om_yr)/max(E_kwh_yr,1e-9)

def design(Q, H, L, capex=None, om=2000.0, cf=0.55, D1=None, bench=False):
    pen = penstock(Q, H, L, v_target=(1.2 if bench else 2.0), K_minor=(2.5 if bench else 1.7))
    run = runner(Q, pen["h_net"], D1=D1)
    eta_t = 0.60 if bench else 0.70              # 3D-printed bench runner is rougher
    eta_g = 0.75 if bench else 0.90              # small DC machine vs field PMSG
    pwr = power_chain(Q, pen["h_net"], eta_turb=eta_t, eta_gen=eta_g)
    out = dict(inputs=dict(Q_m3s=Q, H_gross_m=H, penstock_L_m=L),
               penstock=pen, runner=run, power=pwr)
    # overall from GROSS head (the honest headline number)
    out["eta_gross_water_to_wire"] = pwr["P_electric"]/(RHO*G*Q*H)
    out["screen_area_m2_at_0p3ms"] = Q/0.3
    if not bench:
        E = annual(pwr["P_electric"], cf)
        out["energy"] = dict(capacity_factor=cf, E_kWh_yr=E)
        if capex:
            out["economics"] = dict(capex=capex, om_yr=om,
                                    LCOE_per_kWh=lcoe(capex, om, E))
    return out

def show(d, label):
    p, r, w = d["penstock"], d["runner"], d["power"]
    print(f"\n===== {label} =====")
    i = d["inputs"]
    print(f"Site: Q={i['Q_m3s']*1000:.2f} L/s  H_gross={i['H_gross_m']} m  penstock L={i['penstock_L_m']} m")
    print(f"Penstock: ID {p['D_id']*1000:.0f} mm, v={p['v']:.2f} m/s, loss {p['h_loss']:.2f} m ({p['loss_frac']*100:.1f}%), H_net={p['h_net']:.2f} m")
    print(f"Jet: V1={r['V1']:.2f} m/s  alpha={r['alpha_deg']}°  s0={r['s0']*1000:.1f} mm  width b={r['b']*1000:.0f} mm")
    print(f"Runner: D1={r['D1']*1000:.0f} mm  D2={r['D2']*1000:.0f} mm  blade r={r['r_blade']*1000:.1f} mm  Nb={r['Nb']}  beta1={r['beta1_deg']:.1f}°")
    print(f"Speed: {r['N_rpm']:.0f} rpm (runaway {r['N_runaway']:.0f} rpm)")
    print(f"Power: hydraulic@Hnet {w['P_hydraulic_net_head']:.0f} W -> shaft {w['P_shaft']:.0f} W -> electric {w['P_electric']:.0f} W")
    print(f"Water-to-wire (gross head): {d['eta_gross_water_to_wire']*100:.1f}%")
    print(f"Fish screen min open area: {d['screen_area_m2_at_0p3ms']:.2f} m²")
    if "energy" in d:
        print(f"Annual @ CF {d['energy']['capacity_factor']}: {d['energy']['E_kWh_yr']/1000:.1f} MWh/yr")
    if "economics" in d:
        print(f"LCOE @ ${d['economics']['capex']:,} capex: ${d['economics']['LCOE_per_kWh']:.3f}/kWh")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--Q", type=float, help="flow m3/s")
    ap.add_argument("--H", type=float, help="gross head m")
    ap.add_argument("--L", type=float, default=50.0, help="penstock length m")
    ap.add_argument("--D1", type=float, default=None, help="force runner diameter m")
    ap.add_argument("--capex", type=float, default=None)
    ap.add_argument("--cf", type=float, default=0.55, help="capacity factor")
    ap.add_argument("--bench", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.Q and a.H:
        d = design(a.Q, a.H, a.L, capex=a.capex, cf=a.cf, D1=a.D1, bench=a.bench)
        if a.json: print(json.dumps(d, indent=2))
        else: show(d, "CUSTOM DESIGN")
    else:
        # Reference designs
        show(design(0.150, 5.0, 50.0, capex=75000, cf=0.55), "FIELD REFERENCE — 150 L/s @ 5 m (year-round stream)")
        show(design(0.150, 5.0, 50.0, capex=75000, cf=0.25), "FIELD REFERENCE — irrigation canal duty (CF 0.25)")
        show(design(0.280, 10.0, 80.0, capex=95000, cf=0.55), "UPRATED SITE — 280 L/s @ 10 m (the honest 10 kW-class)")
        show(design(0.00185, 1.5, 3.0, D1=0.100, bench=True), "BENCH RIG — 1.85 L/s @ 1.5 m, 100 mm runner")
