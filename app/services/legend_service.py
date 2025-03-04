from sqlmodel import Session
from app.models.legend import Legend

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
    