from pydantic import BaseModel,EmailStr
from typing import Optional
class UserRegisterationSchema(BaseModel):
    username : str
    password: Optional[str]
    role: str
    email: EmailStr

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
