#to get name and gender of a person and attach Mr or Ms before it depending on gender(using a function)

name = input("Enter full name: ")
gender = None

while gender not in ('M', 'F'):
    gender = input("Enter gender(M/F): ")

def name_prefix(name, gender):
    if gender == 'M':
        print("Mr "+name)
    else:
        print("Ms "+name)

name_prefix(name, gender)