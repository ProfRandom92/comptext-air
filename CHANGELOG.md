# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.0-pre] - Unreleased

### Phase 11: v0.1.0-pre Tag Preparation
- Created `docs/TAGGING_CHECKLIST.md` for release validation.
- Created `docs/RELEASE_NOTES_v0.1.0-pre.md` summarizing the public review candidate.
- Prepared project metadata for the first pre-release.

### Phase 10: Release Readiness and Public Repo Polish
- Added `docs/VALIDATION_BASELINE.md` summarizing the validated state.
- Added `docs/RELEASE_READINESS.md` outlining project maturity and boundaries.
- Added `CONTRIBUTING.md` with validation-first guidelines.
- Added `SECURITY.md` for secret management and claim reporting.
- Finalized repository structure for public review.

### Phase 9: Agent Skill Pack
- Implemented repository-local agent skill pack in `.agent/skills/`.
- Added `agent_prompts/` for Gemini and Codex.
- Created `docs/AGENT_SKILLS.md` documenting the skill pack.

### Phase 8: Generated Audit Reports
- Implemented deterministic JSON report generation for replay contracts and adapters.
- Added `reports/generated/` directory for validation artifacts.
- Created `docs/AUDIT_REPORTS.md`.

### Phase 7: Negative Adapter Fixtures
- Implemented negative validation for runtime adapters.
- Added blocked claims for `provider_runtime`, `mcp_server`, and `auto_apply`.
- Ensured safety fields like `disabled_capabilities` are mandatory.

### Phase 6: AIR Runtime Adapter Design
- Created `schemas/adapter.schema.json`.
- Implemented `fixtures/adapter/ctxt-local.adapter.json`.
- Added `docs/RUNTIME_ADAPTERS.md`.

### Phase 5: Replay Contracts
- Implemented `scripts/validate_replay_contracts.py`.
- Defined fulfillment checks between AIR plans and Evidence chains.
- Added `docs/REPLAY_CONTRACTS.md`.

### Phase 4: Canonical Evidence Hashing
- Replaced placeholder hashes with real SHA-256.
- Implemented `json-c14n-v1` (RFC 8785) canonicalization.
- Verified parent-event hash-chain continuity.
