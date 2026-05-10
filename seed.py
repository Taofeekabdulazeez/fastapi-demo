import os
from core.database import SessionLocal, engine, Base
from todos.models import TodoDB
from users.models import UserDB
from auth.security import get_password_hash

# Ensure tables are created
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    
    try:
        # Check if database already has users to prevent duplicate seeding
        if db.query(UserDB).count() > 0:
            print("Database already contains data. Skipping seeding.")
            return

        print("Seeding database with initial users and to-do items...")
        
        # Create users (default password: "password123")
        hashed_pwd = get_password_hash("password123")
        user1 = UserDB(username="john_doe", email="john@example.com", hashed_password=hashed_pwd, role="admin")
        user2 = UserDB(username="jane_smith", email="jane@example.com", hashed_password=hashed_pwd, role="user")
        
        db.add_all([user1, user2])
        db.commit()
        db.refresh(user1)
        db.refresh(user2)
        
        todos = [
            TodoDB(title="Buy groceries", description="Milk, eggs, bread", done=False, owner_id=user1.id),
            TodoDB(title="Finish project", description="Complete the FastAPI demo", done=False, owner_id=user1.id),
            TodoDB(title="Call mom", description="Catch up with family", done=True, owner_id=user1.id),
            TodoDB(title="Go for a run", description="5km run in the park", done=False, owner_id=user1.id),
            TodoDB(title="Read a book", description="Read 2 chapters of 1984", done=False, owner_id=user1.id),
            TodoDB(title="Clean the house", description="Vacuum and dust", done=True, owner_id=user2.id),
            TodoDB(title="Pay bills", description="Electricity and internet", done=False, owner_id=user2.id),
            TodoDB(title="Learn a new skill", description="Practice guitar for 30 mins", done=False, owner_id=user2.id),
            TodoDB(title="Plan vacation", description="Look up flights to Japan", done=False, owner_id=user2.id),
            TodoDB(title="Walk the dog", description="Take Buster to the park", done=True, owner_id=user2.id),
        ]

        db.add_all(todos)
        db.commit()
        print(f"Successfully seeded database with 2 users and {len(todos)} to-do items.")
    except Exception as e:
        print(f"An error occurred during seeding: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
