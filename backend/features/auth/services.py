from features.auth.model.Users import Users
from database.connection import get_db

from utils.security import PasswordEncryption

class UserLogin():
    def __init__(self,payload):
        self.data=  payload
    
    
    def RegisterUser(self):
        with get_db() as db:
            NewUser= Users(
                username= self.data.username,
                useremail=self.data.email,
                password = PasswordEncryption(self.data.password).Hashing(),
                role = self.data.role
            )
            db.add(NewUser)
            db.commit()
            db.refresh(NewUser)
            return NewUser
    
