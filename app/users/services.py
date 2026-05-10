from fastapi import Depends, HTTPException
from app.users.repository import UserRepository
from app.users.schemas import UserUpdate

class UserService:
    def __init__(self, repo: UserRepository = Depends()):
        self.repo = repo

    def get_all_users(self):
        return self.repo.get_all()

    def get_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update_user(self, user_id: int, user_update: UserUpdate):
        db_user = self.repo.get_by_id(user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repo.update(db_user, user_update)

    def delete_user(self, user_id: int):
        db_user = self.repo.get_by_id(user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        self.repo.delete(db_user)
