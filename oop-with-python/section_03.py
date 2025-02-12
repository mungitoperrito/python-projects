### Class methods v static methods

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

    # Improve raw output when Item instances are printed
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


############
### MAIN ###
############

item_01 = Item("Phone", 100, 1)
item_02 = Item("Compu", 1000, 3)
item_03 = Item("Cable", 10, 5)
item_04 = Item("Mouse", 50, 5)
item_05 = Item("Keyboard", 75, 5)
