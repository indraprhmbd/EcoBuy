# Backend Guidelines

## Architecture Rules

- Use layered architecture:
  - route → service → repository
- Routes must NOT contain business logic
- Services must NOT access request/response objects directly

## Naming Convention

- DB fields: snake_case
- API response: camelCase OR snake_case (pick one, stay consistent)

## Response Standard

{
"data": {},
"message": "success",
"error": null
}

## Error Handling

- Use HTTPException
- Every error must include:
  - message
  - optional code

## Validation Rules

- All input must go through Pydantic
- No raw dict handling in services

## Transaction Rules

Use DB transactions for:

- requesting waste
- completing waste

## Logging

Log:

- incoming requests
- validation failures
- state transitions

## Performance Rules

- Avoid N+1 queries
- Select only required fields
- Use indexes (status, location)

## Forbidden

- Business logic inside routes
- Direct DB access inside routes
- Global mutable state
