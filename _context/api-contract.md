# API Contract

## Base URL

/api/v1

## 1. Create Waste

POST /waste

### Request

{
"type": "jerami",
"weight": 100,
"lat": -7.7,
"lng": 110.3,
"image_url": "string"
}

### Response

{
"id": 1,
"status": "available",
"validation": {
"status": "approved",
"confidence": 0.92,
"reason": "valid waste type"
}
}

---

## 2. Get Waste List

GET /waste

Query:

- status=available

### Response

[
{
"id": 1,
"type": "jerami",
"weight": 100,
"lat": -7.7,
"lng": 110.3,
"status": "available",
"validation_confidence": 0.92
}
]

---

## 3. Get Recommendations

GET /waste/recommendations

Query:

- lat
- lng

### Response

[
{
"id": 1,
"score": 0.87,
"reason": "closest & high volume"
}
]

---

## 4. Request Waste

POST /request

### Request

{
"waste_id": 1
}

### Response

{
"status": "requested"
}

---

## 5. Complete Waste

POST /waste/{id}/complete

### Response

{
"status": "completed"
}

---

## 6. Impact Dashboard

GET /impact

### Response

{
"total_waste": 1200,
"by_type": {
"jerami": 800,
"kotoran": 400
},
"emission_reduction": 1800
}

---

## 7. Health

GET /health

Response:
{
"status": "ok"
}
