# Password Check with Limited Attempts

def check_password():
    correct_password = "python 123"
    attempts=4
    while(attempts > 0):
        password=input("enter the password:")
        if password == correct_password:
            print("Acess granted")
            break
        else:
            attempts-=1
            print("Attempts left : ",attempts)

check_password()


