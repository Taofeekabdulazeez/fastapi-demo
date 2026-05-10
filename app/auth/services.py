from datetime import timedelta
from fastapi import Depends, HTTPException, status
from app.auth.security import verify_password, create_access_token, get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES
from app.users.repository import UserRepository
from app.users.schemas import UserCreate

class AuthService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    def authenticate_user(self, username_or_email: str, password: str):
        user = self.user_repo.get_by_login(username_or_email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    def register_user(self, user: UserCreate):
        db_user = self.user_repo.get_by_username_or_email(user.username, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Username or email already registered")
        
        hashed_pwd = get_password_hash(user.password)
        return self.user_repo.create(username=user.username, email=user.email, hashed_password=hashed_pwd, role=user.role)
