from restaurant import *

class Admin:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def is_valid_admin(self):
        return self.__name == "admin" and self.__password == '1234'

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def remove_employee(self, restaurant, name):
        restaurant.remove_employee(name)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_food_item(self, restaurant, item_details):
        restaurant.add_food_item(item_details)

    def remove_food_item(self, restaurant, item_name):
        restaurant.remove_food_item(item_name)

    def view_menu(self, restaurant):
        restaurant.view_menu()

    def restock_item(self, restaurant, item_name, quantity):
        restaurant.restock_item(item_name, quantity)

    def sales_report(self, restaurant):
        restaurant.sales_report()