from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    authenticated: bool
    issuer_tenant: str
    subject_tenant: str
    idempotency_key: str | None
    role: str


def can_issue(request: Request) -> bool:
    return (
        request.authenticated
        and request.issuer_tenant == request.subject_tenant
        and bool(request.idempotency_key)
        and request.role in {"certificate_issuer", "tenant_admin"}
    )


def main() -> None:
    assert not can_issue(Request(False, "a", "a", "key", "certificate_issuer"))
    assert not can_issue(Request(True, "a", "b", "key", "certificate_issuer"))
    assert not can_issue(Request(True, "a", "a", None, "certificate_issuer"))
    assert not can_issue(Request(True, "a", "a", "key", "learner"))
    assert can_issue(Request(True, "a", "a", "key", "certificate_issuer"))
    print("Certification negative safety cases passed")


if __name__ == "__main__":
    main()
