# Exception
# want to make sure code doesn't break
# Exception hierarchy - Base Exception - Exception - Arithematic error (zero division error; over flow; file not found
try:
    x = eval(input("Enter a number"))
    z = 1/x
except NameError:
    print("Enter a number")
except ZeroDivisionError:
    print("can't enter a zero")
except Exception:
    # type +++++
    print("This a serious problem")
else:
    print("The division is successfull",z)
