# Phase 9 Status: Agent Skill Pack

## Status

Implemented locally.

## Added

- `.agent/skills/comptext-air/SKILL.md`
- `agent_prompts/GEMINI_AIR_VALIDATION_PROMPT.md`
- `agent_prompts/CODEX_AIR_VALIDATION_PROMPT.md`
- `docs/AGENT_SKILLS.md`

## Purpose

Phase 9 adds a repository-local agent skill pack for safe CompText AIR maintenance.

The skill pack gives agents:

- read order
- repository map
- validation commands
- safety boundaries
- forbidden claims
- success criteria

## What Phase 9 enables

Agents can work on CompText AIR with explicit guardrails and repeatable validation steps.

## What Phase 9 does not claim

- no official Gemini plugin support
- no provider runtime
- no production MCP support
- no hidden chain-of-thought capture
- no legal/compliance/forensic assurance
- no package publishing

## Required validation

python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
python scripts/validate_replay_contracts.py
python scripts/validate_adapter_fixtures.py
