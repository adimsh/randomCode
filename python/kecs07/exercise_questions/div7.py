#to check divisibility of a number by 7 using a function

def main():
    num = int(input("Enter a number to check if it is divisible by 7: "))
    result = div7(num)
    if result:
        print(num, "is divisible by 7")
    else:
        print(num, "is NOT divisible by 7")

# Type hints serve as clear documentation for developers reading your code. By looking at the function signature, 
# another programmer (or even you months later) can immediately understand what kind of data the function expects as input.
def div7(n: int) -> bool: #there are lots of other ways, like using enums to enforce strict typechecking
    if n % 7 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
