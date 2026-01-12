#WAP with 2 functions: 
#light(color)- returns 0, 1, 2 depending on the value of string color is 'RED', 'BLUE' or 'GREEN'
#traffic_light()- takes color input(and checks validity) and calls light() to get corresponding integer value, 
#                   then prints a message corresponding to each value.

def traffic_light():

    color = input("What is the color of the traffic light? ")
    while color not in ('RED', 'YELLOW', 'GREEN'):
        color = input("Enter a valid color in CAPITAL letters: ")

    value = light(color)

    if value == 0:
        print("STOP, your life is precious")
    elif value == 1:
        print("Please go SLOW")
    else:
        print("GO! Thankyou for being patient")

def light(color):
    if color == 'RED':
        return 0
    elif color == 'YELLOW':
        return 1
    else:
        return 2

traffic_light()
print("SPEED THRILLS BUT KILLS")
