#to find factors of a whole number using while loop

num = int(input("Enter a (whole)number:"))
factor = 2

if (num == 0):
    print("Every number is a factor of 0.")
elif (num == 1):
    print("1", end = " ")
else:
    print("1", end = " ")
    while factor <= num//2:
        if (num % factor == 0):
            print(factor, end = " ")
        factor += 1
    print(num)
