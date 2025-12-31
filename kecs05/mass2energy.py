#To calculate energy from a given mass using the formula: E = mc^2
from scipy import constants as const

mass = float(input("Enter the mass of the object(in grams):"))

energy = mass*const.c**2

print("Energy generated:", energy, "J")