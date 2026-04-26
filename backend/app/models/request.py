import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer
from sqlalchemy.sql import func

from app.db.database import Base


class RequestStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Request(Base):
    __tablename__ = "requests"
    
    id = Column(Integer, primary_key=True, index=True)
    waste_id = Column(Integer, ForeignKey("wastes.id"), index=True)
    processor_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum(RequestStatus), default=RequestStatus.pending)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
