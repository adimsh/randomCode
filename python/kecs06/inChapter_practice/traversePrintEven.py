#to print even numbers from a given list of numbers

n = int(input("Enter the number of elements in the list:"))

myList = []

for i in range(n):
    element = int(input(f"Enter {i+1}th number: "))
    myList.append(element)

for i in myList:
    if(i % 2 == 0):
        print(i, end = "\t")