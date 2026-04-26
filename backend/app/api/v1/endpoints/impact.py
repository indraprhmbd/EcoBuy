from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.responses import ApiResponse, success_response
from app.db.database import get_db
from app.repositories.impact_repo import ImpactRepository
from app.schemas.impact import ImpactResponse

router = APIRouter()

@router.get("", response_model=ApiResponse[ImpactResponse])
def get_impact_dashboard(db: Session = Depends(get_db)):
    repo = ImpactRepository(db)
    summary = repo.get_summary()
    return success_response(data=summary)

