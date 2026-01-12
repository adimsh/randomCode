import math

# Basic arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

# Trigonometric and logarithmic functions
def log10(x):
    if x <= 0:
        return "Logarithm undefined"
    return math.log10(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)


while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. log10(x)")
    print("6. sin(x)")
    print("7. cos(x)")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == 4:
        a = float(input("Enter dividend: "))
        b = float(input("Enter divisor: "))
        print("Result:", divide(a, b))

    elif choice == 5:
        x = float(input("Enter value of x: "))
        print("Result:", log10(x))

    elif choice == 6:
        x = float(input("Enter angle in radians: "))
        print("Result:", sin(x))

    elif choice == 7:
        x = float(input("Enter angle in radians: "))
        print("Result:", cos(x))

    elif choice == 8:
        print("Exiting calculator...")
        break

    else:
        print("Invalid choice")
