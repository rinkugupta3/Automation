# goal create a shopping cart

import os

# create an empty shopping cart
shopping_list = []


# clear screen
def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")


# Add the items
def add_to_list(item):
    shopping_list.append(new_item)
    # print(shopping_list)


# Show the items
def show_list():
    clear_screen()
    for item in shopping_list:
        print(item)


# remove the items
def remove_from_list():
    while True:
        show_list()
        what_to_remove = input("what would you like to remove? \n >")
        # to use some sort of error handling
        if what_to_remove.upper() == 'DONE':
            break
        try:
            shopping_list.remove(what_to_remove)
            print(f"{what_to_remove} has been removed from the list")
        except ValueError:
            raise ValueError(f"{what_to_remove} is not in the list")

        show_list()


# clear the cart
def clear_cart():
    shopping_list.clear()
    print("Cart cleared")


# Select the items untill you say your DONE or QUIT
# flow control
while True:
    # input - customer is adding items
    new_item = input(" Enter your grocerry > ")
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        try:
            remove_from_list()
        except ValueError as e:
            print(e)
    elif new_item.upper() == 'CLEAR':
        clear_cart()
    else:
        add_to_list(new_item)

show_list()
