#to print the following pattern:

# 12345
#  1234
#   123
#    12
#     1

for y in range(1, 6):
    for x in range(1, 6):
        if x -y >= 0:
            print(x-y+1, end = "")
        else:
            print(" ", end = "")
    print()