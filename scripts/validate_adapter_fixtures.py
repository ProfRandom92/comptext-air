import json
import sys
from pathlib import Path

ADAPTER_FIXTURES_DIR = Path("fixtures/adapter")

VALID_KIND = {"local-cli", "mcp-proxy", "internal-vfs", "unknown"}
VALID_AIR_VERSION = "air-v0.1"

REQUIRED_TOP = [
    "adapter_id",
    "adapter_kind",
    "supported_air_version",
    "command_surface",
    "input_mapping",
    "output_mapping"
]

def fail(msg):
    print(f"FAILURE: {msg}")
    sys.exit(1)

def validate_adapter(fixture, fixture_path):
    if not isinstance(fixture, dict):
        fail(f"{fixture_path}: Adapter must be an object")

    for key in REQUIRED_TOP:
        if key not in fixture:
            fail(f"{fixture_path}: missing required field: {key}")

    if fixture["adapter_kind"] not in VALID_KIND:
        fail(f"{fixture_path}: invalid adapter_kind: {fixture['adapter_kind']}")

    if fixture["supported_air_version"] != VALID_AIR_VERSION:
        fail(f"{fixture_path}: unsupported air version: {fixture['supported_air_version']}")

    # Validate command_surface
    cs = fixture["command_surface"]
    if not isinstance(cs, dict) or "binary" not in cs or "commands" not in cs:
        fail(f"{fixture_path}: invalid command_surface structure")
    
    if not isinstance(cs["commands"], list):
        fail(f"{fixture_path}: command_surface.commands must be a list")

    # Validate input_mapping
    im = fixture["input_mapping"]
    if not isinstance(im, list):
        fail(f"{fixture_path}: input_mapping must be a list")
    for mapping in im:
        if not all(k in mapping for k in ["air_input_kind", "runtime_flag"]):
            fail(f"{fixture_path}: invalid input_mapping entry")

    # Validate output_mapping
    om = fixture["output_mapping"]
    if not isinstance(om, list):
        fail(f"{fixture_path}: output_mapping must be a list")
    for mapping in om:
        if not all(k in mapping for k in ["runtime_key", "air_output_kind"]):
            fail(f"{fixture_path}: invalid output_mapping entry")

def validate_adapter_fixtures():
    print("Validating AIR Adapter fixtures...")
    
    fixtures = list(ADAPTER_FIXTURES_DIR.glob("*.json"))
    if not fixtures:
        print("  No adapter fixtures found to validate.")
        return

    for fixture_path in fixtures:
        print(f"  Validating {fixture_path}...")
        try:
            with open(fixture_path, 'r') as f:
                fixture = json.load(f)
            validate_adapter(fixture, fixture_path)
                
        except json.JSONDecodeError as e:
            fail(f"JSON decode error in {fixture_path}: {e}")
        except Exception as e:
            fail(f"Unexpected error validating {fixture_path}: {e}")

    print("SUCCESS: All adapter fixtures are valid.")

if __name__ == "__main__":
    validate_adapter_fixtures()
