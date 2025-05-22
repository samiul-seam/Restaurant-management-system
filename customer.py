from user import *
from fooditem import *
from datetime import datetime

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = []
        self.order_history = []

    def add_to_cart(self, restaurant, name, quantity):
        item = restaurant.find_item(name)
        if item:
            if quantity > item.quantity:
                print("Item Quantity Exceeded :(")
            else:
                new_item = FoodItem(item.name, item.price, quantity)
                self.cart.append(new_item)
                item.quantity -= quantity
                print(f"{name} added successfully.")
        else:
            print("Item not found.")

    def total_price(self):
        return sum(item.price * item.quantity for item in self.cart)

    def view_menu(self, restaurant):
        restaurant.view_menu()

    def view_cart(self):
        for item in self.cart:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        print(f"Total price: {self.total_price()}")

    def pay_bill(self, restaurant):
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\n--- Receipt ---")
        for item in self.cart:
            print(f"{item.name}: {item.quantity} x {item.price} = {item.price * item.quantity}")
            original_item = restaurant.find_item(item.name)
            if original_item:
                original_item.total_sold += item.quantity
        print(f"Total Bill: {self.total_price()}")
        print("Thank you for your purchase!")
        print(f"Email sent to {self.email}: Your order has been placed.")
        self.order_history.append((datetime.now(), self.cart[:]))
        self.cart.clear()

    def view_order_history(self):
        for order_time, order in self.order_history:
            print(f"Order on {order_time}:")
            for item in order:
                print(f"  {item.name} x {item.quantity} = {item.price * item.quantity}")
