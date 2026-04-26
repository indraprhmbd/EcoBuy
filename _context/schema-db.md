# Database Schema

## users

- id (pk)
- role (farmer | processor)
- created_at

---

## waste

- id (pk)
- user_id (fk)
- type
- weight
- lat
- lng
- image_url
- status (available, requested, completed)
- validation_status (approved, rejected, flagged)
- validation_confidence
- created_at

---

## requests

- id (pk)
- waste_id (fk)
- processor_id (fk)
- status
- created_at

---

## impact_logs

- id (pk)
- waste_id (fk)
- emission_reduction
- created_at

---

## Indexing

- waste(status)
- waste(lat, lng)
- requests(waste_id)
