#to find all primes between 2 given numbers
print("Enter a range:")
start = int(input())
stop = int(input())

for num in range(start+1, stop):
    if num == 1:
            continue
    divisor = 2
    flag = 0 #prime
    while divisor >= 2 and divisor <= int(num**0.5):
        if num % divisor == 0:
            flag = 1
            break
        divisor += 1
    if flag == 0:
        print(num, "is prime")