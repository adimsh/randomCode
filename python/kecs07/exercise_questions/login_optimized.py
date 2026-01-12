def login(uid: str, pwd: str):
    correct_uid = "ADMIN"
    correct_pwd = "St0rE@1"

    attempts = 1

    while attempts <= 3:
        if uid == correct_uid and pwd == correct_pwd:
            print("login successful!")
            break
        else:
            if attempts == 3:
                print("ACCOUNT BLOCKED")
            else:
                print("WRONG CREDENTIALS! Try Again...")
                uid = input("user ID: ")
                pwd = input("password: ")


login(
    input("user ID: "),
    input("password: ")
)
    
