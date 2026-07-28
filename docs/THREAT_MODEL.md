# Certification Threat Model

## Protected assets

- Signing keys and verification-key history
- Certificate identifiers and status
- Learner identity and qualification metadata
- Issuance, revocation and verification audit records

## Principal threats

1. Cross-tenant certificate issuance or lookup.
2. Forged, replayed or modified certificate payloads.
3. Private signing-key extraction or misuse.
4. Public verification leaking personal data.
5. Unauthorised revocation, suspension or reissue.
6. Duplicate issuance caused by retries.
7. Stale verification caches accepting revoked credentials.
8. QR codes redirecting to untrusted hosts.

## Required controls

- Authenticate privileged operations and authorise by tenant and role.
- Keep private keys in managed KMS/HSM storage and prohibit export.
- Sign canonical, versioned payloads and publish versioned public keys.
- Require idempotency keys for issuance and revocation requests.
- Return minimal public verification data.
- Record immutable audits for issue, verify, suspend, revoke and reissue events.
- Bind QR codes to an allow-listed HTTPS verification origin.
- Propagate revocation quickly and bound cache lifetimes.

## Trust boundary

Candidate and browser clients are untrusted. Certificate creation, signing, status transitions and verification decisions are server-authoritative.
