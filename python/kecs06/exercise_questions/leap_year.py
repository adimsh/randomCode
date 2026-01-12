#to check if the year entered by a user is  leap year or not

year = int(input("Enter year to check whether it is a leap year: "))

if (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year.")
elif(year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")