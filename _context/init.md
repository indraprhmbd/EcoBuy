# ECO BUY – Backend System Context

## Goal

Build a production-ready backend for a waste distribution platform with:

- AI validation (rule-based)
- recommendation engine
- impact tracking

## Core Principles

- modular monolith (FastAPI)
- no premature microservices
- deterministic AI (no heavy ML required)
- clean API contract
- observable & debuggable

## Key Features

1. Waste submission + validation
2. Marketplace listing (filtered)
3. Request system (processor)
4. AI recommendation
5. Impact dashboard

## Non-Goals (for MVP)

- payment system
- real-time chat
- logistics routing optimization
- heavy ML / RAG

## Architecture Style

- layered architecture:
  - API layer
  - service layer
  - repository layer

## Performance Targets

- API response < 200ms (non-heavy endpoint)
- validation < 50ms
- recommendation < 150ms (in-memory scoring)

## Reliability

- idempotent endpoints where needed
- clear state transitions
- no silent failure

## Status Philosophy

All business flows must be traceable via:

- status field
- timestamps
- logs
