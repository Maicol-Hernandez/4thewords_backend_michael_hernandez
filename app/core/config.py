import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    db_name: str = "test_db"
    db_user: str = "app_user"
    db_password: str = "secret123"
    db_host: str = "mysql"
    db_port: int = 3306

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
