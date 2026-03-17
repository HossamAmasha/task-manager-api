# Task Manager Full Stack App

A full-stack Task Manager application built with:

* FastAPI (Backend API)
* SQLModel + SQLite (Database)
* Vanilla HTML, CSS, JavaScript (Frontend)
* Docker & Docker Compose (Containerization)

This project demonstrates backend development concepts such as authentication, database integration, API design, filtering, pagination, and secure user-based data access, along with a frontend that interacts with the API.

---

# Features

## Authentication

* User registration
* User login with JWT authentication
* Password hashing using bcrypt
* Protected routes using OAuth2 Bearer tokens

## Tasks (Backend API)

* Create tasks
* Retrieve tasks (user-specific)
* Retrieve a single task
* Update tasks (PUT)
* Partially update tasks (PATCH)
* Delete tasks

## Advanced Backend Features

* Search tasks by title
* Filter tasks by completion status
* Sort tasks (id, title, created_at, updated_at)
* Pagination (limit & offset)
* Task statistics (total, completed, pending)

## Frontend

* Register page
* Login page
* Dashboard page
* Create tasks
* Toggle task completion
* Delete tasks
* Logout

NOTE:
Some backend features (search, filter, sort, pagination) are implemented in the API but not fully exposed in the frontend UI.

---

# Technologies Used

## Backend

* Python
* FastAPI
* SQLModel
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)
* Uvicorn

## Frontend

* HTML
* CSS
* JavaScript (Fetch API)

## DevOps

* Docker
* Docker Compose

---

# Project Structure

task-manager-api/
│
├── auth.py
├── database.py
├── main.py
├── models.py
├── routes.py
├── security.py
│
├── login.html
├── register.html
├── dashboard.html
├── app.js
├── style.css
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── README.md
└── .gitignore

---

# How to Run the Project

## Running the backend

### Option 1: Run Locally (Without Docker)

#### 1. Install dependencies

pip install fastapi uvicorn sqlmodel python-jose passlib[bcrypt] python-multipart

#### 2. Run backend

uvicorn main:app --reload

Backend:
http://127.0.0.1:8000

Docs:
http://127.0.0.1:8000/docs


### Option 2: Run with Docker

#### Build and run

docker build -t task-manager-api .
docker run -p 8000:8000 task-manager-api

---

### Option 3: Run with Docker Compose (Recommended)

docker compose up --build

API:
http://127.0.0.1:8000/docs

---

### 3. Run frontend

python -m http.server 5500

Open:
http://127.0.0.1:5500/login.html

---

# Authentication Flow

1. Register:
   POST /api/v1/auth/register

2. Login:
   POST /api/v1/auth/login

Returns:
access_token

3. Use token:
   Authorization: Bearer <token>

---

# API Endpoints

## Authentication

POST   /api/v1/auth/register
POST   /api/v1/auth/login
GET    /api/v1/auth/me

## Tasks

GET    /api/v1/tasks
GET    /api/v1/tasks/{id}
POST   /api/v1/tasks
PUT    /api/v1/tasks/{id}
PATCH  /api/v1/tasks/{id}
DELETE /api/v1/tasks/{id}

## Task Statistics

GET    /api/v1/tasks/stats

---

# Query Parameters (Backend Only)

Example:

/api/v1/tasks?completed=true&limit=10&offset=0&sort=created_at&search=home

* completed → filter by status
* limit → number of results
* offset → skip results
* sort → id, title, created_at, updated_at
* search → search by title

---

# Example Task

{
"id": 1,
"title": "Finish backend project",
"completed": false,
"created_at": "2026-03-14T21:30:24",
"updated_at": "2026-03-14T21:30:24",
"owner_id": 2
}

---

# Database

* SQLite database (tasks.db)
* Automatically created on startup
* Each task is linked to a specific user (owner_id)

---

# Security

* Password hashing with bcrypt
* JWT authentication
* Protected routes using OAuth2
* Users can only access their own tasks

---

# Future Improvements

* Connect frontend to search/filter/sort
* Better UI/UX
* PostgreSQL database
* Deployment (Render / AWS)
* Task priorities and due dates

---

# Author

Hossam Amasha