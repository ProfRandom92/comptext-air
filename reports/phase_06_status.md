# Phase 6: AIR Runtime Adapter Design

PHASE: 6
MODE: Research & Design
NETWORK: offline-only
CHANGED_FILES:
- schemas/adapter.schema.json
- fixtures/adapter/ctxt-local.adapter.json
- docs/RUNTIME_ADAPTERS.md
- scripts/validate_adapter_fixtures.py
- .github/workflows/validate.yml

VALIDATION:
- python scripts/validate_json.py
- python scripts/validate_air_fixtures.py
- python scripts/validate_evidence_fixtures.py
- python scripts/validate_replay_contracts.py
- python scripts/validate_adapter_fixtures.py

RISKS:
- Descriptive adapters may drift from actual runtime implementation if not synced.
- Over-complexity in mapping logic could make adapters hard to maintain.

NEXT_STEP:
- Phase 7: AIR Context Snapshotting (Conceptual).

STOP_REASON:
- Phase 6 requirements met: Adapter schema, fixture, documentation, and validation implemented.

## Summary

Phase 6 introduces the AIR Runtime Adapter layer. This layer provides the necessary metadata to bridge platform-agnostic AIR plans with specific runtime environments without implementing the runtimes themselves.

### Achievements

- Defined `adapter.schema.json` for descriptive runtime mapping.
- Created `ctxt-local.adapter.json` fixture inspired by `comptext-cli`.
- Documented the role and principles of adapters in `docs/RUNTIME_ADAPTERS.md`.
- Implemented `scripts/validate_adapter_fixtures.py` for CI integration.
- Updated CI workflow to include adapter validation.

### What Phase 6 Proves

- AIR plans can be mapped to local execution surfaces descriptively.
- Runtime safety boundaries can be formally declared.
- Evidence generation can be mapped to standard runtime signals (stdout, exit codes).

### What Phase 6 Does Not Prove

- It does not prove that the runtimes actually exist or function correctly.
- It does not provide an automated execution engine for AIR.
- It does not claim production readiness for any specific adapter.
