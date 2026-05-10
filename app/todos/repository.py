from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.todos.models import TodoDB
from app.todos.schemas import TodoCreate

class TodoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_by_user(self, owner_id: int):
        return self.db.query(TodoDB).filter(TodoDB.owner_id == owner_id).all()

    def get_by_id_and_user(self, task_id: int, owner_id: int):
        return self.db.query(TodoDB).filter(TodoDB.task_id == task_id, TodoDB.owner_id == owner_id).first()

    def create(self, todo: TodoCreate, owner_id: int):
        db_todo = TodoDB(
            title=todo.title,
            description=todo.description,
            done=todo.done,
            owner_id=owner_id
        )
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def update(self, db_todo: TodoDB, new_todo: TodoCreate):
        db_todo.title = new_todo.title
        db_todo.description = new_todo.description
        db_todo.done = new_todo.done
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def delete(self, db_todo: TodoDB):
        self.db.delete(db_todo)
        self.db.commit()
