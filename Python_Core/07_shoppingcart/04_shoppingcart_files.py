# save the cart in the file
import os
# clear screen
def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")
shopping_list = []
cart_file = 'shoppingcart.txt'

# Add the items
def add_to_list(item):
    shopping_list.append(new_item)
    print(" Added ! List has {} items. ".format(len(shopping_list)))

# new funtion with SAVE and write to file
def save_cart_to_file(shopping_list,cart_file):
    with open(cart_file, 'w') as file:
        for item in shopping_list:
            file.write(f"{item}\n")
    print("cart saved to file")

# new funtion with load items in cart
def load_cart_from_file(cart_file):
    cart_items = []
    with open(cart_file, 'r') as file:
        cart_items = [line.strip() for line in file.readlines()]
    return cart_items


# Show the items
def show_list():
    #clear_screen()
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

while True:
    # input - customer is adding items
    new_item = input(" Enter your grocerry > ")
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'SAVE':
        save_cart_to_file(shopping_list, cart_file)
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
print(load_cart_from_file(cart_file))