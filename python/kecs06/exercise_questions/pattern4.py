#to generate the following pattern:

#   *
#  * *
# *   *
#  * *
#   *

# for i in range(3, 0, -1):
#     print(" "*(i-1), end = "")
#     print("*"+" "*(((3-i)*2)-1), end = "")
#     if(i<3):
#         print("*", end = "")
#     print()

# for i in range(1, 3):
#     print(" "*i, end = "")
#     print("*"+" "*(2-i), end = "")
#     if(i<2):
#         print("*", end = "")
#     print()


#competitive approach

#basically, we have to plot the stars at radius of length 2 from the center
N = int(input("Enter size of square: "))
radius = N//2

for y in range(radius, -radius - 1, -1):
    for x in range(-radius, radius + 1):
        if abs(x) + abs(y) == radius:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()