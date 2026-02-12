#!/usr/bin/env python3
"""Efficiency Cascade Calculator for MicroHydro System

Calculates realistic efficiency based on component losses.
"""

def calculate_efficiency(hydraulic_eff=0.9, mechanical_eff=0.95, electrical_eff=0.95):
    total_eff = hydraulic_eff * mechanical_eff * electrical_eff
    return total_eff

if __name__ == '__main__':
    eff = calculate_efficiency()
    print(f"Total System Efficiency: {eff:.2%}")  # ~81%