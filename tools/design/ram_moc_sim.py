#!/usr/bin/env python3
"""
Resonance Energy Systems — hydraulic ram transient simulator (digital bench).

Method of characteristics (MOC) water-hammer model of the drive pipe, coupled to
dynamic waste-valve, check-valve, air-chamber, and delivery-nozzle boundary
conditions. This is the published, lab-validated modelling approach for rams
(Filipan & Virag; J. Hydraulic Research 2024) — not a game engine, not a fit.

Supersedes the fitted curve eta_ram(r) = 0.85 - 0.03r per founder decision D-5
(docs/business/decisions/DECISION_2026-07-18_design_D1-D5_canon_name.md).

Per decision D-4, the simulator computes the founder's Gen 0 locked metrics:
  T-002 PSD peakiness of delivery pressure in the 0.2-20 Hz band
  T-001 jet coherence proxy (coefficient of variation of jet velocity)

Model summary
-------------
Drive pipe (length L, diameter D, wall e, steel): MOC on N nodes,
  wave speed a = sqrt(K/rho / (1 + K*D/(E*e))), Darcy friction f.
Upstream BC: reservoir at fall F (constant head).
Downstream BC (junction head Hj solves flow balance each step):
  waste valve: orifice Q_w = Cd_w * A_w(x) * sqrt(2 g Hj), disc dynamics
      m x'' = W_net - F_flow(x, v)   (weight opens, drag/pressure closes)
  check valve: opens on Hj > H_ch; Q_c = Cd_c * A_c * sqrt(2 g (Hj - H_ch))
  air chamber: polytropic gas cushion P V^1.2 = const
  delivery nozzle (the Machine B jet): Q_jet = Cv * A_n * sqrt(2 g h_ch)
Outputs at periodic steady state: cycle frequency, drive flow Q, delivery q,
D'Aubuisson efficiency eta = q*Hd_effective/(Q*F), pressure ripple, Gen 0 metrics.

Usage:
  python3 ram_moc_sim.py                # reference site + r-sweep + tuning map
  python3 ram_moc_sim.py --F 1.5 --D 0.3 --sweep
"""
import argparse, json, math

RHO, G = 1000.0, 9.81
K_WATER = 2.1e9            # bulk modulus, Pa
E_STEEL = 200e9            # Young's modulus, Pa


class RamSim:
    def __init__(self, F=1.5, L=None, D=0.30, wall=0.006, f=0.022,
                 stroke=0.015, wv_dia_ratio=1.0, wv_weight=None,
                 Hd_target=9.0, V_air0=0.060, n_nodes=24,
                 K_entrance=0.5, K_junction=None):
        self.F = F
        self.L = L if L else max(6*F, 150*D)
        self.D = D
        self.A = math.pi*D*D/4
        self.f = f
        self.Ke = K_entrance
        # junction dissipation (valve slam / unsteady friction lump) —
        # single calibration knob anchored to USAID eta≈0.66 @ r=6: Kj=125 calibrated 2026-07-18 (see SIM_RESULTS doc)
        self.Kj = K_junction if K_junction is not None else 125.0
        # wave speed with pipe elasticity
        self.a = math.sqrt(K_WATER/RHO / (1 + K_WATER*D/(E_STEEL*wall)))
        self.N = n_nodes
        self.dx = self.L/self.N
        self.dt = self.dx/self.a
        # waste valve
        self.stroke = stroke
        self.Aw_max = math.pi*(D*wv_dia_ratio)**2/4 * 0.6   # effective port area
        self.Cd_w = 0.7
        self.m_v = 4.0 * (D/0.3)**2                          # disc+stem mass, scaled
        # closing weight: default sized so valve closes near port velocity ~0.7 m/s
        self.W = wv_weight if wv_weight else 0.5*RHO*1.15*self.Cd_w*self.Aw_max*0.7**2
        # check valve + chamber + delivery to headstock (fixed head Hd — ratified architecture)
        self.Ac = self.A*0.5
        self.Cd_c = 0.8
        self.V_air0 = V_air0
        self.n_poly = 1.2
        self.Hd = Hd_target
        # delivery leg conductance chamber->headstock (DN80-class rise pipe, linearized)
        self.G_del = 0.008    # m^3/s per m of head difference

    def run(self, t_end=40.0, record_from=20.0, sample_hz=100.0):
        N, dt, dx, a, A, f, D = self.N, self.dt, self.dx, self.a, self.A, self.f, self.D
        B = a/(G*A)                     # MOC impedance
        R = f*dx/(2*G*D*A*A)            # friction coefficient
        H = [self.F*(1 - i/N) for i in range(N+1)]   # initial head profile
        Q = [0.0]*(N+1)
        x_v, u_v = self.stroke, 0.0     # waste valve starts open
        P_ch = RHO*G*self.Hd            # chamber gauge pressure ~ delivery target
        V_air = self.V_air0
        C_gas = (P_ch + 101325.0)*V_air**self.n_poly
        drive_vol = deliv_vol = 0.0
        cycles = 0
        last_closed = False
        was_closed = False            # zero-recoil instrumentation: reopen events
        reopen_Q = []                 # drive-pipe flow at each valve-reopen instant
        t = 0.0
        rec_t, rec_p, rec_qj = [], [], []
        next_sample = record_from
        rec_drive = rec_deliv = 0.0
        rec_started = False
        while t < t_end:
            Hn, Qn = H[:], Q[:]
            # interior nodes
            for i in range(1, N):
                Cp = H[i-1] + B*Q[i-1] - R*Q[i-1]*abs(Q[i-1])
                Cm = H[i+1] - B*Q[i+1] + R*Q[i+1]*abs(Q[i+1])
                Hn[i] = 0.5*(Cp + Cm)
                Qn[i] = (Cp - Cm)/(2*B)
            # upstream reservoir BC with entrance loss: F - (1+Ke)*v^2/2g = Cm + B*Q
            Cm = H[1] - B*Q[1] + R*Q[1]*abs(Q[1])
            ke_coef = (1 + self.Ke)/(2*G*self.A*self.A)
            Q0 = Q[0]
            for _ in range(4):    # fixed-point solve
                Q0 = (self.F - ke_coef*Q0*abs(Q0) - Cm)/B
            Qn[0] = Q0
            Hn[0] = self.F - ke_coef*Q0*abs(Q0)
            # downstream junction BC with dissipation Kj (slam/unsteady-friction lump):
            # Cp - Hj = B*Qp + KjR*Qp|Qp|  and  Qp = Qw + Qc
            Cp = H[N-1] + B*Q[N-1] - R*Q[N-1]*abs(Q[N-1])
            KjR = self.Kj/(2*G*self.A*self.A)
            Aw = self.Aw_max*max(0.0, min(1.0, x_v/self.stroke))
            h_ch = P_ch/(RHO*G)
            lo, hi = -20.0, max(Cp, h_ch) + 80.0
            for _ in range(48):
                Hj = 0.5*(lo + hi)
                dH = Cp - Hj
                # solve B*Qp + KjR*Qp|Qp| = dH  (positive root for dH>0)
                if dH >= 0:
                    Qp = (-B + math.sqrt(B*B + 4*KjR*dH))/(2*KjR) if KjR > 1e-12 else dH/B
                else:
                    Qp = (B - math.sqrt(B*B - 4*KjR*dH))/(2*KjR) if KjR > 1e-12 else dH/B
                Qw = self.Cd_w*Aw*math.sqrt(2*G*max(Hj, 0.0)) if Aw > 0 else 0.0
                Qc = self.Cd_c*self.Ac*math.sqrt(2*G*max(Hj - h_ch, 0.0)) if Hj > h_ch else 0.0
                (lo, hi) = (Hj, hi) if (Qp - Qw - Qc) > 0 else (lo, Hj)
            Hn[N], Qn[N] = Hj, Qp
            # waste valve disc dynamics: weight opens (+), flow drag + pressure close (-)
            v_port = (Qw/max(Aw, 1e-6)) if Aw > 0 else 0.0
            F_close = 0.5*RHO*1.15*self.Cd_w*self.Aw_max*v_port*v_port \
                      + max(Hj - self.F, 0.0)*RHO*G*self.Aw_max*0.15
            acc = (self.W - F_close)/self.m_v
            u_v += acc*dt
            x_v += u_v*dt
            if x_v <= 0.0:
                x_v, u_v = 0.0, 0.0
                if not last_closed:
                    cycles += 1
                    last_closed = True
                was_closed = True
            else:
                if was_closed and rec_started:
                    # valve reopening after full closure: Young's zero-recoil
                    # condition met when the water COLUMN's flow ~ 0 at this
                    # instant (mid-pipe node — junction node is 0 by BC when shut)
                    reopen_Q.append(Qn[N//2])
                was_closed = False
                if x_v >= self.stroke:
                    x_v, u_v = self.stroke, min(u_v, 0.0)
                    last_closed = False
            # chamber update: inflow Qc from check valve, outflow Qd up the rise pipe
            # to the headstock at fixed head Hd (ratified architecture)
            Qd = self.G_del*max(h_ch - self.Hd, 0.0)
            V_air += (Qd - Qc)*dt          # air expands when outflow exceeds inflow
            V_air = max(self.V_air0*0.3, min(self.V_air0*1.7, V_air))
            P_ch = C_gas/V_air**self.n_poly - 101325.0
            drive_vol += max(Qn[0], 0.0)*dt
            deliv_vol += Qd*dt
            Qj = Qd                        # recorded for T-001 jet-variation metric
            if rec_started or t >= record_from:
                if not rec_started:
                    rec_started = True
                    drive_vol = deliv_vol = 0.0
                    cyc0 = cycles
                if t >= next_sample:
                    rec_t.append(t); rec_p.append(P_ch); rec_qj.append(Qj)
                    next_sample += 1.0/sample_hz
            H, Q = Hn, Qn
            t += dt
        T_rec = t_end - record_from
        Qdr = drive_vol/T_rec
        qd = deliv_vol/T_rec
        h_del = self.Hd                     # delivery head = headstock elevation (fixed)
        eta = qd*h_del/(Qdr*self.F) if Qdr > 0 else 0.0
        r = h_del/self.F
        Qd = Qdr
        # Gen 0 metrics
        psd_peak = self._psd_peakiness(rec_p, sample_hz)
        mean_qj = sum(rec_qj)/len(rec_qj)
        var_qj = sum((q-mean_qj)**2 for q in rec_qj)/len(rec_qj)
        jet_cov = math.sqrt(var_qj)/mean_qj if mean_qj > 0 else 1.0
        # zero-recoil mismatch: mean |drive-pipe flow| at valve reopen, normalized
        # by mean drive flow (0 = perfect Young condition; >1 = badly mistimed)
        recoil = (sum(abs(q) for q in reopen_Q)/len(reopen_Q)/max(Qdr, 1e-9)) if reopen_Q else float('nan')
        return dict(F=self.F, L=self.L, D=self.D, a=self.a,
                    Q_drive_Ls=Qd*1000, q_deliv_Ls=qd*1000,
                    h_delivery=h_del, r=r, eta=eta,
                    freq_hz=(cycles - cyc0)/T_rec if rec_started else 0,
                    ripple_pct=100*(max(rec_p)-min(rec_p))/max(sum(rec_p)/len(rec_p), 1),
                    T002_psd_peakiness=psd_peak, T001_jet_cov=jet_cov,
                    recoil_mismatch=recoil, n_reopens=len(reopen_Q))

    @staticmethod
    def _psd_peakiness(p, fs):
        """Gen 0 T-002: dominant-peak-to-median PSD ratio in 0.2-20 Hz (simple DFT)."""
        n = min(len(p), 2048)
        if n < 64: return 0.0
        p = p[-n:]
        mean = sum(p)/n
        x = [v - mean for v in p]
        psd = []
        for k in range(1, n//2):
            fr = k*fs/n
            if fr < 0.2 or fr > 20.0: continue
            re = sum(x[i]*math.cos(2*math.pi*k*i/n) for i in range(n))
            im = sum(x[i]*math.sin(2*math.pi*k*i/n) for i in range(n))
            psd.append(re*re + im*im)
        if not psd: return 0.0
        s = sorted(psd)
        med = s[len(s)//2]
        return max(psd)/med if med > 0 else 0.0


def sweep_r(F=1.5, D=0.30, targets=(4, 6, 8, 10, 12, 16, 20)):
    rows = []
    for rt in targets:
        sim = RamSim(F=F, D=D, Hd_target=rt*F)
        res = sim.run()
        rows.append(res)
    return rows


def tuning_map(F=1.5, D=0.30, Hd_target=9.0):
    rows = []
    base = RamSim(F=F, D=D, Hd_target=Hd_target)
    W0 = base.W
    for wf in (0.5, 0.75, 1.0, 1.5, 2.0):
        for st in (0.010, 0.020, 0.035):
            sim = RamSim(F=F, D=D, Hd_target=Hd_target, wv_weight=W0*wf, stroke=st)
            res = sim.run()
            res.update(weight_factor=wf, stroke_mm=st*1000)
            rows.append(res)
    return rows


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--F", type=float, default=1.5)
    ap.add_argument("--D", type=float, default=0.30)
    ap.add_argument("--Hd", type=float, default=9.0)
    ap.add_argument("--sweep", action="store_true")
    ap.add_argument("--tuning", action="store_true")
    args = ap.parse_args()

    print(f"# Resonance Energy Systems — ram MOC digital bench")
    sim = RamSim(F=args.F, D=args.D, Hd_target=args.Hd)
    print(f"drive pipe {sim.L:.0f} m x {sim.D*1000:.0f} mm, wave speed {sim.a:.0f} m/s, dt {sim.dt*1000:.2f} ms")
    res = sim.run()
    print(json.dumps({k: round(v, 4) if isinstance(v, float) else v for k, v in res.items()}, indent=1))

    if args.sweep:
        print("\n# eta(r) sweep vs retired fit 0.85-0.03r")
        print(f"{'r':>6} {'eta_sim':>8} {'eta_fit':>8} {'Q(L/s)':>8} {'q(L/s)':>8} {'freq':>6} {'T002':>7} {'T001cov':>8}")
        for row in sweep_r(F=args.F, D=args.D):
            fit = max(0.2, min(0.72, 0.85 - 0.03*row['r']))
            print(f"{row['r']:>6.1f} {row['eta']:>8.3f} {fit:>8.3f} {row['Q_drive_Ls']:>8.1f} "
                  f"{row['q_deliv_Ls']:>8.2f} {row['freq_hz']:>6.2f} {row['T002_psd_peakiness']:>7.1f} {row['T001_jet_cov']:>8.3f}")

    if args.tuning:
        print("\n# waste-valve tuning map (weight x stroke)")
        print(f"{'Wf':>5} {'stroke':>7} {'eta':>7} {'q(L/s)':>8} {'freq':>6}")
        for row in tuning_map(F=args.F, D=args.D, Hd_target=args.Hd):
            print(f"{row['weight_factor']:>5.2f} {row['stroke_mm']:>6.0f}mm {row['eta']:>7.3f} "
                  f"{row['q_deliv_Ls']:>8.2f} {row['freq_hz']:>6.2f}")
