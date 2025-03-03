### oop principles

from item import Item
from phone import Phone

############
### MAIN ###
############

if __name__ == "__main__":

    # Uncomment to initialize items
    Item.import_from_csv('items.csv')

    item_01 = Item("New thing", 750)
    print(item_01.name)

    # Uncomment to debug
    print(f"Item: {Item.all}")


