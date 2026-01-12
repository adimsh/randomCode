#a program to see the use the keyword 'global'

num = 4
x = 79


def myFunction():
    num = 5 #this creates a local variable with the same name and the global num is hidden from the function block
    print(num)
    global x #the global keyword prevents formation of local variable x instead makes global x accessible inside the fucntion
    x = 99
    print(x)

myFunction()