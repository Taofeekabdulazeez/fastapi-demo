from fastapi import APIRouter, Depends
from app.auth.security import get_current_user
from app.todos.services import TodoService
from app.todos.schemas import Todo, TodoCreate
from app.users.models import UserDB

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.get("/", response_model=list[Todo])
async def get_todos(service: TodoService = Depends(), current_user: UserDB = Depends(get_current_user)):
    return service.get_user_todos(current_user.id)

@router.get("/{task_id}", response_model=Todo)
async def get_todo(task_id: int, service: TodoService = Depends(), current_user: UserDB = Depends(get_current_user)):
    return service.get_todo(task_id, current_user.id)

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate, service: TodoService = Depends(), current_user: UserDB = Depends(get_current_user)):
    return service.create_todo(todo, current_user.id)

@router.put("/{task_id}", response_model=Todo)
async def update_todo(task_id: int, new_todo: TodoCreate, service: TodoService = Depends(), current_user: UserDB = Depends(get_current_user)):
    return service.update_todo(task_id, new_todo, current_user.id)

@router.delete("/{task_id}")
async def delete_todo(task_id: int, service: TodoService = Depends(), current_user: UserDB = Depends(get_current_user)):
    service.delete_todo(task_id, current_user.id)
    return {"message": "Todo deleted successfully"}
