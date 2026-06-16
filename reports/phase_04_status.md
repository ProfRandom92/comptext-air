# Phase 4 Status - Canonical Evidence Hashing

PHASE: 4
MODE: docs-schema-fixture
NETWORK: offline-only

## Result

Phase 4 replaces placeholder evidence hashes with real SHA-256 hashes.

## Rules

- AIR plan hash is computed from the actual AIR fixture file.
- event_hash is computed from canonical JSON of the event without its own event_hash field.
- parent_event_hash must exactly equal the previous event_hash.
- canonicalization profile is CompText json-c14n-v1.
- SHA-256 is the required default algorithm.

## Non-goals

- No BLAKE3 dependency.
- No provider runtime.
- No production MCP claim.
- No hidden chain-of-thought capture.
- No remote Supabase migration.

## Validation

- python scripts/validate_json.py
- python scripts/validate_air_fixtures.py
- python scripts/validate_evidence_fixtures.py
