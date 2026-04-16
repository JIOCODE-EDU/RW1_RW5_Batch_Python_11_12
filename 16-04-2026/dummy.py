# Python Basic Fundamental Statements
'''
print("my name is vivek.")

name = input("Enter your name : ")

print("my name is" , name)
'''
'''
# How to add two numbers

a = 5
b = 10

sum = a + b

print("The sum is :" , sum)

# Simple Calculator

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))


print("Addition" , a + b)
print("Substraction" , a  - b)
print("Multiplication" , a * b)
print("Division" , a / b)


# silly sandwich maker

bread = input("Choose your Bread (white / brown):")
filling = input("Choose your filling (Cheese / jelly / banana):")

print("Here's your silly sandwich:")
print("[" + bread + "bread + " + filling + " + rainbow glitter]")

'''
'''
# Pet Talk Simulator

pet = input("What pet do you have(dog/cat/fish):")

if pet == "dog":
    print("Woof ! I want treats!!!")
elif pet == "cat":
    print("Meow ! I rule this house.")
elif pet == "fish":
    print("Blob blob... I am swimming in style.")
else:
    print("That's a unique pet!!!")
'''

# Rock , Paper and scissors

import random

choices = ["rock" , "paper" , "scissors"]
computer =  random.choice(choices)

player = input("Choose rock , paper and scissors : ")

print("Computer Chose:" , computer)

if player == computer:
    print("It's a tie.")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player =="scissors" and computer == "paper"):
    print("You win.")
else:
    print("Computer win.")


