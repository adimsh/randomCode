#to print the appropriate message for a traffic signal

light = input("what is the light color: ").upper()

#we use .upper() which is a string object fuction since the input string can be in any case(lower, upper or mixed)

if light == "RED":
	print("Stop!")
elif light == "ORANGE":
	print("Get ready!")
elif light == "GREEN":
	print("Go!")
else:
	print("invalid input")
