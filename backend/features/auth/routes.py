from features.auth.services import UserLogin
from fastapi import APIRouter
from features.auth.schemas.login import UserRegisterationSchema, UserLoginSchema
router= APIRouter(prefix="/Authentication",tags=["Authentication"])

@router.post("/RegisterUser")
def register_user_endpoint(
    data: UserRegisterationSchema,
):
    new_user = UserLogin(data).RegisterUser()
    return {
        "message": "User registered successfully",
        "user": {
            "username": new_user.username,
            "email": new_user.useremail,
            "role": new_user.role
        }
    }

@router.post("/LoginUser")
def login_user_endpoint(
    data: UserLoginSchema,
):
    user = UserLogin(data).LoginUser()
    return {
        "message": "Login successful",
        "user": {
            "username": user.username,
            "email": user.useremail,
            "role": user.role,
            "firstlogin": user.firstlogin,
        }
    }
