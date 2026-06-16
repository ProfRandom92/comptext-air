<p align="center">
  <img src="assets/brand/comptext-air-readme-header.png" alt="CompText AIR - Agent Intermediate Representation" width="100%">
</p>

# CompText AIR

Agent Intermediate Representation for CompText.

CompText AIR separates agent intent from runtime evidence. The goal is not to preserve or expose hidden chain-of-thought. The goal is to make agent work auditable through explicit plans, evidence events, replay contracts, and reproducible hashes.

> If chain-of-thought becomes unreadable, replay becomes the safety primitive.

## Architecture

```text
Natural Language
  <-> CompText AIR
  <-> LLM / Codex / Agent Runtime
  <-> Evidence Events
  <-> Replay / Hash Chain
  <-> Natural Language Summary
```

## Current status

Phase 4 is validated.

Implemented:

- AIR intent/plan schema
- Evidence event schema
- AIR fixtures
- Evidence hash-chain fixture
- JSON validation
- AIR fixture validation
- Evidence fixture validation
- Real canonical SHA-256 event hashing
- Parent-event hash-chain validation

Current canonicalization profile:

```text
json-c14n-v1
```

Current required hash algorithm:

```text
sha256
```

BLAKE3 is not mandatory. It may be added later as an optional algorithm after the base evidence format is stable.

## Core distinction

### AIR

AIR describes what should happen:

- intent
- goal
- inputs
- pipeline
- contracts
- outputs
- metadata

### Evidence

Evidence describes what happened:

- AIR artifact reference
- executor
- event type
- action
- input and output hashes
- event hash
- parent event hash

## Validation

Run locally:

```bash
python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
```

## Boundaries

This repository does not claim:

- hidden chain-of-thought capture
- provider runtime
- production MCP support
- legal or forensic assurance
- remote Supabase deployment
- package publishing

## Next phase

Phase 5: AIR-to-Evidence replay contracts.

The next validation layer should prove that an evidence event chain fulfills the AIR plan, not only that the hashes are valid.

<p align="center">
  <img src="assets/brand/comptext-air-readme-footer.png" alt="CompText AIR - Deterministic, portable, verifiable" width="100%">
</p>
