from features.auth.services import UserLogin
from fastapi import APIRouter
from features.auth.schemas.login import UserRegisterationSchema
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
