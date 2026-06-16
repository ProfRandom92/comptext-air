# Gemini CompText AIR Validation Prompt

Work only inside the CompText AIR repository.

Read first:
- AGENTS.md
- README.md
- PROJEKT.md
- docs/AIR_VS_EVIDENCE.md
- docs/REPLAY_CONTRACTS.md
- docs/RUNTIME_ADAPTERS.md
- docs/AUDIT_REPORTS.md
- .agent/skills/comptext-air/SKILL.md

Rules:
- no provider runtime claim
- no production MCP support claim
- no hidden chain-of-thought capture
- no fake hashes
- no simulated evidence described as real
- no network requirement
- no auto-apply behavior
- no legal/compliance/forensic assurance claim
- no external plugin installation

Validation commands:
python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
python scripts/validate_replay_contracts.py
python scripts/validate_adapter_fixtures.py

Stop report format:
- changed files
- validation output
- what changed
- what is proven
- what is not claimed
- exact commit command
