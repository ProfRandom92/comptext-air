import json
import re
from pathlib import Path

HASH_RE = re.compile(r"^[a-f0-9]{64}$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
EVENT_TYPES = {"start", "step", "artifact", "end", "error", "verification"}
EXECUTOR_TYPES = {"agent", "human", "system"}

def fail(msg):
    raise ValueError(msg)

def validate_evidence_event(event, index=None):
    prefix = f"Event[{index}] " if index is not None else "Event "
    
    required = ["event_id", "air_hash", "timestamp", "executor", "event_type", "event_hash"]
    for field in required:
        if field not in event:
            fail(f"{prefix}missing required field: {field}")
            
    if not HASH_RE.match(event["air_hash"]):
        fail(f"{prefix}invalid air_hash")
    if not HASH_RE.match(event["event_hash"]):
        fail(f"{prefix}invalid event_hash")
    if "parent_event_hash" in event and not HASH_RE.match(event["parent_event_hash"]):
        fail(f"{prefix}invalid parent_event_hash")
        
    if not TIMESTAMP_RE.match(event["timestamp"]):
        fail(f"{prefix}invalid timestamp format (expected YYYY-MM-DDTHH:MM:SSZ)")
        
    executor = event["executor"]
    if not isinstance(executor, dict):
        fail(f"{prefix}executor must be an object")
    if "id" not in executor or "type" not in executor:
        fail(f"{prefix}executor missing id or type")
    if executor["type"] not in EXECUTOR_TYPES:
        fail(f"{prefix}invalid executor type")
        
    if event["event_type"] not in EVENT_TYPES:
        fail(f"{prefix}invalid event_type")

def validate_evidence_file(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        fail("Evidence fixture must be an array of events")
        
    previous_hash = None
    for i, event in enumerate(data):
        validate_evidence_event(event, i)
        
        # Hash chain validation
        if i == 0:
            if "parent_event_hash" in event:
                fail(f"Event[0] should not have parent_event_hash")
        else:
            if "parent_event_hash" not in event:
                fail(f"Event[{i}] missing parent_event_hash")
            if event["parent_event_hash"] != previous_hash:
                fail(f"Event[{i}] parent_event_hash mismatch: expected {previous_hash}, got {event['parent_event_hash']}")
        
        previous_hash = event["event_hash"]

def main():
    ok = True
    fixtures_dir = Path("fixtures/evidence")
    if not fixtures_dir.exists():
        print("No evidence fixtures found.")
        return

    for path in sorted(fixtures_dir.glob("*.events.json")):
        try:
            validate_evidence_file(path)
            print(f"OK {path}")
        except Exception as exc:
            print(f"BAD {path}: {exc}")
            ok = False

    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
