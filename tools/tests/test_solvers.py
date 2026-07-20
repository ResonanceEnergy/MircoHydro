#!/usr/bin/env python3
"""Unit tests for the canonical design solvers (P0-1).

These solvers guard the company's claims; this suite guards the solvers.
Run: pytest tools/tests -q     (CI: .github/workflows/ci.yml)
"""
import math, os, sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "design"))

from ram_moc_sim import RamSim
import crossflow_design as cf
import ram_pelton_design as rp


# ---------- ram_moc_sim: physics invariants ----------

def test_wave_speed_steel_300mm():
    """a = sqrt(K/rho / (1 + K*D/(E*e))) — 300 mm / 6 mm wall steel ~ 1173 m/s."""
    s = RamSim(F=1.5, D=0.30, wall=0.006, Hd_target=9.0)
    assert abs(s.a - 1173) < 5


def test_wave_speed_thin_wall_slower():
    thick = RamSim(F=1.5, D=0.30, wall=0.010, Hd_target=9.0)
    thin = RamSim(F=1.5, D=0.30, wall=0.003, Hd_target=9.0)
    assert thin.a < thick.a  # elastic wall lowers wave speed


def test_moc_timestep_consistency():
    s = RamSim(F=1.5, D=0.30, L=45.0, Hd_target=9.0, n_nodes=24)
    assert abs(s.dt - s.dx / s.a) < 1e-12
    assert abs(s.dx * s.N - s.L) < 1e-9


# ---------- ram_moc_sim: input validation ----------

@pytest.mark.parametrize("kwargs", [
    dict(F=0.0), dict(F=-1.0), dict(D=0.0), dict(D=1.5),
    dict(stroke=0.0), dict(stroke=0.5), dict(wall=0.0),
    dict(V_air0=0.0), dict(n_nodes=4), dict(L=-10.0),
    dict(wv_weight=0.0),
])
def test_invalid_inputs_raise(kwargs):
    base = dict(F=1.5, D=0.30, Hd_target=9.0)
    base.update(kwargs)
    with pytest.raises(ValueError):
        RamSim(**base)


def test_headstock_below_fall_raises():
    with pytest.raises(ValueError):
        RamSim(F=2.0, D=0.30, Hd_target=1.5)


# ---------- ram_moc_sim: reference regression (the calibration anchor) ----------

def test_reference_site_regression():
    """B300 anchor: eta and delivery must stay inside the calibrated envelope.

    If this fails after an intentional model change, re-anchor Kj and update
    SIM_RESULTS_RAM_MOC.md — never just widen the bounds.
    """
    s = RamSim(F=1.5, D=0.30, L=45.0, Hd_target=9.0)
    r = s.run(t_end=40.0, record_from=20.0)
    # v2 anchor (2026-07-19): Kj=100 + leak_frac=0.003 -> eta ~0.663
    assert 0.58 <= r["eta"] <= 0.72, r["eta"]
    assert 0.0 < r["eta_rankine"] < r["eta"]  # Rankine is strictly stricter
    assert 1.6 <= r["q_deliv_Ls"] <= 2.2, r["q_deliv_Ls"]
    assert 14.0 <= r["Q_drive_Ls"] <= 22.0, r["Q_drive_Ls"]
    assert 0.3 <= r["freq_hz"] <= 0.8, r["freq_hz"]


def test_energy_conservation_bound():
    """D'Aubuisson bound: delivered energy rate can never exceed drive energy rate."""
    s = RamSim(F=1.5, D=0.30, L=30.0, Hd_target=9.0)
    r = s.run(t_end=30.0, record_from=15.0)
    drive_power = r["Q_drive_Ls"] * s.F        # ~ rho*g cancels both sides
    deliv_power = r["q_deliv_Ls"] * r["h_delivery"]
    assert deliv_power <= drive_power * 1.001  # no perpetual motion
    assert 0.0 <= r["eta"] <= 1.0


# ---------- ram_moc_sim: T-002 Welch metric ----------

def test_psd_peakiness_sine_vs_noise():
    fs = 100.0
    n = 2000
    sine = [math.sin(2 * math.pi * 1.0 * i / fs) for i in range(n)]          # 1 Hz tone
    # deterministic pseudo-noise (no random module — reproducible)
    noise = [math.sin(2.2 * i) * math.cos(3.7 * i + 0.5) for i in range(n)]
    p_sine = RamSim._psd_peakiness(sine, fs)
    p_noise = RamSim._psd_peakiness(noise, fs)
    assert p_sine > 20.0          # dB: coherent tone is strongly peaked
    assert p_sine > p_noise + 6.0  # and clearly above broadband


def test_psd_peakiness_short_record():
    assert RamSim._psd_peakiness([1.0] * 10, 100.0) == 0.0


# ---------- crossflow_design ----------

def test_swamee_jain_laminar():
    assert abs(cf.swamee_jain(1000, 1e-5) - 0.064) < 1e-6


def test_swamee_jain_turbulent_reasonable():
    f = cf.swamee_jain(2e5, 1.5e-6 / 0.2)
    assert 0.01 < f < 0.03


def test_penstock_conserves_head():
    p = cf.penstock(Q=0.150, H_gross=5.0, L=50.0)
    assert 0 < p["h_net"] < 5.0
    assert p["h_loss"] > 0
    assert abs(p["h_net"] + p["h_loss"] - 5.0) < 1e-9


def test_crossflow_design_smoke():
    d = cf.design(Q=0.150, H=5.0, L=50.0)
    r = d["runner"]
    assert r["N_rpm"] > 0 and r["D1"] > 0 and r["b"] > 0
    assert r["N_runaway"] == pytest.approx(1.8 * r["N_rpm"])
    # electric power below hydraulic budget
    P_hyd = 1000.0 * 9.81 * 0.150 * d["penstock"]["h_net"]
    assert 0 < d["power"]["P_electric"] < P_hyd
    assert 0 < d["power"]["eta_water_to_wire_at_net_head"] < 1.0


# ---------- ram_pelton_design ----------

def test_eta_ram_fit_clamps():
    assert rp.eta_ram(3.0) == pytest.approx(0.72)   # upper clamp
    assert rp.eta_ram(24.0) == pytest.approx(0.20)  # lower clamp
    assert rp.eta_ram(6.0) == pytest.approx(0.67, abs=0.01)  # USAID anchor


def test_solve_site_smoke():
    best, rows = rp.solve_site(F=1.5, Q=0.100)
    # solver returns an operating point with positive power and legal geometry
    assert best["feasible"] is True
    assert best["P_W"] > 0
    assert best["dn_mm"] / 1000.0 >= rp.NOZZLE_MIN
    assert best["PCD_mm"] / 1000.0 <= rp.PCD_MAX + 1e-6
    assert rp.PMA_RPM[0] <= best["rpm"] <= rp.PMA_RPM[1]
    # NOTE (D-5 supersession): best['P_W'] uses the retired eta_ram fit and a
    # 100 L/s single-ram assumption; the MOC sim caps a 300 mm ram near
    # ~18 L/s (Finding 1). This test checks geometry math only, not the power
    # claim — solver ingestion of sim curves is queue #4.


def test_v2_leak_channel_costs_efficiency():
    """Model v2: more seat leakage must never increase efficiency."""
    tight = RamSim(F=1.5, D=0.30, L=45.0, Hd_target=9.0, leak_frac=0.0)
    leaky = RamSim(F=1.5, D=0.30, L=45.0, Hd_target=9.0, leak_frac=0.003)
    rt = tight.run(t_end=30.0, record_from=15.0)
    rl = leaky.run(t_end=30.0, record_from=15.0)
    assert rl["eta"] <= rt["eta"] + 0.02
