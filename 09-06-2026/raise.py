# raise keyword
'''
the raise keyword is used to manually trigger an exception in Python.
It allows developers to stop program execution when an error condition occurs.
'''

# syntax

# raise ExceptionType("Error Message")
'''
age = -5

if age < 0:
    raise ValueError("Age cannot be nagative")
'''
# assert keyword in python

'''
the assert keyword is used for debugging and testing conditions.

It checks whether a condition is True.

If the condition is True -> program continue

If the condition is False -> AssertionError is raised.
'''
#syntax
# assert condition , "Error Message"
'''

num = -10

assert num > 0 , "Number must be positive"

print("valid number")
'''
# custom exception with try-except

'''
class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1000

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance.")
    print("withdrwal successfull.")
    
except InsufficientBalanceError as e:
    print("Error :" , e)
'''
#1. check even number using TypeError and ValueError

def check_even():
    
    num = input("Enter an integer:")

    if  "."  in num:
        raise TypeError("Input must be an integer")
    
    num = int(num)
    
    if num % 2 != 0:
        raise ValueError("Number is odd")
    print("Number is even.")

try:

    check_even()

except Exception as e:
    print("Error : " , e)

# student grade validation
'''
class InvalidGradeError(Exception):
    pass

try:
    grade = int(input("Enter grade:"))

    assert grade != "" ,  "Grade input cannot be empty."

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 to 100")

    if grade < 40:
        raise InvalidGradeError("Student has failed.")

    print("Student passed.")

except AssertionError as e:
    print("AssertionError  :" , e)

except ValueError as e:
    print("ValueError : " , e)

except InvalidGradeError as e:
    print("InvalidGradeError : " , e)
'''

# Temperature conversion validation
'''
class HighTemperatureError(Exception):
    pass

try:

    temp = float(input("Enter temperature in celsius: "))

    if not isinstance(temp , (int , float)):
        raise TypeError("Temperature must be a number")

    assert -273 <= temp <= 10000 , "Temperature out of valid range."

    if temp > 1000:
        raise HighTemperatureError("Temperature exceed 1000 C")

    print("Valid Temperature :" , temp , "C")

except TypeError as e:
    print("TypeError : " , e)

except AssertionError as e:
    print("AssertionError : " , e)

except HighTemperatureError as e:
    print("HighTemperatureError : " , e)
        
'''
    
    


