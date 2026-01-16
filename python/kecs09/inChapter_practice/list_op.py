#write a menu driven program to perform various list operations

import ast
the_list = []

while True:
    print("Current status:", the_list, "\n")
    print("L I S T - O P E R A T I O N S", end = "\n\n")
    print("1. Create a new list")
    print("2. Append an element")
    print("3. Insert an element") 

    # print("4. Append a list(nested list)") - no need for this now since 2 takes care of it
    # we can do it like this tho(instead of using eval() like NCERT which is very unsafe against injection attacks.)
    # usr_inp = input("Enter list elements seperated by commas...")
    # list_to_append = [item.strip() for item in usr_inp.split(",")]


    print("4. Modify an existing element")
    print("5. Delete an existing element by it's position")
    print("6. Delete an existing element with a given value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Exit", end = "\n\n")

    option = input("Choose an option!")
    while True:
        try:
            option = int(option)
            if 1 <= option <= 9:
                break
            else:
                option = input("Please choose a number between 1 and 10.")
        except ValueError:
            option = input("Choose a valid option")


    if option == 1:
        the_list = []

    elif option == 2:
        element = input("Enter element to append: ") # if we simply did int here we won't be able to get any other kinds of input
        try: 
            element = ast.literal_eval(element)
        except (ValueError, SyntaxError):
            pass
        the_list.append(element)
    
    elif option == 3:
        while True:
            try:
                pos = int(input("Choose the position where you want to insert the element: "))
                if pos in range(1, len(the_list) + 1):
                    break
                else:
                    print("Enter a valid position...")
            except ValueError:
                print("Enter position in numerals...")
        index = pos - 1
        usr_inp = input("Enter an element to insert: ")
        try:
            element = ast.literal_eval(usr_inp)
        except (ValueError, SyntaxError):
            pass
        the_list.insert(index, element)

    elif option == 4:
        pos = int(input("Choose the position you wish to modify: "))
        index = pos - 1
        element = input("Enter the new element: ")
        the_list[index] = element

    elif option == 5:
        pos = int(input("Choose the position you wish to delete: "))
        index = pos - 1
        popped = the_list.pop(index)
        print("Deleted", popped, "at position", pos)

    elif option == 6:
        this_element = int(input("Choose the value you wish to delete: "))
        the_list.remove(this_element)
        print("Deleted", this_element)

    elif option == 7:
        the_list.sort()

    elif option == 8:
        the_list.sort(reverse = True)

    elif option == 9:
        break