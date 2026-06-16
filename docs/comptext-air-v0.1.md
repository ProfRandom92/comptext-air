# CompText AIR v0.1

This document describes the structure and fields of CompText AIR (Agent Intermediate Representation) version 0.1, as defined by `air.schema.json`.

## Schema: `air.schema.json`

The `air.schema.json` defines the core structure of an AIR artifact. Each artifact represents a distinct, immutable record of an agent's action or proposal within the CompText ecosystem.

### Fields:

*   **`version`** (string):
    *   **Description:** Specifies the version of the AIR schema to which this artifact conforms (e.g., "v0.1").
    *   **Significance:** Ensures forward and backward compatibility and proper interpretation of the artifact's structure.
*   **`timestamp`** (string, `date-time` format):
    *   **Description:** An ISO 8601 formatted timestamp indicating when the AIR artifact was generated.
    *   **Significance:** Provides a precise chronological record of agent operations, crucial for audit trails and temporal analysis.
*   **`agent_id`** (string):
    *   **Description:** A unique identifier for the specific agent instance that created this AIR artifact.
    *   **Significance:** Identifies the origin of the agent's action, enabling accountability and tracing.
*   **`task_id`** (string):
    *   **Description:** A unique identifier for the overarching task or session with which this AIR artifact is associated.
    *   **Significance:** Groups related agent actions under a single logical unit, simplifying task management and analysis.
*   **`input_prompt_hash`** (string, SHA-256 hash):
    *   **Description:** A SHA-256 hash of the input prompt (or previous AIR artifact's output proposal hash) that triggered the generation of this AIR.
    *   **Significance:** Establishes a verifiable link to the preceding state or instruction, forming a crucial part of the audit chain and ensuring immutability of context.
*   **`output_proposal_hash`** (string, SHA-256 hash):
    *   **Description:** A SHA-256 hash of the `payload` field contained within this AIR artifact.
    *   **Significance:** Guarantees the integrity and immutability of the agent's proposed action or output. Any alteration to the payload would result in a different hash.
*   **`payload`** (object):
    *   **Description:** A generic JSON object that holds the actual content of the agent's action, proposal, or intermediate representation. The structure of this object will vary depending on the agent's task and the specific operation being performed.
    *   **Significance:** Encapsulates the core data produced by the agent, allowing for flexible and extensible definitions of agent behaviors without altering the core AIR schema.

## Examples of Valid AIR Artifacts

### Minimal AIR Artifact Example

```json
{
  "version": "v0.1",
  "timestamp": "2026-01-01T12:00:00Z",
  "agent_id": "agent-alpha-123",
  "task_id": "task-456",
  "input_prompt_hash": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "output_proposal_hash": "f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1",
  "payload": {
    "action": "log",
    "message": "Agent started successfully."
  }
}
```

### AIR Artifact within a Hash Chain Example

This example demonstrates how `input_prompt_hash` can link to a previous `output_proposal_hash`, forming a verifiable chain.

```json
{
  "version": "v0.1",
  "timestamp": "2026-01-01T12:05:00Z",
  "agent_id": "agent-beta-789",
  "task_id": "task-456",
  "input_prompt_hash": "f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1",
  "output_proposal_hash": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
  "payload": {
    "action": "execute_command",
    "command": "git status --porcelain"
  }
}
```

## Validation Rules

To be considered a valid CompText AIR artifact, the following rules must be met:

1.  **JSON Syntax:** Must be a valid JSON object.
2.  **Required Fields:** Must contain all required fields: `version`, `timestamp`, `agent_id`, `task_id`, `input_prompt_hash`, `output_proposal_hash`, and `payload`.
3.  **No Extra Fields:** Must not contain any fields outside of the defined schema (strict mode).
4.  **Version:** Must use a supported version string (e.g., `"v0.1"`).
5.  **Hash Format:** `input_prompt_hash` and `output_proposal_hash` must be lower-case hexadecimal strings exactly 64 characters long (SHA-256).
6.  **Timestamp:** Must follow ISO 8601 `date-time` format.
7.  **Payload:** Must be a JSON object.

### Invalid AIR Artifact Examples

#### Missing Required Field

```json
{
  "version": "v0.1",
  "timestamp": "2026-01-01T12:00:00Z",
  "agent_id": "agent-alpha-123",
  "task_id": "task-456",
  "input_prompt_hash": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "payload": {
    "action": "log",
    "message": "Missing output_proposal_hash"
  }
}
```

#### Invalid Hash Format

```json
{
  "version": "v0.1",
  "timestamp": "2026-01-01T12:00:00Z",
  "agent_id": "agent-alpha-123",
  "task_id": "task-456",
  "input_prompt_hash": "invalid-hash",
  "output_proposal_hash": "f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1",
  "payload": {
    "action": "log",
    "message": "Invalid input_prompt_hash format"
  }
}
```
