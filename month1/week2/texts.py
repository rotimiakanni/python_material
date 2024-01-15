# Reading and writing text files is essential for working with data in Python. Here's what you need to know:
#   - A file is a collection of data stored on a disk with a name and sometimes a path.
#   - A file path is a string that specifies the location of a file.
#   - A file can be opened in different modes: read, write, append, and read/write.
#   - A file can be opened using the open() function.
#   - A file can be closed using the close() method.
#   - A file can be read using the read() method.
#   - A file can be read line-by-line using the readlines() method.
#   - A file can be written to using the write() method.
#   - A file can be written to line-by-line using the writelines() method.
#   - A file can be read and written to using the readwrite() method.


# Example: Open a file in read mode and print its contents.
file = open("data/shopping_list.txt", "r")
content = file.read()
print(content)

# Example: Open a file in read mode and print its contents line-by-line.
file = open("data/shopping_list.txt", "r")
content = file.readlines()  # returns a list of each line in the file
print(content)

# Example: Open a file in write mode and write to it.
file = open("data/shopping_list.txt", "w")  # creates a new file if it doesn't exist
# writes to the file and overwrites the existing contents
file.write("Milk\n")
file.write("Eggs\n")
file.write("Bread\n")
file.close()  # close the file after reading and writing to it

# Example: Open a file in append mode and append to it.
file = open("data/shopping_list.txt", "a")  # creates a new file if it doesn't exist
# appends to the file and doesn't overwrite the existing contents
file.write("Ice\n")
file.write("Tea\n")
file.write("Maggi\n")
file.close()  # close the file after reading and writing to it

# Example: Open a file in read/write mode and read from it.
file = open("data/shopping_list.txt", "r+")  # creates a new file if it doesn't exist
# reads from the file and doesn't overwrite the existing contents
content = file.read()
print(content)
# writes to the file and overwrites the existing contents
file.write("Milk\n")
file.write("Eggs\n")
file.write("Bread\n")
file.close()  # close the file after reading and writing to it


# Opening a file using the with statement
# The with statement is used to open a file and automatically close it after reading and writing to it.
# The with statement is used with the open() function.

# Example: Open a file using the with statement and read from it.
with open("data/shopping_list.txt", "r") as file:
    content = file.read()
    print(content)  # the file is automatically closed after reading from it

# Example: Open a file using the with statement and write to it.
with open("data/shopping_list.txt", "w") as file:
    file.write("Milk\n")
    file.write("Eggs\n")
    file.write("Bread\n")
    # the file is automatically closed after writing to it
