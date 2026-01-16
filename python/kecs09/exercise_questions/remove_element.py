#write a program that reads a list and write a function to delete an element either by value or by index

def delete_by_value(the_list, the_value):
    if not the_list:
        print("The list is empty")
    elif the_value not in the_list:
        print("The value is not in the list")
    else:
        ind = the_list.index(the_value)
        for i in range(ind, len(the_list) - 1):
            the_list[i] = the_list[i + 1]
        return the_list[:len(the_list) - 1]

def delete_by_index(the_list, index):
    if not the_list:
        print("The list is empty")
    elif index not in range(len(the_list)):
        print("Index out of bound")
    else:
        for i in range(index, len(the_list) - 1):
            the_list[i] = the_list[i + 1]
        return the_list[:len(the_list) - 1]


inp_list = []
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    item = int(input("Enter element {}: ".format(i + 1)))
    inp_list.append(item)
print(inp_list)


while True:
    option = int(input("Choose 1 to delete an element by value, 2 to delete an element by index~\n"))
    if option == 1:
        new_list = delete_by_value(inp_list, int(input("Enter value to delete: ")))
        break
    elif option ==2:
        new_list = delete_by_index(inp_list, int(input("Enter index of the element to delete: ")))
        break
    else:
        print("invalid input")
print(new_list)
        