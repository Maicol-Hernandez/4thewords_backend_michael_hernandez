from sqlmodel import Session
from app.models.legend import Legend
from fastapi import HTTPException

class LegendService:
    def __init__(self, session: Session):
        self.session = session
        
    def create_legend(self, legend_data: dict, image_url: str) -> Legend:
        legend = Legend(**legend_data, image_url=image_url)
        self.session.add(legend)
        self.session.commit()
        self.session.refresh(legend)
        return legend
        
    def get_legends(self, filters: dict):
        query = self.session.query(Legend)
        
        if "category" in filters:
            query = query.filter(Legend.category == filters["category"])
        if "province" in filters:
            query = query.filter(Legend.province == filters["province"])
            
        return query.all()
    
    def delete_legend(self, legend_id: int):
        legend = self.session.get(Legend, legend_id)
        if legend is None:
            raise HTTPException(status_code=404, detail="Legend not found")
        self.session.delete(legend)
        self.session.commit()
        
        return True