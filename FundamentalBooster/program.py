# Fundametal Booster - Interactive Personal Data Collector

#====== Welcome section ===

print("Welcome to the Interactive Personal Data Collector!")

print("\n This will collect your personal information.")

print("\n perform some calculation , and show you data type details.")

print("\n Let's get started!!!")

#====== collect information section ========


print("=" * 50)

name = input("Please Enter your name: ")

age_str = input("Please Enter your age: ")

age = int(age_str)

height_str = input("Please Enter your height in meters:")

height=  float(height_str)

fav_num_str = input("Please Enter your favourite number:")

fav_num = int(fav_num_str)


#========= data processing ===========

print("\n" + "=" * 50)

print("Processing your data..........")

print("=" * 50)

# calculate birth year

cur_year = 2026

birth_year = cur_year - age

# Calculate height to centimeter

height_cm = height * 100


# perform some arithmetic operation

sum_value=  age + fav_num

product_value = age * fav_num

# Type conversion

height_as_int = int(height)

age_as_float = float(age)

age_as_string = str(age)

# display result

print("\n" + "=" * 50)

print("Thank you! you here is the information we collected:")

print("=" * 50)

# Display each variable with its type and memory address

print(f"\n Variable Details:")

print(f"name:{name} -> type:{type(name)} -> Address:{id(name)}")

print(f"age:{age} -> type:{type(age)} -> Address:{id(age)}")

print(f"height:{height} -> type:{type(height)} -> Address:{id(height)}")

print(f"favourite number:{fav_num} -> type:{type(fav_num)} -> Address:{id(fav_num)}")


# ====== Display conversion ========

print("=" * 50)

print("Type Conversion")

print("=" * 50)

print(f"\n Height as integer : {height_as_int} -> type:{type(height_as_int)}")

print(f"\n Age as float : {age_as_float} -> type:{type(age_as_float)}")

print(f"\n Age as string : {age_as_string} -> type:{type(age_as_string)}")

# ===== Display Operation ======

print("=" * 50)

print("Calulated results:")

print("=" * 50)

print(f"\n Your height in centimeter: {height_cm}cm")

print(f"Approximately! your birth year: {birth_year}")

print(f"\n Sum of your age and favourite number : {sum_value}")

print(f"\n Product of your age and favourite number: {product_value}")

# String Concatination

greeting = "Hello , " + name + "!"

message = f"Your Favourite number is {fav_num}"

print(f" -> '{greeting}'")

print(f" -> type:{type(greeting)}")

print(f" -> Address:{id(greeting)}")

print(f" -> '{message}'")

print(f" -> type:{type(message)}")

print(f" -> Address:{id(message)}")

# ====== Summary Table =========

print("=" * 50)

print("Summary Table:")

print("=" * 50)

print(f"\n {'variable':<20}{'value':<20} {'type':<25} {'id':<15}")

print(f"\n {'name':<20} {str(name):<20} {str(type(name)):<25} {id(name):<15}")

# ==== Closing Message=====

print("=" * 50)

print("Thank you for using the personal data collector!!")

print("=" * 50)

print("\n You've successfully explore:")

print("\n input() and print() functions")

print("\n String , integer and Float data types")

print("\n Atrithmetic Operation( + , - , * , /).")

print("type() and id() built-in functions")

print("String Concatination")

print("Type casting")

print("=" * 50)




















