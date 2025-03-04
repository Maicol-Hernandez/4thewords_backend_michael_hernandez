from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.api.v1.routers import heroes #, items

app = FastAPI()

# Incluir routers
app.include_router(heroes.router)
# app.include_router(items.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()