# CRUD Operation in Python
# C : Create
# R : Read
# U : Update
# D : Delete

# Empty List

users = []

# CREATE

user1={
    'id':1,
    'name':'Alice',
    'email':'alice@gmail.com'
}

user2={
    'id':2,
    'name':'Zeel',
    'email':'zeel@gmail.com'
}

user3={
    'id':3,
    'name':'Karan',
    'email':'karan@gmail.com'
}

#add users

users.append(user1)
users.append(user2)
users.append(user3)

print("User Added Successfully!")

# Read

print("\n All Users:")

for user in users:
    print(user)

# search

search_id = 1

print("\n Searching User:")

for user in users:

    if user['id'] == search_id:
        print("User Found:" , user)

# UPDATE

print("\n Updating User Email....")

for user in users:

    if user['id'] == 2:
        user['email'] = 'zeel@example.com'

print("User Updated!")

'''
# DELETE

print("\n Deleting user.....")

for user in users:

    if user['id'] == 1:
        users.remove(user)
        break
print("User Deleted!")
'''
# count users

print("\n Total Users:" , len(users))

# check email exists

check_email = 'zeel@example.com'

found = False

for user in users:

    if user['email'] == check_email:
        found = True

if found:
    print("Email Exists")
else:
    print("Email not found")

# sort user by name

sorted_users = sorted(users , key = lambda x : x ['name'])

print('\n Sorted Users:')

for user in sorted_users:
    print(user)


# Final User List

print("\n ============= Final Users ================")

for user in users:

    print(f"""
ID : {user['id']}
Name : {user['name']}
Email:{user['email']}
""")

# Type casting constructor

# list()  ---> tuple()

a = [1 , 2 , 3 , 4]

b = tuple(a)

c = set(a)

print(b)

print(c)

# del keyword

# Used to delete variables , list element , disctionary keys , etc.....

x = [10 , 20 , 30]

del x[1]

print(x)

person = {'name':'vishva' , 'age':30}

del person['age']

print(person)

del x

print(x)
