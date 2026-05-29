# Function in Python

# Functions, Recursion , Lambda Functions , Global Keyword and Multiple Return Value

# What is Function?

# Functions are reusable blocks of code used to perform a specific task.

# Reusability , Cleaner Code , Better Optimization , Reduce repetition

# Type of Functions

# Built-in Functions

# UDF Functions

def prints():
    print("Welcome Students!!")

prints()


def multi(a , b):
    print("Multiplication: " , a * b)

multi(4 , 5)

# Recursion Function

# A functions calling itself.

# Factorial , Fibonacci , Tree structure , Problem Solving

def factorial(n):

    if (n == 1):
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))


# 2. Sum of two numbers

def total(n):

    if n == 0:
        return 0

    return n  + total(n - 1)

print(total(5))

# Anonymous  / Lambda Function

# small anonymous function
# Written in one line
#No function name

# syntax

# lambda arguments : expression

square = lambda x : x * x

print(square(5))


add = lambda a , b : a + b

print(add(10 , 20))

# list

numbers = [1 , 2 , 3 , 4 , 5]

result = list(map(lambda x: x * 2 , numbers))

print(result)

# filter

numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

odd = list(filter(lambda x : x % 2 != 0 , numbers))

print(odd)

# Normal Function
'''
def keyword
Multiple line
Named
'''
# Lmbda Function
'''
lambda Keyword
Single line
Anonymous
'''

# Global Keyword

# Variables created outside fucntion are called Global variables

# To modify global variable inside function use 'global'

x = 10

def show():
    print(x)

show()

count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()

print(count)

# Return Multiple value

# Python functions can return:

# single value
# multiple value

def calculation(a , b):

    return a + b , a - b

result = calculation(10 , 5)

print(result)


def student():

    name = "Alice"
    marks = 90

    return name , marks

n, m = student()

print(n)
print(m)

# Returning multiple calculation
# Returning user data
# Returning API responses

# Built-in Functions

numbers = [1 , 2 , 3 , 4 , 5]

print("Length:" , len(numbers))
print("Maximun :" , max(numbers))
print("Mininum : " , min(numbers))

# this is pre-defined functions inside Python. you don't create them.

# User Defined Function(UDF)

def greet(name):
    return "Hello " + name

print(greet("Students"))

# Arbitraty Arguments (*args)

# When number of inputs is unkown

def add_number(*args):
    total = 0

    for num in args:
        total += num
    return total

print(add_number(1 , 2 , 3 , 4  , 5))

# *args collects multiple value into a tuple

# Keyword Argument (**kwargs)

# When passing named values

def student_info(**kwargs):
    for key , value in kwargs.items():
        print(key , ":" , value)

student_info(name="Rahul",  age = 20 , course="Python")

# **kwargs stored data in dictionary

# doc (Documentation String)

# Used to describe function

def multiply(a , b):
    """ This function returns the multiplication of two numbers"""
    return a * b
print(multiply(4 , 5))
print(multiply.__doc__)

# TNRN Classification

'''
T -> Take Arguments
N -> No Arguments
R -> Return value
N -> No return value
'''

'''
TNRN -> Take no arguments , return no value
TSRN -> Take some Arguments , Return no value
TNRS -> Take no Arguments , Return Some value
TSRS -> Take some Arguments , Return Some Value
'''

# 1. TNRN

'''
No Parameter
No Return statement

def function_name():
    # code
'''

def greet():
    print("Hello,  Python Students")

greet()

# 2. TSRN

'''
Accept parameter
Does not return result
'''

def add(a , b):
    print("Addition : " , a + b)

add(10 , 20)

# 3. TNRS

'''
No Parameter
Return value using return
'''

def message():
    return "Hello Students"

print(message())

# TSRS Function

'''
Accept parameter
Returns output
'''

def multiply(a , b):
    return a * b

result = multiply(4 , 7)

print(result)























