#to check whether a number is palindrom or not
num = int(input("Enter a number: "))

def check_palindrome(num):
    """checks whether num is a palindrome"""
    reverse = 0
    if(num < 10):
        print(num, "is a palindrome.")
    else:
        temp = num
        while temp > 0:
            digit = temp % 10
            temp //= 10
            reverse = reverse * 10 + digit
        if(reverse == num):
            print(num, "is a palindrome.")
        else:
            print(num, "is NOT a palindrome.")

check_palindrome(num)