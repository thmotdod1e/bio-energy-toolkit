#!/usr/bin/env python3
"""
Bio-Energy Comparative Analysis Toolkit
Core calculation logic for comparing solar energy generation
vs. carbon sequestration via afforestation.
"""

import re
import os
import sys


def load_assumptions(file_path="ASSUMPTIONS.md"):
    """
    Parse ASSUMPTIONS.md and extract key numerical values.
    
    Returns a dictionary with the following keys:
      - 'solar_output_kwh_per_m2_year': float
      - 'co2_kg_per_tree_year': float
      - 'trees_per_hectare': float
      - 'trees_per_m2': float (derived)
    """
    assumptions = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        # If file not found, fall back to default values (should not happen)
        print(f"Warning: {file_path} not found, using default assumptions.", file=sys.stderr)
        assumptions['solar_output_kwh_per_m2_year'] = 180.0
        assumptions['co2_kg_per_tree_year'] = 22.0
        assumptions['trees_per_hectare'] = 1000.0
        assumptions['trees_per_m2'] = 0.1
        return assumptions
    
    # Pattern to match numbers inside backticks that are followed by units
    # Example: `180 kWh/m²/year`
    solar_pattern = r'`(\d+(?:,\d+)?)\s*kWh/m²/year`'
    co2_pattern = r'`(\d+(?:,\d+)?)\s*kg CO₂/tree/year`'
    density_pattern = r'`(\d+(?:,\d+)?)\s*trees/hectare`'
    
    solar_match = re.search(solar_pattern, content)
    if solar_match:
        value = solar_match.group(1).replace(',', '')
        assumptions['solar_output_kwh_per_m2_year'] = float(value)
    else:
        assumptions['solar_output_kwh_per_m2_year'] = 180.0
    
    co2_match = re.search(co2_pattern, content)
    if co2_match:
        value = co2_match.group(1).replace(',', '')
        assumptions['co2_kg_per_tree_year'] = float(value)
    else:
        assumptions['co2_kg_per_tree_year'] = 22.0
    
    density_match = re.search(density_pattern, content)
    if density_match:
        value = density_match.group(1).replace(',', '')
        assumptions['trees_per_hectare'] = float(value)
    else:
        assumptions['trees_per_hectare'] = 1000.0
    
    # Derive trees per square meter
    assumptions['trees_per_m2'] = assumptions['trees_per_hectare'] / 10000.0
    
    return assumptions


def calculate_solar_energy(area_m2, assumptions=None):
    """
    Calculate total annual energy output (kWh) for a given land area covered by solar panels.
    
    Parameters:
      area_m2 (float): Land area in square meters.
      assumptions (dict, optional): Assumptions dictionary as returned by load_assumptions().
                                    If None, loads assumptions from ASSUMPTIONS.md.
    
    Returns:
      float: Annual energy output in kWh.
    """
    if assumptions is None:
        assumptions = load_assumptions()
    
    solar_output = assumptions['solar_output_kwh_per_m2_year']
    return solar_output * area_m2


def calculate_co2_sequestration(area_m2, assumptions=None):
    """
    Calculate total annual CO2 sequestration (kg) for a given land area planted with trees.
    
    Parameters:
      area_m2 (float): Land area in square meters.
      assumptions (dict, optional): Assumptions dictionary as returned by load_assumptions().
                                    If None, loads assumptions from ASSUMPTIONS.md.
    
    Returns:
      float: Annual CO2 sequestration in kg.
    """
    if assumptions is None:
        assumptions = load_assumptions()
    
    trees_per_m2 = assumptions['trees_per_m2']
    co2_per_tree = assumptions['co2_kg_per_tree_year']
    
    total_trees = trees_per_m2 * area_m2
    return total_trees * co2_per_tree


def compare_land_use(area_m2):
    """
    Compute both solar energy output and CO2 sequestration for a given area.
    
    Parameters:
      area_m2 (float): Land area in square meters.
    
    Returns:
      dict: {
        'area_m2': area_m2,
        'solar_energy_kwh': float,
        'co2_sequestration_kg': float
      }
    """
    assumptions = load_assumptions()
    solar = calculate_solar_energy(area_m2, assumptions)
    co2 = calculate_co2_sequestration(area_m2, assumptions)
    
    return {
        'area_m2': area_m2,
        'solar_energy_kwh': solar,
        'co2_sequestration_kg': co2
    }


if __name__ == '__main__':
    # Simple test: compute for 1000 m² and print results
    result = compare_land_use(1000.0)
    print(f"Area: {result['area_m2']} m²")
    print(f"Solar energy output: {result['solar_energy_kwh']:.1f} kWh/year")
    print(f"CO₂ sequestration: {result['co2_sequestration_kg']:.1f} kg/year")
    print()
    
    # Show assumptions used
    assumptions = load_assumptions()
    print("Assumptions used:")
    print(f"  Solar output: {assumptions['solar_output_kwh_per_m2_year']} kWh/m²/year")
    print(f"  CO₂ per tree: {assumptions['co2_kg_per_tree_year']} kg/tree/year")
    print(f"  Tree density: {assumptions['trees_per_hectare']} trees/hectare")
    print(f"               = {assumptions['trees_per_m2']} trees/m²")