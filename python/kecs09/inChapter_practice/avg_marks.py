# # WAP to calculate average marks of n students using a function where n is entered by the user
# import ast

# while True:
#     try:
#         n = int(input("Enter number of student: "))
#         break
#     except ValueError:
#         print("Invalid input. Enter a numerical value.")

# # to input a list there are following methods:

# # 1. using a loop - but the list can only have one type of items (we can prolly do it using eval but that becomes too complicated and compromised)
# marks1 = []
# for i in range(n):
#     element = int(input(f"Enter marks of student {i + 1}: "))
#     marks1.append(element)

# # 2. using ast.literal_eval() in ast module - we have to enter the list in proper syntax
# while True:
#     usr_inp2 = input("Enter list of marks: ")
#     try:
#         marks2 = list(ast.literal_eval(usr_inp2)) # the list()- makes it so that anything other than a list raises an error
#         break
#     except (ValueError, SyntaxError):
#         print("Enter a list(in proper syntax)")
# # n = len(marks2)


# # 3. using split() on the input string and strip() on individual list items(that split returns)
# usr_inp3 = input("Enter marks of students seperated by commas: ")
# marks3 = [float(item.strip()) for item in usr_inp3.split(",")]

# # 4. using eval()
# marks4 = list(eval(input("Enter marks of students seperated by commas")))
# # here marks seperated by commas are evaluated as a tuple which is converted to list using list()


#actual program

import ast

def calculate_average(marks_list):
    if not marks_list: return 0
    return sum(marks_list) / len(marks_list)

# Using your Method 1 (The most reliable for beginners)
while True:
    try:
        n = int(input("Enter number of students: "))
        if n > 0: break
        print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Enter a numerical value.")

marks = []
for i in range(n):
    while True:
        try:
            # We use float in case marks are 95.5
            val = float(input(f"Enter marks for student {i+1}: "))
            marks.append(val)
            break
        except ValueError:
            print("Invalid marks. Please enter a number.")

avg = calculate_average(marks)
print(f"\nThe average marks of {n} students is: {avg:.2f}")
