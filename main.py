from fastapi import FastAPI
from routes import router as task_router
from auth import router as auth_router
from database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(task_router)
app.include_router(auth_router)
