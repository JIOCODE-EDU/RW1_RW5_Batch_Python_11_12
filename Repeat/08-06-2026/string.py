# String Fromatting

name = "Aisha"
age = 21

# f-string

print(f"My name is {name} and I am {age} years old.")

# Using .format()

print("My name is {} and I am {} years old.".format(name , age))

# Using % formatting

print("My name is %s and I am %d years old." %(name , age))

price = 199.4567

# decimal values

print(f"Price : {price:.2f}")

# List and Tuple (Basics & Mutability)

# List - Mutable
my_list = [10 , 20 , 30]
print(my_list)
my_list[1] = 99
print(my_list)
my_list.append(40)
print(my_list)
my_list.remove(99)
print(my_list)

# Tuple  - Immutable

my_tuple = (10 , 20 , 30 , 40)
print(my_tuple)

#my_tuple[1] = 99

print(my_tuple[1])

# indexing and slicing

text = "Python"

# indexing

print("first letter  :" , text[0])
print("last letter  :" , text[-1])

# slicing

print("First 3 letters : " , text[:3])
print("Last 3 letters : " , text[-3 :])
print("Every second letter : " , text[::2])

# Reverse string

print("Reverse String : " , text[::-1])

# Using list with slicing and formatting

students = ["Amit" , "Sara" , "Rohit" ,  "Zeel" , "Riya"]

print("First two students: " , students[:2])

# Loop through list

for student in students:
    print(f"Welcome , {student}")

# list length

print("Total students : " , len(students))

# checking element

print("Is sara Present?" , "Sara" in students)

# Nested List

matrix = [
        [1 , 2 , 3],
        [4 , 5 , 6],
        [7 , 8 , 9]
]

print("Matrix : " , matrix)
print("Middle Element :" , matrix[1][1])

# String Methods

message = "Python Programming Language"

print("Uppercase :" , message.upper())
print("Lowercase :" , message.lower())
print("Capitalized : " , message.capitalize())
print("Replace : " , message.replace("Python" , "Html"))
print("Split :" , message.split())

# List Method

numbers = [5 , 2 , 7 , 8 , 1]

numbers.sort()

print(numbers)

numbers.reverse()

print(numbers)

numbers.insert(1 , 100)

print(numbers)

# tuple Packing and Unpacking

person = ("Aisha" , 21 , "India")

# Unpacking

name , age , country=  person

print(name)
print(age)
print(country)
