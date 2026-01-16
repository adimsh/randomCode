#WAP to accept a list of n integers(+ve & -ve) then seperate them into two lists and finally print all 3 lists

n = int(input("Enter the number of elements in your list: "))
inp_list = []
for i in range(n):
    item = int(input(f"Enter integer {i + 1}: "))
    inp_list.append(item)

pos_list = []
neg_list = []

for i in inp_list:
    if i < 0:
        neg_list.append(i)
    else:
        pos_list.append(i)

print(inp_list, pos_list, neg_list, sep = "\n")
