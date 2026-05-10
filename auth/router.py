from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.database import get_db
from auth.security import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from users.models import UserDB
from users.schemas import User, UserCreate, Token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
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

@router.post("/signup", response_model=User)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter((UserDB.email == user.email) | (UserDB.username == user.username)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_pwd = get_password_hash(user.password)
    new_user = UserDB(username=user.username, email=user.email, hashed_password=hashed_pwd, role=user.role)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
