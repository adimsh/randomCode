#to get num and den of a fraction as an input and determining whether it is improper, if yes passing it into a function 'mixedFraction()' to find out it's mixed equivalent
#if the den of the improper fraction is 1 the function tells the user, it is a whole number, same for when num % den == 0 

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

def mixedFraction(n, d):
    if d == 1 or n % d == 0:
        print(n, "/", d, "is a whole number i.e.", int(n % d))
    else:
        whole = n//d
        numerator = n % d
        print(n, "/", d, "is an improper fraction and it's mixed fraction representation is", whole, "(", numerator, "/", d, ")")

if num >= den:
    mixedFraction(num, den)
else:
    print(num, "/", den, "is a proper fraction")