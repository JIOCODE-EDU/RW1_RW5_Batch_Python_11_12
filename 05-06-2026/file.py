# Text file Handeling in Python

# What is file handeling?

'''
Text file handeling in python is the process of creating , opening , reading  , writing , appending , and managing text
text files using Python Programs.

It allows data to be stored permenently in files insted of temporary memory.
'''

# Defination of Modes of Opening File in Python

'''
File modes are the diffrent ways used to open a file in Python for performing operations
like reading , writing , appending or binary handling.
'''

# Defination of I/O Operation with Files in Python

'''
I/O operations in Python are used to read data from a file and write data into a file.

Input Operation : Reading data from a file
Output Operation : Writing data into a file
'''


# syntax

# file = open("filename" , "mode")

'''

Mode                            Meaning
r                                      Read Mode
w                                     Write Mode
a                                      Append Mode(adds data at end)
x                                      Create new file
rb                                     Read binary file
wb                                    Write binary file
r+                                      Read and Write
a+                                      Append and read
'''

# 1. Read Mode()

# use to read data from file.
'''
file = open("text/demo.txt" , "r")
content = file.read()
print(content)
file.close()
'''
#2. Write Mode()

# use to write data into a file.
'''
file = open("text/demo.txt" , "w")
file.write("\n Python file Handeling!!!!")
file.close()
'''
#3. Append Mode()

# Adds new Data at end of the file
'''
file = open("text/demo.txt" , "a")
file.write("\n Python is easy to learn.")
file.close()
'''
#4. Create Mode()
'''
file = open("newfile.py" , "x")
file.close()
'''
# I/O Operations

# Read files

file = open("text/demo.txt" , "r")
print(file.read())
file.close()

# Read one line at a time.
# readlines()
# readline()

file = open("text/demo.txt" , "r")
print(file.readlines())
print(file.readline())
file.close()

# Output Operation

# write text into file

file = open("newfile.txt" , "w")
file.write("Hello Python!")
file.close()

# writelines()

file = open("newfile.txt" , "w")

lines = [
    "Line 1 : Python\n",
    "Line 2 : File Handeling\n",
    "Line 3 : Easy Lerning\n"
    ]

file.writelines(lines)
file.close()

# Using with statement
# best method for file handeling beacuse file closes automatically.

with open("newfile.txt" , "r") as file:
    content = file.read()
    print(content)

# Binary File Handeling

# Used for images , audio , videos , etc...

file = open("newfile.txt" , "rb")
content = file.read()
print(content)
file.close()

# Read and Write Binary File (r+)

file = open("newfile.txt", "r+")
print(file.read())
file.write("Python File Handeling")
file.close()

# Create and Read file

file = open("files.txt" , "w")
file.write("Hello Python!!")
file.close()

file = open("files.txt" , "r")
print(file.read())
file.close()





















