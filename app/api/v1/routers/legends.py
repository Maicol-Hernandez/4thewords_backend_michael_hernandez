from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.services.legend_service import LegendService
from app.schemas.legend import LegendCreate, LegendResponse
from app.api.v1.dependencies import get_db

router = APIRouter(prefix="/v1/legends", tags=["legends"])

@router.get("/", response_model=list[LegendResponse])
def get_legends(db: Session = Depends(get_db)):
    service = LegendService(db)
    return service.get_legends()

@router.post("/", response_model=LegendResponse)
def create_legend(legend_data: LegendCreate, db: Session = Depends(get_db)):
    service = LegendService(db)
    return service.create_legend(legend_data.dict())

