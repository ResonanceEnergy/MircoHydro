#!/usr/bin/env python3
"""Bank interaction model (GAP-5 / IP claim b evidence): N rams, one headstock.

Method: extract ONE ram's periodic delivery waveform q(t) and drive draw Q(t)
from the calibrated v2 MOC sim, then superpose N=6 copies at controlled phase
offsets through the SHARED rise pipe (head loss ~ (sum q)^2 couples the rams).

Questions answered:
  1. Does phase spread (staggered vs synchronized) change total delivered
     energy through the shared pipe?  (loss ~ q^2 says yes: peaks are costly)
  2. How much does anti-synchronization smooth headstock inflow (T-001 at the
     tank) and intake peak draw (screen/channel sizing)?

HONESTY: superposition assumes rams do not couple through the DRIVE side
(separate drive pipes per canon bank layout) and that the fixed-head headstock
decouples them downstream — both per ratified architecture. Phase-LOCKING
mechanisms (how to hold the stagger) are the self-tuning controller's job
(IP disclosure 2 claim b); this model quantifies the prize, not the servo.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ram_moc_sim import RamSim, RHO, G

N_RAMS = 6
K_RISE = 120.0          # shared DN100 rise pipe loss coeff: h_loss = K*(sum_q)^2  (~0.5 m at 6x1.9 L/s)




def waveform_via_series():
    """Cheap faithful route: sample q(t) and Q(t) by rerunning run() with the
    recorded series the sim already outputs (50 Hz export exists for the full
    system; here we re-generate at 100 Hz for one ram)."""
    # re-use export_full_system's loop shape inline (single ram, knee config)
    base = RamSim(F=1.5, D=0.30, Hd_target=9.0)
    s = RamSim(F=1.5, D=0.30, L=30.0, Hd_target=9.0, stroke=0.008,
               wv_weight=base.W*0.65, V_air0=0.040, n_nodes=16)
    N, dt, a, A = s.N, s.dt, s.a, s.A
    B = a/(G*A); R = s.f*s.dx/(2*G*s.D*A*A)
    H = [s.F*(1 - i/N) for i in range(N+1)]
    Q = [0.0]*(N+1)
    x_v, u_v = s.stroke, 0.0
    P_ch = RHO*G*s.Hd; V_air = s.V_air0
    C_gas = (P_ch + 101325.0)*V_air**s.n_poly
    t = 0.0; fs = 100.0; nxt = 30.0
    tt, qd_s, q0_s = [], [], []
    while t < 60.0:
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
        Aw_open = s.Aw_max*max(0.0, min(1.0, x_v/s.stroke))
        Aw = Aw_open + s.leak_frac*s.Aw_max
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
        Qw_open = s.Cd_w*Aw_open*math.sqrt(2*G*max(Hj, 0.0)) if Aw_open > 0 else 0.0
        v_port = (Qw_open/max(Aw_open, 1e-6)) if Aw_open > 0 else 0.0
        F_close = 0.5*RHO*1.15*s.Cd_w*s.Aw_max*v_port*v_port \
                  + max(Hj - s.F, 0.0)*RHO*G*s.Aw_max*0.15
        u_v += (s.W - F_close)/s.m_v*dt
        x_v += u_v*dt
        if x_v <= 0.0:
            x_v, u_v = 0.0, 0.0
        elif x_v >= s.stroke:
            x_v, u_v = s.stroke, min(u_v, 0.0)
        Qd = s.G_del*max(h_ch - s.Hd, 0.0)
        V_air += (Qd - Qc)*dt
        V_air = max(s.V_air0*0.3, min(s.V_air0*1.7, V_air))
        P_ch = C_gas/V_air**s.n_poly - 101325.0
        if t >= nxt:
            tt.append(t); qd_s.append(Qd); q0_s.append(max(Qn[0], 0.0))
            nxt += 1.0/fs
        H, Q = Hn, Qn
        t += dt
    return tt, qd_s, q0_s, fs


def analyze():
    tt, qd, q0, fs = waveform_via_series()
    n = len(qd)
    # find the fundamental period from delivery autocorrelation (~0.9 Hz)
    mean_q = sum(qd)/n
    # phase-offset superposition
    def bank(spread):
        """spread: fraction of one period between adjacent rams (0=sync, 1/N=perfect stagger)."""
        period = 1.0/0.9
        off = [int(k*spread*period*fs) % n for k in range(N_RAMS)]
        tot = [sum(qd[(i + off[k]) % n] for k in range(N_RAMS)) for i in range(n)]
        tot_in = [sum(q0[(i + off[k]) % n] for k in range(N_RAMS)) for i in range(n)]
        m = sum(tot)/n
        cov = math.sqrt(sum((x-m)**2 for x in tot)/n)/m if m > 0 else 0
        # shared rise pipe: instantaneous loss K*(q_tot)^2 -> delivered head reduced
        loss_power = sum(RHO*G*K_RISE*x*x*x for x in tot)/n     # rho*g*h_loss(q)*q
        del_power = RHO*G*9.0*m - loss_power
        peak_in = max(tot_in)
        return cov, del_power, loss_power, peak_in, m
    print("# 6-ram bank vs phase spread (superposition through shared DN100 rise pipe)")
    print(f"{'config':>22} {'inflow CoV':>10} {'P_del W':>9} {'P_loss W':>9} {'peak intake L/s':>16}")
    base = None
    for name, sp in (("synchronized", 0.0), ("half stagger", 0.5/N_RAMS),
                     ("perfect stagger 1/6", 1.0/N_RAMS)):
        cov, dp, lp, pk, m = bank(sp)
        if base is None: base = (cov, dp, lp, pk)
        print(f"{name:>22} {cov:>10.3f} {dp:>9.1f} {lp:>9.2f} {pk*1000:>16.1f}")
    cov_s, dp_s, lp_s, pk_s = base
    cov_p, dp_p, lp_p, pk_p, _ = bank(1.0/N_RAMS)
    print(f"\nanti-sync benefit: ripple {cov_s:.3f}->{cov_p:.3f} "
          f"({100*(1-cov_p/max(cov_s,1e-9)):.0f}% smoother), "
          f"rise-pipe loss {lp_s:.2f}->{lp_p:.2f} W, "
          f"peak intake draw {pk_s*1000:.1f}->{pk_p*1000:.1f} L/s "
          f"({100*(1-pk_p/max(pk_s,1e-9)):.0f}% lower screen/channel sizing)")


if __name__ == "__main__":
    analyze()
