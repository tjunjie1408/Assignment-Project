# driver_module.py

from utils import read_file, write_file

def update_driver_profile(driver_id, name, contact):
    """Updates driver profile details."""
    drivers = read_file("drivers.txt")
    updated = False
    for i, driver in enumerate(drivers):
        if driver[0] == driver_id:
            drivers[i] = [driver_id, name, contact]
            updated = True
            break
    if not updated:
        drivers.append([driver_id, name, contact])
    write_file("drivers.txt", drivers)
    print("Driver profile updated.")

def view_route(route_id):
    """Fetches and displays the route by ID."""
    routes = {
        "1": "Johor – Kuala Lumpur – Butterworth - Kedah – Perlis",
        "2": "Johor – Kuala Lumpur – Terengganu – Kelantan"
    }
    route = routes.get(route_id, "Unknown route")
    print(f"Route {route_id}: {route}")

def driver_menu():
    print("\nDriver Menu")
    print("1. Update Profile")
    print("2. View Route")
    choice = input("Select an option: ")
    if choice == "1":
        driver_id = input("Enter driver ID: ")
        name = input("Enter name: ")
        contact = input("Enter contact info: ")
        update_driver_profile(driver_id, name, contact)
    elif choice == "2":
        route_id = input("Enter route ID: ")
        view_route(route_id)
