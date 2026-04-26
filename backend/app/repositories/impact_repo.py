from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.waste import ImpactLog, Waste


class ImpactRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, impact_log: ImpactLog) -> ImpactLog:
        self.db.add(impact_log)
        self.db.commit()
        self.db.refresh(impact_log)
        return impact_log

    def get_summary(self):
        total_waste = self.db.query(func.sum(Waste.weight)).filter(Waste.status == 'completed').scalar() or 0.0
        emission_reduction = self.db.query(func.sum(ImpactLog.emission_reduction)).scalar() or 0.0
        
        types = self.db.query(Waste.type, func.sum(Waste.weight)).filter(Waste.status == 'completed').group_by(Waste.type).all()
        by_type = {t[0]: t[1] for t in types}
        
        return {
            "total_waste": total_waste,
            "by_type": by_type,
            "emission_reduction": emission_reduction
        }
