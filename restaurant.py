class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.items = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added successfully.")

    def remove_employee(self, employee_name):
        for em in self.employees:
            if em.name == employee_name:
                self.employees.remove(em)
                print(f"{employee_name} is removed successfully.")
                return
        print(f"{employee_name} not found.")

    def selection_sort_employees(self):                                  ## Selecton Sort Algorithm
        n = len(self.employees)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.employees[j].name < self.employees[min_idx].name:
                    min_idx = j
            if min_idx != i:
                self.employees[i], self.employees[min_idx] = self.employees[min_idx], self.employees[i]

    def view_employee(self):
        self.selection_sort_employees()
        print(f"name\tphone\t\taddress\tdesignation\tsalary\temail")
        for em in self.employees:
            print(f"{em.name}\t{em.phone}\t{em.address}\t{em.designation}\t\t{em.salary}\t{em.email}")
    
    def add_food_item(self, item_details):
        existing_item = self.find_item(item_details.name)
        if existing_item:
            print("Item already exists. Use restock option instead.")
        else:
            self.items.append(item_details)
            print(f"{item_details.name} is added successfully.")

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def remove_food_item(self, name):
        item = self.find_item(name)
        if item:
            self.items.remove(item)
            print(f"{name} is removed successfully.")
        else:
            print("Item is not found.")

    def insertion_sort_food_items(self):                                    ## Insertion Sort Algorithm
        for i in range(1, len(self.items)):
            key = self.items[i]
            j = i - 1
            while j >= 0 and self.items[j].name > key.name:
                self.items[j + 1] = self.items[j]
                j -= 1
            self.items[j + 1] = key

    def view_menu(self):
        self.insertion_sort_food_items()
        print("Food Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t\t{item.price}\t{item.quantity}")

    def restock_item(self, item_name, quantity):
        item = self.find_item(item_name)
        if item:
            item.quantity += quantity
            print(f"{item_name} restocked with {quantity} units.")
        else:
            print("Item not found.")

    def sales_report(self):
        total_revenue = sum(item.price * item.total_sold for item in self.items)
        print("--- Sales Report ---")
        print(f"Total Revenue: {total_revenue}")
        print("Top Selling Items:")
        for item in sorted(self.items, key=lambda x: x.total_sold, reverse=True):
            print(f"{item.name}: Sold {item.total_sold}")

