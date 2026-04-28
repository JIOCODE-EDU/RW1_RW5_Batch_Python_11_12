# Python Statements

# if....statement

'''
doorOpen = False

if doorOpen:
    print("Welcome to Home.")
    
else:
    print("Meet me again tomorrow.")

# if...elif..else statement
'''
'''
# check positive , nagative and zero

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} Positive Number")
elif num < 0:
    print(f"{num} Nagative Number")
else:
    print("Zero")
'''
'''
# Find Largest of two numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a > b :
    print("Largest number is" , a)
else:
    print("Largest number is" , b)
'''

'''
# check Leap year

year = int(input("Enter year: "))

if(year % 4 == 0 and year % 100 != 0)or(year % 100 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
'''
# Loop in Python

'''
# while loop

i = 0

while i > 6:
    print(i)
    i += 1
'''

# for loop

for i in range(10):
    print(i)

# list

fruits = ["apple" , "banana" , "orange" ,"watermelon"]

for fruit in fruits:
    print(fruit)


