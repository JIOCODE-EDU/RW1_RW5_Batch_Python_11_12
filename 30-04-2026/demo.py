# Python Collection 

print("======= Python Collection Datatypes =====")

# -------- List ---------

print("List Examples")

my_list = [10 , 20 , 30 , 40]

print("Original List:" , my_list)

# Mutability

my_list[0] = 100

print("After Mutability List:" , my_list)

# append()

my_list.append(50)

my_list.append(60)

my_list.append(10)

my_list.append(10)

print("After use buill-in function List:" , my_list)

# max() and min()

print("Max:" , max(my_list))
print("Min:" , min(my_list))

# Remove duplicates menually

unique = []
for i in my_list:
    if i not in unique:
        unique.append(i)
print("Unique List:" , unique)


# -------- Tuple --------

print("Tuple Examples")

my_tuple = (1 , 2 , 3 , 4)

print("Tuple :" , my_tuple)

# Immutable

# count occurrence

print("Count of 3:" , my_tuple.count(4))

# Swapping using tuple

a , b = 10 , 20

print("Values:" , a , b)

a , b = b , a

print("Values:" , a , b)


# -------- set -------

print("Set Examples")

dataset = [1 , 2 , 3 , 4 , 5 , 6]

setdata = set(dataset)

print("Set Values:", setdata)

# Set Operator

a = {1 , 2 , 3}
b = {3 , 4 , 5}

print("Union:" ,  a | b)

#------- Dictionary ---------

print("Dict Examples")

student = {
        "name":"Ved",
        "marks": 85
    }

print("student:" , student)

student["marks"] = 90

print("Updated student:" , student)

print("Student Marks: " , student["marks"])

# throught loop create dictionary

for key , value in student.items():
    print(key , ":" , value)

# Find topper

students = {"A":80 , "B":95 , "C":70 , "D":45}

topper = max(students , key=students.get)

print("Topper: " , topper)

#------- List Comprehension -------

print("List Comprehension Examples:")

numbers = [i for i in range(5)]

print("Numbers: " , numbers)

even = [i for i in range(10) if i % 2 == 0]

print("Even Number: " , even)

#------- Type Casting -----------

print("Type casting Examples:")

t = (1 , 2 , 3)
list_1 = list(t)

print("List: " , list_1)

L = [1 , 2 , 3]
t_1 = tuple(L)

print("Tuple: " , t_1)
















