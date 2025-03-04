from sqlmodel import Session
from app.models.hero import Hero

class HeroService:
    def __init__(self, session: Session):
        self.session = session

    def get_heroes(self) -> list[Hero]:
        return self.session.query(Hero).all()

    def create_hero(self, hero_data: dict) -> Hero:
        hero = Hero(**hero_data)
        self.session.add(hero)
        self.session.commit()
        self.session.refresh(hero)
        return hero