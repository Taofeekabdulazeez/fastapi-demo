from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from auth.security import get_current_user
from todos.models import TodoDB
from todos.schemas import Todo, TodoCreate
from users.models import UserDB

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.get("/", response_model=list[Todo])
async def get_todos(db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    todos = db.query(TodoDB).filter(TodoDB.owner_id == current_user.id).all()
    return todos

@router.get("/{task_id}", response_model=Todo)
async def get_todo(task_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    todo = db.query(TodoDB).filter(TodoDB.task_id == task_id, TodoDB.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    db_todo = TodoDB(
        title=todo.title,
        description=todo.description,
        done=todo.done,
        owner_id=current_user.id
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.put("/{task_id}", response_model=Todo)
async def update_todo(task_id: int, new_todo: TodoCreate, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    db_todo = db.query(TodoDB).filter(TodoDB.task_id == task_id, TodoDB.owner_id == current_user.id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db_todo.title = new_todo.title
    db_todo.description = new_todo.description
    db_todo.done = new_todo.done
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete("/{task_id}")
async def delete_todo(task_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    db_todo = db.query(TodoDB).filter(TodoDB.task_id == task_id, TodoDB.owner_id == current_user.id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
