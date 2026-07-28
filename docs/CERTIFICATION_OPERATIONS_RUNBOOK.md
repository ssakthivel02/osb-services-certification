# Certification Operations Runbook

## Health checks

Validate API health, signing-key availability, verification-key publication, audit sink availability and revocation-store freshness.

## Issuance incident

1. Pause issuance for the affected tenant or qualification.
2. Preserve request IDs, audit events and signing-key version.
3. Identify duplicate, unauthorised or malformed certificates.
4. Revoke affected certificates with a machine-readable reason.
5. Reissue only after source evidence is revalidated.

## Signing-key compromise

1. Declare a security incident.
2. Disable the compromised key version.
3. Publish updated verification metadata.
4. Determine the affected issuance window.
5. Revoke and reissue impacted certificates.
6. Retain evidence and complete post-incident review.

## Verification degradation

Serve a clear unavailable response rather than treating unknown status as valid. Do not expose learner personal data in logs or error messages.

## Recovery evidence

Record recovery time, restored record counts, audit continuity, key-version integrity and verification tests before returning to normal operation.
