# Identity Operator in  Python

# Identity Operator check whether two variables point to the same object in memory.

# is return True if both variables refer to the same object
# is not return True if both variable refer to diffrent object

a = [1 , 2]
b = a
c = [1 , 2]

print(a is b)
print(a is c)
print(a is not c)

# Explanation

# a and b refer to the same list object.
# c has the same value but is a diffrent object in memory.


# Membership Operator in Python

# Membership operator check whether a value exists in a sequence like list , tuple , string or dictionary.

# in returns True if value exists
# not in return True if value does not exists

numbers = [1 , 2 , 3 , 4]

print(2 in numbers)
print(5 in numbers)
print(5 not in numbers)


# string

text = "python"

print("Py" in text)

# Bitwise Operator in Python

# Bitwise operator work on binary numbers(bits).
# & Bitwise AND
# ^  Bitwise XOR

# Bitwise AND

a = 5 # 0101
b = 3 # 0011

print( a & b)

'''
0101
0011
0001
'''

# Bitwise XOR

a = 5
b = 3

print(a ^ b)

'''
0101
0011
0111
'''

# Python Control Flow

# Conditional statements allow a program to make decisions based on conditions.

# if , elif , else

#  if statement

# the if statement allow a program to check whether a condition is True.

# syntax

# if condition:

age = 17

if age >= 18:
    print("You are eligible to vote")

# if.....else statement

# Used when you want two possible outcomes.

# syntax
'''
if condition:

else:

'''

number = 6

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# if....elif....else statement

'''
if condition:

elif condition:

elif condition:

else:

'''

marks = 45

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")





