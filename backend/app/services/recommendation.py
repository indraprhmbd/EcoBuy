import math
from typing import Any


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    # simple euclidean distance for MVP
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

def score_recommendation(waste: Any, target_lat: float, target_lng: float) -> float:
    dist = calculate_distance(target_lat, target_lng, waste.lat, waste.lng)
    dist_score = 1 / (dist + 0.0001) * 0.5
    weight_score = min(waste.weight / 1000, 1.0) * 0.3
    type_match = 1.0 * 0.2 
    return dist_score + weight_score + type_match
