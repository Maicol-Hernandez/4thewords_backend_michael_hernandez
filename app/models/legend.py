from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class LegendBase(SQLModel):
    name: str = Field(index=True)
    category: str
    
class Legend(LegendBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)