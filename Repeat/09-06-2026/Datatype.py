# DataTypes in Python

'''
python provide several built-in collection data types used to store multiple values in a single veriables.
'''

'''

1. List
2. Tuple
3. Set
4. Dictionary

'''

# 1. List

# A list is an ordered and mutable collection of items.

fruits = ["apple" , "orange" , "Banana" , "Kiwi"]

print(fruits)

# Access element

print(fruits[0])

fruits[0] = "mango"

print(fruits)

# 2. Tuple

# A tuple is an ordered and immutable collection of items.

colors = ("red" , "pink" , "blue" , "mango")

print(colors[0])

# List comprehension program

# 1. square from 1 tp 10

square = [x*x for x in range(1 , 11)]

print(square)

even_numbers = [x for x in range(1 , 21) if x % 2 != 0 ]

print(even_numbers)

# convert string to lowercase

words = ["hello" , "WORLD" , "pYtHoN"]

lowercase_words = [w.lower() for w in words]

print(lowercase_words)

