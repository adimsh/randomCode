#To check whether a given number is an Armstrong number...

num = int(input("Enter a number:"))

#if num < 10
if num < 10:
	print("Yay!", num, "is an Armstrong number.")

#to check the number of digits in the number
digits = 0
temp_num = num

while temp_num > 0:
	digits += 1
	temp_num //= 10
	
#armstrong logic
og = num
total = 0
while num > 0:
	temp = num % 10
	num = num // 10
	total += temp**digits
	
#final verdict
if total == og:
	print("Yay!", og, "is an Armstrong number.")
else: 
	print("Alas!", og, "is not an Armstrong number.")
