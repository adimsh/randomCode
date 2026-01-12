#this one can search for any sub-string no matter the length

def count_occurence(daString, subString):
    return daString.count(subString)

def main():
    inp_string = input("Enter string you wish to search in: \n")
    inp_sub_string = input("Enter sub-string you wish to search for: \n")

    print(count_occurence(inp_string, inp_sub_string))


if __name__ == "__main__":
    main()
