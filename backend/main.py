from carbon_calculator import calculate_emissions

def get_user_input():
    electricity = float(input("Enter electricity usage in kWh: "))
    mileage = float(input("Enter car mileage in km: "))
    return electricity, mileage

def display_results(elec_emissions,car_emissions,total):
    print(f"Electricity Emissions: {elec_emissions:.2f} kg CO₂")
    print(f"Car Emissions: {car_emissions:.2f} kg CO₂")
    print(f"Total Carbon Footprint: {total:.2f} kg CO₂")
    
if __name__ == "__main__":
    electricity,mileage = get_user_input()
    total, elec_emissions,car_emissions = calculate_emissions(electricity,mileage)
    display_results(total,elec_emissions,car_emissions)