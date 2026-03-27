from features.auth.model.Users import Users
from database.connection import get_db
from fastapi import HTTPException
from utils.security import PasswordEncryption

class UserLogin():
    def __init__(self, payload):
        self.data = payload
    
    def RegisterUser(self):
        with get_db() as db:
            existing_user= db.query(Users).filter(Users.useremail == self.data.email).first()
            if existing_user:
                raise HTTPException(status_code=400, detail="Duplicate entry Email already exist")
            NewUser= Users(
                username= self.data.username,
                useremail=self.data.email,
                password = PasswordEncryption(self.data.password).Hashing(),
                role = self.data.role,
                firstlogin= True
            )
            db.add(NewUser)
            db.commit()
            db.refresh(NewUser)
            return NewUser
        
        
    def LoginUser(self):
        with get_db() as db:
            existing_user = db.query(Users).filter(Users.useremail == self.data.email).first()
            if not existing_user:
                raise HTTPException(status_code=404, detail="Sorry user not found")

            if existing_user.isdeleted:
                raise HTTPException(status_code=403, detail="User account is inactive")

            password_is_valid = PasswordEncryption(self.data.password).VerifyPassword(existing_user.password)
            if not password_is_valid:
                raise HTTPException(status_code=401, detail="Invalid email or password")

            return existing_user
