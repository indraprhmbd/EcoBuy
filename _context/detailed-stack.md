# Tech Stack

## Backend

- FastAPI
- Uvicorn
- Python 3.11+

## Database

- PostgreSQL
- ORM: SQLAlchemy (2.0 style)
- Migration: Alembic

## Storage

- S3-compatible bucket (image upload)

## Infra

- VPS (Dockerized)
- Nginx (reverse proxy)

## Dev Tools

- pytest (testing)
- pydantic (validation schema)
- httpx (internal calls if needed)

## Frontend (separate)

- Vue + Vite
- TanStack Query

## Design Decisions

### Why FastAPI

- fast iteration
- native validation (pydantic)
- async support

### Why Modular Monolith

- easier debugging
- single deploy unit
- no network overhead

### Why NOT microservices

- unnecessary complexity
- no scaling need yet

### AI Approach

- rule-based
- deterministic
- explainable
