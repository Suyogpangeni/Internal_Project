from argon2 import PasswordHasher

class PasswordEncryption():
    def __init__(self,password):
        self.password=password
    def Hashing(self):
        HashedPasswored=PasswordHasher().hash(self.password)
        return HashedPasswored
    
