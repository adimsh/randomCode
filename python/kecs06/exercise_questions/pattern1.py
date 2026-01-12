#to print the diamond pattern i.e.
#   *  
#  ***
# *****
#  ***
#   *

# for i in range (1, 4):
#     print(" "*(3-i)+"*"*(2*i-1)+" "*(3-i))
# for i in range(2, 0, -1):
#     print(" "*(3-i)+"*"*(2*i-1)+" "*(3-i))

#Competitive approach:
N = int(input("Enter size of grid: "))
radius = N//2

for y in range(radius, -radius - 1, -1):
    for x in range(-radius, radius + 1):
        if abs(x) + abs(y) <= radius:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()