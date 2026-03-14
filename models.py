from typing import Optional
from sqlmodel import SQLModel, Field

class TaskBase(SQLModel):
    title: str
    Task_Done: bool = False

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class TaskCreate(TaskBase):
    pass