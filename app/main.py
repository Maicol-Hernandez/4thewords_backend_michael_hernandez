from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.api.v1.routers import legends

app = FastAPI()

# Incluir routers
# app.include_router(heroes.router)
app.include_router(legends.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()