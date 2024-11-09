# admin_module.py

from utils import read_file, write_file

def manage_vehicle(vehicle_id, status):
    """Updates the status of a vehicle in the system."""
    vehicles = read_file("vehicles.txt")
    updated = False
    for i, vehicle in enumerate(vehicles):
        if vehicle[0] == vehicle_id:
            vehicles[i] = [vehicle_id, status]
            updated = True
            break
    if not updated:
        vehicles.append([vehicle_id, status])
    write_file("vehicles.txt", vehicles)
    print("Vehicle status updated.")

def generate_report():
    """Generates a summary report based on all records."""
    print("\n--- Report Summary ---")
    print("Orders:")
    for order in read_file("orders.txt"):
        print(", ".join(order))
    print("\nVehicles:")
    for vehicle in read_file("vehicles.txt"):
        print(", ".join(vehicle))
    print("\nDrivers:")
    for driver in read_file("drivers.txt"):
        print(", ".join(driver))
    print("----------------------")

def admin_menu():
    print("\nAdmin Menu")
    print("1. Manage Vehicle")
    print("2. Generate Report")
    choice = input("Select an option: ")
    if choice == "1":
        vehicle_id = input("Enter vehicle ID: ")
        status = input("Enter status: ")
        manage_vehicle(vehicle_id, status)
    elif choice == "2":
        generate_report()
