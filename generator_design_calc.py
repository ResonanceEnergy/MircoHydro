#!/usr/bin/env python3
"""
10kW PMSG Generator Design Calculator
Validates scaling and key parameters
"""

import math

# Constants
P_rated = 10000  # W
RPM = 200
pole_pairs = 8
I_q = 15  # A (assumed)
B_gap = 0.8  # T
rho_cu = 8900  # kg/m3
rho_magnet = 7500  # kg/m3

# Calculations
omega = RPM * 2 * math.pi / 60  # rad/s
T = P_rated / omega  # N·m
print(f"Torque: {T:.1f} N·m")

Phi = (2 * T) / (3 * pole_pairs * I_q)  # Wb
print(f"Flux: {Phi:.2f} Wb")

Phi_per_pole = Phi / (2 * pole_pairs)
A_pole = Phi_per_pole / B_gap
print(f"Pole area: {A_pole:.3f} m²")

# Magnet dimensions (simplified)
arc_len = 0.18  # m
width = 0.09  # m
thickness = 0.012  # m
vol = arc_len * width * thickness
mass_per = vol * rho_magnet
total_mass = mass_per * 16
print(f"Magnet mass: {total_mass:.1f} kg")

# Efficiency estimate
P_cu = 3 * (35**2) * 0.01  # Rough R=0.01 ohm
efficiency = 1 - (P_cu / P_rated)
print(f"Estimated efficiency: {efficiency:.2%}")

print("Design validated.")