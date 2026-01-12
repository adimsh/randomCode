#WAP to count the occurences of a character(input by the user) in a string(given by user) using a function

def main():
    inp_string = input("Enter the string you wish to search: \n")
    inp_char = input("Enter the char you are checking for: ")
    result = countChar(inp_string, inp_char)
    print(result)



def countChar(daString, daChar):
    count = 0
    for i in daString:
        if i == daChar:
            count += 1

    return count


if __name__ == "__main__":
    main()