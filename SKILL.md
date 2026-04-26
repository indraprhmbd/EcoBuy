# SKILL.md — Global Engineering Skill Context

## Purpose

This file defines the engineering standards, architecture rules, and decision-making principles
that must be applied consistently across the entire system.

It acts as a persistent "senior engineer mindset" for all code generation and implementation.

## Core Philosophy

- Build systems, not scripts
- Prefer clarity over cleverness
- Prefer simplicity over overengineering
- Every component must be explainable, testable, and maintainable

## System Thinking First

Before implementing anything, always understand:

1. Business flow (what problem is being solved)
2. Data flow (how data moves through the system)
3. State transitions (how entities change over time)
   No code should be written without this context.

## Architecture Rules

### Pattern (MANDATORY)

route → service → repository → database

### Responsibilities

- route:
  - handles HTTP layer only
  - no business logic
- service:
  - contains all business logic
  - orchestrates operations
- repository:
  - handles database access
  - no business logic

## Modularity

- keep modules isolated by domain
- avoid tight coupling
- prefer composition over inheritance

## Backend Standards (FastAPI)

### General

- use Pydantic for all input/output validation
- enforce type safety
- use dependency injection where needed

### API Design

- RESTful and predictable
- consistent response structure:
  {
  "data": {},
  "message": "success",
  "error": null
  }

### Performance

- avoid N+1 queries
- fetch only required fields
- keep endpoints < 200ms when possible

## Database Principles

- use PostgreSQL
- normalize where appropriate
- include timestamps in all tables
- use enums for status fields

### Safety

- no raw SQL unless necessary
- always parameterized queries

## State Management (Critical)

All entities must have clear states.
Example:

- available
- requested
- completed
  Transitions must be:
- explicit
- validated
- logged

## AI Layer Principles

### Philosophy

- AI must be:
  - deterministic
  - lightweight
  - explainable

### Implementation

- use rule-based logic
- use scoring systems where needed

### Avoid

- heavy ML models (unless required)
- external AI dependencies (unless justified)

## Frontend Principles (Vue)

- UI reflects backend state
- no hidden logic in components
- minimal global state
- API-driven UI

## Security

- validate all inputs
- never expose secrets
- use environment variables
- use presigned URLs for file uploads

## Logging & Observability

Log:

- incoming requests
- validation failures
- state transitions
  No silent failures.

## Testing

Test at minimum:

- validation logic
- core API endpoints
- state transitions
  No deploy without passing tests.

## Deployment Awareness

- assume Docker-based deployment
- avoid environment-specific hacks
- use environment variables for configuration

## Coding Standards

- use clear, descriptive naming
- avoid overly clever code
- prioritize readability

## Anti-Patterns (FORBIDDEN)

- business logic inside routes
- direct DB calls in routes
- unvalidated inputs
- silent failures
- unnecessary abstraction
- premature microservices

## Decision Rules

When making decisions:

1. choose the simplest solution that works
2. ensure it scales logically
3. ensure it is easy to debug
4. ensure it aligns with existing architecture

## When Uncertain

- do not guess blindly
- make reasonable assumptions
- document them clearly
- keep implementation minimal

## Goal

Produce systems that are:

- maintainable
- scalable
- debuggable
- production-aligned
