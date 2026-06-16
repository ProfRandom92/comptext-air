# Phase 2 - AIR Validation

## Goal

Turn the Phase 1 AIR foundation into a validated local contract pack.

## Allowed files

- schemas/**
- fixtures/**
- docs/**
- lexicon/**
- scripts/**
- reports/**
- .github/workflows/**

## Tasks

1. Validate all JSON files.
2. Add schema validation for AIR fixtures.
3. Add negative fixture examples.
4. Add docs explaining valid vs invalid AIR.
5. Add a report in reports/phase_02_status.md.

## Forbidden

- no provider runtime
- no production MCP claim
- no hidden chain-of-thought capture
- no remote Supabase migration
- no package publishing
- no comptext-cli runtime integration yet

## Required validation

python scripts/validate_json.py
python scripts/validate_air_fixtures.py
