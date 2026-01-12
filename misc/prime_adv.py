#A more efficient way to find out whether a number is prime or composite

a = int(input("Enter a number:\n"))

if(a <= 1):
	print(a, "is neither a prime number nor a composite number.")
else:
	for x in range(2, int(a**0.5)+1):
		if(a%x == 0):
			print(a, "is a composite number.")
			exit()

print(a, "is a prime number.")
