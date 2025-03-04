import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    db_name: str = "test_db"
    db_user: str = "app_user"
    db_password: str = "secret123"
    db_host: str = "mysql"
    db_port: int = 3306
    
    app_name: str = "fastapi"
    mysql_root_password: str = "root"
    environment: str = "dev"
    reload: bool = True
    
    model_config = SettingsConfigDict(extra="forbid")

settings = Settings()
