### refactor, getter and setters

from item import Item
from phone import Phone

############
### MAIN ###
############

if __name__ == "__main__":

    # # Uncomment to initialize items
    # Item.import_from_csv('items.csv')

    phone_01 = Phone("ABC Phone v10", 500, 4)
    phone_02 = Phone("ABC Phone v20", 750, 3)
    phone_01.broken = 1
    phone_02.broken = 2

    # # Uncomment to debug
    print(f"Item: \n{Item.all}")
    # print("\n")
    print(f"Phone: \n{Phone.all}")
