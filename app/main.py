from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.api.v1.endpoints import legends

app = FastAPI(root_path="/api/v1")

# Incluir routers
# app.include_router(heroes.router)
app.include_router(legends.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()