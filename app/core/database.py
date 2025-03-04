from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

# DB_NAME = os.getenv("DB_NAME", "test_db")
# print(f"Hello {DB_NAME} from Python")
# DB_USER = os.getenv("DB_USER", "app_user")
# DB_PASSWORD = os.getenv("DB_PASSWORD", "secret123")
# DB_HOST = os.getenv("DB_HOST", "mysql")
# DB_PORT = os.getenv("DB_PORT", "3306")

# Use asyncmy for asynchronous operations
DATABASE_URL = f"mysql+mysqldb://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

# Asynchronous driver (app)
engine = create_engine(DATABASE_URL, echo=True)

# Synchronous driver (migrations) - Use mysqlclient
sync_engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(sync_engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)