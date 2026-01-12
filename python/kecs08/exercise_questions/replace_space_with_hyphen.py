# WAP with a UDF that accepts a string argument where each word is seperated with a space and returns the string after replacing spaces with hypen(-) symbols
# method 1- using replace() -- too direct -- discouraged
# method 2 - manual

def replace_space_with_hyphen(the_string: str) -> str:
    result = ''
    for i in the_string:
        if i == " ":
            result += '-'
            continue
        result += i
    return result

print(replace_space_with_hyphen(input("Enter a string: ")))
        