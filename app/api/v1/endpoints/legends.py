from sqlmodel import Session
from app.core.utils import save_uploaded_image
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from typing import Optional
from app.schemas.legend import LegendCreate, LegendResponse
from app.services.legend_service import LegendService
from app.api.v1.dependencies import get_db

router = APIRouter(prefix="/legends", tags=["legends"])


@router.post("/", response_model=LegendResponse)
async def create_legend(legend_data: LegendCreate, image: UploadFile = File(...), db: Session = Depends(get_db)):
    image_url = await save_uploaded_image(image)
    service = LegendService(db)
    return service.create_legend(legend_data.dict(), image_url)

@router.get("/", response_model=list[LegendResponse])
def get_legends(category: Optional[str] = None, province: Optional[str] = None, db: Session = Depends(get_db)):
    service = LegendService(session=db)
    
    return service.get_legends({"category": category, "province": province})

@router.delete("/{id}", status_code=204)
def delete_legend(id: int, db: Session = Depends(get_db)):
    service = LegendService(session=db)
    try:
        service.delete_legend(id)
    except HTTPException as error:
        raise error
