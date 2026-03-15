# Task Manager API

A RESTful Task Manager API built with **FastAPI**, **SQLModel**, and **SQLite**.

This project demonstrates backend development concepts including authentication, database integration, API design, filtering, pagination, and secure user-specific data access.

---

# Features

- User registration
- User login with JWT authentication
- Password hashing using bcrypt
- Protected routes using OAuth2 Bearer tokens
- User-specific tasks (each user only sees their own tasks)
- Full CRUD operations for tasks
- Search tasks by title
- Filter tasks by completion status
- Sort tasks by multiple fields
- Pagination support (limit & offset)
- Partial updates using PATCH
- Task statistics endpoint
- Automatic API documentation with Swagger
- SQLite persistent database

---

# Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn

---

# Project Structure

```
task-manager-api
│
├── auth.py        # Authentication routes (register, login, get current user)
├── database.py    # Database configuration and engine
├── main.py        # FastAPI app entry point
├── models.py      # SQLModel database models and schemas
├── routes.py      # Task API routes
├── security.py    # Password hashing and JWT utilities
├── README.md
└── .gitignore
```

---

# How to Run the Project

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

FastAPI automatically generates interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

# Authentication

Protected endpoints require a **Bearer Token**.

Example request header:

```
Authorization: Bearer <your_token>
```

You obtain the token using:

```
POST /api/v1/auth/login
```

You can also check the authenticated user with:

```
GET /api/v1/auth/me
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|------|------|------|
| POST | /api/v1/auth/register | Register a new user |
| POST | /api/v1/auth/login | Login and receive JWT token |
| GET | /api/v1/auth/me | Get the currently authenticated user |

---

## Tasks

| Method | Endpoint | Description |
|------|------|------|
| GET | /api/v1/tasks | Retrieve tasks |
| GET | /api/v1/tasks/{id} | Retrieve a specific task |
| POST | /api/v1/tasks | Create a new task |
| PUT | /api/v1/tasks/{id} | Replace a task |
| PATCH | /api/v1/tasks/{id} | Partially update a task |
| DELETE | /api/v1/tasks/{id} | Delete a task |

---

## Task Statistics

| Method | Endpoint | Description |
|------|------|------|
| GET | /api/v1/tasks/stats | Get statistics for the authenticated user's tasks |

---

# Query Parameters

The `GET /api/v1/tasks` endpoint supports several optional query parameters.

Example:

```
/api/v1/tasks?completed=true&limit=10&offset=0&sort=created_at&search=home
```

| Parameter | Description |
|------|------|
| completed | Filter tasks by completion status |
| limit | Number of tasks to return |
| offset | Number of tasks to skip |
| sort | Sort tasks by `id`, `title`, `created_at`, or `updated_at` |
| search | Search tasks by title |

---

# Example Task Object

```
{
  "id": 1,
  "title": "Finish backend project",
  "completed": false,
  "created_at": "2026-03-14T21:30:24",
  "updated_at": "2026-03-14T21:30:24",
  "owner_id": 2
}
```

---

# Database

The project uses **SQLite** as the database.

The database file is automatically created when the application starts.

```
tasks.db
```

SQLModel automatically creates all tables during application startup.

---

# Security

- Passwords are hashed using **bcrypt**
- Authentication is handled using **JWT tokens**
- Protected routes require **OAuth2 Bearer authentication**
- Users can only access their own tasks

---

# Future Improvements

- Frontend dashboard
- Docker containerization
- PostgreSQL database
- Cloud deployment
- Task priorities and due dates

---

# Author

Hossam Amasha