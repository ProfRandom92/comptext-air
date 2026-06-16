[$ctxt-runtime](C:\Users\contr\Desktop\comptext-cli-agent-work\.agents\skills\ctxt-runtime\SKILL.md) [$ctxt-antigravity-runtime](C:\Users\contr\Desktop\comptext-cli-agent-work\.agents\skills\ctxt-antigravity-runtime\SKILL.md) [$cli-developer](C:\Users\contr\.agents\skills\cli-developer\SKILL.md)

TASK:
Prepare CompText AIR (Agent Intermediate Representation) foundation in this repository.

MODE:
- Read-only first.
- No commits.
- No pushes.
- No destructive actions.
- No remote migrations.
- No provider calls.
- No external agent execution.
- No production MCP claims.
- Produce a plan before editing.

CONTEXT:
CompText AIR is a typed intermediate representation between natural language and agent/runtime actions.

Goal architecture:

Natural Language
  ↔ CompText AIR
  ↔ LLM / Codex / Agent Runtime
  ↔ Evidence Events
  ↔ Replay / Hash Chain
  ↔ Natural Language Summary

PHASE 1 — AUDIT:
Inspect:
- README
- Cargo.toml/package files
- src
- tests
- docs
- fixtures
- existing DSL/parser/evidence/hash/replay/MCP code

Return:
1. current repo state
2. existing commands
3. safest integration path
4. proposed files
5. test plan
6. risks
7. approval checkpoint

PHASE 2 — MINIMAL FILES:
After approval, add:

- schemas/air.schema.json
- schemas/evidence.schema.json
- schemas/contract.schema.json
- docs/air/README.md
- docs/air/comptext-air-v0.1.md
- docs/lexicon/comptext-air-lexicon.md
- docs/lexicon/comptext-air-lexicon.json
- fixtures/air/minimal.audit.air.json
- fixtures/air/hash-chain.audit.air.json

PHASE 3 — VALIDATION:
If repo has test infrastructure, add tests proving:

- AIR fixture parses
- required fields exist
- unknown top-level fields are rejected
- evidence event fixture parses
- hash-chain fixture has ordered parent references

NON-GOALS:
- no hidden CoT capture
- no live LLM calls
- no remote Supabase
- no MCP server
- no autonomous execution
- no broad refactor
