from fastapi import APIRouter
from sqlmodel import Session, select

from models import Task, TaskCreate
from database import engine

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to the Task Manager API"}

@router.get("/tasks")
def get_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        return tasks

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task:
            return task
        return {"error": "Task not found"}

@router.post("/tasks")
def add_task(task: TaskCreate):
    with Session(engine) as session:
        new_task = Task(title=task.title,Task_Done=task.Task_Done)
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return {"message": "Task Added", "task": new_task}

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task:
            task.title = updated_task.title
            task.Task_Done = updated_task.Task_Done
            session.commit()
            session.refresh(task)
            return {"message": "Task Updated", "task": task}
        return {"error": "Task not found"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task:
            session.delete(task)
            session.commit()
            return {"message": "Task Deleted"}
        return {"error": "Task not found"}