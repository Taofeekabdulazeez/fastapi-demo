from fastapi import APIRouter, Depends
from app.auth.security import get_current_admin_user
from app.users.services import UserService
from app.users.schemas import User, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_admin_user)]
)

@router.get("/", response_model=list[User])
async def get_users(service: UserService = Depends()):
    return service.get_all_users()

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, service: UserService = Depends()):
    return service.get_user(user_id)

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate, service: UserService = Depends()):
    return service.update_user(user_id, user_update)

@router.delete("/{user_id}")
async def delete_user(user_id: int, service: UserService = Depends()):
    service.delete_user(user_id)
    return {"message": "User deleted successfully"}
