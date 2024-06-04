# while condition, this will run as long condition is ture.
# Prefer using the while loop when the number of iterations is UNKNOWN.

# count =1
# while count <= 5:
#     print(count)
#     #count += 1
#     # or
#     count = count +1

# write a program to skip the odd numbers

x = 10
while x:
    x = x-1
    if x % 2 != 0 : continue
    print (x)

# break - exist of the loop

while True:
    name = input("Enter your name: ")
    if name == 'stop' : break
    age = int(input("Enter age: "))
    print("Hello", name , '====>', age)