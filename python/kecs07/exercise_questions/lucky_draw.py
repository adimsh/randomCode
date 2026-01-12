#to generate a random number b/w 1 and 600(boundary values included)
from random import randint as check

def main():
    token = -1

    while True:
        try:
            token = int(input("Enter your token number: "))

            if token in range(1, 601):
                break
            else: 
                print("Invalid token number. Try again!")

        except ValueError:
            print("Invalid entry. Enter a number.")

    draw(token)

def draw(x):
    if check(1, 600) == x:
        print("Yay! You won.")
    else: 
        print("Sorry! Better luck next time.")

if __name__ == "__main__":
    main()
