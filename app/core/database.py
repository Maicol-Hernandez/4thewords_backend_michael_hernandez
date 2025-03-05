import os
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings


# Use asyncmy for asynchronous operations
DATABASE_URL = os.getenv("DATABASE_URL", f"mysql+mysqldb://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}")

# Asynchronous driver (app)
engine = create_engine(DATABASE_URL, echo=True)

# Synchronous driver (migrations) - Use mysqlclient
sync_engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(sync_engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)