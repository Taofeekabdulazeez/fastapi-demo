from fastapi import Depends, HTTPException
from app.todos.repository import TodoRepository
from app.todos.schemas import TodoCreate

class TodoService:
    def __init__(self, repo: TodoRepository = Depends()):
        self.repo = repo

    def get_user_todos(self, owner_id: int):
        return self.repo.get_by_user(owner_id)

    def get_todo(self, task_id: int, owner_id: int):
        todo = self.repo.get_by_id_and_user(task_id, owner_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def create_todo(self, todo: TodoCreate, owner_id: int):
        return self.repo.create(todo, owner_id)

    def update_todo(self, task_id: int, new_todo: TodoCreate, owner_id: int):
        db_todo = self.repo.get_by_id_and_user(task_id, owner_id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return self.repo.update(db_todo, new_todo)

    def delete_todo(self, task_id: int, owner_id: int):
        db_todo = self.repo.get_by_id_and_user(task_id, owner_id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        self.repo.delete(db_todo)
