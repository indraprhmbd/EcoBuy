def test_health_check(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_waste(client):
    payload = {
        "type": "jerami",
        "weight": 100,
        "lat": -7.7,
        "lng": 110.3,
        "image_url": "test.jpg"
    }
    response = client.post("/api/v1/waste", json=payload)
    assert response.status_code == 200
    res_json = response.json()
    data = res_json["data"]
    assert data["status"] == "available"
    assert "id" in data
    assert data["validation"]["status"] == "approved"

def test_request_waste(client):
    # Create waste first
    payload = {
        "type": "kotoran",
        "weight": 50,
        "lat": -7.7,
        "lng": 110.3,
        "image_url": "test.jpg"
    }
    waste_res = client.post("/api/v1/waste", json=payload).json()
    waste_id = waste_res["data"]["id"]
    
    # Request it
    req_payload = {"waste_id": waste_id}
    response = client.post("/api/v1/request", json=req_payload)
    assert response.status_code == 200
    assert response.json()["data"]["status"] == "requested"

def test_complete_waste(client):
    # 1. Create waste
    payload = {
        "type": "jerami",
        "weight": 100,
        "lat": -7.7,
        "lng": 110.3,
        "image_url": "test.jpg"
    }
    waste_id = client.post("/api/v1/waste", json=payload).json()["data"]["id"]
    
    # 2. Request waste
    client.post("/api/v1/request", json={"waste_id": waste_id})
    
    # 3. Complete waste
    response = client.post(f"/api/v1/waste/{waste_id}/complete")
    assert response.status_code == 200
    assert response.json()["data"]["status"] == "completed"


def test_impact_dashboard(client):
    response = client.get("/api/v1/impact")
    assert response.status_code == 200
    data = response.json()["data"]
    assert "total_waste" in data
    assert "emission_reduction" in data

