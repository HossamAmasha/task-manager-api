from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class TaskBase(SQLModel):
    title: str
    completed: bool = False

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    owner_id: int = Field(foreign_key="user.id")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    title: str | None = None
    completed: bool | None = None

class UserBase(SQLModel):
    username: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

class UserCreate(UserBase):
    password: str

class UserPublic(SQLModel):
    id: int
    username: str

class TaskStats(SQLModel):
    total: int
    completed: int
    pending: int

class Token(SQLModel):
    access_token: str
    token_type: str
