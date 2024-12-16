# backend/carbon_calculator.py

def calculate_emissions(electricity_kwh, car_mileage_km):
    # Emission factors (approximate)
    electricity_emission_factor = 0.233  # kg CO₂ per kWh
    car_emission_factor = 0.120  # kg CO

    # Calculate emissions
    electricity_emissions = electricity_kwh * electricity_emission_factor
    car_emissions = car_mileage_km * car_emission_factor

    # Total emissions
    total_emissions = electricity_emissions + car_emissions

    return total_emissions, electricity_emissions, car_emissions
