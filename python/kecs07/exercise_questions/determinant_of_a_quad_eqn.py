#to calculate the determinant/discriminant b^2-4ac of a quadratic eqn and output it's interpretation

print(f"For a quad eqn of the form: a(x)^2 + b(x) + c\nEnter the values of a, b and c respectively.")
a = int(input())
b = int(input())
c = int(input())


def determinant(a, b, c):
    det = b**2 - 4*a*c
    if det > 0:
        print("The quad eqn has 2 distinct roots.")
    elif det == 0:
        print("The quad eqn has 2 equal roots.")
    else:
        print("The quad eqn has no real roots.")

determinant(a,b,c)