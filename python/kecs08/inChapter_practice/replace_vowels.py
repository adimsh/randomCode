# WAP w/ a user-defined function that accepts a string as an argument and replaces all vowels with *

# def rep_vowels(the_string):
#     for vowel in ('a', 'e', 'i', 'o', 'u'):
#         the_string = the_string.replace(vowel, '*')
#     return the_string

# inp_string = input("Enter a string: \n")
# print(rep_vowels(inp_string))



#Now without using the replace() function

# def rep_vowels(the_string):
#     vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

#     for i in the_string:
#         if i in vowels:
#             i = '*'  >>> we can't do this since strings are immutable
    
#     return the_string



def rep_vowels(the_string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    stringList = []

    for i in the_string:
        if i in vowels:
            i = '*'
        stringList.append(i)
    
    return ''.join(stringList) #str() would just change the entire list representation into a string

inp_string = input("Enter a string: \n")
print(rep_vowels(inp_string))

#another way to do this is to concatenate elements one by one starting from an empty string
#because even though we cannot replace characters in a list we can still concatenate to it
#that way we won't even need to use a list