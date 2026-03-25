from auth.model.Users import Users
from auth.schemas.login import UserRegisterationSchema
from database.connection import get_db
class UserLogin():
    def __init__(slef):
        pass
    async def RegisterUser(data:UserRegisterationSchema):
        NewUser= Users(
            username= data.username,
            useremail=data.email,
            
        )
        