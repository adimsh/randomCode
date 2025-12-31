#To find how high a ladder reaches on a wall given the length of the ladder and the angle it makes with the ground
import math

length = float(input("Enter the length of the ladder(in ft): "))
angle = math.radians(int(input("Enter the angle the ladder makes with the ground:")))

height = round(math.sin(angle)*length, 2)

print(f"The ladder reaches {height}ft on the wall.")