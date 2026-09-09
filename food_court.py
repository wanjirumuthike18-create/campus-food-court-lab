class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_order(self):
        print("----- ORDER -----")
        print(f"Customer: {self.customer.name}")
        for item in self.items:
            print(f"{item.name} - KSh {item.price}")
        print(f"Total: KSh {self.calculate_total()}")


burger = MenuItem("Burger", 350)
pizza = MenuItem("Pizza", 500)
fries = MenuItem("Fries", 150)
milkshake = MenuItem("Milkshake", 200)

customer1 = Customer("Kevin")
order1 = Order(customer1)
order1.add_item(burger)
order1.add_item(fries)
order1.add_item(milkshake)
order1.show_order()

