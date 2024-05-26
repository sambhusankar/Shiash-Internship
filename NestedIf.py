#check user Credentials by a UserAuth system
username = "sankar"
password = "sankar@123"
def UserAuthentication():
    print("..............Welcome to my Authentication System....................")
    user_name = input("Please enter your username :  ")
    if username == user_name:
        user_password = input("Please enter your password :   ")
        if user_password == password:
            print("You are logged in successfully ", username)
        else:
            print("Wrong password")
    else:
        print("We are not finding your username ")
        print("Try Again    Thank you....")

UserAuthentication()