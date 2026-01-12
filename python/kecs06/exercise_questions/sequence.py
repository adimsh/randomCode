#generate n terms of the following sequence: -5, 10, -15, 20, -25, ...

n = int(input("Enter number of terms: "))

for i in range(n):
    mag = 5*(i+1)
    if(i % 2 == 0):
        sign = -1
    else:
        sign = 1
    print(mag*sign, end = ", ")
