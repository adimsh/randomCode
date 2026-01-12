#a program to accept the first and last names entered by the user and greet them hello using a function

fname = input("Enter first name: ")
lname = input("Enter last name: ")

def greetings(fn, ln):
    fln = fn + " " + ln
    print("Hello!", fln)

greetings(fname, lname)