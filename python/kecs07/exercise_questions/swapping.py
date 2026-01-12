#program with a function to swap the (two) integer parameters if 1 < 2

def swap(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    return (num1, num2)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = swap(a, b)

print(a, b)