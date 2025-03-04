from sqlmodel import SQLModel, create_engine, Session
import os

DB_NAME = os.getenv("DB_NAME", "test_db")
DB_USER = os.getenv("DB_USER", "app_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "secret123")
DB_HOST = os.getenv("DB_HOST", "mysql")
DB_PORT = os.getenv("DB_PORT", "3306")

# Use asyncmy for asynchronous operations
DATABASE_URL = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Asynchronous driver (app)
engine = create_engine(DATABASE_URL, echo=True)

# Synchronous driver (migrations) - Use mysqlclient
sync_engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(sync_engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)