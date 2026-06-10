# Type Casting

# Type casting mean converting one data type into another data type.

num = 10
result = float(num)
print(result)
print(type(result))

# Constructor

# A constructor is a special method used to initialize objects in a class.

# __init__().

class Student:
    def __init__(self , name):
        self.name = name

s1 = Student("Zeel")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)

# del keyword

# The del keyword is used to delete variables , objects or items from a list / dictionary.
'''
x = 100

print(x)

del x

print(x)
'''
# list

numbers = [10 , 20 , 30 , 40]

del numbers[0]

print(numbers)

# Dictionary

student = {
        "name" : "Rajesh",
        "age" : 20,
        "course" : "Python"
    }

print(student)

del student["age"]

print(student)

# List of Dictionaries

students  = [
        {"id":101 , "name":"Alice"  , "score" : 85},
        {"id":102 , "name":"Bob"  , "score" : 34},
        {"id":103 , "name":"Charlie"  , "score" : 75}
    ]


print(student)

# Print the name of each student using a loop

print("Student Names : ")

for student in students:
    print(student["name"])

# Print the average score of all students

total = 0

for student in students:
    total += student["score"]

average = total / len(students)

print(f"\n Average Score : {average:.2f}")

# Add a new student record to the list

new_student = {"id" : 104 , "name": "Zeel" , "score" : 89}

students.append(new_student)

print(students)

# Update the score of a student with ID 102 to 88

for student in students:
    if student["id"] == 102:
        student["score"] = 88
print("\n After Updating score")
print(students)


