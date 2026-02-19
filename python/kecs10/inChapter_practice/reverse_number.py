# to reverse a number

num = int(input('Enter a number: '))
num_dup = num # because num will be butchered in method 1

#1. 
reverse = 0
while num > 0:
    reverse = reverse*10 + (num % 10)
    num //= 10
print(reverse)

#2.
num_dup = str(num_dup)
num_dup = num_dup[::-1]
num_dup = int(num_dup)
print(num_dup)