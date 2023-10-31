class FoodItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Burger(FoodItem):
    def __init__(self, name, price,condiments):
        super().__init__(name, price)
        self.condiments = condiments

class Drink(FoodItem):
    def __init__(self, name, price,size):
        super().__init__(name, price)
        self.size = size

class Side(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Combo(FoodItem):
    def __init__(self, burger,side,drink):
        self.burger = burger
        self.side = side
        self.drink = drink

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_order(self):
        print("Order for " + self.customer_name + ":")
        total_price = 0
        for item in self.items:
            print("- " + item.name + " - $" + str(round(item.price, 2)))
            total_price += item.price
        total_price = round(total_price, 2)
        print("Total: $" + str(total_price))

menu = {
    'Burger': Burger('Cheeseburger', 5.99, ['Cheese', 'Lettuce', 'Tomato']),
    'Drink': Drink('Soda', 1.99, 'Medium'),
    'Side': Side('Fries', 2.49),
    }   

def display_menu():
    print("Menu:")
    for category, item in menu.items():
        print(f"{category}: {item.name} - ${item.price:.2f}")
    print("Combo: Cheeseburger Combo (Burger, Fries, Medium Soda) - $9.99")


def take_order():
    print("Welcome to Burger Shop")
    print("Please enter your name:")
    customer_name = input()
    order = Order(customer_name)

    while True:
        display_menu()
        print("Enter the item you want to order (Burger/Drink/Side/Combo) or 'done' to finish:")
        item_choice = input().capitalize()

        if item_choice == 'Done':
            break

        if item_choice in menu:
            item = menu[item_choice]
            order.add_item(item)
            print(f"{item.name} has been added to your order.")
        elif item_choice == 'Combo':
            burger = menu['Burger']
            side = menu['Side']
            drink = menu['Drink']
            combo = Combo(burger, side, drink)
            order.add_item(combo)
            print(f"Cheeseburger Combo has been added to your order.")
        else:
            print("Sorry, we don't have that item. Please choose from the menu or 'done' to finish your order.")

    order.display_order()
    print("Thank you for your order!")
 

take_order()