from fastapi import APIRouter, Depends
from app.auth.services import AuthService
from app.users.schemas import User, UserCreate, Token, UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model=Token)
async def login_for_access_token(login_data: UserLogin, service: AuthService = Depends()):
    return service.authenticate_user(login_data.username_or_email, login_data.password)

@router.post("/signup", response_model=User)
async def signup(user: UserCreate, service: AuthService = Depends()):
    return service.register_user(user)
