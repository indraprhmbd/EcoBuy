# AI Design

## Philosophy

- AI must be deterministic, explainable, and lightweight
- No black-box behavior

---

## 1. Validation Engine

### Input

- type
- weight
- optional image

### Logic

- whitelist waste types
- validate weight range
- optional image heuristic (basic)

### Output

{
"status": "approved | rejected | flagged",
"confidence": 0.0 - 1.0,
"reason": "string"
}

---

## 2. Recommendation Engine

### Factors

- distance
- weight
- type match

### Scoring

score =
(1/distance) _ 0.5 +
(weight_normalized) _ 0.3 +
(type_match) \* 0.2

### Output

- top N results
- include reason (e.g., "closest", "largest volume")

---

## 3. Impact Engine

### Rule-based mapping

jerami → 1.5 CO2/kg  
kotoran → 2.0 CO2/kg

### Output

- emission reduction
- aggregated metrics

---

## Constraints

- Must execute < 200ms
- No external model dependency
