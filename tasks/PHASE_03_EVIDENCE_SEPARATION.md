# Phase 3 - Evidence Separation

## Goal

Separate AIR plan artifacts from evidence/runtime artifacts.

AIR describes intent, pipeline, contracts, inputs, and outputs.
Evidence describes runtime events, hashes, artifacts, and replay verification.

## Allowed files

- schemas/**
- fixtures/**
- docs/**
- scripts/**
- reports/**
- tasks/**
- PROJEKT.md

## Tasks

1. Keep schemas/air.schema.json as intent/plan schema.
2. Stabilize schemas/evidence.schema.json for runtime evidence events.
3. Move or create evidence fixtures under fixtures/evidence/.
4. Add scripts/validate_evidence_fixtures.py.
5. Add docs explaining AIR vs Evidence.
6. Write reports/phase_03_status.md.

## Forbidden

- no provider runtime
- no production MCP claim
- no hidden chain-of-thought capture
- no remote Supabase migration
- no comptext-cli integration yet

## Required validation

python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
