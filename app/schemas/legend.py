from pydantic import BaseModel
from typing import Optional


class LegendCreate(BaseModel):
    name: str
    category: str
    
class LegendResponse(LegendCreate):
    id: int