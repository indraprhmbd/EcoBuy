from sqlalchemy.orm import Session

from app.models.request import Request


class RequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, request: Request) -> Request:
        self.db.add(request)
        self.db.commit()
        self.db.refresh(request)
        return request
