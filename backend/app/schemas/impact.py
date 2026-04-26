from typing import Dict

from pydantic import BaseModel


class ImpactResponse(BaseModel):
    total_waste: float
    by_type: Dict[str, float]
    emission_reduction: float
