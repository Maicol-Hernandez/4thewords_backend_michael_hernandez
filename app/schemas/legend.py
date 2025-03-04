from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LegendCreate(BaseModel):
    name: str
    category: str
    description: str
    legend_date: str
    province: str
    canton: str
    district: str
    
class LegendResponse(LegendCreate):
    id: int
    image_url: str
    created_at: datetime
    