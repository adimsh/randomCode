#to check whether a number is positive, negative or zero

num = int(input("Enter a number: "))

if num > 0:
	print(num, "is positive")
elif num < 0:
	print(num, "is negative")
else: 
	print("It's zero")
