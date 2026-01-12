#To swap two numbers without using a third variable

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("value of first var:", a, "\n", "value of second var:", b, sep = "")

a, b = b, a

print("value of first var:", a, "\n", "value of second var:", b, sep = "")
