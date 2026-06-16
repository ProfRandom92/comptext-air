# PROJEKT.md - CompText AIR Project State

CURRENT_PHASE: 11
CURRENT_TASK: v0.1.0-pre tag preparation
STATUS: phase-11-tag-preparation
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
- Release readiness documentation
- Tagging and release preparation

## Current validated state

Phase 11 validates:

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
- Repository-local agent skill pack
- Release readiness baseline
- Tagging checklist and release notes (Prepares release documentation without creating a tag)

## Current boundary

This repository does not own:

- provider runtime
- production MCP support
- hidden chain-of-thought capture
- remote Supabase deployment
- package publishing
- legal/compliance/forensic assurance claims

## Next phase

Phase 12: Conceptual AIR Context Snapshotting.
