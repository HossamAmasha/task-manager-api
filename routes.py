from fastapi import APIRouter, HTTPException, status, Query ,Depends
from sqlmodel import Session, select
from sqlalchemy import desc
from datetime import datetime, timezone
from models import Task, TaskCreate, TaskUpdate, User, TaskStats
from database import engine
from auth import get_current_user

router = APIRouter(prefix="/api/v1", tags=["Tasks"])

@router.get("/")
def home():
    return {"message": "Welcome to the Task Manager API"}

@router.get("/tasks", response_model=list[Task])
def get_tasks(
    completed: bool | None = None,
    limit: int = Query(default=10, ge=1 ,le=100), # limits the number of tasks to return (incase of huge number of tasks)
    offset: int = Query(default=0, ge=0),  # returns from the first (if = 5 skips the first 5)
    sort: str = Query(default="id"),
    search: str | None = None,
    current_user: User = Depends(get_current_user)
              ):
    
    with Session(engine) as session:

        statement = select(Task).where(Task.owner_id == current_user.id)

        if completed is not None:
            statement = statement.where(Task.completed == completed)

        if search:
            statement = statement.where(Task.title.contains(search))

        if sort == "title":
            statement = statement.order_by(Task.title)
        elif sort == "created_at":
            statement = statement.order_by(Task.created_at)
        elif sort == "updated_at":
            statement = statement.order_by(Task.updated_at)
        else:
            statement = statement.order_by(Task.id)

        statement = statement.offset(offset).limit(limit)

        tasks = session.exec(statement).all()
        return tasks
    
@router.get("/tasks/stats", response_model=TaskStats)
def get_task_stats(current_user: User = Depends(get_current_user)):
    with Session(engine) as session:

        user_tasks = session.exec(select(Task).where(Task.owner_id == current_user.id)).all()

        total = len(user_tasks)
        completed = sum(1 for task in user_tasks if task.completed)
        pending = total - completed

        return TaskStats(
            total=total,
            completed=completed,
            pending=pending
            )

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int,
             current_user: User = Depends(get_current_user)
             ):
    
    with Session(engine) as session:
        task = session.get(Task, task_id)

        if task is None or task.owner_id != current_user.id:
            raise HTTPException(status_code=404, detail="Task not found")
        
        return task

@router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def add_task(task: TaskCreate,
             current_user: User = Depends(get_current_user)
             ):
    
    with Session(engine) as session:

        new_task = Task(
            title=task.title,
              completed=task.completed,
              owner_id=current_user.id
              )
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return new_task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int, 
    updated_task: TaskCreate,
    current_user : User = Depends(get_current_user)
    ):

    with Session(engine) as session:
        task = session.get(Task, task_id)

        if task is None or task.owner_id != current_user.id:
            raise HTTPException(status_code=404, detail="Task not found")

        task.title = updated_task.title
        task.completed = updated_task.completed
        task.updated_at = datetime.now(timezone.utc)
        session.commit()
        session.refresh(task)
        return task
    
@router.patch("/tasks/{task_id}", response_model=Task)
def patch_task(
    task_id: int,
    updated_task: TaskUpdate,
    current_user: User = Depends(get_current_user)
):
    
    with Session(engine) as session:
        task = session.get(Task, task_id)

        if task is None or task.owner_id != current_user.id:
            raise HTTPException(status_code=404, detail="Task not found")
        
        if updated_task.title is not None:
            task.title = updated_task.title

        if updated_task.completed is not None:
            task.completed = updated_task.completed

        task.updated_at = datetime.now(timezone.utc)

        session.commit()
        session.refresh(task)
        return task
              

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user)
    ):

    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task is None or task.owner_id != current_user.id:
            raise HTTPException(status_code=404, detail="Task not found")

        session.delete(task)
        session.commit()
        return {"message": "Task Deleted"}

