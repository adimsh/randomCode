# Write a program to input names of n students and
# store them in a tuple. Also, input a name from the
# user and find if this student is present in the tuple or not.

n = int(input("Enter total number of students: "))
names = tuple()
for i in range(n):
    name = input(f"Enter name {i + 1}: ")
    names += (name, )

# 1. Using a user defined function
# def search_name(a_name: str) -> bool:
#     if not a_name:
#         print("Blank string...")
#     else:
#         flag = 0
#         for i in names:
#             if i == a_name:
#                 flag = 1
#                 break
#         return bool(flag)

# improvement in above function---
# def search_name(a_name):
#     for i in names:
#         if i == a_name:
#             return True
#     return False

        
# inp = input("Enter a name to search: ")
# check = search_name(inp)
# if check:
#     print("found the name brodi!!!")
# else:
#     print("it's not in here dawg...")


# 2. Using built in function

inp = input("Enter a name to search: ")
try:
    check = names.index(inp)
    print("found the name brodi!!!")
except ValueError:
    print("it's not in here dawg...")
