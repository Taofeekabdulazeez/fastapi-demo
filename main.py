from fastapi import FastAPI
from app.core.database import engine, Base

# Import models before calling create_all
from app.users.models import UserDB
from app.todos.models import TodoDB

from app.auth.router import router as auth_router
from app.users.router import router as users_router
from app.todos.router import router as todos_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI ToDo Demo API")

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(todos_router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI ToDo API"}
