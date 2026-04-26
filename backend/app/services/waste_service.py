import logging

from sqlalchemy.orm import Session

from app.models.waste import ImpactLog, Waste, WasteStatus
from app.repositories.impact_repo import ImpactRepository
from app.repositories.waste_repo import WasteRepository
from app.schemas.waste import WasteCreate
from app.services.impact import calculate_impact
from app.services.recommendation import score_recommendation
from app.services.validation import validate_waste

logger = logging.getLogger(__name__)

class WasteService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = WasteRepository(db)
        self.impact_repo = ImpactRepository(db)

    def create_waste(self, waste_in: WasteCreate, user_id: int = 1) -> Waste:
        logger.info(f"Validating waste creation for user {user_id}: {waste_in.type}")
        validation = validate_waste(waste_in.type, waste_in.weight, waste_in.image_url)
        
        if validation.status == "rejected":
            logger.warning(f"Waste validation rejected: {validation.reason}")
            
        waste = Waste(
            user_id=user_id,
            type=waste_in.type,
            weight=waste_in.weight,
            lat=waste_in.lat,
            lng=waste_in.lng,
            image_url=waste_in.image_url,
            validation_status=validation.status,
            validation_confidence=validation.confidence,
            validation_reason=validation.reason
        )
        return self.repo.create(waste)

    def get_recommendations(self, lat: float, lng: float, limit: int = 5):
        wastes = self.repo.get_list(status=WasteStatus.available.value)
        
        scored_wastes = []
        for w in wastes:
            score = score_recommendation(w, lat, lng)
            scored_wastes.append({
                "id": w.id,
                "score": score,
                "reason": "closest & high volume" if score > 0.8 else "good match"
            })
        
        scored_wastes.sort(key=lambda x: x["score"], reverse=True)
        return scored_wastes[:limit]

    def complete_waste(self, waste_id: int):
        waste = self.repo.get_by_id(waste_id)
        if not waste:
            logger.error(f"Complete waste failed: Waste {waste_id} not found")
            raise ValueError("Waste not found")
        
        if waste.status != WasteStatus.requested:
            logger.error(f"Complete waste failed: Waste {waste_id} is in status {waste.status}")
            raise ValueError("Waste must be requested before it can be completed")
            
        logger.info(f"Completing waste {waste_id}")
        self.repo.update_status(waste, WasteStatus.completed)
        
        impact = calculate_impact(waste.type, waste.weight)
        impact_log = ImpactLog(
            waste_id=waste.id,
            emission_reduction=impact
        )
        self.impact_repo.create(impact_log)
        
        logger.info(f"Waste {waste_id} completed. Impact logged: {impact} CO2 saved.")
        return {"status": "completed"}

