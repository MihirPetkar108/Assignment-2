def isValid(Username, Password):
    if not Username.isalnum():
        print("Error: Username must be alphanumeric")
        return False
    
    if len(Password) < 8:
        print("Error: Password must be at least 8 characters long")
        return False
    
    print("Login Successful")
    return True


Username = input("Enter your username: ")
Password = input("Enter your password: ")

isValid(Username, Password)