from typing import Optional
from pydantic import BaseModel, ConfigDict

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    task_id: int
    owner_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)
