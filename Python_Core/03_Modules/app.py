# def>>>>>>>define funtion from the app file
# Define funtion and then call funtion
# first funtion
#################### Without Dunder Funtion ###############
# def print_hello():
#     print("Hello from the app")
#
#
# # second funtion
# def second_print_hello():
#     print("Testing from the second print hello")
#
# print_hello()
# second_print_hello()

###################### DUNDER Funtion ################
# __name__=="__main__" is to detmine if a script is being run directly or if it is being imported as a module
# __name__ dunder that holds the current modules and you need to compare with the entry point that "__main__"

def first_print():
    print("Hello from the app")

def second_print():
    print("Testing from the second print hello")

def third_print():
    string1 = 'Hello World'
    print(string1.replace("H", "J"))

def fourth_print():
    x = 5
    y = 10
    result = x < y
    print (result)

def fifth_print():
    score = eval(input("Enter your score"))
    if score >= 90:
        print("your grade is A")
    elif score >= 80:
        print("your grade is B")
    else:
        print('Take the test again')

if __name__ == "__main__":
    first_print()
    second_print()
    third_print()
    fourth_print()
    fifth_print()
