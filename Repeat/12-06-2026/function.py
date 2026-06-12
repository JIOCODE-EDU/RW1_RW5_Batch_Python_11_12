# Functions in Python

# Functions are reusable blocks of code used to perform a specific task.

# Reusability / Cleaner code / Better Organization / Reduce Repetition
'''
def prints():
    print("Welcome Students")

prints()
'''
# Function with parameter
'''
def add(a , b):
    print(a + b)

add(10 , 20)
add(20 , 30)
'''
# Recursion

# A function calling itself.

# Used to : Factorial , Fibonacci , Tree Structure , Problem solving

# 1. Base Case
# 2. Recursive Call
'''
def factorial(n):

    if n == 1:
        return 1

    return n  * factorial(n - 1)

print(factorial(5))

# sum of numbers

def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)

print(total(5))
'''
# Anonymous  / Lamda Function

# Small anonymous function / Writtten in one line / No function name

# syntax : lambda argument : expression
'''
def squares(a):
    return a * a

print(squares(5))

square = lambda x : x * x

print(square(5))
'''

# map()
'''
numbers = [1 , 2 , 3 , 4]

result = list(map(lambda x : x * 2 , numbers))
result1 = list(filter(lambda x : x % 2 == 0 , numbers))

print(result)
print(result1)
'''
# Global Keyword

# Variables created outside function are called : Global Variables

# to modify global variable inside funtion using 'global'
'''
x = 10

def show():
    print(x)
show()
'''
# counter
'''
count = 0

def increment():
    global count
    
    count += 1

increment()
increment()
increment()

print(count)
'''
# function scope with global

def greet():
    global count
    count = 0

def increment():
    global count
    count += 1
    print(count)

greet()   
increment()
increment()
increment()

# TNRN classification

# T ->  Take Arguments
# N -> No Arguments
# R -> Return value
# N -> No Return value

#  TNRN / TSRN / TNRS / TSRS

# TNRN

def greet():
    print("Welcome students")

greet()

# TSRN

def add(a , b):
    print("Addition : " , a + b)

add(10 , 20)

# TNRS

def message():
    return "Hello Students"

print(message())

# TSRS

def multi(a , b):
    return a * b

print(multi(4 , 5))





    
