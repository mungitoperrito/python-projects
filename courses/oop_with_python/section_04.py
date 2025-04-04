### Static methods

import csv

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


    # First paramter is class(cls)
    @classmethod
    def import_from_csv(cls, csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)             # Debug
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    # First paramter is neither instance(self) nor class(cls)
    @staticmethod
    def is_integer(number):
        # CAUTION: is_integer considers x.0 to be an int
        # if isinstance(number, float):
        #     return number.is_integer()
        # elif isinstance(number, int):
        #     return True
        # else:
        #     return False

        # Should not return True for x.0
        if isinstance(number, float):
            return False
        elif isinstance(number, int):
            return True
        else:
            return False


    # Improve raw output when Item instances are printed
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


############
### MAIN ###
############

Item.import_from_csv('items.csv')

# # Uncomment to debug
# print(Item.all)

# # Uncomment to debug
# for i in Item.all:
#     print(i)

if __name__ == "__main__":

    # Uncomment to test is_integer static method
    for value in [5, 5.0, 5.1]:
        print(f"{value}: {Item.is_integer(value)}")

