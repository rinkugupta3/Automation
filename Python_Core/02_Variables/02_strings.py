# String is a data type used in programming, that is used to represent text rather than numbers.
# Srring is the list of characters or sequence of characters
# String funtions - capitalize, upper, range, len, split

# Notation of list []
# In below 'my_name' is variable
# Index position 0 1 2 3 4 5 6 7

my_name = ['D', 'h', 'i', 'r', 'a', 'j']
another_name = 'Gupta'

print(my_name[0])
print(another_name[0])

message1 = "Hello Python World"
message2 = message1

print(message2)

message1 = 'Hello Python'
print(message1)
print(message2)

# Don't start with double quotation

m3 = 'I told my friend, "Python is my fav lang"'
m4 = "One of Python's strenght is , IT's easy"
print(m3)
print(m4)

# Immutable nature

# String is an object -  have funtions

my_string = 'dhiraj'
print(my_string.capitalize())
print(my_string.upper())
print(len(my_string))

print(my_string[0:3])  # range: including the beginning and the end index
print(my_string[2:])  # start and end inside []
print(my_string[-3:])

# intract with the terminal is by using an input funtions return string, if want to return number and then use type

what_is_name = input('Enter your name: ')
# print("Extracting the value-------->", what_is_name.capitalize())
# what_is_age = int (input('Enter your age: '))
what_is_age = input('Enter your age: ')  # string
age_int = int(what_is_age)  # int

# what_is_age = input('Enter your age: ')
# print("Extracting the age value---->", type(what_is_age))

# My age is ---- and my name is ------
# print("My age is" + what_is_age + "and my name is " + what_is_name)

# string formating
print("My age is {1} and my name is {0}".format(what_is_name.capitalize(), what_is_age))

# %d = used for integer
# %s = used for string

print("using %d and %s ", "My age is %d and my name is %s" % (age_int, what_is_name,))

# f string formating
print('using f-string ----->', f"My age is {age_int} and my name is {what_is_name}")

bill = 23.6666
print("Total : ${:.2f}".format(bill))

# csv = comma seperated values

names_class = 'sekhar,john,jack,jim'
print(names_class)

# split with comma delimater
print(names_class.split(','))

# find lenght total
print(len(names_class.split(',')))

print(names_class.split(',')[0])
print(names_class.split(',')[1])
print(names_class.split(',')[2])
print(names_class.split(',')[3])

# string are immutable in nature
# Function = replace

my_name = 'dhiraj'
# my_name[0] = "M"
print(my_name)

new_string = "M" + my_name[1:]
print(new_string)

# search in the string

my_search = "today is the second day of python class"
my_index_loc = my_search.find("python")
print("search found --->", my_search[my_index_loc:33])
print(my_index_loc)
# will find total character upto find character

# string1 = 'Hello World' and replace H with J
# Example1
test = 'Hello World'
print(test)
new_test = "J" + test[1:]
print(new_test)

# Example2
string1 = 'Hello World'
print(string1.replace("H", "J"))


# Example3
def replace_letter(word, target_letter, replacement_letter):
    return word.replace(target_letter, replacement_letter)


word = "banana"
target_letter = "a"
replacement_letter = "i"
new_word = replace_letter(word, target_letter, replacement_letter)
print(new_word)
