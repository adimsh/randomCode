#to add the digits of a number

num = int(input("Enter a number to add it's digits: "))
result = 0
og = num

while num > 0:
    digit = num % 10
    num //= 10
    result += digit

print("sum of digits of", og, "is:", result)