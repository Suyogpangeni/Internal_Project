from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

password_hasher = PasswordHasher()

class PasswordEncryption():
    def __init__(self,password):
        self.password=password
    def Hashing(self):
        HashedPasswored=password_hasher.hash(self.password)
        return HashedPasswored
    def VerifyPassword(self, hashed_password):
        try:
            return password_hasher.verify(hashed_password, self.password)
        except (VerifyMismatchError, VerificationError):
            return False
