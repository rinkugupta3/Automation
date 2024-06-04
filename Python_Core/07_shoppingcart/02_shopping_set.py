# goal create a shopping cart
# no duplicates - Set

import os


# create an empty shopping cart


# clear screen
def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")


# Add the items
def add_to_list(cart, item):
    cart.add(item)
    # print(shopping_list)


# Show the items
def show_list(cart):
    clear_screen()
    for item in cart:
        print(item)


# remove the items
def remove_from_list(shopping_list):
    show_list(shopping_list)
    what_to_remove = input("what would you like to remove? \n >")
    # to use some sort of error handling
    try:
        shopping_list.discard(what_to_remove)
    except ValueError:
        pass

    show_list(shopping_list)


# clear the cart


# Select the items untill you say your DONE or QUIT
# flow control
def main():
    shopping_list = set()
    while True:
        # input - customer is adding items
        new_item = input(" Enter your grocerry > ")
        if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
            break
        elif new_item.upper() == 'SHOW':
            show_list(shopping_list)
            continue
        elif new_item.upper() == 'REMOVE':
            remove_from_list(shopping_list)

        else:
            add_to_list(shopping_list, new_item)

    show_list(shopping_list)


if __name__ == "__main__":
    main()