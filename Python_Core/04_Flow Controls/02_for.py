###########################
# For Loop - iterate over a sequence
# use For look when you know the number of iteration
# or you want to iterate over of sequence

fruits = ['apples', 'bananas', 'mangoes']
for fruit in fruits:
    print(fruit)

########################################
# write a program which print hello world 10 times

for i in range(10):
    print(i+1, '--- hello world')

 ########################################
# how to find numbers of states
# using f string

states = ['virginia', 'new jersey', 'north carolina', 'california']
capitals = ['richmond', 'trenton', 'raleigh', 'sacramento']
print(len(states))

for i in range(len(states)):
    print("The capital of " + states [i] + " is " + capitals[i])

# using f string
    print( f"The capital of {states [i]}  is { capitals[i]} " )

######## one more scenario ###############
    states = ['virginia', 'new jersey', 'north carolina', 'california', 'oregon']
    capitals = ['richmond', 'trenton', 'raleigh', 'sacramento', 'salem']

# The zip() function returns a zip object, which is an iterator of tuples where the first item
# in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
    for state, capital in zip(states,capitals):
        print("The capital of " + state + " is " + capital)

##################################################
# mixing loops
# combine For and if

numbers = [1,2,3,4,5,6,7,8,9,10]
# print only even numbers
# modules operator "%" which is divide
for num in numbers:
    if num % 2 == 0:
        print(num)


#######################################################
# loan calculator
# break statement need to be used with For and if

money_owed = float(input("how much loan do you want ?"))
apr = float(input("what is annual percentage rate of the loan ?"))
months = int(input("how many months do you want on this loan ?"))
payment = float(input("how much will you pay of each month ?"))

monthly_rate = apr/100/12

for i in range(months):
    interest = money_owed * monthly_rate
    money_owned = money_owed + interest

    if (money_owned - payment < 0):
        print("you paid iof the loan in ", i+1, "months")
        break
    money_owed = money_owed - payment
    print("Paid ", payment, "of which is ", interest, " was interest")
    print("Now I owe ", money_owed)

##############################################
# Break and Continue
# break = exist or terminated the loop prematurely
# break = if certain conditions are met and then will exist loop
# contuine = used to skip the rest of the code inside the loop for the current iteration
# and proceed to tne next iteration

for i in range (5):
    if i == 3:
        break
        #continue
    print(i)


