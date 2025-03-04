from fastapi import Depends, HTTPException, Query
from sqlmodel import Session
from app.services.legend_service import LegendService
from app.schemas.legend import LegendCreate, LegendResponse
from app.api.v1.dependencies import get_db

router = APIRouter(prefix="/v1/legends", tags=["legends"])

@router.get("/", response_model=list[LegendResponse])
def get_legends(*, db: Session = Depends(get_db), offset: int = 0, limit: int = Query(default=100, le=100)):
    service = LegendService(db)
    return service.get_legends()

@router.post("/", response_model=LegendResponse)
def create_legend(*, db: Session = Depends(get_db),legend: LegendCreate):
    service = LegendService(db)
    return service.create_legend(legend.dict())

