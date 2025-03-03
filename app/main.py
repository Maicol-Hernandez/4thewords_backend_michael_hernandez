from typing import Union
from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.models import Hero, Team
from app.database import create_db_and_tables, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.get("/heroes")
def get_heroes(session: Session = Depends(get_session)):
    heroes = session.query(Hero).all()
    return heroes
    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}