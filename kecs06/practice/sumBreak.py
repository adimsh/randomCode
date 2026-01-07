#To add all the numbers entered by a user till he enters a negative number

num = float(input("Enter number:"))
add = 0

while True:
    add += num
    num = float(input("Enter number:"))
    if num < 0:
        break
print("Sum: ", int(add))
