num = int(input("Enter a number to find it's factorial:"))

if num < 0:
    print("Negative numbers do not have a factorial.")
elif num == 0 or num == 1:
    print("Factorial of ", num, "is 1.")
else:
    fact = 1
    for i in range(2, num+1):
        fact *= i
    print("Factorial of", num, "is", fact)