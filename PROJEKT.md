# PROJEKT.md - CompText AIR Project State

CURRENT_PHASE: 8
CURRENT_TASK: Generated Audit Reports
STATUS: phase-8-generated-reports
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
- Machine-readable audit reports

## Current validated state

Phase 8 validates:

- JSON syntax across repository fixtures and schemas
- AIR plan fixtures
- evidence event fixtures
- real SHA-256 event hashes
- AIR artifact hash references
- parent_event_hash continuity
- CompText json-c14n-v1 canonicalization profile
- AIR-to-Evidence replay contract fulfillment
- Negative adapter validation (blocking forbidden claims and missing safety fields)
- Deterministic JSON audit report generation

## Current boundary

This repository does not own:

- provider runtime
- production MCP support
- hidden chain-of-thought capture
- remote Supabase deployment
- package publishing
- legal/compliance/forensic assurance claims

## Next phase

Phase 8: Generated Audit Reports.

Goal: generate deterministic machine-readable validation reports for replay contracts and adapter validation.
