# match-case Statement in Python

# works similar to switch-case

# syntax

'''
match variable:
    case value1:
            code
    case value2:
            code
    case _:
            # default case

'''

# Simple Calculator

num1 = 10
num2 = 5

operator = "%"

match operator:

    case "+":
        print("Addition = " , num1 + num2)
    case "-":
        print("Subtraction = " , num1 - num2)
    case "*":
        print("Multiplication = " , num1 * num2)
    case "/":
        print("Division = " , num1 / num2)
    case _:
        print("Invalid Operator")


# Python Loops

# 1. While loop

# A while loop runs as long as the condition is True.

# syntax

'''
while condition:
    # code block
'''
'''
i = 1

while i >= 0:
    print(i)
    i += 1
'''

# for Loop

# used to iterate : ranges , lists , strings , tuples , dictionaries

# syntax
'''
for variable in sequence:
    # code
'''

# Print Number 1 to 5

for i in range(1 , 6 , 2):
    print(i)

# Loop with String

name = "Python"

for i in name:
    print(i)


# Loop with List

fruits = ["Apple" , "Banana" , "Mango" , "Orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

for item in fruits:
    print(item)

# range function

# used to generate a sequence of numbers.

# range (start , stop , step)

# parameter

# start : starting value
# stop : ending value (excluded)
# step : increment / decrement

# example 1

for i in range(5):
    print(i)


for i in range( -5 , 10):
    print(i)

for i in range(10 , 0 , -1):
    print(i)

# Nested Loop

# used for : patterns , tables , matrices , grids
'''
for i in range():
    for j in range():
        # code
'''

for i in range(1 , 5):
    for j in range(1 , 4):
        print(j , end=" ")
    print()

for i in range(1 , 6):
    for j in range(1 , 11):
        print(j*i , end=" ")
    print()



