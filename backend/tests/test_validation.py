from app.services.ai_service import validate_waste


def test_validate_valid_waste():
    res = validate_waste("jerami", 100)
    assert res.status == "approved"
    assert res.confidence == 0.92

def test_validate_valid_waste_with_image():
    res = validate_waste("kotoran", 50, "http://image.url")
    assert res.status == "approved"
    assert res.confidence == 0.95

def test_validate_invalid_waste_type():
    res = validate_waste("plastic", 100)
    assert res.status == "rejected"
    assert res.reason == "invalid waste type"

def test_validate_invalid_weight():
    res = validate_waste("jerami", -10)
    assert res.status == "rejected"
    assert res.reason == "weight out of range"
