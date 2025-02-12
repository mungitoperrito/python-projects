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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions on init
        Item.all.append(self)

    # Define a property rather than an attribute
    @property
    def name(self):
        # Double underscore makes the variable private
        return self.__name

    @property
    def price(self):
        # Double underscore makes the variable private
        return self.__price

    # This has to follow @ property definition
    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def calculate_discounted_price(self):
        return self.__price * (1 - self.discount)

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
               f"'{self.__name}'," + \
               f"{self.__price}," + \
               f"{self.quantity}" + \
               f")"
