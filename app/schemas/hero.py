from pydantic import BaseModel
from typing import Optional

class HeroCreate(BaseModel):
    name: str
    secret_name: str
    age: Optional[int] = None
    
    team_id: Optional[int] = None

class HeroResponse(HeroCreate):
    id: int