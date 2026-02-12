# Security Checklist

## Immediate actions
1. Revoke and rotate the previously committed Google API key.
2. Update local secrets in `gcp.env` (not committed).
3. Confirm all required Google API restrictions are enabled:
   - Allowed APIs only
   - Allowed referrers/IPs only
   - Per-key quotas and alerts

## Repository hygiene
- `gcp.env` is now git-ignored and templated via `gcp.env.example`.
- If this repo was pushed to a remote, scrub git history before sharing:
  - Rewrite history to remove old `gcp.env` contents.
  - Force-push the cleaned branch.
  - Invalidate old clones/forks that may still contain leaked secrets.

## Operational guardrails
- Store production secrets in a secret manager, not plaintext files.
- Rotate keys regularly.
- Run secret scanning in CI before merge.
