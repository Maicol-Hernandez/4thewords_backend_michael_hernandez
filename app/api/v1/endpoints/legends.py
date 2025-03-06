from sqlmodel import Session
from app.core.utils import save_uploaded_image
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Form
from typing import Optional
from app.schemas.legend import LegendCreate, LegendResponse
from app.services.legend_service import LegendService
from app.api.v1.dependencies import get_db

router = APIRouter(prefix="/legends", tags=["legends"])


@router.post("/", response_model=LegendResponse)
async def create_legend(legend_data: str = Form(...), image: UploadFile = File(...), db: Session = Depends(get_db)):
    data = LegendCreate.model_validate_json(legend_data)

    image_url = await save_uploaded_image(image)
    service = LegendService(db)

    return service.create_legend(data.model_dump(), image_url)


@router.get("/", response_model=list[LegendResponse])
def get_legends(
    name: Optional[str] = None,
    created_at: Optional[str] = None,
    category: Optional[str] = None,
    province: Optional[str] = None,
    canton: Optional[str] = None,
    district: Optional[str] = None,
    db: Session = Depends(get_db)
):
    service = LegendService(db)

    return service.get_legends({
        "name": name,
        "created_at": created_at,
        "category": category,
        "province": province,
        "canton": canton,
        "district": district
    })


@router.put("/{id}", response_model=LegendResponse)
async def update_legend(id: int, legend_data: str = Form(...), image: UploadFile = File(...), db: Session = Depends(get_db)):
    data = LegendCreate.model_validate_json(legend_data)

    image_url = await save_uploaded_image(image)
    service = LegendService(db)

    return service.update_legend(id, data.model_dump(), image_url)


@router.delete("/{id}", status_code=204)
def delete_legend(id: int, db: Session = Depends(get_db)):
    service = LegendService(db)
    try:
        service.delete_legend(id)
    except HTTPException as error:
        raise error
