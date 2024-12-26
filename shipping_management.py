def shipping_management_main():
    print("Welcome to the Shipping Management System")
    while True:
        print("\nFeatures Menu")
        print("1. User Main")
        print("2. Admin Main")
        print("3. Driver Main")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            user_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            driver_main()
        elif choice == "4":
            print("Thank you for using the Shipping Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

current_user = None #User feature

def get_next_order_number():
    user_order_file = f"{current_user}_order_history.txt"
    try:
        with open(user_order_file, "r") as file:
            lines = file.readlines()
            if not lines:
                return 1
            last_order = lines[-1]
            last_order_number = int(last_order.split("Order number: ")[-1].strip())
            return last_order_number + 1
    except FileNotFoundError:
        return 1

def make_order():
    size = int(input('Choose the consignment size:\n1. small parcel\n2. bulk order\n3. special cargo\nPlease enter the number(1-3):'))
    if size == 1:
        size = "small parcel"
    elif size == 2:
        size = "bulk order"
    elif size == 3:
        size = "special cargo"
    else:
        print('Invalid choice')
        user_menu()

    weight = int(input('Enter the weight of parcel(kg):'))
    if weight <= 10:
        weight = "Motorcycle"
    elif 10 < weight <= 50:
        weight = "Van"
    elif 50 < weight <= 100:
        weight = "Truck"
    else:
        print('Invalid choice')
        user_menu()

    package = int(input('Choose the package you want:\n1. Normal package\n2. Special package\n*Special package including liquid and glass.\nPlease enter the number(1/2):'))
    if package == 1:
        package = 'Normal package'
    elif package == 2:
        package = 'Special package'
    else:
        print('Invalid choice')
        user_menu()

    order_payment = int(input('Choose the payment method:\n1. credit/debit card\n2. UPI\n3. Mobile wallet\n4. Cash\n5. Other\nPlease enter the number(1-5):'))
    if 1 <= order_payment <= 5:
        order_payment = "Done payment"
    else:
        print('Invalid choice')
        user_menu()

    order_number = get_next_order_number()
    order = f"{order_payment} | {size}, {weight}, {package}. Order number: {order_number}"

    user_order_file = f"{current_user}_order_history.txt"
    with open(user_order_file, "a") as file:
        file.write(f"{order}\n")

    print(f"{order_payment}\nOrder checking: {size}, {weight}, {package}. This is order number {order_number}")
    user_menu()

def check_order():
    user_order_file = f"{current_user}_order_history.txt"
    try:
        with open(user_order_file, "r") as file:
            print("Your Order History:")
            print(file.read())
    except FileNotFoundError:
        print("No orders found.")
    user_menu()

def cancel_order():
    user_order_file = f"{current_user}_order_history.txt"
    try:
        with open(user_order_file, "r") as file:
            orders = file.readlines()
    except FileNotFoundError:
        print("No orders to cancel.")
        user_menu()

    if not orders:
        print("No orders to cancel.")
        user_menu()

    print("Your Order History:")
    for idx, order in enumerate(orders, start=1):
        print(f"{idx}. {order.strip()}")

    try:
        order_to_cancel = int(input("Enter the order number you want to cancel: "))
        order_found = False
        for order in orders:
            if f"Order number: {order_to_cancel}" in order:
                orders.remove(order)
                order_found = True
                break

        if order_found:
            with open(user_order_file, "w") as file:
                file.writelines(orders)
            print(f"Order number {order_to_cancel} canceled successfully.")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    user_menu()

def re_order():
    make_order()

def review():
    rating = int(input("Please rate from 1 to 5 stars:"))
    if 1 <= rating <= 5:
        print(f"Thank you for your rating of {rating} stars!")
    else:
        print("Please enter valid option.")

    command = input("Please share your command of our service:")
    words = command.split()

    if len(words) >= 100:
        print("Your command is too long. Please limit it in 100 words.")
    else:
        print("Thanks for your command!")

def exit():
    print("Thank you!")
    main()

def user_menu():
    menu = int(input("Order management:\n1-Make Orders\n2-Check Orders\n3-Cancel Orders\n4-Reorder\n5.Rating and Review\n6.Exit\nPlease enter the number: "))
    if menu == 1:
        make_order()
    elif menu == 2:
        check_order()
    elif menu == 3:
        cancel_order()
    elif menu == 4:
        re_order()
    elif menu == 5:
        review()
    elif menu == 6:
        exit()
    else:
        print("Please Choose A Valid Option.")

def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                existing_username, _ = user.strip().split(',')
                if existing_username == username:
                    print("Username already signed up. Try a different one.")
                    return
    except FileNotFoundError:
        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")
        print("Sign-up successful.")

def log_in():
    global current_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                existing_username, existing_password = user.strip().split(',')
                if existing_username == username and existing_password == password:
                    current_user = username
                    print("Login successful!")
                    user_menu()
                    return
            print("Invalid username or password.")
    except FileNotFoundError:
        print("No users found. Please sign up first.")

def main():
    while True:
        choice = input("Choose an option:\n1. Sign Up\n2. Log In\n3. Exit\nEnter your choice (1/2/3): ")
        if choice == '1':
            sign_up()
        elif choice == '2':
            log_in()
        elif choice == '3':
            print("Goodbye!")
            quit()
        else:
            print("Invalid choice. Please try again.")

# 图的初始化（代表不同地点之间的距离）
def load_graph_from_file(file_name):
    """Loads graph data from a specified file."""
    graph = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Ignore empty lines
                    start, end, distance = line.strip().split(',')
                    distance = float(distance)
                    if start not in graph:
                        graph[start] = {}
                    graph[start][end] = distance
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty graph.")
    return graph

# Load the graph from the file
graph = load_graph_from_file("routes.txt")

# 简单的Dijkstra算法（无需外部库）
def read_routes_from_txt(file_name):
    """Reads route information from a .txt file."""
    routes = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Ignore empty lines
                    parts = line.strip().split(',')
                    if len(parts) == 3:  # Ensure there are exactly 3 parts
                        start, end, distance = parts
                        if start not in routes:
                            routes[start] = {}
                        routes[start][end] = float(distance)
                    else:
                        print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty route list.")
    return routes

def write_route_to_txt(file_name, start, end, distance):
    """Appends a new route to the .txt file."""
    with open(file_name, 'a') as file:
        file.write(f"{start},{end},{distance}\n")

def add_route(file_name):
    """Adds a new route to the text file."""
    print("\n--- Add Route Information ---")
    start = input("Enter starting location: ").strip()
    end = input("Enter destination: ").strip()
    try:
        distance = float(input("Enter distance (in km): ").strip())
    except ValueError:
        print("Invalid distance. Please enter a numeric value.")
        return

    write_route_to_txt(file_name, start, end, distance)
    print(f"Route added: {start} -> {end} ({distance} km)")

def view_routes(file_name):
    """Displays all routes stored in the text file."""
    print("\n--- All Routes ---")
    routes = read_routes_from_txt(file_name)
    if not routes:
        print("No routes available.")
        return

    for start, destinations in routes.items():
        for end, distance in destinations.items():
            print(f"Start: {start}, End: {end}, Distance: {distance} km")

def dijkstra(graph, start, end):
    """Finds the shortest path using Dijkstra's algorithm."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    unvisited = set(graph.keys())

    while unvisited:
        current_node = min(
            (node for node in unvisited if node in distances),
            key=lambda node: distances[node],
            default=None
        )

        if current_node is None or distances[current_node] == float('inf'):
            break

        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in distances:  # Check if neighbor is in distances
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node

    path, current = [], end
    while current:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return distances[end], path

def route_and_fuel_management(file_name):
    """Manages routes and calculates costs."""
    print("\n--- Route and Fuel Management ---")
    routes = read_routes_from_txt(file_name)

    if not routes:
        print("No routes available. Please add routes first.")
        return

    start = input("Enter the start location: ").strip()
    end = input("Enter the destination location: ").strip()

    # Check if both start and end locations are in the graph
    if start not in routes or end not in routes:
        print("Invalid locations entered. Please try again.")
        return

    # Proceed with Dijkstra's algorithm if locations are valid
    distance, path = dijkstra(routes, start, end)
    if distance == float('inf'):
        print(f"No route found from {start} to {end}.")
    else:
        print(f"Shortest distance: {distance} km")
        print(f"Path: {' -> '.join(path)}")

# Admin menu
FILE_NAME = "routes.txt"

# Constants
FUEL_PRICE = 2.15
SPECIAL_GOODS_EXTRA_PERCENTAGE = 1.2
SPECIAL_GOODS_TYPES = ["normal", "fragile", "hazardous", "perishable"]

# Vehicle prices
vehicle_prices = {
    "Motorcycle": 2.0,  # Price per km for normal goods
    "Van": 5.0,
    "Truck": 8.0
}

# Choose vehicle based on weight
def choose_vehicle_by_weight(weight):
    if weight <= 10:
        return "Motorcycle", vehicle_prices["Motorcycle"]
    elif 10 < weight <= 100:
        return "Van", vehicle_prices["Van"]
    else:
        return "Truck", vehicle_prices["Truck"]

# Fuel and Transport Cost Calculation
def calculate_fuel_cost(distance, vehicle_type):
    """Calculate fuel used and cost based on distance and vehicle type."""
    fuel_efficiency_mapping = {
        "Motorcycle": 35,
        "Van": 15,
        "Truck": 8
    }
    fuel_efficiency = fuel_efficiency_mapping.get(vehicle_type, 0)
    if fuel_efficiency == 0:
        raise ValueError("Invalid vehicle type for fuel efficiency calculation.")
    
    fuel_used = distance / fuel_efficiency
    fuel_cost = fuel_used * FUEL_PRICE
    return fuel_used, fuel_cost

def calculate_transport_cost(distance, price_per_km):
    """Calculate transport cost based on distance and price per kilometer."""
    return distance * price_per_km

def validate_cargo_type(cargo_type):
    """Validate the cargo type input."""
    if cargo_type not in SPECIAL_GOODS_TYPES:
        raise ValueError("Invalid cargo type. Please enter one of the following: " + ", ".join(SPECIAL_GOODS_TYPES))

# Route and Cost Calculation
def route_and_cost_calculation():
    """Prompt user for route details and calculate costs."""
    print("\n--- Route and Cost Calculation ---")
    start = input("Enter the start location: ").strip()
    end = input("Enter the destination location: ").strip()
    
    # Validate distance input
    try:
        distance = float(input("Enter the distance (in km): "))
    except ValueError:
        print("Invalid distance. Please enter a numeric value.")
        return

    # Validate weight input
    try:
        weight = float(input("Enter the weight of the shipment (in kg): "))
    except ValueError:
        print("Invalid weight. Please enter a numeric value.")
        return

    # Validate cargo type input
    cargo_type = input("Enter the type of cargo (normal, fragile, hazardous, perishable): ").strip().lower()
    try:
        validate_cargo_type(cargo_type)
    except ValueError as e:
        print(e)
        return

    # Choose vehicle
    vehicle_type, price_per_km = choose_vehicle_by_weight(weight)

    # Special goods surcharge
    if cargo_type in SPECIAL_GOODS_TYPES:
        price_per_km *= SPECIAL_GOODS_EXTRA_PERCENTAGE

    # Calculate fuel and transport costs
    fuel_used, fuel_cost = calculate_fuel_cost(distance, vehicle_type)
    transport_cost = calculate_transport_cost(distance, price_per_km)

    # Output results
    print(f"\nRoute: {start} -> {end}")
    print(f"Distance: {distance} km")
    print(f"Vehicle: {vehicle_type}")
    print(f"Fuel Used: {fuel_used:.2f} liters")
    print(f"Fuel Cost: RM{fuel_cost:.2f}")
    print(f"Transport Cost: RM{transport_cost:.2f}")

vehicles = {}

def load_vehicles_from_file(file_name):
    """Load vehicles from a text file."""
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Ignore empty lines
                    vehicle_id, vehicle_type, performance_rating, inspection_due = line.strip().split(',')
                    vehicles[vehicle_id] = {
                        "type": vehicle_type,
                        "performance_rating": float(performance_rating),
                        "maintenance_history": [],
                        "inspection_due": inspection_due.lower() == 'true'
                    }
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty fleet.")
    except Exception as e:
        print(f"Error reading file '{file_name}': {e}")

def save_vehicles_to_file(file_name):
    """Save vehicles to a text file."""
    with open(file_name, 'w') as file:
        for vehicle_id, details in vehicles.items():
            inspection_due = 'true' if details["inspection_due"] else 'false'
            file.write(f"{vehicle_id},{details['type']},{details['performance_rating']},{inspection_due}\n")

def add_vehicle(vehicle_id, vehicle_type, performance_rating):
    """Add a new vehicle to the fleet."""
    if vehicle_id in vehicles:
        print("Vehicle ID already exists.")
    else:
        vehicles[vehicle_id] = {
            "type": vehicle_type,
            "performance_rating": performance_rating,
            "maintenance_history": [],
            "inspection_due": False
        }
        print(f"Vehicle {vehicle_id} added successfully.")

def log_vehicle_maintenance(vehicle_id, date, description):
    """Log maintenance for a specific vehicle."""
    if vehicle_id in vehicles:
        vehicles[vehicle_id]["maintenance_history"].append((date, description))
        print(f"Maintenance logged for vehicle {vehicle_id}.")
    else:
        print("Vehicle ID not found.")

def set_inspection_alert(vehicle_id, due):
    """Set inspection alert for a specific vehicle."""
    if vehicle_id in vehicles:
        vehicles[vehicle_id]["inspection_due"] = due
        print(f"Inspection alert set for vehicle {vehicle_id}.")
    else:
        print("Vehicle ID not found.")

def view_vehicle_performance(vehicle_id):
    """View performance and maintenance history of a specific vehicle."""
    if vehicle_id in vehicles:
        vehicle = vehicles[vehicle_id]
        print(f"Vehicle ID: {vehicle_id}")
        print(f"Vehicle Type: {vehicle['type']}")
        print(f"Performance Rating: {vehicle['performance_rating']}")
        print("Maintenance History:")
        for date, description in vehicle["maintenance_history"]:
            print(f" - {date}: {description}")
        print(f"Inspection Due: {'Yes' if vehicle['inspection_due'] else 'No'}")
    else:
        print("Vehicle ID not found.")

def view_all_vehicles():
    """View all vehicles in the fleet."""
    if not vehicles:
        print("No vehicles in the fleet.")
    else:
        for vehicle_id in vehicles:
            view_vehicle_performance(vehicle_id)
            print("-" * 30)

# Load routes from a file
def load_graph_from_file(file_name):
    """Loads graph data from a specified file."""
    graph = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Ignore empty lines
                    start, end, distance = line.strip().split(',')
                    distance = float(distance)
                    if start not in graph:
                        graph[start] = {}
                    graph[start][end] = distance
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty graph.")
    return graph

# Load the graph from the file
graph = load_graph_from_file("routes.txt")

# Admin menu
def admin_menu():
    VEHICLE_FILE_NAME = "vehicles.txt"
    ROUTE_FILE_NAME = "routes.txt"
    
    # Load vehicles from file at the start of the admin menu
    load_vehicles_from_file(VEHICLE_FILE_NAME)

    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Vehicle")
        print("2. Log Vehicle Maintenance")
        print("3. Set Inspection Alert")
        print("4. View Vehicle Performance")
        print("5. View All Vehicles")
        print("6. Add Route Information")
        print("7. View All Routes")
        print("8. Route and Fuel Management")
        print("9. Route and Cost Calculation")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            vehicle_id = input("Enter Vehicle ID: ").strip()
            vehicle_type = input("Enter Vehicle Type: ").strip()
            performance_rating = float(input("Enter Performance Rating: "))
            add_vehicle(vehicle_id, vehicle_type, performance_rating)
        elif choice == '2':
            vehicle_id = input("Enter Vehicle ID: ").strip()
            date = input("Enter Maintenance Date (YYYY-MM-DD): ").strip()
            description = input("Enter Maintenance Description: ").strip()
            log_vehicle_maintenance(vehicle_id, date, description)
        elif choice == '3':
            vehicle_id = input("Enter Vehicle ID: ").strip()
            due = input("Is inspection due? (yes/no): ").strip().lower() == 'yes'
            set_inspection_alert(vehicle_id, due)
        elif choice == '4':
            vehicle_id = input("Enter Vehicle ID: ").strip()
            view_vehicle_performance(vehicle_id)
        elif choice == '5':
            view_all_vehicles()
        elif choice == '6':
            add_route(ROUTE_FILE_NAME)
        elif choice == '7':
            view_routes(ROUTE_FILE_NAME)
        elif choice == '8':
            route_and_fuel_management(ROUTE_FILE_NAME)
        elif choice == '9':
            route_and_cost_calculation()
        elif choice == '10':
            # Save vehicles to file before exiting
            save_vehicles_to_file(VEHICLE_FILE_NAME)
            print("\nExiting Admin Menu. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Driver Management System

drivers = {}

def read_file(file_name):
    """Read data from a text file and return as a list of lists."""
    data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip():  # Ignore empty lines
                    data.append(line.strip().split(','))
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return data

def write_file(file_name, data): # Write data to a text file
    with open(file_name, 'w') as file:
        for entry in data:
            file.write(','.join(entry) + '\n')

def append_file(file_name, new_entry): # Append data to a text file
    with open(file_name, 'a') as file:
        file.write(','.join(new_entry) + '\n')

def driver_main():
    print("Welcome to the Driver Management System")

    while True:
        print("\nMain Menu")
        print("1. Driver Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            driver_id = driver_login()
            if driver_id:
                driver_menu(driver_id)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def driver_login():
    while True:
        print("\nDriver Login")
        print("1. Login")
        print("2. Create New Profile")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            profiles = read_file('drivers.txt')
            driver_id = input("Enter your Driver ID: ")

            for profile in profiles:
                if profile[0] == driver_id:
                    print(f"Welcome, {profile[1]}!")
                    return driver_id
            print("Invalid Driver ID. Please try again.")
        elif choice == '2':
            add_new_profile()
        elif choice == '3':
            print("Exiting login system.")
            return None
        else:
            print("Invalid choice. Please try again.")

def driver_menu(driver_id):
    while True:
        print("\nDriver Main Menu")
        print("1. Profile Management")
        print("2. Delivery Management")
        print("3. Route Management")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            profile_menu(driver_id)
        elif choice == '2':
            delivery_menu(driver_id)
        elif choice == '3':
            route_menu(driver_id)
        elif choice == '4':
            print("Exiting Driver Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def profile_menu(driver_id):
    while True:
        print("\nProfile Management Menu")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_profile(driver_id)
        elif choice == '2':
            update_profile(driver_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def delivery_menu(driver_id):
    while True:
        print("\nDelivery Management Menu")
        print("1. View Delivery Details")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_delivery_details(driver_id)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def route_menu(driver_id):
    while True:
        print("\nRoute Management Menu")
        print("1. View Pre-Planned and Best Route")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_best_route(driver_id)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def view_profile(driver_id):
    profiles = read_file('drivers.txt')

    for profile in profiles:
        if profile[0] == driver_id:
            print("\nDriver Profile:")
            print(f"Name: {profile[1]}")
            print(f"Contact: {profile[2]}")
            print(f"Address: {profile[3]}")
            print(f"Availability: {profile[4]}")
            print(f"License: {profile[5]}")
            print(f"Health Report: {profile[6]}")
            return
    print("Profile not found.")

def update_profile(driver_id):
    profiles = read_file('drivers.txt')

    for i, profile in enumerate(profiles):
        if profile[0] == driver_id:
            print("\nCurrent Profile Details:")
            print(f"1. Name: {profile[1]}")
            print(f"2. Contact: {profile[2]}")
            print(f"3. Address: {profile[3]}")
            print(f"4. Availability: {profile[4]}")
            print(f"5. License: {profile[5]}")
            print(f"6. Health Report: {profile[6]}")

            field_to_update = input("Enter the number of the field you want to update: ")
            if field_to_update in ['1', '2', '3', '4', '5', '6']:
                new_value = input("Enter the new value: ")
                profile[int(field_to_update)] = new_value
                profiles[i] = profile
                write_file('drivers.txt', profiles)
                print("Profile updated successfully.")
                return
            else:
                print("Invalid choice. Returning to menu.")
                return
    print("Profile not found.")

def view_delivery_details(driver_id):
    deliveries = read_file('deliveries.txt')

    print("\nDelivery Details:")
    found = False
    for delivery in deliveries:
        if delivery[0] == driver_id:
            print(f"Delivery ID: {delivery[1]}, Status: {delivery[2]}, Route: {delivery[3]}, Schedule: {delivery[4]}")
            found = True
    if not found:
        print("No delivery details found.")

def add_new_profile():
    profiles = read_file('drivers.txt')
    print("\nEnter New Profile Details:")
    driver_id = input("Driver ID: ")
    if any(profile[0] == driver_id for profile in profiles):
        print("Driver ID already exists. Cannot add duplicate profile.")
        return

    name = input("Name: ")
    contact = input("Contact: ")
    address = input("Address: ")
    availability = input("Availability (Yes/No): ")
    license = input("License: ")
    health_report = input("Health Report: ")

    new_profile = [driver_id, name, contact, address, availability, license, health_report]
    append_file('drivers.txt', new_profile)
    print("New profile added successfully.")

def view_consignment_details(driver_id):
    consignments = read_file('consignments.txt')
    print("\nConsignment/Shipment Details:")
    found = False
    for consignment in consignments:
        if consignment[0] == driver_id:
            print(
                f"Package: {consignment[1]}, Weight: {consignment[2]}, Special Requirements: {consignment[3]}, Freight: {consignment[4]}, Time Duration: {consignment[5]}")
            found = True
    if not found:
        print("No consignment details found.")

def view_best_route(driver_id):
    routes = read_file('routes.txt')

    print("\nPre-Planned and Best Route:")
    found = False
    for route in routes:
        if route[0] == driver_id:
            print(f"Route ID: {route[1]}, Route: {route[2]}, Fuel Efficiency: {route[3]}, Time Efficiency: {route[4]}")
            found = True

    if not found:
        print("No route details found.")

# Start the admin menu
shipping_management_main()