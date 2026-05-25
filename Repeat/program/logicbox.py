# Main program logic with loop and controlled statements.
'''
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

            if pattern_choice in ["1" , "2" , "3"]:
                while True:
                    rows = input("Enter the number of rows for the pattern:")

                    if rows.isdigit():
                        
                        rows = int(rows)

                        if rows < 0:
                            print("Number of row must be positive")

                    else:
                        print("Invalid Input. Please enter an integer.")

                print("\n Parrern:")

                if pattern_choice == "1":

                    #  Right-angle Triangle
'''
for i in range(1 , 6):
    for j in range(i + 2):
        print(j , end="")
    print()

                        
                    

                
                            
