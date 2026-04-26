# Environment Variables

## Required

DATABASE_URL=
S3_BUCKET=
S3_REGION=
S3_ACCESS_KEY=
S3_SECRET_KEY=

APP_ENV=development | production

---

## Optional

LOG_LEVEL=info
CORS_ORIGIN=\*

---

## Rules

- Never hardcode secrets
- Use .env locally
- Use GitHub Secrets in CI/CD
