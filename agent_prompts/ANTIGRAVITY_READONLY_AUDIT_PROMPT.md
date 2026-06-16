# Antigravity / Agent Read-Only Audit Prompt

Audit this repo for CompText AIR readiness.

Strict mode:
- read-only
- no edits
- no commits
- no pushes
- no installs unless needed only for inspection
- no network actions unless explicitly approved

Find:
- parser/DSL code
- CLI commands
- runtime contracts
- evidence/hash/replay code
- docs and fixtures
- tests
- CI workflows
- risky claims about MCP/providers/autonomy

Output:
1. repo map
2. useful existing code
3. missing AIR pieces
4. risky/obsolete claims
5. recommended phase 1 patch plan
