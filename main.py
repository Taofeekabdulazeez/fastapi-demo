from fastapi import FastAPI
from core.database import engine, Base

# Import models before calling create_all
from users.models import UserDB
from todos.models import TodoDB

from auth.router import router as auth_router
from users.router import router as users_router
from todos.router import router as todos_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI ToDo Demo API")

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(todos_router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI ToDo API"}
