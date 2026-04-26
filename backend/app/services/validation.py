from app.schemas.waste import ValidationInfo

VALID_WASTE_TYPES = ["jerami", "kotoran"]

def validate_waste(waste_type: str, weight: float, image_url: str = None) -> ValidationInfo:
    if waste_type not in VALID_WASTE_TYPES:
        return ValidationInfo(status="rejected", confidence=1.0, reason="invalid waste type")
    
    if weight <= 0 or weight > 10000:
        return ValidationInfo(status="rejected", confidence=0.9, reason="weight out of range")
        
    confidence = 0.92
    if image_url:
        confidence = 0.95
        
    return ValidationInfo(status="approved", confidence=confidence, reason="valid waste type")
