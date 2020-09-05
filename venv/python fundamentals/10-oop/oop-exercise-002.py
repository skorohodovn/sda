class User():
    def __init__(self, name):
        self.name = name

    def set_password(self, password):
        if len(password) < 6:
            password += "#" * (6 - len(password))
            self.__password = password
        else:
            self.__password = password

    def get_password(self):
        pass_len = len(self.__password)
        return self.__password[0] + (pass_len-2) * "*" + self.__password[-1]

    def del_pass(self):
        del self.__password


user_1 = User("nikolai")
user_1.set_password("abc")
print(f"{user_1.get_password()}")

user_2 = User("sergei")
user_2.set_password("123")

user_3 = user_1
user_1.set_password("jgjrkgljf")

print(f"{user_1.get_password()}")
print(f"{user_3.get_password()}")