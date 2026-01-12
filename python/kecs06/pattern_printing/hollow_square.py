N = int(input("Enter length of side of the square(unit: *)- "))
radius = N//2

for y in range(radius, -radius - 1, -1):
    for x in range(-radius, radius+1):
        if abs(x) == radius or abs(y) == radius:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()

#better solution(works for even values)-

# N = int(input("Enter length of side of the square: "))

# for i in range(N):
#     for j in range(N):
#         if i == 0 or i == N-1 or j == 0 or j == N-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
