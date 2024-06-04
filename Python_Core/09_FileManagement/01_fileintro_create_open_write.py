# create file
# read file
# write file
# manipulate file
# open() - modes - w(write), r(read), a(append), x(exclusive creation)

# create, read, write and manipulate
# open() - modes - w(write), r(read), a(append), x (exclusive creation)

# with statement - ensures that the resources are properly cleaned up

# will create file and then write to the file.
file = open('filename.txt', 'w')
file.write("Hello I'm learning about files to create,open,write....\n")
file.write("I'm writting a second line in the file")
file.close()


