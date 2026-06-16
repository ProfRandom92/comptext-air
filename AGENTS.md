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
- No git commit unless explicitly requested.
- No git push unless explicitly requested.

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

## Required phase report

PHASE:
MODE:
NETWORK:
CHANGED_FILES:
VALIDATION:
RISKS:
NEXT_STEP:
STOP_REASON:
