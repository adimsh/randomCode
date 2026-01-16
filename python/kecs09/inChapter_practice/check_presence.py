# Write a user-defined function to check if a number is present in the list or not. If the number is present, return the position of the number. Print an appropriate message if the number is not present in the list.

def check_presence(element, the_list: list):
    if element in the_list:                 # we can also do this using the try-catch block i.e. if the index() raises a ValueError that means the element is not in the list
        a = the_list.index(element)
        print(f"{element} is in {the_list} at index {a}")
        return a
    else:
        print(element, "is not in", the_list)
        return 0

my_list = []
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    item = int(input("Enter an element"))
    my_list.append(item)

check_presence(int(input("Enter number you want to check for: ")), my_list)

