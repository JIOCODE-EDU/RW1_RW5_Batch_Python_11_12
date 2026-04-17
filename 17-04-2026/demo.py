# Python Variables , DataTypes and Operators

# Variable Assignement

x = 5
y = "Hello World"
z = 3.14

# Variable Naming Rules

# Must start with a letter and underscore

# cannot start with a number

# 12 = "hello"
# 12demo = 2.15

# can only contain alpha-numeric charcters and underscore

name20 = "vivek"

print(name20)

# Case-sensitive language (age , Age and AGE are diffrent variables)

my_var = "my world!!"
_var1 = 25

print(my_var)
print(_var1)

# Data Types

# Python has several buit-in datatypes:

# basic Types
# Numeric Types

demo = 20 # int
demo1 = 20.3 # float
complex = 3 + 5j

# Text Type

name = "my name is vishal." # string

# boolean type

# bool : True and False

# type() operator

a = 10

print("Type of a : " , type(a))

b = "hello"

print("Type of b :" , type(b))

c = True

print("Type of c : " , type(c))

# list types data

# list of Python

# tuple

# set

# dict

# Python Operators

'''
1. Arithmetic Operator
2. Assignment Operator
3. Comparison Operator
4. Logical Operator
5. Membership Operator
6. Identity Operator
'''

# 1. Arithmetic Operator

a = 10
b = 3

print("Addition" , a + b)
print("Substraction" , a - b)
print("Multiplication" , a * b)
print("Divison" , a / b)
print("Modulus" , a % b)
print("Exponentiation" , a ** b)
print("Floor Division" , a // b)

# Asignment Operator

x = 10
y = 2

x+=y

print("+= : ", x) # x = x + y

x -= y

print("-= :" , x) # x = x - y

x *= y

print("*= :" , x) # x = x * y

x /= y

print("/= :" , x)

x %= y

print("%= :" , y)
print("%= :" , x)

y **= x

print("**= :" , y) # y = y ** x

# comparision operator

x = 10
y = 8

print("Equal :" , x == y)
print("Not Equal :" , x != y)
print("Greater than :" , x > y)
print("Less than :" , x < y)
print("Greater than or Equal :" , x >= y)
print("Less than or Equal :" , x <= y)

# Logical Operator

a = True
b = False

print("AND :" , a and b)
print("OR :" , a or b)
print("NOT :" , not b)






