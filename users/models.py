from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

class UserDB(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    
    todos = relationship("TodoDB", back_populates="owner", cascade="all, delete-orphan")
