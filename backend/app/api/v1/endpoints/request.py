from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.responses import ApiResponse, success_response
from app.db.database import get_db
from app.schemas.request import RequestCreate, RequestResponse
from app.services.request_service import RequestService

router = APIRouter()

@router.post("", response_model=ApiResponse[RequestResponse])
def request_waste(req_in: RequestCreate, db: Session = Depends(get_db)):
    service = RequestService(db)
    try:
        result = service.create_request(req_in)
        return success_response(data=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

