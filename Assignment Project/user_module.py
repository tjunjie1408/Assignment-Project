# user_module.py

from utils import append_file, read_file

def create_order(order_id, order_details):
    append_file("orders.txt", [order_id, order_details])
    print("Order created successfully.")

def track_order(order_id):
    orders = read_file("orders.txt")
    for order in orders:
        if order[0] == order_id:
            print("Order found:", order)
            return
    print("Order not found.")

def choose_vehicle(order_id, consignment_size):
    vehicle = "Van" if consignment_size == "small" else "Truck" if consignment_size == "bulk" else "Specialized Carrier"
    append_file("vehicles.txt", [order_id, consignment_size, vehicle])
    print(f"Vehicle chosen for Order {order_id}: {vehicle}")

def record_payment(order_id, payment_method):
    append_file("payments.txt", [order_id, payment_method])
    print(f"Payment recorded for Order {order_id}.")
    
def user_menu():
    print("\nUser Menu")
    print("1. Create Order")
    print("2. Track Order")
    print("3. Choose Vehicle")
    print("4. Make Payment")
    choice = input("Select an option: ")
    if choice == "1":
        order_id = input("Enter order ID: ")
        order_details = input("Enter order details: ")
        create_order(order_id, order_details)
    elif choice == "2":
        order_id = input("Enter order ID: ")
        track_order(order_id)
    elif choice == "3":
        order_id = input("Enter order ID: ")
        consignment_size = input("Enter consignment size (small, bulk, special): ")
        choose_vehicle(order_id, consignment_size)
    elif choice == "4":
        order_id = input("Enter order ID: ")
        payment_method = input("Enter payment method: ")
        record_payment(order_id, payment_method)
