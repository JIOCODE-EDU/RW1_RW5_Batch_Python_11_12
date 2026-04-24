# Print number from 1 to 10
'''
for i in range(1 , 11):
    print(i)
'''
# Print even numbers
'''
for i in range(1 , 21):
    if i % 2 == 0:
        print(i)
'''
'''
#sum of first N numbers

n = 10
total = 0;

for i in range(1 , n + 1):
    total+= i

print("Sum: " , total)

# While loop

n = 10
fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial:" , fact)

# 1 * 2 * 3 * 4 * 5

# Pattern Programs

# Right triangle

rows = 5

for i in range(1 , rows + 1):
    print("*" * i)

# reverced triangle

rows = 5

for i in range(rows , 0 , -1):
    print("*" * i)


# Nested Loops

# Multiplication table

for i in range(1 , 6):
    for j in range(1 , 11):
        print(i * j ,end="  ")
    print()
'''

# Break and Continue statements
'''
for i in range(1 , 10):
    if i == 8:
        break
    print(i)
'''
for i in range(1 , 10):
    if i == 6:
        continue
    print(i)

# Reverse a number

num = 1234
rev = 0

while num > 0:
    calc = num % 10
    rev = rev * 10 + calc
    num //= 10

print("Reversed: " , rev)

# loop with string

text = "Python"

for ch in text:
    print(ch)
