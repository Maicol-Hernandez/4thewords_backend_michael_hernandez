from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.database import create_db_and_tables
from app.api.v1.endpoints import legends

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mounts the "app/static" directory at the "/static" path
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
# app.include_router(heroes.router)
app.include_router(legends.router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()