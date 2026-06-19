# Array in Python
'''
arr = [10 , 20 , 30]

print(arr)

'''
# UDA (user-defined Array)
'''
arr = []

size = int(input("Enter array size : "))

for i in range(size):
    value = int(input(f"a[{i}] = "))
    arr.append(value)

print("Array : " , arr)
'''
# Python 2D Array

# Array inside another array

# rows / columns

# It look like a table or matrix
'''
arr  = [
    [1 , 2 , 3],
    [1 , 2 , 3]
]

print(arr)
print(arr[0][1])
'''
# UDA (2D array)
'''
arr = []

rows = int(input("Enter rows : "))
columns = int(input("Enter columns:"))

for i in range(rows):

    row = []

    for j in range(columns):

        value = int(input(f"arr[{i}][{j}] = "))
        row.append(value)

    arr.append(row)

print(arr)

'''

# Sum of all element in 2D array
'''
arr = [
    [1 , 2],
    [3 , 4]
    ]

total = 0

for i in arr:
    for j in i:
        total += j

print('total :'  , total)
'''
# Sorting in 1D/2D Array

# Arranging data in order

# Acending
# Decending

numbers = [5 , 8 , 2 , 9 , 1]

numbers.sort()

print(numbers)

numbers.sort(reverse = True)

print(numbers)




