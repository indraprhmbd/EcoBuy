# Deployment

## Stack

- FastAPI (Docker)
- Nginx
- PostgreSQL
- S3

## Flow

git push → CI
→ test
→ SSH VPS
→ docker compose up -d --build

## ENV

- DATABASE_URL
- S3_KEY
- S3_SECRET
- S3_BUCKET

## Health Check

GET /health

## Logs

- docker logs backend
