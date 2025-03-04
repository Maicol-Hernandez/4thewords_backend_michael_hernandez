from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, List

class LegendBase(SQLModel):
    name: str = Field(index=True, max_length=100)
    category: str = Field(index=True, max_length=50)
    description: str = Field(max_length=500)
    image_url: str
    legend_date: date
    province: str = Field(max_length=50)
    canton: str = Field(max_length=50)
    district: str = Field(max_length=50)
    
class Legend(LegendBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[date] = Field(default_factory=date.today)
    updated_at: Optional[date]
    deleted_at: Optional[date]