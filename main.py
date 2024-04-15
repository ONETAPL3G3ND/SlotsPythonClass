#slots helps save memory due to the fact that we immediately indicate the variables that will be created,
# thereby we allocate memory only for them. But there is one disadvantage of this method.
# Because adding a new variable takes more time

class user:
    __slots__ = ("username", "password")

    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.money = 0 AttributeError: 'user' object has no attribute 'money'

if __name__ == "__main__":
    User = user("Kilka", "pass0110")

    print(User.username)
