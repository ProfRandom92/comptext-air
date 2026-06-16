# Phase 05 Status Report - Replay Contracts

PHASE: 5
MODE: local-validation
NETWORK: offline-only
STATUS: phase-5-replay-contracts

## Summary

Implemented the first real end-to-end replay contract test for CompText AIR. This proves that an Evidence event chain fulfills an AIR plan by verifying hash continuity and requirement satisfaction (pipeline, contracts, outputs).

## Changed Files

- `scripts/validate_replay_contracts.py`: New validator for AIR-to-Evidence fulfillment.
- `scripts/regenerate_evidence_fixtures.py`: Updated to generate evidence that fully satisfies the `hash-chain.audit.air.json` plan.
- `fixtures/evidence/hash-chain.events.json`: Regenerated with full plan fulfillment.
- `docs/REPLAY_CONTRACTS.md`: Documentation for the replay contract mechanism.
- `PROJEKT.md`: Updated project state.
- `.github/workflows/validate.yml`: Added replay contract validation to CI.

## Validation Results

- `python scripts/validate_json.py`: OK
- `python scripts/validate_air_fixtures.py`: OK
- `python scripts/validate_evidence_fixtures.py`: OK
- `python scripts/validate_replay_contracts.py`: SUCCESS

## Risks

- The "represented by" mapping is currently heuristic (checking action names and metadata). As the schema evolves, we may need more formal mapping rules.
- Hash-chain depth is currently minimal (4 events). Larger chains should be tested in future phases.

## Next Step

Phase 6: Lexicon-backed Evidence. Align evidence actions and metadata with the formal CompText AIR lexicon.
