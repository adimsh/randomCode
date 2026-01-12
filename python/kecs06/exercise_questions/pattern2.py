#to generate the following pattern:

#     1
#    212
#   32123
#  4321234
# 543212345

num = int(input("Enter a number: "))

for i in range(1, num+1):
    print(" "*(num-i), end = "")
    for j in range(i, 0, -1):
        print(j, end = "")
    for j in range(2, i+1):
        print(j, end = "")
    print()
