import json
from pathlib import Path

from canonical_json import hash_event, hash_json_file, hash_json_value

AIR_PATH = Path("fixtures/air/hash-chain.audit.air.json")
OUT_PATH = Path("fixtures/evidence/hash-chain.events.json")


def build_event(event_id, timestamp, event_type, action, air_hash, parent_hash=None, inputs=None, outputs=None, metadata=None):
    event = {
        "event_id": event_id,
        "air_ref": {
            "path": str(AIR_PATH),
            "hash": air_hash,
        },
        "timestamp": timestamp,
        "executor": {
            "id": "comptext-air-local",
            "type": "system",
        },
        "event_type": event_type,
        "action": action,
        "metadata": metadata or {},
    }

    if parent_hash is not None:
        event["parent_event_hash"] = parent_hash

    if inputs:
        event["inputs"] = inputs

    if outputs:
        event["outputs"] = outputs

    event["event_hash"] = hash_event(event)
    return event


def main():
    air_hash = hash_json_file(AIR_PATH)

    start = build_event(
        event_id="evt-001",
        timestamp="2026-06-16T10:00:00Z",
        event_type="start",
        action="load_air_plan",
        air_hash=air_hash,
        inputs=[
            {
                "key": "air_plan",
                "hash": air_hash,
            }
        ],
        metadata={
            "phase": "phase-4",
            "claim": "AIR plan loaded from local fixture and hashed with json-c14n-v1."
        },
    )

    validate_parent_input = hash_json_value({
        "previous_event_id": start["event_id"],
        "previous_event_hash": start["event_hash"],
        "contract": "parent_event_hash_equals_previous_event_hash"
    })

    verify = build_event(
        event_id="evt-002",
        timestamp="2026-06-16T10:00:05Z",
        event_type="verification",
        action="verify_parent_link",
        air_hash=air_hash,
        parent_hash=start["event_hash"],
        inputs=[
            {
                "key": "parent_link_contract",
                "hash": validate_parent_input,
            }
        ],
        metadata={
            "contract": "parent_event_hash_equals_previous_event_hash"
        },
    )

    report_payload = {
        "air_path": str(AIR_PATH),
        "events": ["evt-001", "evt-002"],
        "root_hash": verify["event_hash"],
        "status": "valid"
    }

    report_hash = hash_json_value(report_payload)

    end = build_event(
        event_id="evt-003",
        timestamp="2026-06-16T10:00:10Z",
        event_type="end",
        action="emit_validation_result",
        air_hash=air_hash,
        parent_hash=verify["event_hash"],
        outputs=[
            {
                "key": "validation_result",
                "hash": report_hash,
            }
        ],
        metadata={
            "result": "valid",
            "root_event_hash": verify["event_hash"]["value"]
        },
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps([start, verify, end], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
