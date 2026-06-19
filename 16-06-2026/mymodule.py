'''
Creating, importing & renaming modules
__name__ with __main__
Creating & using package
dir() and __init__.py
'''
# A module is a Python file that contains functions , variables or classes which can be reused in another program.

# Creating a module

def prints(name):
    print("Name : " , name)

def add(a , b):
    return a + b

#2. create __name with __main__

# Every Python file has a special built-in variable called __name__.

# __name__ = module_name

# This is used to control which code should run directly.

# 3. creating & using pakages defination

# 4. dir() function

# dir() function is a built-in function used to display all properties  , method , and functions of an object or module.

import sys

print(dir(sys))

#5. __init__.py

# __init__.py is  a special file used to mark a folder as a Python Package.

# It can also contain initialization code for the package.

# Renaming Module using as

# Higher Order Functions

print("============= Higher Order Fubnctions ===========")

# map()

# map() applies a function to every item.

number = [1 , 2 , 3 , 4 , 5]

square = list(map(lambda x : x * x , number))

print("Map Result:" , square)

# reduce

# reduce() combines all values into one value.

from functools import reduce

number = [1 , 2 , 3 , 4 , 5]

total = reduce(lambda x , y : x - y , number)

print(total)

#










