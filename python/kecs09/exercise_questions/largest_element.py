#write a program that returns the largest element of the list passed as parameter

def return_largest(a_list):
    if not a_list:
        return None
    else:
        largest = a_list[0]
        for i in a_list: # we can do for i in a_list[1:] i.e. slicing to avoid comparing the first element to itself
            if i > largest:
                largest = i
        return largest

print(return_largest([4, 56, -999]))