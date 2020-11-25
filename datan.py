import encryption
class database:
    def __init__(self,filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.current_usern = None
        self.load()

    def load(self):
        self.file = open(self.filename, "rb")
        self.users = {}
        for line in self.file:
            username,password,secret = line.strip().split(b"!!")
            username = encryption.decrypt(username)
            password = encryption.decrypt(password)
            secret = encryption.decrypt(secret)
            self.users[username] = [password,secret]

        self.file.close()

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            return False

    def validate(self, username, password):
        if self.get_user(username):
            if self.users[username][0] == password:
                self.current_usern = username
                return True
        else:
            return False

    def add_user(self,username,password):
        if username.strip() not in self.users:
            self.users[username.strip()] = [password.strip(),"hi"]
            self.save()
            return True
        else:
            return False
    def save(self):
        with open(self.filename, "wb") as f:
            for user in self.users:

                user_e = encryption.encrypt(user)
                password_e = encryption.encrypt(self.users[user][0])
                secret_e = encryption.encrypt(self.users[user][1])
                f.write(user_e +b"!!"+ password_e +b"!!"+secret_e+b"\n")

    def change_sec(self,secret):
        self.users[self.current_usern][1] = secret
    def find_secret(self):
        return self.users[self.current_usern][1]
