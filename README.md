# Task Manager API

A RESTful Task Manager API built with **FastAPI**, **SQLModel**, and **SQLite**.

This project demonstrates backend development concepts including authentication, database integration, API design, and versioning.

---

## Features

- User registration
- User login with JWT authentication
- Password hashing with bcrypt
- Protected routes
- User-owned tasks
- Create, read, update, and delete tasks (CRUD)
- Search tasks by title
- Filter tasks by completion status
- Sort tasks by creation date
- Pagination support
- Partial updates using PATCH
- Task statistics endpoint
- API versioning (`/api/v1`)

---

## Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn

---

## Project Structure

```
task-manager-api
│
├── auth.py        # Authentication routes (register, login)
├── database.py    # Database engine and configuration
├── main.py        # FastAPI application entry point
├── models.py      # Database models
├── routes.py      # Task routes
├── security.py    # JWT and password hashing
├── README.md
└── .gitignore
```

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/HossamAmasha/task-manager-api.git
cd task-manager-api
```

### 2. Install dependencies

```
pip install fastapi uvicorn sqlmodel python-jose passlib[bcrypt]
```

### 3. Run the server

```
uvicorn main:app --reload
```

### 4. Open the API documentation

FastAPI provides automatic interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

## Authentication

Protected endpoints require a **Bearer token**.

Example header:

```
Authorization: Bearer <your_token>
```

You obtain the token using:

```
POST /auth/login
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|------|------|------|
| POST | /auth/register | Register a new user |
| POST | /auth/login | Login and receive JWT token |

### Tasks

| Method | Endpoint | Description |
|------|------|------|
| GET | /api/v1/tasks | Retrieve tasks |
| GET | /api/v1/tasks/{id} | Retrieve a specific task |
| POST | /api/v1/tasks | Create a new task |
| PATCH | /api/v1/tasks/{id} | Partially update a task |
| DELETE | /api/v1/tasks/{id} | Delete a task |

### Task Utilities

| Method | Endpoint | Description |
|------|------|------|
| GET | /api/v1/tasks/search | Search tasks by title |
| GET | /api/v1/tasks/stats | Task statistics |

---

## Example Task Object

```json
{
  "id": 1,
  "title": "Finish backend project",
  "completed": false,
  "created_at": "2026-03-14T21:30:24",
  "updated_at": "2026-03-14T21:30:24"
}
```

---

## Future Improvements

- Frontend dashboard
- Docker containerization
- PostgreSQL database
- Deployment to the cloud
- Task priorities and due dates

---

## Author

Hossam Amasha
