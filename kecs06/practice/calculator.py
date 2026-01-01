#to create a simple calculator that performs the 4 basic arithmetic operations.
#the - operator always returns the positive difference.
#if the divisor is 0 for the / operator the system asks the user to enter another number.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator(+, -, *, /): ")

while num2 == 0 and op == '/':
	print("The divisor can't be zero for the division operator.\nPlease enter another number", sep = "")
	num2 = float(input("Enter second number: "))
	
if op == '+':
	add = num1 + num2 #we shouldn't use sum as an identifier since it is a python keyword
	print("sum of", num1, "and", num2, "is:", add)
	
elif op == '-':
	if num1 > num2:
		diff = num1 - num2
	else:
		diff = num2 - num1
	print("difference of", num1, "and", num2, "is:", diff)
	
elif op == '*':
	product = num1 * num2
	print("product of", num1, "and", num2, "is:", product)

elif op == '/':
	quotient = num1 / num2
	print("quotient of", num1, "and", num2, "is:", quotient)
	
else:
	print("invalid operation. Goodbye!")
