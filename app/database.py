from sqlmodel import create_engine, SQLModel, Session
import os

# Use asyncmy for asynchronous operations
DB_URL = os.getenv("DB_URL", "mysql+asyncmy://app_user:secret123@mysql/test_db")

# Asynchronous driver (app)
async_engine = create_engine(DB_URL, echo=True)

# Synchronous driver (migrations) - Use mysqlclient
sync_engine = create_engine(DB_URL.replace("+asyncmy", "+mysqldb"), echo=True)

def get_session():
    with Session(sync_engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(sync_engine)