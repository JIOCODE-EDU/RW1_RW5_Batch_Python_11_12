# String Foramatting

name = "Aisha"
age = 21

# using f-string

print(f"My name is {name} and i am {age} years old.")

# using .format()

print("My name is {} and i am {} years old.".format(name , age))

# Using % formatting

print("My name is %s and I am %d years old." %(name , age))

price = 199.456

print(f"Price:{price:.2f}")

# List and Tuple (Mutability)

# list

my_list = [10 , 20 , 30]

print("Original List:" , my_list)

my_list[1] = 200

print("Modified List:" , my_list)

# append()

my_list.append(50)
my_list.append(60)

print("After append list :" , my_list)

# remove()

my_list.remove(10)

print("After remove list :" , my_list)

# Tuple - Immutable

my_tuple = (10 , 20 , 30 , 40)

print("Tuple : " , my_tuple)

# Access Element

print("First Tuple Element :" , my_tuple[1])

# Indexing and slicing

text = "Python"

# indexing

print("First letter:" , text[0])
print("Last letter:" , text[len(text) - 1])
print("Last letter:" , text[-1])

# slicing

print("First 3 letters:" , text[0:3])
print("Last 3 latters:" , text[3:])
print("Last 3 latters:" , text[-3:])

# reverse string

print("Reverse String:" , text[::-1])

# Using List with slicing and formatting

students = ["Dixit" , "Jinal" , "Raj" , "Janvi" , "Jiya" , "Rutva"]

print("\nOriginal List:" , students)

print("\nFirst three students:" , students[:3])

# loop

for student in students:
    print(f"Welcome , {student}")

# length

print("Length of List:"  , len(students))

# checking element

print("Is Jiya Present?:" , "Jiya" in students)

# Nested list

matrix = [
        [1 , 2 , 3],
        [4 , 5 , 6],
        [7 , 8 , 9]
    ]

print("Matrix :" , matrix)

# Accessing element

print("Middle element:" , matrix[1][1])

# String Method

message = "python programming"

print("Uppercase:" , message.upper())
print("Capitalized:",  message.capitalize())
print("Replace:"  , message.replace("python" , "AI/ML"))
print("Split:" , message.split())

# list method

numbers = [5 , 8 , 2 , 7 , 1]

numbers.sort()

print("Sorted List:" , numbers)

numbers.reverse()

print("Reversed List:" , numbers)

numbers.insert(1 , 100)

print("After insert:" , numbers)







