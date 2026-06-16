# Codex CompText AIR Validation Prompt

Task: modify CompText AIR safely and minimally.

Read first:
- AGENTS.md
- PROJEKT.md
- README.md
- .agent/skills/comptext-air/SKILL.md
- docs/AIR_VS_EVIDENCE.md
- docs/REPLAY_CONTRACTS.md
- docs/RUNTIME_ADAPTERS.md
- docs/AUDIT_REPORTS.md

Hard boundaries:
- AIR is intent/plan IR
- Evidence is runtime observation
- Adapter files are descriptive contracts only
- Replay is the safety primitive when chain-of-thought is not readable
- Generated reports are local artifacts and are not committed as JSON

Do not:
- add provider execution
- add MCP runtime claims
- add hidden chain-of-thought capture
- add auto-apply
- add network requirement
- add fake hashes
- add legal/compliance/forensic assurance claims

Run before completion:
python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
python scripts/validate_replay_contracts.py
python scripts/validate_adapter_fixtures.py

Return:
- files changed
- exact validation output
- exact commit command
