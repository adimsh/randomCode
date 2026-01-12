#write a program to accept a number, pass it as an argument in the function and increment it by 5.
#Then display the id() of the argument(before function call) and id() of the parameter before and after increment.

num = int(input("Enter a number: "))

print(id(num))

def incr(x):
    print(id(x))
    x += 5
    print(id(x))

incr(num)