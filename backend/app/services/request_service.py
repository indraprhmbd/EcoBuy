import logging

from sqlalchemy.orm import Session

from app.models.request import Request, RequestStatus
from app.models.waste import WasteStatus
from app.repositories.request_repo import RequestRepository
from app.repositories.waste_repo import WasteRepository
from app.schemas.request import RequestCreate

logger = logging.getLogger(__name__)

class RequestService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = RequestRepository(db)
        self.waste_repo = WasteRepository(db)

    def create_request(self, req_in: RequestCreate, processor_id: int = 2) -> dict:
        waste = self.waste_repo.get_by_id(req_in.waste_id)
        if not waste:
            logger.error(f"Request creation failed: Waste {req_in.waste_id} not found")
            raise ValueError("Waste not found")
            
        if waste.status != WasteStatus.available:
            logger.error(f"Request creation failed: Waste {req_in.waste_id} is {waste.status}")
            raise ValueError("Waste is not available")
            
        logger.info(f"Processor {processor_id} requesting waste {req_in.waste_id}")
        self.waste_repo.update_status(waste, WasteStatus.requested)
        
        request = Request(
            waste_id=req_in.waste_id,
            processor_id=processor_id,
            status=RequestStatus.pending
        )
        self.repo.create(request)
        
        logger.info(f"Request created successfully for waste {req_in.waste_id}")
        return {"status": "requested"}

