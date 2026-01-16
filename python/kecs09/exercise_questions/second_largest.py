# Write a function to find the second largest number from a list of numbers

def second_largest(a_list):
    largest = a_list[0]
    second_largest = largest

    for i in a_list:
        if i > largest:
            largest, second_largest = i, largest
    return second_largest

print(second_largest([4, 5, 77, -33, 21, 88, 67, 898, 00, -983]))

# there's actually a buncha problems with this...
# 1. if the second largest number never actually becomes the largest... like if l = 23, sl = 10 and we encounter 21, then it should become sl but it doesn't here.
# 2. if the first value is the greatest... like [40, 30, 20, 10]-- making the sl = l is the problem here
# 3. if there is less than 2 elements in the list
# 4. if there is only one distinct element i.e. all elements are same

# better approach
def second_largest_revised(a_list):
    if len(a_list) < 2:
        return None
    else:
        l = sl = float('-inf')
        for i in a_list:
            if i > l:
                l, sl = i, l
            elif i > sl and i != l: # this second condition prevent duplicates of l to become sl
                sl = i
        # this is an edge case like: [-9, -9, -9] -- here sl remains -inf till the end
        if sl == float('-inf'):
            return None
        else:
            return sl


print(second_largest_revised([4, 5, 77, -33, 21, 88, 67, 898, 00, -983]))


# best approach
def second_largest_peak_pythonic(a_list):
    a_set = set(a_list) # removes duplicates (FAAHHHHH!!!)
    a_set.remove(max(a_set)) # since there is only one ocurrence of the largest anyways (FAAHHHHH!!!)
    return max(a_set) # FAAHHHHH!!!

print(second_largest_peak_pythonic([4, 5, 77, -33, 21, 88, 67, 898, 00, -983]))

