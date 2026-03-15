# Task Manager API

A REST API for managing tasks built with **FastAPI**, **SQLModel**, and **SQLite**.

## Features

- Create tasks
- Retrieve all tasks
- Retrieve a specific task
- Update tasks
- Delete tasks
- Persistent storage using SQLite

Each task contains:
- id
- title
- Task_Done (completion status)

## Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite

## How to Run the Project

1. Install dependencies:

```
pip install fastapi uvicorn sqlmodel
```

2. Run the server:

```
uvicorn main:app --reload
```

3. Open the API docs in your browser:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get a single task |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Author

Hossam Amasha
