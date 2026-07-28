# ADR 0001: Server-authoritative certification

## Status

Accepted.

## Decision

Certificate issuance, canonicalisation, signing, status transitions, revocation and verification decisions execute only in trusted server components. Clients may render and request operations but cannot authoritatively create or alter credentials.

## Consequences

- Signing keys never reach browsers or mobile clients.
- Public verification exposes only the minimum required fields.
- Every lifecycle transition is audited with tenant, actor, request and key-version context.
- Offline displays are informational and must be revalidated when authoritative status is required.
