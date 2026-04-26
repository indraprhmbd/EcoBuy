from typing import Optional

from pydantic import BaseModel, ConfigDict


class ValidationInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    status: str
    confidence: float
    reason: Optional[str] = None

class WasteCreate(BaseModel):
    type: str
    weight: float
    lat: float
    lng: float
    image_url: Optional[str] = None

class WasteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: str
    validation: ValidationInfo

class WasteListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    type: str
    weight: float
    lat: float
    lng: float
    status: str
    validation_confidence: float
    image_url: Optional[str] = None


class RecommendationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    score: float
    reason: str

