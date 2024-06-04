# Append, extend, copy, insert
# list is a mutable (modify the contents after creation) sequence of the objects
# ordered collection of items, place different data types
# List has serval built in methods,
# allows duplicates

# basic list
l1 = [1,2,3]
#print (len(l1))

l2 = [3,4,5]
l3 = l1 + l2
print (l3)

# repetition
l4 = ['dhiraj'] * 4
print (l4)

# list is sequence of characters
print(list("dhiraj gupta"))

l5 = [1,2,34] + list('34')
print(l5)

# title will change first letter to upper case
bicycles = ['trek', 'street', 'mountain', 'specialized']
print(bicycles[0].title())

# last item in the list = -1
print(bicycles[-1].title())

# range of items start:number of items
print(bicycles[0:3])

# update or modify list
bicycles [3] = 'extraordinary'
print(bicycles[0:4])

# add to the list then use append()
bicycles2 = ['trek', 'street', 'mountain', 'specialized']
bicycles2.append('extraordinary')
print(bicycles2[0:5])

bikes = []
bikes.append('yamaha')
bikes.append('bmw')
bikes.append('suziki')
print(bikes)

# extend - to add two more items
bikes.extend(['tesla', 'nissan'])

# add items at a particular position - insert
bikes.insert(0,'honda')
print(bikes)

# delete use del statement and this is based on index
del bikes [0]
print(bikes)

# remove method remove() you can pass the items from the list
bikes.remove('yamaha')
print(bikes)

# pop
bicycles2 = ['trek', 'street', 'mountain', 'specialized']
popped_bicycles = bicycles2.pop(2)
print(popped_bicycles)
print(bicycles2)

# organize the list - sort() - default is False
bicycles3 = ['trek', 'street', 'mountain', 'specialized']
bicycles3.sort(reverse=False)
print(bicycles3)

# temp sorting - sorted()
bicycles4 = ['trek', 'street', 'mountain', 'specialized']
print("original list--->", bicycles4)
print("sorted lis---->",sorted(bicycles4))
print("original list--->", bicycles4)

# reversed order
bicycles5 = ['trek', 'street', 'mountain', 'specialized']
rev = bicycles5.reverse()
print(list(reversed(bicycles5)))
print("This return reserved---->", rev)

# copy() - shallow copy and deep copy
# list() # constructor
# slicing - help to create copy

interests = [
    'learnin g python',
    'automate the boring stuff wuth python',
    'python data analusis',
    'fluent in python',
    'python for kids',
    'Hello we app with python'
]

# remove items from the list
for item in interests:
    interests.remove(item)

# however directly modifying a list during the iteration can lead to unexpected behaviour

print("before copy ----->", interests)

for item in interests.copy():
    interests.remove(item)
print("after copy ----->", interests)

# clear function - clear()
interests2 = [
    'learnin g python',
    'automate the boring stuff wuth python',
    'python data analusis',
    'fluent in python',
    'python for kids',
    'Hello we app with python'
]

interests2.clear()
print("using clear ---->", interests2)

