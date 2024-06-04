# if statement is used for conditional execution
# condition execution
# decision making
# error handling
# filtering data
# control flow

if True:
   print("True")
else:
   print("False")


if False:
   print("True")
else:
   print("False")

###################################
# if 0: will evaluate to False and ny non-zero number is considered truthy
# condition 1 or 0 ; 1=True 0=False
# any none zero is true

if 1:
   print("True")
else:
    print("False")

if 1 == True:
    print("True")

########################### multiway branding with elif = optimize condition check
# elif works only if the previous condition isn't true

score = eval(input("Enter your score"))

if score >=90:
    print("your grade is A")
elif score >= 80:
    print("your grade is B")
else:
    print('Take the test again')

##########################
import random
items = ['scissors','paper','rock']
computer_choice = random.choice (items)
#print(computer_choice)
user_choice = input("Do you want - rock, paper or scissors?\n")

if user_choice == computer_choice:
    print ("Tie")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('Win, the computer has ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Win, the computer has ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('Win, the computer has ' + computer_choice)
else:
    print("You loose: (Computer wins)")