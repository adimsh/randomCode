#To swap two numbers using a third variable

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("value of first var:", a, "\n", "value of second var:", b, sep = "")

temp = a
a = b
b = temp

print("value of first var:", a, "\n", "value of second var:", b, sep = "")
