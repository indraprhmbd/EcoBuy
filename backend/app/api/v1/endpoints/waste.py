from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from app.core.responses import ApiResponse, success_response
from app.db.database import get_db
from app.schemas.waste import RecommendationResponse, WasteCreate, WasteListResponse, WasteResponse
from app.services.waste_service import WasteService
from app.services.ai_service import AIService
from app.services.storage import storage_service

router = APIRouter()

@router.post("/validate")
async def validate_waste(file: UploadFile = File(...)):
    contents = await file.read()
    
    # 1. Analyze with AI
    ai_service = AIService()
    analysis = await ai_service.analyze_waste(contents)
    
    # 2. Upload to S3
    try:
        image_url = storage_service.upload_file(contents, file.filename or "waste.jpg")
        analysis["image_url"] = image_url
    except Exception as e:
        print(f"S3 Upload Error: {e}")
        analysis["image_url"] = None

    return success_response(data=analysis)

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

