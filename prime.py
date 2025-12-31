#To check if a number is prime or composite

a = int(input("Enter a number:\n"))
count = 0

if(a == 1):
	print("1 is neither a prime number nor a composite number.")

for x in range(1, a//2 + 1):
	if(a%x == 0):
		count += 1

if (count == 1):
	print(a, "is a prime number.")
else:
	print(a, "is a composite number with", count+1, "factors.")
