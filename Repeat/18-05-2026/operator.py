# Operators

# Python Operators

# Arithmetic Operator

'''
Addition
Substraction
Multiplication
Division
Modulus
Expontiations
Floor Division
'''

# Examples

x = 4
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x // y)

# Comparison Operator

'''
== Equal
!= Not Equal
< Less than
> Grether than
>= Grether than and Equal
>= Less than and Equal
'''

x = 20
y = 20

print( x == y)
print( x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

# Assignment Operator

'''
= asignement
+=  , -= , *= , /= , **= , //=
'''

x = 10
y = 2

x = y

print(x)
print(y)

x += y # x = x + y

print(x)
print(y)

x -= y # x = x - y

print(x)

x *= y # x = x * y

print(x)
print(y)

y /= x # y = y / x

print(x)
print(y)

x **= y # x = x ** y

print(x)

x //= y

print(x)

# Logical Operator

# and , or , not

# and Return True if both statement are true( x < 5 and x > 2)

# or Returns True if one of the statement is true.

# not Reverse the result

# Check if a number is even or odd

num = int(input("Enter a number:"))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Find the minimun of two numbers

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 < num2:
    print(f"The minimum number is {num1}")
else:
    print(f"The minimum number is {num2}")

# Find the Largest of three numbers

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 >= num2 and num1 >= num3:
    print(f"the largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"the largest number is  {num2}")
else:
    print(f"the largest number is {num3}")


