# Testing Strategy

## Scope

Test:

- validation logic
- API endpoints (core flows)
- state transitions

---

## Minimum Tests

1. Create waste
2. Reject invalid waste
3. Request waste
4. Complete waste
5. Recommendation returns sorted results

---

## Tools

- pytest
- httpx (for API test)

---

## Rules

- No test = no deploy
- Keep tests fast (<1s each)

---

## Example

- test_validation_reject_invalid_type
- test_request_changes_status
