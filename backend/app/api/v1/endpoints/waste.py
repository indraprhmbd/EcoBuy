from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.responses import ApiResponse, success_response
from app.db.database import get_db
from app.schemas.waste import RecommendationResponse, WasteCreate, WasteListResponse, WasteResponse
from app.services.waste_service import WasteService

router = APIRouter()

@router.post("", response_model=ApiResponse[WasteResponse])
def create_waste(waste_in: WasteCreate, db: Session = Depends(get_db)):
    service = WasteService(db)
    try:
        waste = service.create_waste(waste_in)
        return success_response(data=waste)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=ApiResponse[List[WasteListResponse]])
def get_waste_list(status: str = "available", db: Session = Depends(get_db)):
    service = WasteService(db)
    wastes = service.repo.get_list(status=status)
    return success_response(data=wastes)

@router.get("/recommendations", response_model=ApiResponse[List[RecommendationResponse]])
def get_recommendations(lat: float, lng: float, db: Session = Depends(get_db)):
    service = WasteService(db)
    recs = service.get_recommendations(lat, lng)
    return success_response(data=recs)

@router.post("/{waste_id}/complete", response_model=ApiResponse)
def complete_waste(waste_id: int, db: Session = Depends(get_db)):
    service = WasteService(db)
    try:
        result = service.complete_waste(waste_id)
        return success_response(data=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

