#to find the sum of the sequence: 1/(x**3), for x = [1, n(given by user)]

n = int(input("Enter a number: "))

result = 0
for i in range(1, n+1):
    term = 1/(i**3)
    result += term
    print("1/("+str(i)+"^3) ", end = " ")
    if i == n:
        continue
    print("+", end = " ")

print("= ", result)