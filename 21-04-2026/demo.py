# Python String Manipulation

s1 = 'He\nllo'
s2 = "World"
s3 = ''' Multiline
string'''
s4 = r"Raw \n string"

print(s1)
print(s2)
print(s3)
print(s4)


#common String Method

s = "Hello ,  World!"
   # 123456789012345
   # 012345678901234

print(s.upper())
print(s.lower())
print(s.split())
print(s.endswith("d"))
print(s.startswith("h"))
print(s.find("l"))
print(s.count("l"))

# String Formatting

name = "Alice"
age = 30

# f-string

print(f"Name:{name} , Age:{age}")

#.format()

print("Name:{} , Age:{}".format(name , age))


# Slicing

s = "Hello , Python!!"
    #0123456789

print(s[0])
print(s[9])
print(s[2:5])
print(s[:5])
print(s[::-1])

# Joining and Splitting in Python

words = ["Python" , "is" , "awesome"]

print(" ".join(words))
print("_".join(words))
print("+".join(words))


splits = "a , b , c"

print(splits.split(","))







