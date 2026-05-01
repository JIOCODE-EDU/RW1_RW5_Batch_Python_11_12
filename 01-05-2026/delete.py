'''
# Delete Keyword

print("\n DELETE Example")

list_1 = [10 , 20 , 30 , 40]

print("Before delete: " , list_1)

del list_1[3]

print("After deleting index:" ,  list_1)

del list_1[2]

print("After deleting index:" , list_1)

# Delete dictionary key

dict_1 = {"a" : 1 , "b" : 2}

del dict_1["a"]

print("Disctionary after delete:" , dict_1)
'''
# Tuple do not modify and delete
'''
t_1 = (1 , 2 , 3 , 4)

del t_1[0]
'''
'''
# Small program

print("\nSmall Program")

students = ["Aman", "Ravi" , "Kiran" , "Rajesh" , "Aman" , "aman"]

print("Original List:" , students)

unique_students = list(set(students))

student_data = {name:len(name) for name in unique_students}

print("Student Data: " , student_data)

# create List , Tuple , set and dict using user input

user_input = input("Enter element seperated by space:")

user_list = user_input.split()

print("user list" , user_list)

user_tuple = tuple(user_list)

print("user tuple" , user_tuple)

user_set = set(user_tuple)

print("user set" , user_set)

user_dict = {i:value for i, value in enumerate(user_list)}

print("user set" , user_dict)
'''
dict_input = input("Enter key:value pairs seperated by space:")

my_dict = {}

pairs = dict_input.split()

for item in pairs:
    key , value = item.split(":")
    my_dict[key] = value

print("Disctionary:" , my_dict)



















