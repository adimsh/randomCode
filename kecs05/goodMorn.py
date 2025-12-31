#To repeat GOOD MORNING n times

while True:
	try:
		n = int(input("Enter a number:"))
		break
	except ValueError:
		print("Please enter a valid number:")

for i in range(n):
	print("GOOD MORNING", sep = "\n")
