import enum

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.sql import func

from app.db.database import Base


class WasteStatus(str, enum.Enum):
    available = "available"
    requested = "requested"
    completed = "completed"

class ValidationStatus(str, enum.Enum):
    approved = "approved"
    rejected = "rejected"
    flagged = "flagged"

class Waste(Base):
    __tablename__ = "wastes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, index=True)
    weight = Column(Float)
    lat = Column(Float, index=True)
    lng = Column(Float, index=True)
    image_url = Column(String, nullable=True)
    
    status = Column(Enum(WasteStatus), default=WasteStatus.available, index=True)
    
    validation_status = Column(Enum(ValidationStatus))
    validation_confidence = Column(Float)
    validation_reason = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    @property
    def validation(self):
        return {
            "status": self.validation_status,
            "confidence": self.validation_confidence,
            "reason": self.validation_reason
        }

class ImpactLog(Base):
    __tablename__ = "impact_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    waste_id = Column(Integer, ForeignKey("wastes.id"))
    emission_reduction = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
