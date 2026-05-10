from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from todos.schemas import Todo

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    role: Optional[str] = "user"

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None

class User(UserBase):
    id: int
    role: str
    todos: List[Todo] = []

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str
