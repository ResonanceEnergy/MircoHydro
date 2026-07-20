#!/usr/bin/env python3
"""D-6 / D-7 digital bench: first-order jet conditioning model.

Predicts jet quality (T-001 CoV proxy + spreading angle) for the ratified
three-arm conditioning test (D-6) and the vortex nozzle (D-7), from swirl and
turbulence bookkeeping along tank -> penstock -> manifold -> nozzle.

HONESTY BANNER: this is a first-order engineering model (swirl decay laws,
contraction kinematics, calibrated to published anchors) — NOT CFD, NOT a
bench. Absolute numbers carry ~±50%; the RANKING and the mechanism analysis
are the deliverables. CFD or the physical rig supersedes (D-6/D-7 gates).

Anchors used:
  - good fixed nozzle, clean approach: jet CoV ~0.01 (PowerSpout-class practice)
  - bend close to nozzle costs >2 efficiency points (Staubli line) ~ CoV +0.02-0.03
  - swirl decay half-length 20-35D in smooth pipe (swirl literature)
  - honeycomb swirl transmission ~5% (wind-tunnel practice, cell L/D~10)
Mechanism note for D-6 arm B (founder's fluted pipe): helical ribs IMPOSE a
fixed swirl (they cannot remove swirl). Against a *steady* clean inflow this
adds deviation. But if the egg headstock's tangential entry (D-8) hands the
penstock a VARIABLE swirl, flutes lock it to a known constant — trading mean
deviation for reduced variance ("deterministic swirl" hypothesis, H-flute).
Both scenarios are computed.
"""
import math

# ---- geometry (canon reference site) ----
D_PEN = 0.090            # penstock ID, m
L_PEN = 12.0             # m
D_HDR = 0.110            # manifold/header bore
L_HDR_A = 8 * D_HDR      # straight header run (built ~8x bore)
A_RATIO = ((D_HDR/2)**2) / ((0.0095/2)**2)   # header->jet area ratio ~134

K_SWIRL_DECAY = 0.030    # per x/D, smooth pipe
K_PROFILE_RECOVER = 0.080
HONEYCOMB_S_TRANS = 0.05
HONEYCOMB_DP_TRANS = 0.30
TU_PIPE = 0.05

def contraction(S_in, Tu_in, Dp_in, a=A_RATIO):
    """Contraction kinematics: v_ax x a, v_t x sqrt(a) -> swirl angle shrinks;
    axial turbulence crushed ~1/a, lateral partially survives."""
    tan_theta = S_in / math.sqrt(a)
    Tu_jet = math.sqrt((Tu_in/a)**2 + (Tu_in*0.35/math.sqrt(a))**2) * 3.0
    Dp_jet = Dp_in * 0.5
    return tan_theta, Tu_jet, Dp_jet

def cov(tan_theta, Tu_jet, Dp_jet):
    return math.sqrt((1.0*tan_theta)**2 + (1.0*Tu_jet)**2 + (0.5*Dp_jet)**2)

def run_arm(name, S_tank, flutes=False, honeycomb=False, tight_elbow=False):
    # penstock inlet swirl from tank draw (D-8 tangential entry residual)
    S = S_tank
    # penstock run: smooth decay, or flutes LOCK swirl to their helix value
    if flutes:
        S_flute = 0.10           # helix ~12 deg, engagement 0.5
        S = S_flute              # imposed regardless of inflow
        Tu = TU_PIPE + 0.010     # rib-generated turbulence
    else:
        S = S * math.exp(-K_SWIRL_DECAY * L_PEN / D_PEN)
        Tu = TU_PIPE
    # manifold sweep (one wide-radius bend): adds swirl + profile distortion
    S_bend, Dp = 0.06, 0.10
    if tight_elbow:
        S_bend, Dp = 0.15, 0.25  # the "hook" the founder rejected
    S = math.sqrt(S**2 + S_bend**2)
    # header treatment
    run_D = L_HDR_A / D_HDR      # ~8 diameters of straight run
    if honeycomb:
        S *= HONEYCOMB_S_TRANS
        Dp *= HONEYCOMB_DP_TRANS
        Tu += 0.020              # cell-scale turbulence...
        run_D -= 2.0             # honeycomb occupies ~2D
        Tu *= math.exp(-0.25 * run_D)   # ...decays fast over remaining run
        Tu += TU_PIPE * 0.8
    S *= math.exp(-K_SWIRL_DECAY * run_D)
    Dp *= math.exp(-K_PROFILE_RECOVER * run_D)
    tt, tj, dj = contraction(S, Tu, Dp)
    c = cov(tt, tj, dj)
    spread_deg = math.degrees(math.atan(tt))
    return dict(arm=name, S_at_nozzle=S, cov=c, spread_deg=spread_deg,
                tan_theta=tt, Tu_jet=tj, Dp_jet=dj)

def vortex_nozzle(vane_deg=20.0):
    """D-7: swirl imposed INSIDE/AT the nozzle — no contraction relief."""
    tan_theta = math.tan(math.radians(vane_deg)) * 0.6   # partial engagement
    Tu_jet, Dp_jet = 0.02, 0.02
    return dict(arm=f"D-7 vortex nozzle ({vane_deg:.0f} deg vanes)",
                S_at_nozzle=float('nan'), cov=cov(tan_theta, Tu_jet, Dp_jet),
                spread_deg=math.degrees(math.atan(tan_theta)),
                tan_theta=tan_theta, Tu_jet=Tu_jet, Dp_jet=Dp_jet)

def main():
    print("# D-6 three-arm prediction (steady tank inflow, S_tank = 0.05)")
    rows = [run_arm("A smooth + plain header", 0.05),
            run_arm("B fluted penstock", 0.05, flutes=True),
            run_arm("C smooth + honeycomb", 0.05, honeycomb=True)]
    for r in rows:
        print(f"  {r['arm']:28s} CoV={r['cov']:.4f}  spread={r['spread_deg']:.2f} deg  (S_nozzle={r['S_at_nozzle']:.4f})")
    print("# D-6 with VARIABLE tank swirl (S_tank 0.02..0.30, D-8 tangential entry worst case)")
    for name, kw in (("A smooth", {}), ("B fluted", dict(flutes=True)), ("C honeycomb", dict(honeycomb=True))):
        covs = [run_arm(name, s, **kw)["cov"] for s in (0.02, 0.10, 0.20, 0.30)]
        mean = sum(covs)/len(covs)
        var = math.sqrt(sum((c-mean)**2 for c in covs)/len(covs))
        print(f"  {name:12s} CoV mean={mean:.4f}  spread-over-inflow={var:.4f}  (H-flute test: B's variance vs A's)")
    print("# D-7:")
    for v in (10.0, 20.0, 30.0):
        r = vortex_nozzle(v)
        print(f"  {r['arm']:34s} CoV={r['cov']:.3f}  spread={r['spread_deg']:.1f} deg")
    print("# tight-elbow counterfactual (the rejected hook), arm A geometry:")
    r = run_arm("A + hook before header", 0.05, tight_elbow=True)
    print(f"  {r['arm']:28s} CoV={r['cov']:.4f}  spread={r['spread_deg']:.2f} deg")

if __name__ == "__main__":
    main()
