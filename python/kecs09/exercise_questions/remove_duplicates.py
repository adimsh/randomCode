# program to read a list of elements and remove duplicates from it


n = int(input("Enter no of elements: "))
a_list = []
for i in range(n):
    item = int(input(f"Enter item {i + 1}: "))
    a_list.append(item)

i = 0
while i < len(a_list):  # don't use for loop here since in this, the range(to iterate) is calculated only once at the start and remove() inside the loop messes with the control flow
    j = i + 1
    while j < len(a_list):  # don't use n as the size of the list keeps changing
        if a_list[i] == a_list[j]:
            a_list.pop(j) # we don't have to increment j after poping since the next element shifts back to j anyways
        else:
            j += 1
    i += 1

print(a_list)

# the best approach

unique_list = []

for i in a_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)

