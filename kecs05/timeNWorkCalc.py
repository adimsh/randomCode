#To calculate the time it will take 3 men to complete a piece of work if their individual times are given

x = float(input("Time taken by first man:"))
y = float(input("Time taken by second man:"))
z = float(input("Time taken by third man:"))

time_together = (x*y*z)/(x*y + y*z + z*x)
print("Time taken to complete the work, when all 3 men work together is:", time_together)
