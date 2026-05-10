from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class TodoDB(Base):
    __tablename__ = "todos"

    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("UserDB", back_populates="todos")
