# FastAPI Demo

A simple FastAPI application demonstration.

## Prerequisites

- Python 3.7+ installed on your system.

## Getting Started

Follow these steps to run the application locally on your Windows machine:

### 1. Activate the Virtual Environment

It looks like a virtual environment (`venv`) is already set up in the project directory. Activate it using the following command in your terminal (PowerShell or Command Prompt):

```bash
.\venv\Scripts\activate
```

### 2. Install Dependencies

If you haven't already installed the required packages, you'll need `fastapi` and `uvicorn` (an ASGI server used to run FastAPI applications):

```bash
pip install fastapi "uvicorn[standard]"
```

*Note: You can also freeze your dependencies later by running `pip freeze > requirements.txt`.*

### 3. Run the Application

Start the development server with live reload enabled (this means the server will automatically restart when you make code changes):

```bash
uvicorn main:app --reload
```

### 4. Access the Application

Once the server is running, you can access the application in your browser at the following URLs:

- **Root Endpoint:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **About Endpoint:** [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about)

#### Interactive API Documentation
FastAPI automatically generates interactive API documentation based on your code. You can explore and test your endpoints here:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
