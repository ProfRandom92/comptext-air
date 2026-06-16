# PROJEKT.md - CompText AIR Project State

CURRENT_PHASE: 4
CURRENT_TASK: Canonical evidence hashing
STATUS: validated
NETWORK: offline-only
DEFAULT_BRANCH: main

## Mission

CompText AIR is the Agent Intermediate Representation layer for CompText.

Core sentence:

If chain-of-thought becomes unreadable, replay becomes the safety primitive.

## Current scope

The repository owns the AIR contract layer:

- AIR intent/plan schema
- evidence event schema
- contract and replay documentation
- validation scripts
- local fixtures
- local/dev Supabase drafts
- agent handoff prompts
- CI validation workflow

## Current validated state

Phase 4 validates:

- JSON syntax across repository fixtures and schemas
- AIR plan fixtures
- evidence event fixtures
- real SHA-256 event hashes
- AIR artifact hash references
- parent_event_hash continuity
- CompText json-c14n-v1 canonicalization profile

## Current boundary

This repository does not own:

- provider runtime
- production MCP support
- hidden chain-of-thought capture
- remote Supabase deployment
- package publishing
- legal/compliance/forensic assurance claims

## Next phase

Phase 5: AIR-to-Evidence replay contracts.

Goal: prove that evidence events fulfill the AIR plan, including required pipeline steps, required outputs, shared AIR artifact hash, and root evidence hash reporting.
