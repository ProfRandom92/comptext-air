# CompText AIR Agent Skill

## Purpose

CompText AIR is the Agent Intermediate Representation layer for CompText.

Core rule:

If chain-of-thought becomes unreadable, replay becomes the safety primitive.

This skill helps an agent work safely inside this repository without inventing runtime claims, fake evidence, fake hashes, or hidden reasoning artifacts.

## Required read order

1. AGENTS.md
2. README.md
3. PROJEKT.md
4. docs/AIR_VS_EVIDENCE.md
5. docs/REPLAY_CONTRACTS.md
6. docs/RUNTIME_ADAPTERS.md
7. docs/AUDIT_REPORTS.md
8. schemas/air.schema.json
9. schemas/evidence.schema.json
10. schemas/adapter.schema.json

## Repository map

- schemas/air.schema.json: AIR intent and plan schema
- schemas/evidence.schema.json: evidence event schema
- schemas/adapter.schema.json: runtime adapter description schema
- fixtures/air/: valid and invalid AIR fixtures
- fixtures/evidence/: evidence event fixtures
- fixtures/adapter/: adapter fixtures
- scripts/: local validators and canonical hashing utilities
- reports/: phase status reports
- reports/generated/: generated local validation reports, not committed

## Required validation commands

Run all of these before reporting success:

python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
python scripts/validate_replay_contracts.py
python scripts/validate_adapter_fixtures.py

## Allowed actions

- Edit repository documentation
- Edit schemas with matching fixture updates
- Add or update fixtures
- Update validators
- Generate deterministic local reports
- Regenerate real evidence hashes using repository scripts
- Add negative fixtures that must fail validation

## Forbidden actions

- Do not claim provider runtime support
- Do not claim production MCP support
- Do not claim hidden chain-of-thought capture
- Do not add network requirements
- Do not auto-apply runtime actions
- Do not claim legal assurance
- Do not claim compliance assurance
- Do not claim forensic assurance
- Do not create fake hashes
- Do not create simulated evidence while calling it real
- Do not install external plugins or dependencies unless explicitly requested

## Evidence and hashing rules

Evidence hashes must be real SHA-256 hashes generated through the repository canonical JSON profile.

Use:

python scripts/regenerate_evidence_fixtures.py

Then validate:

python scripts/validate_evidence_fixtures.py
python scripts/validate_replay_contracts.py

## Negative fixture rules

Invalid fixtures under fixtures/adapter/invalid/ must fail for the expected reason.

A negative fixture unexpectedly passing is a validation failure.

## Success criteria

A task is successful only when:

- all required validators pass
- changed files are listed
- safety boundaries are stated
- no runtime/provider/MCP overclaim is introduced
- no hidden chain-of-thought is captured
- exact commit command is provided
