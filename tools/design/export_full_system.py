#!/usr/bin/env python3
"""Full-system run at the ratified operating point -> physics proof data +
animation time-series for the Blender visualization.

Operating point (Findings 4-6, 9): B300 knee — F=1.5 m, D=300 mm steel,
L=30 m (L/D=100), waste valve 8 mm stroke @ Wf=0.65, chamber 40 L
(exemption-class), headstock +9.0 m (r=6). Downstream chain per canon:
headstock -> penstock (HDPE, 12 m run assumed) -> twin nozzles -> Turgo
(D-1: 4-8 m band) -> PMA -> MPPT. Chain efficiencies per DESIGN_BASIS canon
(0.75 turgo / 0.85 PMA / 0.92 electronics) until bench data supersedes.

Outputs:
  engineering/data/full_system_timeseries.json   (50 Hz, last 20 s: t, x_v,
     Hj, P_ch, Q0, Qd + derived jet/wheel channels; summary block)
  engineering/data/full_system_operating_point.json
Also prints the per-window energy balance and the Joukowsky check used by
PHYSICS_PROOF_FULL_SYSTEM.md.
"""
import json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ram_moc_sim import RamSim, RHO, G

# ---- downstream chain constants (canon; bench supersedes) ----
CV_NOZZLE = 0.97
ETA_TURGO = 0.75
ETA_PMA = 0.85
ETA_ELEC = 0.92
SPEED_RATIO = 0.46
PCD = 0.150            # m, Turgo pitch circle (B-Standard compact wheel)
PENSTOCK_L = 12.0      # m, headstock->turbine run (site assumption, stated)
PENSTOCK_D = 0.090     # m HDPE ID
F_DARCY = 0.019


def main():
    base = RamSim(F=1.5, D=0.30, Hd_target=9.0)
    s = RamSim(F=1.5, D=0.30, L=30.0, Hd_target=9.0, stroke=0.008,
               wv_weight=base.W*0.65, V_air0=0.040, n_nodes=16)
    N, dt, dx, a, A = s.N, s.dt, s.dx, s.a, s.A
    B = a/(G*A); R = s.f*dx/(2*G*s.D*A*A)
    H = [s.F*(1 - i/N) for i in range(N+1)]
    Q = [0.0]*(N+1)
    x_v, u_v = s.stroke, 0.0
    P_ch = RHO*G*s.Hd; V_air = s.V_air0
    C_gas = (P_ch + 101325.0)*V_air**s.n_poly
    t, t_end, rec_from = 0.0, 60.0, 40.0
    fs = 50.0; next_s = rec_from
    series = dict(t=[], x_v=[], Hj=[], P_ch_kPa=[], Q0_Ls=[], Qd_Ls=[], V_air_L=[])
    drive_vol = deliv_vol = 0.0
    Hj_max = -1e9; v_pre_slam = 0.0; v_run_max = 0.0
    cycles = 0; was_pos = True
    closed_t = 0.0
    while t < t_end:
        Hn, Qn = H[:], Q[:]
        for i in range(1, N):
            Cp = H[i-1] + B*Q[i-1] - R*Q[i-1]*abs(Q[i-1])
            Cm = H[i+1] - B*Q[i+1] + R*Q[i+1]*abs(Q[i+1])
            Hn[i] = 0.5*(Cp + Cm); Qn[i] = (Cp - Cm)/(2*B)
        Cm = H[1] - B*Q[1] + R*Q[1]*abs(Q[1])
        ke = (1 + s.Ke)/(2*G*A*A); Q0 = Q[0]
        for _ in range(4):
            Q0 = (s.F - ke*Q0*abs(Q0) - Cm)/B
        Qn[0] = Q0; Hn[0] = s.F - ke*Q0*abs(Q0)
        Cp = H[N-1] + B*Q[N-1] - R*Q[N-1]*abs(Q[N-1])
        KjR = s.Kj/(2*G*A*A)
        Aw = s.Aw_max*max(0.0, min(1.0, x_v/s.stroke))
        h_ch = P_ch/(RHO*G)
        lo, hi = -20.0, max(Cp, h_ch) + 80.0
        for _ in range(48):
            Hj = 0.5*(lo + hi); dH = Cp - Hj
            if dH >= 0:
                Qp = (-B + math.sqrt(B*B + 4*KjR*dH))/(2*KjR)
            else:
                Qp = (B - math.sqrt(B*B - 4*KjR*dH))/(2*KjR)
            Qw = s.Cd_w*Aw*math.sqrt(2*G*max(Hj, 0.0)) if Aw > 0 else 0.0
            Qc = s.Cd_c*s.Ac*math.sqrt(2*G*max(Hj - h_ch, 0.0)) if Hj > h_ch else 0.0
            (lo, hi) = (Hj, hi) if (Qp - Qw - Qc) > 0 else (lo, Hj)
        Hn[N], Qn[N] = Hj, Qp
        if t >= rec_from:
            Hj_max = max(Hj_max, Hj)
        # track column velocity just before slam (valve moving toward closed)
        v_col = Qn[N//2]/A
        if x_v > 0 and u_v < 0:
            v_pre_slam = v_col
        v_run_max = max(v_run_max, abs(v_col))
        v_port = (Qw/max(Aw, 1e-6)) if Aw > 0 else 0.0
        F_close = 0.5*RHO*1.15*s.Cd_w*s.Aw_max*v_port*v_port \
                  + max(Hj - s.F, 0.0)*RHO*G*s.Aw_max*0.15
        u_v += (s.W - F_close)/s.m_v*dt
        x_v += u_v*dt
        if x_v <= 0.0:
            x_v, u_v = 0.0, 0.0
            if was_pos and t >= rec_from:
                cycles += 1
            was_pos = False
        else:
            was_pos = True
            if x_v >= s.stroke:
                x_v, u_v = s.stroke, min(u_v, 0.0)
        Qd = s.G_del*max(h_ch - s.Hd, 0.0)
        V_air += (Qd - Qc)*dt
        V_air = max(s.V_air0*0.3, min(s.V_air0*1.7, V_air))
        P_ch = C_gas/V_air**s.n_poly - 101325.0
        if t >= rec_from:
            drive_vol += max(Qn[0], 0.0)*dt
            deliv_vol += Qd*dt
            if t >= next_s:
                series['t'].append(round(t - rec_from, 3))
                series['x_v'].append(round(x_v*1000, 3))          # mm
                series['Hj'].append(round(Hj, 3))                 # m head
                series['P_ch_kPa'].append(round(P_ch/1000, 2))
                series['Q0_Ls'].append(round(Qn[0]*1000, 3))
                series['Qd_Ls'].append(round(Qd*1000, 4))
                series['V_air_L'].append(round(V_air*1000, 2))
                next_s += 1.0/fs
        H, Q = Hn, Qn
        t += dt

    T = t_end - rec_from
    Q_mean = drive_vol/T
    q_mean = deliv_vol/T
    eta = q_mean*s.Hd/(Q_mean*s.F)
    freq = cycles/T
    # ---- downstream chain, derived from the sim's delivered flow ----
    v_pen = q_mean/(math.pi*PENSTOCK_D**2/4)
    h_pen_loss = F_DARCY*(PENSTOCK_L/PENSTOCK_D)*v_pen**2/(2*G) + 1.7*v_pen**2/(2*G)
    H_net = s.Hd - h_pen_loss
    Vj = CV_NOZZLE*math.sqrt(2*G*H_net)
    A_jets = q_mean/Vj
    d_single = math.sqrt(4*A_jets/math.pi)
    d_twin = math.sqrt(4*(A_jets/2)/math.pi)
    P_jet = 0.5*RHO*q_mean*Vj*Vj
    P_shaft = P_jet*ETA_TURGO
    P_elec = P_shaft*ETA_PMA*ETA_ELEC
    rpm = SPEED_RATIO*Vj/(math.pi*PCD)*60.0
    # ---- energy balance (per recorded window) ----
    E_in = RHO*G*drive_vol*s.F
    E_del = RHO*G*deliv_vol*s.Hd
    # ---- Joukowsky ----
    jouk_head = a*abs(v_pre_slam)/G   # full-slam theoretical spike (head, m)

    op = dict(
        config=dict(F_m=1.5, D_mm=300, L_m=30.0, LD=100, stroke_mm=8,
                    Wf=0.65, V_air_L=40, Hd_m=9.0, r=6,
                    wave_speed_ms=round(a, 1),
                    penstock=dict(L_m=PENSTOCK_L, D_mm=PENSTOCK_D*1000, f=F_DARCY)),
        ram=dict(eta_daubuisson=round(eta, 3), Q_drive_Ls=round(Q_mean*1000, 2),
                 q_deliv_Ls=round(q_mean*1000, 3), freq_hz=round(freq, 3),
                 Hj_peak_m=round(Hj_max, 1), v_col_prelslam_ms=round(abs(v_pre_slam), 3),
                 v_col_max_ms=round(v_run_max, 3),
                 joukowsky_full_slam_head_m=round(jouk_head, 1)),
        jet=dict(H_net_m=round(H_net, 2), penstock_loss_m=round(h_pen_loss, 3),
                 Vj_ms=round(Vj, 2), d_nozzle_single_mm=round(d_single*1000, 1),
                 d_nozzle_twin_mm=round(d_twin*1000, 1)),
        wheel=dict(type="Turgo (D-1: 4-8 m band)", PCD_mm=PCD*1000,
                   rpm=round(rpm, 0), runaway_rpm=round(1.8*rpm, 0)),
        power=dict(P_jet_W=round(P_jet, 1), P_shaft_W=round(P_shaft, 1),
                   P_electric_W=round(P_elec, 1),
                   annual_kWh=round(P_elec*8760*0.9/1000, 0),
                   chain="jet x0.75 turgo x0.85 PMA x0.92 MPPT (canon, bench supersedes)"),
        energy_window=dict(T_s=T, E_in_kJ=round(E_in/1000, 2),
                           E_delivered_kJ=round(E_del/1000, 2),
                           E_loss_kJ=round((E_in - E_del)/1000, 2),
                           balance_check_eta=round(E_del/E_in, 3)),
    )
    out_dir = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "..", "..", "engineering", "data"))
    with open(os.path.join(out_dir, "full_system_timeseries.json"), "w") as fh:
        json.dump(dict(fs_hz=fs, summary=op, series=series), fh)
    with open(os.path.join(out_dir, "full_system_operating_point.json"), "w") as fh:
        json.dump(op, fh, indent=1)
    print(json.dumps(op, indent=1))
    print(f"series samples: {len(series['t'])}")


if __name__ == "__main__":
    main()
