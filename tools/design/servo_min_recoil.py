#!/usr/bin/env python3
"""Sim queue #2c — self-tuning ram, digital prototype v3: SWEEP-THEN-TRACK.

Lessons recorded on the way here (kept in git history, per canon):
  v1: naive extremum-seek on raw |recoil| -> climbed into a fake low-recoil
      basin created by valve-bounce chatter; lost 4x output.
  v2: debounced events (closure >= 50 ms) killed the chatter artifact but a
      REAL second attractor at heavy tune remains — |recoil| is multi-modal
      in valve weight, so blind descent from arbitrary mistune can converge
      to the wrong basin.
  v3 (this file): the solar-MPPT answer to the same multi-modal problem —
      a COMMISSIONING SWEEP maps recoil across the full weight range once,
      the controller jumps to the global minimum (the knee), then TRACKS it
      with small steps + best-point memory. On sustained degradation
      (score > 2.5x commissioned best) it re-sweeps automatically.
Hardware needs: one pressure/flow sensor + one weight/preload actuator.

Scenario: start badly mistuned (Wf = 1.4); supply fall drops 1.5 -> 1.2 m at
t = 110 s. Baseline: fixed valve at the same mistune.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ram_moc_sim import RamSim, RHO, G

HOLD = 0.05          # s of closure for a debounced reopen event
SWEEP_WFS = (0.40, 0.55, 0.70, 0.85, 1.00, 1.20, 1.45, 1.65)
SWEEP_EVENTS = 4     # debounced events per sweep step
TRACK_BATCH = 5
TRACK_STEP = 0.04    # fraction of W_nom
RESWEEP_RATIO = 2.5


def run_case(servo, t_end=200.0, drift_t=110.0, F0=1.5, F1=1.2, Wf0=1.4):
    s = RamSim(F=F0, D=0.30, L=30.0, Hd_target=9.0, stroke=0.008, n_nodes=16)
    W_nom = s.W
    s.W = W_nom*Wf0
    N, dt, dx, a, A, f, D = s.N, s.dt, s.dx, s.a, s.A, s.f, s.D
    B = a/(G*A); R = f*dx/(2*G*D*A*A)
    F_now = F0
    H = [F_now*(1 - i/N) for i in range(N+1)]
    Q = [0.0]*(N+1)
    x_v, u_v = s.stroke, 0.0
    P_ch = RHO*G*s.Hd; V_air = s.V_air0
    C_gas = (P_ch + 101325.0)*V_air**s.n_poly
    closed_t = 0.0; was_closed = False
    # servo state machine
    mode = "SWEEP" if servo else "OFF"
    sweep_i = 0; sweep_scores = []
    if servo:
        s.W = W_nom*SWEEP_WFS[0]
    ev_batch = []
    direction = 1.0; prev_score = None
    best_score = None; best_W = s.W
    commissioned = None
    events_log = []
    windows = [(85.0, drift_t, "pre-drift"), (drift_t + 50.0, t_end, "post-drift")]
    acc = [dict(drive=0.0, deliv=0.0, absq=[]) for _ in windows]
    W_track = []
    t = 0.0
    while t < t_end:
        if F_now == F0 and t >= drift_t:
            F_now = F1
        Hn, Qn = H[:], Q[:]
        for i in range(1, N):
            Cp = H[i-1] + B*Q[i-1] - R*Q[i-1]*abs(Q[i-1])
            Cm = H[i+1] - B*Q[i+1] + R*Q[i+1]*abs(Q[i+1])
            Hn[i] = 0.5*(Cp + Cm); Qn[i] = (Cp - Cm)/(2*B)
        Cm = H[1] - B*Q[1] + R*Q[1]*abs(Q[1])
        ke = (1 + s.Ke)/(2*G*s.A*s.A); Q0 = Q[0]
        for _ in range(4):
            Q0 = (F_now - ke*Q0*abs(Q0) - Cm)/B
        Qn[0] = Q0; Hn[0] = F_now - ke*Q0*abs(Q0)
        Cp = H[N-1] + B*Q[N-1] - R*Q[N-1]*abs(Q[N-1])
        KjR = s.Kj/(2*G*s.A*s.A)
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
        v_port = (Qw/max(Aw, 1e-6)) if Aw > 0 else 0.0
        F_close = 0.5*RHO*1.15*s.Cd_w*s.Aw_max*v_port*v_port \
                  + max(Hj - F_now, 0.0)*RHO*G*s.Aw_max*0.15
        u_v += (s.W - F_close)/s.m_v*dt
        x_v += u_v*dt
        if x_v <= 0.0:
            x_v, u_v = 0.0, 0.0
            was_closed = True
            closed_t += dt
        else:
            if was_closed and closed_t >= HOLD:
                qr = abs(Qn[N//2])
                for wi, (t0, t1, _) in enumerate(windows):
                    if t0 <= t < t1:
                        acc[wi]['absq'].append(qr)
                if mode == "SWEEP":
                    ev_batch.append(qr)
                    if len(ev_batch) >= SWEEP_EVENTS:
                        med = sorted(ev_batch)[len(ev_batch)//2]
                        sweep_scores.append((med, SWEEP_WFS[sweep_i]))
                        ev_batch = []
                        sweep_i += 1
                        if sweep_i < len(SWEEP_WFS):
                            s.W = W_nom*SWEEP_WFS[sweep_i]
                        else:
                            commissioned, wf_star = min(sweep_scores)
                            s.W = W_nom*wf_star
                            best_score, best_W = commissioned, s.W
                            events_log.append((t, f"commissioned: Wf*={wf_star:.2f} score={commissioned*1000:.2f} L/s"))
                            mode = "TRACK"; prev_score = None
                elif mode == "TRACK":
                    ev_batch.append(qr)
                    if len(ev_batch) >= TRACK_BATCH:
                        score = sorted(ev_batch)[len(ev_batch)//2]
                        ev_batch = []
                        if score < best_score:
                            best_score, best_W = score, s.W
                        if score > RESWEEP_RATIO*commissioned:
                            mode = "SWEEP"; sweep_i = 0; sweep_scores = []
                            s.W = W_nom*SWEEP_WFS[0]
                            events_log.append((t, "degradation detected -> re-sweep"))
                        else:
                            if prev_score is not None and score > prev_score:
                                direction = -direction
                            s.W = max(0.3*W_nom, min(2.5*W_nom, s.W + direction*TRACK_STEP*W_nom))
                        prev_score = score
            was_closed = False
            closed_t = 0.0
            if x_v >= s.stroke:
                x_v, u_v = s.stroke, min(u_v, 0.0)
        Qd = s.G_del*max(h_ch - s.Hd, 0.0)
        V_air += (Qd - Qc)*dt
        V_air = max(s.V_air0*0.3, min(s.V_air0*1.7, V_air))
        P_ch = C_gas/V_air**s.n_poly - 101325.0
        for wi, (t0, t1, _) in enumerate(windows):
            if t0 <= t < t1:
                acc[wi]['drive'] += max(Qn[0], 0.0)*dt
                acc[wi]['deliv'] += Qd*dt
        if int(t) % 10 == 0 and (not W_track or W_track[-1][0] != int(t)):
            W_track.append((int(t), s.W/W_nom))
        H, Q = Hn, Qn
        t += dt
    out = []
    for wi, (t0, t1, name) in enumerate(windows):
        T = t1 - t0
        Qd_m = acc[wi]['drive']/T
        qd_m = acc[wi]['deliv']/T
        Fw = F0 if name == "pre-drift" else F1
        eta = qd_m*s.Hd/(Qd_m*Fw) if Qd_m > 1e-9 else 0.0
        rec = (sum(acc[wi]['absq'])/len(acc[wi]['absq'])/max(Qd_m, 1e-9)) if acc[wi]['absq'] else float('nan')
        out.append(dict(window=name, eta=eta, Q_Ls=Qd_m*1000, q_Ls=qd_m*1000, recoil=rec))
    return out, W_track, events_log


def main():
    print("# Sweep-then-track servo vs fixed mistuned valve")
    print("# start Wf=1.4 (mistuned); F: 1.5 -> 1.2 m at t=110 s")
    for servo in (False, True):
        tag = "SERVO" if servo else "FIXED"
        res, wt, ev = run_case(servo)
        for r in res:
            print(f"{tag} {r['window']:>10}: eta={r['eta']:.3f} Q={r['Q_Ls']:.1f} L/s "
                  f"q={r['q_Ls']:.2f} L/s recoil={r['recoil']:.3f}")
        if servo:
            for te, msg in ev:
                print(f"  [{te:6.1f}s] {msg}")
            print("  W/W_nom:", " ".join(f"{t}s:{w:.2f}" for t, w in wt[::2]))


if __name__ == "__main__":
    main()
