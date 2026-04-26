def calculate_impact(waste_type: str, weight: float) -> float:
    factors = {
        "jerami": 1.5,
        "kotoran": 2.0
    }
    return weight * factors.get(waste_type, 0.0)
