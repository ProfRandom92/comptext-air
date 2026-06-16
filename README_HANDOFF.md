# CompText AIR Agent Handoff Pack

Status: **handoff-ready / read-only bootstrap**  
Target: `ProfRandom92/comptext-cli`  
Concept: **CompText AIR — Agent Intermediate Representation**

This pack is meant to be given to Codex, Antigravity, Claude Code, Gemini CLI, OpenCode, or another coding agent.

## Core thesis

CompText should evolve from a compression/context tool into an **Agent Intermediate Representation (AIR)**:

```text
Natural Language
  ↔ CompText AIR
  ↔ LLM / Codex / Agent Runtime
  ↔ Evidence Events
  ↔ Replay / Hash Chain
  ↔ Natural Language Summary
```

CompText AIR must not rely on hidden or visible chain-of-thought as the proof layer.  
Instead, it should validate observable evidence:

- deterministic schemas
- typed AIR objects
- evidence events
- replay artifacts
- input/output digests
- hash-chain continuity
- contract validation
- deterministic summaries

## Important

Do not merge old repos blindly.

Recommended source mapping:

```text
comptext-cli      = main implementation target
comptext-dsl      = DSL / parser / language ideas
comptext-codex    = Codex prompts / task mapping
comptext-sparkctl = evidence / replay / governance ideas
Comptextv7        = showcase / reviewer docs
comptext-mcp      = later adapter, not phase 1
```

## First agent task

Open:

```text
00_START_HERE/AGENT_HANDOFF.md
```
