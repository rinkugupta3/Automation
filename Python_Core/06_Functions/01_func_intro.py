#Funtion
#    - Function is a block of reusable code - does a specific task
#    - Organize code into logical units - easy to read, manage and understand
#    - def key work >>>> funtion_name ():
#    - Funtion can accept parameters
#    - Function can also return values
# Function can set default values
# (*args = positional args)
# double args **kwargs = keyword args = takes the keyword and the values

def greet(name):
    print("Hello, ", name)

greet('Dhiraj')
greet('Mike')

# function can also return values
def add_numbers(a,b):
    return a + b
results = add_numbers(2,3)
print(results)

def add_numbers_new(a,b):
    return a + b
results = add_numbers_new(2,3)
print(results)

# Function can set default values
def add_numbers_new(a,b = 2):
    return a + b
results = add_numbers_new(2)
print(results)

# (*args = positional args)
def add_numbers_args(*args):
    return sum(args)
print(add_numbers_args(2,3,5))
print(add_numbers_args(20,30,50,12,23))

# double args **kwargs = keyword args = takes the keyword and the values
# good while working in shopping cart
def add_num_kwargs(**kwargs):
    total = 0
    for num in kwargs.values():
        total = total + num
    return total
print(add_num_kwargs(app=5,ban=2,car=4))