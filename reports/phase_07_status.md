# Phase 07 Status Report - Negative Adapter Fixtures

PHASE: 7
MODE: offline-only
NETWORK: none
CHANGED_FILES:
- fixtures/adapter/invalid/*.adapter.json
- scripts/validate_adapter_fixtures.py
- docs/RUNTIME_ADAPTERS.md
- PROJEKT.md

## Goal
Prove that invalid or over-claiming AIR runtime adapters fail validation.

## Validation Results
- Valid adapter fixtures pass validation.
- Invalid adapter fixtures fail as expected.
- Missing `disabled_capabilities` is blocked.
- Missing `evidence_mapping` is blocked.
- Over-claiming `provider_runtime` is blocked.
- Over-claiming `mcp_server` is blocked.
- Over-claiming `auto_apply` is blocked.
- Over-claiming `network_required` is blocked.

## Blocked Claims
The following claims are explicitly forbidden in AIR adapters:
- provider_runtime
- mcp_server
- external_agent_execution
- auto_apply
- network_required
- production_runtime
- legal_assurance
- compliance_assurance
- forensic_assurance

## Risks
- None identified. Validation is strictly local and semantic.

## Next Step
Phase 8 (if applicable) or project wrap-up.
