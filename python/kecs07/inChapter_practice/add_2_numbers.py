#program to add 2 numbers and display their sum using a user-defined function

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def addition(x, y): 
    add = x + y
    return add

print(addition(num1, num2))