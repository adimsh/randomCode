#write a program to calculate the factorial of a number input by the user using a function


def calcFact(x):
    """
        to calculate factorial of a number
    """
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

if __name__ == "__main__": #this line makes sure, when this file is imported as a module
                           #the following i/o code doesn't run(as, the entire file runs when it is imported)
    num = int(input("Enter a number to find it's factorial: "))
    print("Factorial of", num, "is :", calcFact(num))