#WAP to calculate value of exponentiation given power and base using function

base = int(input("Enter base value: "))
power = int(input("Enter power: "))

def calcPow(b, p):
    result = 1
    for i in range(p):
        result *= b
    return result

print(calcPow(base, power))