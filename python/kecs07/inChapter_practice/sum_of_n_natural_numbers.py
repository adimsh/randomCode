#a program to generate sum of n natural numbers using a function

num = int(input("Enter the number: "))

def sumN(x):
    temp = 0
    for i in range(x):
        temp += i+1
    return temp


print("sum of", num, "natural numbers is:", sumN(num))