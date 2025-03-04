from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.services.hero_service import HeroService
from app.schemas.hero import HeroCreate, HeroResponse
from app.api.v1.dependencies import get_db

router = APIRouter(prefix="/v1/heroes", tags=["heroes"])

@router.get("/", response_model=list[HeroResponse])
def get_heroes(db: Session = Depends(get_db)):
    service = HeroService(db)
    return service.get_heroes()

@router.post("/", response_model=HeroResponse)
def create_hero(hero_data: HeroCreate, db: Session = Depends(get_db)):
    service = HeroService(db)
    return service.create_hero(hero_data.dict())