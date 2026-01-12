#WAP to check if a string input by the user is a palindrome using a user-defined function

def palin(st):
    i = 0            # first index
    j = len(st)-1    # last index

    while i <=j : 
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
    
    return True

your_string = input("Enter a string to check whether it is a palindrome or not: ")

if palin(your_string):
    print("It is a palindrome")
else:
    print("It ain't a palindrome")
