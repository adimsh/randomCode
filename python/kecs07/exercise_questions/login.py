# WAP with a user-defined login function that takes (uid, pwd) as parameters and 
# blocks after 3 unsuccessful login attempts. If login is successful it says login successful

# extra functionalities- adding new uid and pwd and maintaining a dict of uid and pwd

def login(uid, pwd):
    correct_uid = "ADMIN"
    correct_pwd = "St0rE@1"
    count = 0

    while True:
        count += 1
        if count == 3:
            print("Too many unsuccessful login attempts.\nACCOUNT BLOCKED")
            break

        if uid == correct_uid and pwd == correct_pwd:
            print("login successful.")
            break
        else:
            print("Wrong credentials. TRY AGAIN")
        uid = input("Enter user ID: ")
        pwd = input("Enter password: ")

a = input("Enter user ID: ")
b = input("Enter password: ")
login(a, b)