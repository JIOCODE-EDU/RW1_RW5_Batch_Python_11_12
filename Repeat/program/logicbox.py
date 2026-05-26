# Main program logic with loop and controlled statements.

while True:
    print("Welcome to the pattern Generator and Number analyzer!!")
    
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == "1":

        while True:
            print("Choose a Pattern type: ")
            print("1. Right-angle Triangle")
            print("2. Pyramid")
            print("3. Left-angled  Triangle")

            pattern_choice = input("Enter your choice:")

            rows = int(input("Enter the number of rows for the pattern:"))
            
            print("\n Parrern:")

            if pattern_choice == "1":

                #  Right-angle Triangle

                    for i in range(1 , rows + 1):
                        print("*" * i)

            elif pattern_choice == "2":

                # Pyramid
                    for i in range(1 , rows + 1):
                        print(" " * (rows-i) , end="")

                        print("*" * (2 * i - 1))

            elif pattern_choice == "3":

                # Left-angle Triangle

                for i in range(1 , rows + 1):
                    print("  " * (rows - i) + "*" * i)
                    
    elif choice == "2":

            start = int(input("Enter start number: "))
            end = int(input("Enter end number:"))

            total = 0

            print()

            for num in range(start , end + 1):
                if num % 2 == 0:
                    print(num , "is even")
                else:
                    print(num , "is Odd")

                total = total + num

            print("\n Sum = " , total)

    elif choice == "3":
        print("Program end.")

    else:
        print("Invalid Choice")
                        
                    

                
                            
