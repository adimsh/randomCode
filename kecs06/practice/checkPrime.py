#to check whether given number is prime or not

num = int(input("Enter a number(whole): "))

if num == 0 or num == 1:
    print(num, "is neither prime nor composite.")
else:
    i = 2
    flag = 0 #prime
    while i >= 2 and i <= int(num**0.5):
        if num % i == 0:
            flag = 1
            break
        i += 1
    if flag == 0:
        print("Prime")
    else:
        print("Composite")

    