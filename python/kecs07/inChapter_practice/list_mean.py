#to input a list(of numbers) and calculate it's mean using a user-defined function that accepts a list variable as an argument
#we are also going to keep the name for the argument and parameter(in the function header) same

myList = []
flag = 0 #okay input

n = int(input("Enter number of elements in your list:"))
for i in range(n):
    while flag == 0:
        try:
            print("Enter element", i + 1, ":")
            element = int(input())
            flag = 1
        except ValueError:
            print("Invalid input, enter a number")
    myList.append(element)
    flag = 0

#better 'pythonic' way

# myList = []

# n = int(input("Enter number of elements in your list: "))

# for i in range(n):
#     while True:
#         try:
#             element = int(input(f"Enter element {i + 1}: "))
#             myList.append(element)
#             break   # exit loop when input is valid
#         except ValueError:
#             print("Invalid input, enter a number")

# print(myList)

def list_mean(myList):
    sum_of_obs = 0
    for i in myList:
        sum_of_obs += i
    mean = sum_of_obs/len(myList) #or we can make a count var and set it to 0 then increment it by 1 in the above for loop for each iteration
    return mean

print(list_mean(myList))

