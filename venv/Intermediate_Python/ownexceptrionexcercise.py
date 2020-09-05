class PasswordTooShort(Exception):
    pass

class PasswordTooLong(Exception):
    pass

class InvalidPassword(Exception):
    pass

def validatepassword():
    input_password = input("Input password:")
    if len(password) < 3:
        raise PasswordTooShort()

