# Python Mutable and Immutable Data Types

# In Python, every value is stored as an Object.

# Mutable Object : Can be chnage after creation

# Immutable Object : Cannot be change after creation

# Concept

'''
1. Momery Management
2. Variable behavior
3. Function arguments
4. Performance
5. Debugging
6. Learning Objectives
'''

# Everything in Python is an Object.

x = 10
name = "Python"
numbers = [1 , 2 , 3 , 4]

# Each Object has:  Value , Type  , Memory Address

# We can check memory location using : id() buit-in function

x = 10
y = 11
print(id(x))
print(id(y))

# Common Immutable Types
'''
int 10
float 10.5
complex  2+3J
bool True
str "Hello"
frozenset frozenset({1 , 2})
bytes b"abcd"
tuple(1 , 2)

'''
# int

x = 10

print("Before: " , id(x))

x = x + 1

print("After: " , id(x))


# String

name = "Python"

#name[0] = "J"

# Common Mutable Types
'''
list  [1 , 2 , 3]
dict {"a" : 1}
set {1 , 2 , 3}
bytearray bytearray(5)
'''

# Mutable List

numbers = [1 , 2 , 3 , 4 , 5]

print("Before:" , numbers)
print("Before Id:" , id(numbers))

numbers.append(4)

print("After:" , numbers)
print("After Id:"  , id(numbers))

# Mutable Dictionary

students = {
    "name":"Rajesh",
    "age":20
    }

students["age"] = 21

print(students)

# String

a_str = "Hello World"
             
print(a_str)
print(a_str[5])
print(a_str[0:5])
print(a_str[6:11])

# Set Data Types

# Set - They are mutable and new element can be added once sets are defined.

basket = {'apple' , 'Banana' , 'Orange' , 'pear' ,'Kiwi' , 'Banana'}

print(basket)

a = set('abcdefghijk')
b = set('abracadabra')

print(a)
print(b)







