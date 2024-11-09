# main.py

import user_module
import driver_module
import admin_module

def main():
    print("Welcome to Shipment Management System")
    while True:
        print("\n1. User\n2. Driver\n3. Admin\n4. Exit")
        role = input("Choose your role: ")
        if role == "1":
            user_module.user_menu()
        elif role == "2":
            driver_module.driver_menu()
        elif role == "3":
            admin_module.admin_menu()
        elif role == "4":
            print("Exiting program.")
            break

main()
