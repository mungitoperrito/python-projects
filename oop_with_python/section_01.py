# ### Initial pass
# class Item:
#     pass

# item_01 = Item()
# item_01.name = "Phone"
# item_01.price = 100
# item_01.quantity = 5

# print(type(item_01))

# Create a method
class Item:
    def calculate_total_price(self, item, price):
        return item * price

item_01 = Item()
item_01.name = "Phone"
item_01.price = 100
item_01.quantity = 5

print(item_01.calculate_total_price(item_01.price, item_01.quantity))

item_02 = Item()
item_02.name = "Compu"
item_02.price = 1000
item_02.quantity = 3

print(item_02.calculate_total_price(item_02.price, item_02.quantity))
