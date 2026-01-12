num = int(input("Enter a number to see it's multiplication table:"))

# for i in range(10):
#     print(f"{num} x {i+1} = {num*(i+1)}")

# doing the same thing using a function

def mul_table(x):
    """this function prints out multiplication table of a number upto 10"""
    for i in range(1, 11):
        value = x*i
        print(x, "x", i, "=", value)

mul_table(num)