#Input- User's name and age
#Output- A message telling the user when they will turn 100yo

name = input("Enter your name:")
age = int(input("Enter your current age: "))
curr_year = int(input("What year is it right now?"))

cent_year = 100-age+curr_year

print(f"My boy, {name}! You will turn 100 years old in the year {cent_year}.")
