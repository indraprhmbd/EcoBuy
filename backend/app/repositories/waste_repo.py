from sqlalchemy.orm import Session

from app.models.waste import Waste, WasteStatus


class WasteRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, waste: Waste) -> Waste:
        self.db.add(waste)
        self.db.commit()
        self.db.refresh(waste)
        return waste

    def get_by_id(self, waste_id: int) -> Waste:
        return self.db.query(Waste).filter(Waste.id == waste_id).first()

    def get_list(self, status: str = "available"):
        return self.db.query(Waste).filter(Waste.status == status).all()

    def update_status(self, waste: Waste, new_status: WasteStatus) -> Waste:
        waste.status = new_status
        self.db.commit()
        self.db.refresh(waste)
        return waste
