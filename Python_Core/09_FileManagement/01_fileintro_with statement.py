# create file
# read file
# write file
# manipulate file
# open() - modes - w(write), r(read), a(append), x(exclusive creation)

# create, read, write and manipulate
# open() - modes - w(write), r(read), a(append), x (exclusive creation)

# file = open('09_FileManagement/filename.txt','w')
# file.write("Hello i am learning about files\n")
# file.write("I am writing a second line to my file")
# file.close()

# file = open('09_FileManagement/filename.txt','r')
# print(file.read())

# with statement - ensures that the resources are properly cleaned up

filename = 'filename.txt'

try:
    with open(filename) as file:
        lines = file.readlines()
except IOError:
    print("Could not find files")
else:
    for line in lines:
        print(line)
finally:
    file.close()
    print("will print - everythingh is clean")

# will add/append extra line in the file
with open(filename, 'a') as file:
    file.write("\n I am adding extra information to the file with append command")
