#to traverse through a list of given numbers

n = int(input("Enter number of elements in the list: "))
myList = []

for i in range(n):
    element = input(f"Enter element {i+1}:\n")
    try:
        myList.append(int(element))
    except ValueError:
        myList.append(element)
#we can use nested try-except blocks for checking multiple data types like: int, float, etc.

print(f"Your list is:\n {myList}")
    