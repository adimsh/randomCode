def insert(the_list, element, index):
    the_list.append(0) # to make space
    for i in range(len(the_list) - 1, index, -1):
        the_list[i] = the_list[i - 1]
    the_list[index] = element
    return the_list

n = int(input("Enter number of elements: "))
inp_list = []
for i in range(n):
    item = int(input(f"Enter element {i + 1}: "))
    inp_list.append(item)

print(inp_list)
value = int(input("Enter value to insert: "))
pos = int(input("Enter position in list: ")) - 1

print(insert(inp_list, value, pos))