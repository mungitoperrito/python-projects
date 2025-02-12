### Intro to __init__

class Item:
    def __init__(self, name: str, price: float, quantity=0):

        # Validate arguemnts
        assert price > 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item_01 = Item("Phone", 100, 5)
item_02 = Item("Compu", 1000, 3 )
# item_03 = Item("FailPrice", -50, 3 )      # Uncomment to test assert
# item_04 = Item("FailQuantity", 50, -3 )   # Uncomment to test assert

print(item_01.calculate_total_price())
print(item_02.calculate_total_price())
