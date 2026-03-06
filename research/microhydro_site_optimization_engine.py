# microhydro_site_optimization_engine.py
# MicroHydro Site Selection Optimization Engine
# Adapted from AAC Arbitrage Engine technology for optimal hydroelectric site identification

import requests
import pandas as pd
import numpy as np
from datetime import datetime
import json
import os

class SiteOptimizationEngine:
    def __init__(self):
        self.data_sources = {
            'usgs_water_flow': 'https://waterservices.usgs.gov/nwis/iv/',
            'elevation_api': 'https://api.opentopodata.org/v1/test-dataset',
            'climate_data': 'https://climate.nasa.gov/api/v1.0/',
            'regulatory_data': 'https://www.epa.gov/api/'
        }
        self.sites_db = []

    def fetch_water_flow_data(self, site_id):
        """Fetch real-time water flow data from USGS (mocked for demo)"""
        # Mock data for demonstration - replace with real API calls
        import random
        mock_flows = [random.uniform(50, 200) for _ in range(7)]  # 7 days of data
        return {'mock': True, 'flows': mock_flows}

    def calculate_hydro_potential(self, flow_rate, head_height, efficiency=0.8):
        """Calculate hydroelectric potential in kW"""
        # Power = (flow_rate_m3s * head_m * density * gravity * efficiency) / 1000
        flow_m3s = flow_rate * 0.0283168  # Convert cfs to m³/s
        power_kw = (flow_m3s * head_height * 1000 * 9.81 * efficiency) / 1000
        return power_kw

    def assess_site_viability(self, site_data):
        """Assess overall site viability score"""
        scores = {
            'flow_stability': self._score_flow_stability(site_data.get('flow_history', [])),
            'head_potential': min(site_data.get('head_m', 0) / 50, 1),  # Normalize to 50m max
            'environmental_impact': self._score_environmental_impact(site_data),
            'regulatory_feasibility': self._score_regulatory(site_data),
            'economic_viability': self._score_economics(site_data)
        }

        # Weighted average
        weights = {'flow_stability': 0.3, 'head_potential': 0.25, 'environmental_impact': 0.2,
                  'regulatory_feasibility': 0.15, 'economic_viability': 0.1}

        total_score = sum(scores[k] * weights[k] for k in scores)
        return total_score, scores

    def _score_flow_stability(self, flow_history):
        """Score flow stability based on variance"""
        if not flow_history:
            return 0.5
        variance = np.var(flow_history)
        mean_flow = np.mean(flow_history)
        cv = variance ** 0.5 / mean_flow if mean_flow > 0 else 1
        return max(0, 1 - cv)  # Lower CV = higher stability

    def _score_environmental_impact(self, site_data):
        """Score environmental impact"""
        # Placeholder scoring based on site characteristics
        impact_factors = 0
        if site_data.get('fish_passage_required', False):
            impact_factors += 0.2
        if site_data.get('wetland_nearby', False):
            impact_factors += 0.3
        if site_data.get('endangered_species', False):
            impact_factors += 0.5
        return max(0, 1 - impact_factors)

    def _score_regulatory(self, site_data):
        """Score regulatory feasibility"""
        # Placeholder based on permits required
        permits_needed = site_data.get('permits_required', [])
        base_score = 1.0
        penalty_per_permit = 0.1
        return max(0, base_score - len(permits_needed) * penalty_per_permit)

    def _score_economics(self, site_data):
        """Score economic viability"""
        capex = site_data.get('estimated_capex', 1000000)
        potential_kw = site_data.get('potential_kw', 0.1)  # Avoid zero
        if potential_kw <= 0:
            return 0
        lcoe_target = 0.10  # $0.10/kWh target
        estimated_lcoe = capex / (potential_kw * 8760 * 20)  # 20 year payback
        return min(1, lcoe_target / estimated_lcoe if estimated_lcoe > 0 else 0)

    def optimize_site_selection(self, candidate_sites):
        """Main optimization function"""
        optimized_sites = []

        for site in candidate_sites:
            # Fetch real-time data
            flow_data = self.fetch_water_flow_data(site.get('usgs_id'))

            if flow_data and flow_data.get('mock'):
                # Use mock data
                flow_values = flow_data['flows']
            elif flow_data:
                # Extract flow rates from real API
                flow_values = [v[1] for v in flow_data.get('value', {}).get('timeSeries', [{}])[0].get('values', [{}])[0].get('value', []) if v[1] != '']
            else:
                flow_values = []

            site['flow_history'] = flow_values
            potential_kw = self.calculate_hydro_potential(
                site.get('avg_flow_cfs', 0),
                site.get('head_m', 0)
            )
            site['potential_kw'] = potential_kw

            # Assess viability
            viability_score, component_scores = self.assess_site_viability(site)
            site['viability_score'] = viability_score
            site['component_scores'] = component_scores

            optimized_sites.append(site)

        # Sort by viability score
        optimized_sites.sort(key=lambda x: x['viability_score'], reverse=True)

        return optimized_sites

def main():
    engine = SiteOptimizationEngine()

    # Sample candidate sites (in real implementation, load from database/API)
    candidate_sites = [
        {
            'name': 'River Bend Site A',
            'usgs_id': '12345678',
            'head_m': 25,
            'fish_passage_required': True,
            'wetland_nearby': False,
            'endangered_species': False,
            'permits_required': ['FERC', 'EPA'],
            'estimated_capex': 800000
        },
        {
            'name': 'Mountain Stream Site B',
            'usgs_id': '87654321',
            'head_m': 40,
            'fish_passage_required': False,
            'wetland_nearby': True,
            'endangered_species': False,
            'permits_required': ['State Water', 'Local'],
            'estimated_capex': 600000
        }
    ]

    optimized_sites = engine.optimize_site_selection(candidate_sites)

    print("MicroHydro Site Optimization Results:")
    print("=" * 50)

    for i, site in enumerate(optimized_sites[:5]):  # Top 5
        print(f"\n{i+1}. {site['name']}")
        print(f"   Viability Score: {site['viability_score']:.2f}")
        print(f"   Potential Power: {site['potential_kw']:.1f} kW")
        print(f"   Average Flow: {site.get('avg_flow_cfs', 0):.1f} cfs")
        print(f"   Head: {site['head_m']} m")

if __name__ == "__main__":
    main()