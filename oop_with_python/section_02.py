### Intro to __init__

class Item:
    # Class attributes
    discount = 0.2      # price discount
    all = []            # list of all class instances

    def __init__(self, name: str, price: float, quantity=0):
        # Validate arguments
        assert price > 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

        # Instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions on init
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * (1 - self.discount)
        # Use self.discount instead of Item.discount so individual
        #    instances can override the value

    # Improve raw output when Item instances are printed
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        # Before
        # <__main__.Item object at 0x000001D453607050>
        # After
        # Item('Phone', 100, 1)

item_01 = Item("Phone", 100, 1)
item_02 = Item("Compu", 1000, 3)
item_03 = Item("Cable", 10, 5)
item_04 = Item("Mouse", 50, 5)
item_05 = Item("Keyboard", 75, 5)

# # Uncomment to see list of all instances (before __repr__)
# for i in Item.all:
#     print(i.name)

# Uncomment to see list of all instances
print(Item.all)

# # Uncomment to test asserts
# item_03 = Item("FailPrice", -50, 3 )
# item_04 = Item("FailQuantity", 50, -3 )

# # Uncomment to show class variable
# print(Item.discount)

# # Uncomment to show method working
# print(item_01.calculate_total_price())
# print(item_02.calculate_total_price())

# # Uncomment to show all variables
# print(Item.__dict__)            # Class level
# print(item_01.__dict__)         # Instance level

# # # Uncomment to overide class variable on instance level
# remember_price_01 = item_01.price
# item_01.apply_discount()
# print(item_01.calculate_total_price())

# item_01.price = remember_price_01
# item_01.discount = 0.5
# item_01.apply_discount()
# print(item_01.calculate_total_price())

# remember_price_02 = item_02.price
# item_02.apply_discount()
# print(item_02.calculate_total_price())

# item_02.price = remember_price_02
# item_02.apply_discount()
# print(item_02.calculate_total_price())
