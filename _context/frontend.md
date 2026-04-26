# Frontend Guidelines

## Principles

- UI follows API, not the other way around
- No hardcoded data

## State Management

- Use TanStack Query
- Avoid global state unless necessary

## API Layer

Create abstraction:

- api/waste.ts
- api/request.ts
- api/impact.ts

## Error Handling

- Always handle API errors
- Show meaningful feedback to users

## Component Structure

- Keep components small and reusable
- Separate:
  - form
  - list
  - dashboard

## UX Rules

- Fast interaction (minimal steps)
- Clear status visibility
- No unnecessary navigation

## Forbidden

- Direct fetch inside components (wrap via API layer)
- Business logic inside UI components
