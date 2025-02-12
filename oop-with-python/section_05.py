### Inheritance

import csv


class Item:
    # Class attributes
    discount = 0.2      # price discount
    all = []            # list of all class instances

    def __init__(self, name: str, price: float, quantity=0):
        # Validate arguments
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"

        # Instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions on init
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_discounted_price(self):
        # Old method changed stored price
        # self.price = self.price * (1 - self.discount)

        return self.price * (1 - self.discount)

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
        # Should not return True for x.0
        if isinstance(number, float):
            return False
        elif isinstance(number, int):
            return True
        else:
            return False

    # Improve raw output when Item instances are printed
    def __repr__(self):
        # Use generic class name
        return f"{self.__class__.__name__}" + \
               f"(" + \
               f"'{self.name}'," + \
               f"{self.price}," + \
               f"{self.quantity}" + \
               f")"


class Phone(Item):
    all = []

    def __init__(self, name, price, quantity=0, broken=0):
        super().__init__(name, price, quantity)

        # Validate arguments
        assert broken >= 0, f"Broken {broken} is not valid"

        # Instance attributes
        self.broken = broken

        # Actions on init
        Phone.all.append(self)


############
### MAIN ###
############

# # Uncomment to initialize items
# Item.import_from_csv('items.csv')

if __name__ == "__main__":

    # # Uncomment to test is_integer static method
    # for value in [5, 5.0, 5.1]:
    #     print(f"{value}: {Item.is_integer(value)}")

    phone_01 = Phone("ABC Phone v10", 500, 4)
    phone_02 = Phone("ABC Phone v20", 750, 3)
    phone_01.broken = 1
    phone_02.broken = 2

    # # Uncomment to debug
    print(f"Item: \n{Item.all}")
    # print("\n")
    print(f"Phone: \n{Phone.all}")

    print(phone_02.calculate_total_price())