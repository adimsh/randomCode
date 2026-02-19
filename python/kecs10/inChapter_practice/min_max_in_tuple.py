# WAP to input n numbers into a tuple and print the max and min

# inp_tuple = eval(input("Enter numbers seperated by commas: "))
# print("Max value: {}\nMin value: {}".format(max(inp_tuple), min(inp_tuple)))

# proper method: 

# 1. make an empty list, take entries using append() then typecast to tuple- more efficient
# 2. make an empty tuple, take entries using concatenation: my_tuple + (num, )- less efficient since every concatenation creates a new tuple

# 2.

my_tuple = ()
n = int(input("Enter number of elements in your tuple: "))

for i in range(n):
    entry = int(input(f"Enter number {i + 1}: "))
    my_tuple += (entry, )

print("Max value: {}\nMin value: {}".format(max(my_tuple), min(my_tuple)))