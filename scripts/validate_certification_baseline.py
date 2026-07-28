from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = load("config/certificate-policy.json")
    signing = load("config/signing-policy.json")

    require(certificate["apiVersion"] == "v1", "API must be versioned")
    require(certificate["certificateId"]["immutable"], "Certificate IDs must be immutable")
    require("revoked" in certificate["status"], "Revocation state is required")
    require("tenantMatch" in certificate["issueRequires"], "Tenant isolation is required")
    require(certificate["verification"]["minimalDisclosure"], "Public verification must minimise disclosure")
    require(certificate["revocation"]["reasonRequired"], "Revocation reason is required")
    require({"en-GB", "ta-IN"}.issubset(certificate["locales"]), "English and Tamil locales are required")
    require(signing["privateKeyExportable"] is False, "Private signing keys must not be exportable")
    require(signing["keyRotationDays"] <= 90, "Signing keys must rotate at least every 90 days")
    require(signing["verificationKeys"]["versioned"], "Verification keys must be versioned")
    require(signing["compromiseResponse"]["securityIncident"], "Key compromise must trigger incident response")
    print("Certification baseline validation passed")


if __name__ == "__main__":
    main()
