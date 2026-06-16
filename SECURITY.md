# Security Policy

## Secrets and Credentials
CompText AIR is a contract and validation repository. It **does not handle secrets**, API keys, or personal credentials.
- **Fixtures:** All fixtures must use synthetic or public data.
- **Reports:** Generated audit reports must never contain sensitive local environment data.
- **Pre-commit:** Please check your changes for any accidental inclusion of `.env` files or hardcoded keys.

## Reporting Vulnerabilities
If you identify a way to bypass the validation logic or discover an unsafe claim being made by the repository, please report it as a security issue.

Specific areas of concern:
- **Hash Collisions:** Vulnerabilities in the canonicalization or hashing process.
- **Fulfillment Bypass:** Evidence chains that appear to satisfy a plan but skip critical steps.
- **Boundary Overclaims:** Introduction of forbidden claims (like production MCP or provider runtime) that bypass the adapter validator.

## Security Boundaries
This project provides technical validation of agent activity. It does not provide:
- Network security.
- Process isolation.
- Legal or forensic guarantees.

The safety of the execution environment (the "Runtime") is the responsibility of the adapter implementation, not the AIR layer itself.
