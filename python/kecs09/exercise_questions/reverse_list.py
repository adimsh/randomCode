def reverse(the_list):
    return the_list[::-1]

n = int(input("Enter number of elements: "))
inp_list = []
for i in range(n):
    item = int(input(f"Enter element {i + 1}: "))
    inp_list.append(item)

print(reverse(inp_list))