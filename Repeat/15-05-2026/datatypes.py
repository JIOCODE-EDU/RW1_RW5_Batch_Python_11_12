# Python DataTypes:

# Frozen Sets : They are immutable and new element cannot added after its defined.

fs  = frozenset('HelloPython')

print(fs)

cities = frozenset(["surat" , "Ahmedabed" , "Vadodara" ,  "Pune" , "Mumbai"])

print(cities)

# Number data Types

# Number have four type in Python : Int , float , complex , long

int_num = 10
float_num = 10.5
# complex_num = 3.15j
# long_num = 123456789L

print(int_num)
print(float_num)

# List Data Types in Python

# A list contain items seperated by comms and enclosed within brackets[]. list is similar to arrays in C programming
# but difference is that all the items belonging to a list can be of different data type.


list = [123 , "abcd" , 10.2 , "D"]

print(list)

list1 = ["Hello" , "World"]

print(list1)

print(list[2 : 4])

print(list1 * 2)

print(list + list1)

# Dictionary Data Types

# Ditc consists of key-value pairs. it is enclosed by curly braces {} and values can be using square Brackets[].

dic = {'name' : "red" , 'age' : 10}

print(dic)

print(dic["name"])

print(dic.values())

print(dic.keys())

# Tuple Data Types

# Lists are enclosed in brackets [] and Tuplr are closed in parentheses () and cannot be updated. Tuple are immutable.

tuple = (123 , 'hello')
tuple1 = ('world')

print(tuple)

print(tuple[0])

#print(tuple + tuple1)

#tuple1[1] = "python"

print(tuple1)

# Python Operators

'''
1. Arithmetic   ` + , - , / , * , %`
2. Assignment  ` =  , += , -=`
3. Comparision ` ==  , != , <  , >`
4. Logical   ` and or not`
5. Identity ` is is not`
6. Membership ` in not in`
7. bitwise `&  ,^ `
'''






