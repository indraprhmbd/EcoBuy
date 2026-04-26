# Backend Structure

app/
├── main.py
├── api/
│ └── routes/
│ ├── waste.py
│ ├── request.py
│ ├── impact.py
│
├── services/
│ ├── validation.py
│ ├── recommendation.py
│ ├── impact.py
│
├── repositories/
│ ├── waste_repo.py
│ ├── request_repo.py
│
├── models/
│ ├── waste.py
│ ├── request.py
│
├── schemas/
│ ├── waste.py
│
├── core/
│ ├── config.py
│ ├── db.py
