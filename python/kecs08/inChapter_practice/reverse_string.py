#WAP to reverse a string input by the user using a function

def reverse_string(the_string):
    reversed = ''
    for i in range(-1, -len(the_string) - 1, -1):
        reversed += the_string[i] 
    return reversed

your_string = input("Enter a string to reverse it: ")
print(reverse_string(your_string))

# method 2: using slicing

# def reverse_string(the_string):
#     return the_string[::-1]

# your_string = input("Enter a string to reverse it: ")
# print(reverse_string(your_string))
