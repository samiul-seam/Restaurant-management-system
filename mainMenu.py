from user import *
from admin import *
from restaurant import *
from customer import *
from fooditem import *

res = Restaurant("Mamar Restaurant")

def customer_menu():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone: ")
    address = input("Enter your Address: ")

    customer = Customer(name, phone, email, address)
    print(f"Welcome {customer.name} to our Restaurant")

    while True:
        print("\n1. View Menu\n2. Add To Cart\n3. View Your Cart\n4. Pay Bill\n5. Order history\n6. Exit")
        choice = (input("Enter your choice: "))

        if choice == '1':
            customer.view_menu(res)
        elif choice == '2':
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter quantity: "))
            customer.add_to_cart(res, item_name, item_quantity)
        elif choice == '3':
            customer.view_cart()
        elif choice == '4':
            customer.pay_bill(res)
        elif choice == '5':
            customer.view_order_history()
        elif choice == '6':
            break
        else:
            print("Invalid Input")

def admin_menu():
    name = input("Enter Admin Name: ")
    password = input("Enter Admin Password: ")

    admin = Admin(name, password)
    if not admin.is_valid_admin():
        print("You are not Admin")
        return

    print(f"Welcome {name} ")

    while True:
        print("\n1. Add New Employee\n2. View Employees\n3. Remove Employee\n4. Add New Item\n5. Delete Item\n6. View Menu\n7. Restock_item\n8. Sales_report\n9. Exit")
        choice = (input("Enter your choice: "))

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            designation = input("Designation: ")
            salary = int(input("Salary: "))
            emp = Employee(name, phone, email, address, designation, salary)
            admin.add_employee(res, emp)
        elif choice == '2':
            admin.view_employee(res)
        elif choice == '3':
            name = input("Enter Employee name: ")
            admin.remove_employee(res, name)
        elif choice == '4':
            item_name = input("Item name: ")
            item_price = int(input("Price: "))
            item_quantity = int(input("Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_food_item(res, item)
        elif choice == '5':
            item_name = input("Enter item name to remove: ")
            admin.remove_food_item(res, item_name)
        elif choice == '6':
            admin.view_menu(res)
        elif choice == '7':
            item_name = input("Item name: ")
            item_quantity = int(input("Quantity: "))
            admin.restock_item(res,item_name, item_quantity)
        elif choice == '8':
            admin.sales_report(res)
        elif choice == '9':
            break
        else:
            print("Please enter a valid number.")

while True:
    print("\n*** Welcome to Restaurant Management System ***")
    print("1. Admin\n2. Customer\n3. Exit")
    choice = (input("Enter your choice: "))

    if choice == '1':
        admin_menu()
    elif choice == '2':
        customer_menu()
    elif choice == '3':
        break
    else:
        print("Invalid Input")