# WAP with a UDF to calculate the sum of all the numbers in a string...
# method 1: using isdigit()
# method 2: using try-except block and ValueError

def sum_of_digits_in_a_string(the_string: str) -> int:
    """this function calculates the sum of all the digits embedded in the given string using the isdigit() built-in function"""
    result = 0
    for i in the_string:
        if i.isdigit():  #we can also use isnumeric()
            result += int(i)
    return result

def sum_of_digits_in_a_string_2(the_string: str) -> int:
    """this function also calculates the sum of all the digits embedded in the string but using the try-except block"""
    result = 0
    for i in the_string:
        try:
            result += int(i)
        except ValueError:
            continue #this is not necessary the loop still continues
    return result

def main():
    inp = input("Enter an alphanumeric string: ")
    x = sum_of_digits_in_a_string(inp)
    y = sum_of_digits_in_a_string_2(inp)
    print(x)
    print(y)

if __name__ == "__main__":
    main()


# chatgpt's one liner method:

# def sum_of_digits(the_string):
#     return sum(int(c) for c in the_string if c.isdigit())

# inp = input("Enter an alphanumeric string: ").strip()
# print("Sum of digits:", sum_of_digits(inp))
