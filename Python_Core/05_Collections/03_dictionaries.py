# dictionaries allow you to store and reterive data using key value pairs
# unordered
# key have to be unique
# can store different data types
# using {} curly braces
# add items to dictionaries
# remove items from dictionaries
# update items from dictionaries
# loop items
# check
# Get method >>>> help to reterive values
# dictionary inside a dictionary
# list of values

dict1 = {
    'color' : 'green',
    'points' : 5
}
print(dict1)
for i in dict1:
    print(i)

# accessing values
print(dict1['color'])

# add items to dictionaries
dict1['name'] = 'Dhiraj'
print(dict1)

# remove items from dictionaries
del dict1['points']
print(dict1)


# loop items
user = {
    'name' : 'Dhiraj',
    'age' : '47',
    'city' : 'Edison',
}

for k,v in user.items():
     print('Key: ' , k)
     print('Value: ' , v)

for v in user.values():
    print('Values--->: ' , v)

# check
if 'school' in user:
    print(user['School'])
else:
    print('key not found')

# Get method >>>> help to reterive values
school_value = user.get('school', 'key not found')
print(school_value)

# update items from dictionaries
user['name'] = 'Mike'
print(user)

# dictionary inside a dictionary
students = {
    'dhiraj' : {
        'python' : 88,
        'Tableau' : 75
    },
'mike' : {
        'python' : 88,
        'Tableau' : 75
    }
}

for student_name, marks in students.items():
    print("Student Name : ", student_name)

# For Tabing use \t
    py_mark = marks['python']
    tb_mark = marks['Tableau']
    print("\tPython marks:",py_mark)
    print("\tTableau marks:", py_mark)

# list of values
fav_books = {
    'dhiraj' : ['python', 'machine_learning', 'neural_networks'],
    'samantha' : ['Tableau', 'respberry pi'],
    'mike' : ['java', 'oracle']
}
for student_name, books in fav_books.items():
    print("Student Name : ", student_name.title())

    for book in books:
        print("\tFavourite Books:", book)