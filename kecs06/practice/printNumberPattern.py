#to print a number pattern for an integer input

num = int(input("Enter a number(natural):"))

for i in range(1, num+1):
    for j in range(i):
        print(j+1, end = " ")
        j += 1
    print()