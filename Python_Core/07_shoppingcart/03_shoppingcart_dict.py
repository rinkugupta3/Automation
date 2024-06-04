# Dictonary
# add same items more

shopping_list = {}
product_name = input(" Enter your product name: ")
quantity = int(input(" Enter quantity: "))
price = float(input(" Enter price: "))

'''
{
    'Apple': {'quantity':10, 'price':0.5},
    'Banana': {'quantity':5, 'price':1}
}
'''

# add to cart
def add_to_list(item, quantity,price):
    if item in shopping_list:
        shopping_list[item] ['quantity'] += quantity
    else:
        shopping_list[item] = {'quantity':quantity, 'price':price}


# calculate the total price
def cal_total_price():
    total_price = 0
    for items, data in shopping_list.items():
        quantity = data['quantity']
        price = data['price']
        total_price += quantity * price
    return total_price

add_to_list(product_name, quantity, price)

for items, data in shopping_list.items():
    quantity = data['quantity']
    price = data['price']

    print(f"{items} : {quantity} * {price}")

total_price = cal_total_price()
print(total_price)