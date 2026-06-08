# Exception Handeling in Python
'''
An Exception is an error that occurs during program executing.
if an Exception is not handled ,  the program stop immidiately.
'''
# print(10 / 0)

# to avoid program crashes, Python provides exception handeling using:

'''

try
catch
else
finally
'''

# 1. try........except

# used to handle errors safely.

# syntax:

'''

try:
    # code block
except:
    # error handeling code

'''
'''
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input")
'''
# try -> contains risky code
#except -> runs if error occurs

#2. try.........except........else

# else block executes only when no exception occurs.

# syntax

'''

try:
    # code block
except:
   # Error Handling
else:
    # execcutes if no error

'''
'''
try:
    num = int(input("Enter Number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot devide by zero")

else:
    print("Result : " , result * 10)
'''
# 3. try..............except...........finally

# finally block always executes weather error occur or not.

# syntax

'''
try:
except:
finally:
'''
'''
try:
    file = open("demo1.txt" , "r")

    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Program finished.")

#4. try.........except.......else........finally
'''
# Combination of all blocks.
'''
try:

    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("cannot devided by zero")

else:
    print("result : " , result)

finally:
    print("program finished.")
'''
# Important Exception Types in Python
'''
1. ZeroDivisionError
2. ValueError
3. TypeError
4. IndexError
5. KeyError
6. FileNotFoundError
'''
# Prevent program crash
# Improve program reliability
# Makes debugging easier
# Handles unexpected errors gracefully
'''
try:
    atm_pin = int(input("Enter ATM PIN:"))

except ValueError:
    print("PIN must contain numbers only")

else:
    print("PIN accepted")
'''
#Programs

#1. Divide two numbers using try............except
'''
try:
    num1 = int(input("Enter first Number: "))
    num2= int(input("Enter second Number: "))
    result = num1 / num2
    print("result : " , result)

except ZeroDivisionError:
    print("cannot devided by zero")
'''
#2. handle list index error
'''
try:

    numbers = [10,  20 , 30 , 40 , 50]
    index = int(input("Enter index number:"))
    print("Element : " , numbers[index])

except IndexError:
    print("Index does not exist.")
'''

# 3. Read file using try.........except...........else
'''
try:
    filename = input("Enter filename: ")
    
    file = open(filename , "r")

except FileNotFoundError:
    print("File not found")

else:
    print("file content")
    print(file.read())

    file.close()
'''

#4. handeling string index error using else

try:

    text = "Python"

    index = int(input("Enter index number : "))

    result = text[index]

except IndexError:
    print("Index does not exist")

else:
    print("Character :" , result)

    




    
    

    

    





