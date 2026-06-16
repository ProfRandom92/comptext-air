# Contributing to CompText AIR

We welcome contributions that improve the Agent Intermediate Representation layer. To maintain the integrity and safety of this repository, please follow these guidelines.

## Core Principles

1.  **Validation First:** No change is complete without local validation. Run the validation suite before submitting any proposal.
2.  **No Fake Hashes:** All hashes in fixtures must be real, recomputed SHA-256 hashes using the canonicalization profile.
3.  **Boundary Safety:** Do not introduce claims related to provider runtimes, production MCP support, or legal assurance.
4.  **Descriptive Adapters:** Runtime adapters must remain descriptive and include all mandatory safety fields.

## Contribution Workflow

### 1. Development
- Ensure all JSON files follow the schemas in `schemas/`.
- If you modify an AIR plan or Evidence trail, you MUST recompute the hashes.
- Use `scripts/regenerate_evidence_fixtures.py` if applicable.

### 2. Validation
Run all scripts in the `scripts/` directory:
```bash
python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
python scripts/validate_replay_contracts.py
python scripts/validate_adapter_fixtures.py
```

### 3. Documentation
- If you add a new feature or phase, update the relevant `docs/*.md` files.
- Ensure the `VALIDATION_BASELINE.md` reflects any changes to the core components.

### 4. Pull Requests
- Summarize the intent of the change.
- Confirm that all validation scripts pass.
- Include any updated generated reports in `reports/generated/`.

## Forbidden Actions
- Do not commit secrets or API keys.
- Do not add dependencies that require external network access for core validation.
- Do not claim "hidden chain-of-thought" capture capabilities.
