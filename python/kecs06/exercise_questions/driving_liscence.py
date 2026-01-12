name = input("Enter you full name:")
age = int(input("Enter your age:"))

if(age<18):
    print(name, "is not eligible to apply for a driving liscence.")
else:
    print(name, "can apply for a driving liscence")