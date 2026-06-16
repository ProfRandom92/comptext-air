# Phase 4 - Canonical Hashing

## Goal

Turn structural evidence chains into reproducible cryptographic evidence chains.

Default hash algorithm:

- sha256

Optional later:

- blake3
- multihash-style typed hashes

## Rationale

SHA-256 is the required default because CompText AIR is an audit/evidence/interoperability format. SHA-256 is broadly supported in Python, Rust, GitHub Actions, Postgres/Supabase extensions, and standard security tooling.

BLAKE3 is attractive for performance and large local artifacts, but it should be optional until the base evidence format is stable.

## Canonicalization

Use deterministic canonical JSON:

- UTF-8
- sorted object keys
- compact separators
- no insignificant whitespace
- hash the event without its own event_hash field
- for chains, parent_event_hash must equal the previous event_hash

Target rule:

event_hash = sha256(canonical_json(event_without_event_hash))

parent_event_hash = previous event_hash

## Allowed files

- schemas/**
- fixtures/**
- docs/**
- scripts/**
- reports/**
- tasks/**
- PROJEKT.md

## Tasks

1. Update evidence schema so hashes are typed objects:
   - algorithm
   - canonicalization
   - value
2. Keep sha256 as the only required algorithm for now.
3. Add scripts/canonical_json.py or inline canonicalization helper.
4. Update scripts/validate_evidence_fixtures.py to recompute event_hash.
5. Regenerate fixtures/evidence/hash-chain.events.json with real hashes.
6. Document why SHA-256 is the default and BLAKE3 is optional later.
7. Write reports/phase_04_status.md.

## Forbidden

- no provider runtime
- no production MCP claim
- no hidden chain-of-thought capture
- no remote Supabase migration
- no package publishing
- no mandatory BLAKE3 dependency yet

## Required validation

python scripts/validate_json.py
python scripts/validate_air_fixtures.py
python scripts/validate_evidence_fixtures.py
