# break Statement

# Stops the loop immidiately.

for i in range(1 , 7):
    if i == 4:
        break
    print(i)

# continue statement

for i in range(1 , 7):
    if i == 5:
        continue
    print(i)

# pass statement

for i in range(1  , 7):
    if i == 5:
        pass
    print(i)

# Null Statement(does nothing)

# Pattern in Python

# Right-angled Triangle

for i in range(1 , 6):
    for j in range(i):
        print("*" , end=" ")
    print()

# Number Triangle

for i in range(1 , 6):
    for j in range(i):
        print(i , end=" ")
    print()

# Inverted Triangle

for i in range(6 , 0 , -1):
    for j in range(i):
        print("*" , end=" ")
    print()

# Pyramid Pattern

row = 5

for i in range(1 , row + 1):
    for j in range(row-i):
        print(" " ,  end="")

    for k in range(2 * i - 1):
        print("*" , end="")
    print()

# Floyd's Triangle

num = 1

for i in range(1 , 6):
    for j in range(i):
        print(num , end=" ")
        num += 1
    print()

# else with loops

# the else block runs when loop finishes normally.

for i in range(5):
    print(i)
else:
    print("Loop finished.")

# break

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop Finished.")

# else does not run beacuse loop stopped using break.

# List and Tuple

my_list = [10 , 70 , 80 , 20]

print("Original List:" , my_list)

my_list[0] = 50

print("Modified List:" , my_list)

# Tuple in Python

my_tuple = (10 , 20 , 30)

print("Tuple : " , my_tuple)

my_tuple[0] = 20












