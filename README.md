# FastAPI ToDo API

A robust, feature-rich FastAPI application demonstrating a scalable architecture, PostgreSQL database integration, and JWT-based authentication with role-based access control.

## Architecture

This project is structured using a feature-based, modular architecture, making it highly scalable and easy to maintain:

- `core/`: Contains core configurations like the database connection (`database.py`).
- `auth/`: Contains the JWT security logic and authentication routers (`/auth/login`, `/auth/signup`).
- `users/`: Contains User models, schemas, and endpoints. Endpoints are restricted to **Admin** users only.
- `todos/`: Contains Todo models, schemas, and endpoints. Each Todo is linked to the authenticated user.
- `seed.py`: A utility script to populate the database with mock data.

## Features

- **PostgreSQL Integration**: Uses SQLAlchemy as the ORM to manage database records.
- **JWT Authentication**: Secure login using Bearer tokens (powered by `PyJWT` and `passlib[bcrypt]`).
- **Role-Based Access Control**: Users have roles (`user`, `admin`). Only admins can access the `/users` management endpoints.
- **1-to-Many Relationships**: Users own their ToDo items. A user can only see, update, and delete their own ToDos.

## Prerequisites

- Python 3.9+ installed on your system.
- PostgreSQL database running locally or remotely.

## Getting Started

Follow these steps to run the application locally on your Windows machine:

### 1. Set Up Environment Variables

Create a `.env` file in the root directory and add your PostgreSQL database URL along with a secret key for JWT generation:

```env
DATABASE_URL=postgresql://your_db_user:your_db_password@localhost:5432/your_db_name
SECRET_KEY=your-super-secret-key-123
```

### 2. Activate the Virtual Environment

Activate the virtual environment (`venv`) using the following command in your terminal (PowerShell or Command Prompt):

```bash
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages from the terminal. The core dependencies include:

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy psycopg2-binary python-dotenv passlib "bcrypt==3.2.2" PyJWT python-multipart
```

*(Note: You can also freeze your dependencies by running `pip freeze > requirements.txt` and install via `pip install -r requirements.txt`)*

### 4. Seed the Database (Optional)

The application will automatically create the database tables when the server starts. However, you can instantly populate the database with initial mock users and to-do items by running:

```bash
python seed.py
```
*Note: This creates an admin user (`john_doe`) and a regular user (`jane_smith`). The password for both is `password123`.*

### 5. Run the Application

Start the development server with live reload enabled:

```bash
uvicorn main:app --reload
```

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can explore and test your endpoints here:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### How to Test Authentication in Swagger
1. Go to the Swagger UI page (`/docs`).
2. Click the green **Authorize** button at the top right.
3. Enter the credentials of a seeded user (e.g., Username: `john_doe` and Password: `password123`).
4. Click **Authorize**. FastAPI will securely retrieve the JWT and automatically attach your Bearer token to all subsequent protected requests!
