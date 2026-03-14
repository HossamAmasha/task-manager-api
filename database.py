from pathlib import Path
from sqlmodel import SQLModel, create_engine

BASE_DIR = Path(__file__).resolve().parent
database_url = f"sqlite:///{BASE_DIR / 'tasks.db'}"

engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)