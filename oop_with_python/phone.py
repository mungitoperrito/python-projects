from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity=0, broken=0):
        super().__init__(name, price, quantity)

        # Validate arguments
        assert broken >= 0, f"Broken {broken} is not valid"

        # Instance attributes
        self.broken = broken

        # Actions on init
