# A set is an unordered collection of unique elements
# A set doesn't have duplicate
# set is denoted {}
# an empty set is set()
# a empty set is dictonary
############################Today Class#############
# SET >>>> ADD, Remove, UPDATE
# Inner Join >>>> with operator >>>> & (apersend) >>>>>>>>>will list are items which are comman
# Outer Join >>> with operator >>>>> | (pipe) >>>>> will list all items but not duplicate
# difference method >>>> will return new set containing elements that are present in first set but not in th second set
# symetric difference = retuns a new set that contains elements that are in either of the set but not in the intersection
# gotchas #output >>>> will cause an error as can't mix in list

fruits = {'apple', 'banana', 'orange'}
s1 = set([3,4,5])
print(type(fruits))
print(type(s1))
# Output>>>>> <class 'set'>

s2 = {}
print(type(s2))
# output>>>>>>>>>>>>>> <class 'dict'> dictonary

empty_set = set()
print(empty_set)
empty_set.add('bikes')
print(empty_set)

fruits.add('banana')
print(fruits)
# NO duplicate will not be added

fruits.remove('apple')
fruits.update(['grapes', 'strawberry'])
print(fruits)

for i in fruits:
    print(i)
# output will be listed one by one with for statement

blue_eyes = {'Sue', 'Kathy', 'Cris', 'Jim'}
orange_hair = {'Sue', 'Ryan', 'Kathy', 'Dhiraj'}

# inner join
ij = blue_eyes.intersection(orange_hair)
print(ij)

ij1 = blue_eyes & orange_hair
print(ij1)

# outer join
oj = blue_eyes.union(orange_hair)
print(oj)

oj1 = blue_eyes | orange_hair
print(oj1)

# difference method >>>> will return new set containing elements that are present in first set but not in th second set
diff = blue_eyes.difference(orange_hair)
print(diff)

# symetric difference = retuns a new set that contains elements that are in either of the set but not in the intersetion
sd = blue_eyes.symmetric_difference(orange_hair)
print(sd)

# gotchas
#
#my_set = {1,[2,3]}
#print(my_set)
#
#3output >>>> will cause an error as can't mix in list

s3 = {3,1,4,5,2}
print(s3)

# output will be inorder numbers