import time
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings


def get_engine(max_retries=5, retry_interval=2):
    for i in range(max_retries):
        try:
            engine = create_engine(settings.db_url, echo=True)
            # Prueba la conexión
            with engine.connect() as conn:
                pass
            return engine
        except Exception as e:
            if i < max_retries - 1:
                print(
                    f"Error connecting to database: {e}. Retrying in {retry_interval} seconds..."
                )
                time.sleep(retry_interval)
            else:
                raise


# Asynchronous driver (app)
engine = get_engine()

# Synchronous driver (migrations) - Use mysqlclient
sync_engine = get_engine()


def get_session():
    with Session(sync_engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
