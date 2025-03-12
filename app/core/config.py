import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    db_conection: str = os.getenv("DB_CONNECTION", "mysql")
    db_name: str = os.getenv("DB_DATABASE", "app_db")
    db_user: str = os.getenv("DB_USERNAME", "root")
    db_password: str = os.getenv("DB_PASSWORD", "root")
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = os.getenv("DB_PORT", 3306)
    db_url: str = f"{db_conection}+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    app_name: str = "fastapi"
    mysql_root_password: str = "root"
    environment: str = "dev"
    reload: bool = True

    model_config = SettingsConfigDict(extra="forbid")


settings = Settings()
