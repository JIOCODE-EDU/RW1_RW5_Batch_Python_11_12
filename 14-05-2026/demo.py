# Q-5

while True:

    print("\nPress 1 for Pizza")
    print("Press 2 for Burger")
    print("Press 3 for Sandwhich")
    print("Press 4 for Exit\n")

    a = input("Enter Your Choice -_- ")

    match a:

        case '1':
            
                    print("\nPress 1 for Thin Crust")
                    print("Press 2 for Chess Brust")
                    print("Press 3 for Dough Pizza")
                    print("Press 4 for Exit")

                    b = input("Enter Your Choice -_- ")

                    match b:

                        case '1':
                            print("\nHere is your Thin Crust Pizza")

                        case '2':
                            print("\nHere is your Chess Brust")

                        case '3':
                            print("\nHere is your Dough Pizza")

                        case '4':
                            print("\nExiting Pizza Menu.....")
                        

                        case _:
                            print("\nEnter valid Choice")

        case '2':
            print("\nHere is your Burger")

        case '3':
            bread = input("Choose your Bread (White/Brown) -_- ")
            filling = input("Choose your filling (Cheese/Jelly) -_- ")

            print("Here is your Silly sandwhich")
            print("["+bread + " bread + " + filling + " + Hot sause ]")

        case '4':
             print("\nExiting Program.....")
             break


        case _:
            print("\nEnter a valid number")
