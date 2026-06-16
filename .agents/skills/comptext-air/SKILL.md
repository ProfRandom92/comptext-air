---
name: comptext-air
description: Safe workflow for CompText AIR schemas, fixtures, lexicon, evidence events, replay contracts, and local validation.
---

# Purpose

CompText AIR is the Agent Intermediate Representation layer for CompText.

## Hard rules

- No provider calls.
- No hidden chain-of-thought capture.
- No production MCP claims.
- No remote Supabase migrations.
- No publishing.
- No secrets.
- No push unless explicitly requested.

## Validation

Run:

python scripts/validate_json.py
