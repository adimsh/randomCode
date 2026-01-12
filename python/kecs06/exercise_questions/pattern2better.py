#to print the following pattern
#    1
#   212
#  32123
# 4321234
#543212345

num = int(input("Enter a positive integer: "))
for y in range(num):
    for x in range(-num + 1, num):
        if abs(x) <= y:
            print(abs(x) + 1, end = "")
        else:
            print(" ", end = "")
    print()