# Python Basics

# Functions : Built-in Function (system function) / UDF (user defined function)
'''
print()
input()
id()
len()
type()
etc.....
'''

print("Hello , my name is Tushar.")

#Add Two Numbers

a = 10
b = 20

sum = a + b

print(sum)

# Input()

name = input("What is your name : ")

print("Welcome to Python Programming" , name)

name = "vivek"
print(type(name))

# simple calculator

a =  int(input("Enter first Number : "))
b =  int(input ("Enter second Number: "))

print("Addition:" , a + b)
print("Substraction:" , a - b)
print("Multiply:" , a * b)
print("Division:" , a / b)

# Silly Sandwich Maker

bread = input("Choose your bread (white / brown): ")
filling = input("Choose your filling (Cheese / Jelly / Banana): ")

print("Here is silly Sandwich: ")

print("[" + bread + "bread" + " " + filling + " + rainbow glitter.] ")
 

