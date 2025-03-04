from sqlmodel import Session
from app.models.legend import Legend

class LegendService:
    def __init__(self, session: Session):
        self.session = session
        
    def get_legends(self) -> list[Legend]:
        return self.session.query(Legend).all()
    
    def create_legend(self, legend_data: dict) -> Legend:
        legend = Legend(**legend_data)
        self.session.add(legend)
        self.session.commit()
        self.session.refresh(legend)
        return legend
    
    