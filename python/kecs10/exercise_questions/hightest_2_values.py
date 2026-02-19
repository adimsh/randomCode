# WAP to find the highest 2 values in a dictionary

my_dict = {
    'apples': 12,
    'bananas': 7,
    'oranges': 15,
    'mangoes': 4,
    'grapes': 20
}

def H2V(x: dict) -> tuple:
    if not x:
        print("Empty dictionary...")
    elif len(x) == 1:
        print("The dictionary has a single element: ", x)
    else:
        largest = s_largest = float('-inf')
        for i in x:                 # we can do this- for value in x.values():
            if x[i] > largest:
                largest, s_largest = x[i], largest
            elif x[i] > s_largest and x[i] != largest:
                s_largest = x[i]
            
        if s_largest == float('-inf'):
            print("All values in the dict are same...")
            print(x)
        else:
            return largest, s_largest

print(H2V(my_dict))

# we can do this in two turns as well