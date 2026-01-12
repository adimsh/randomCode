#to print the smallest and largest of 5 numbers entered by the user

num = int(input("Enter first number: "))
smlst = num
grtst = num

for i in range(4):
    num = int(input("Enter next number: "))
    if num > grtst:
        grtst = num
    elif num < smlst:
        smlst = num

print(f"smallest: {smlst}, greatest: {grtst}")