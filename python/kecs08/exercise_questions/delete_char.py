#WAP with a user defined function deleteChar(the_string, del_this) that deletes all occurences of the 'del_this' char from the 'the_string' string

def deleteChar(the_string: str, del_this: str) -> str:
    new_string = ''
    for i in the_string:
        if i == del_this:
            continue
        new_string += i
    return new_string

print(deleteChar(
    input("Enter a string: "),
    input("Enter a char to delete: ")
))

# __________________________________________________________________________________________

# we can also do this using (these can support substrings as well): 

# 1. the find()/index() function along with slicing or len() (find is preffered over index since that raises a ValueError if the substring isn't found)
# 2. the replace() function
# 3. the split() and join() function or joining the split parts using a loop

#3.2- 

# def deleteChar(the_string,  del_this):
#     deleted_string = ''
#     x = the_string.split(del_this)
#     for i in x:
#         deleted_string += i
#     return deleted_string

#3.1- 

# def deleteChar(the_string, del_this):
#     return ''.join(the_string.split(del_this))