from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.users.models import UserDB
from app.users.schemas import UserUpdate

class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_by_id(self, user_id: int):
        return self.db.query(UserDB).filter(UserDB.id == user_id).first()

    def get_by_username(self, username: str):
        return self.db.query(UserDB).filter(UserDB.username == username).first()

    def get_by_username_or_email(self, username: str, email: str):
        return self.db.query(UserDB).filter((UserDB.email == email) | (UserDB.username == username)).first()

    def get_by_login(self, login_str: str):
        return self.db.query(UserDB).filter((UserDB.email == login_str) | (UserDB.username == login_str)).first()

    def get_all(self):
        return self.db.query(UserDB).all()

    def create(self, username: str, email: str, hashed_password: str, role: str):
        new_user = UserDB(username=username, email=email, hashed_password=hashed_password, role=role)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update(self, db_user: UserDB, user_update: UserUpdate):
        if user_update.username is not None:
            db_user.username = user_update.username
        if user_update.email is not None:
            db_user.email = user_update.email
        if user_update.role is not None:
            db_user.role = user_update.role
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, db_user: UserDB):
        self.db.delete(db_user)
        self.db.commit()
