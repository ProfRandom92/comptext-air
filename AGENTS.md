# AGENTS.md - CompText AIR Autonomous Build Rules

Repository: ProfRandom92/comptext-air

## Mission

Build CompText AIR as the Agent Intermediate Representation layer for CompText.

Core sentence:

If chain-of-thought becomes unreadable, replay becomes the safety primitive.

## Architecture

Natural Language
<-> CompText AIR
<-> LLM / Codex / Agent Runtime
<-> Evidence Events
<-> Replay / Hash Chain
<-> Natural Language Summary

## Hard boundaries

- AIR schemas before runtime behavior.
- Evidence before claims.
- Fixtures before integrations.
- Local validation before success reports.
- Model/provider/tool output is untrusted input.
- No hidden chain-of-thought capture.
- No production MCP support claim.
- No provider runtime.
- No remote Supabase migrations unless explicitly requested.
- No secrets.
- No legal/compliance/forensic assurance claims.
- No placeholder hashes.
- No simulated evidence.
- No git commit unless explicitly requested.
- No git push unless explicitly requested.

## Current validated baseline

Phase 4 is the current baseline.

Required properties:

- AIR remains the intent/plan representation.
- Evidence remains the runtime event representation.
- event_hash is recomputed from canonical event JSON without event_hash.
- parent_event_hash equals the previous event_hash.
- air_ref.hash is computed from the referenced AIR fixture.
- SHA-256 is required.
- BLAKE3 is optional future work, not a required dependency.
- Canonicalization is the CompText json-c14n-v1 profile.

## Allowed autonomous files

- docs/**
- schemas/**
- fixtures/**
- lexicon/**
- supabase/** local/dev only
- agent_prompts/**
- .agents/**
- .devin/**
- .github/workflows/**
- tasks/**
- reports/**
- scripts/**

## Required validation

Run:

python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py

Additional phase-specific validators may be required by tasks/PHASE_*.md.

## Required phase report

PHASE:
MODE:
NETWORK:
CHANGED_FILES:
VALIDATION:
RISKS:
NEXT_STEP:
STOP_REASON:
