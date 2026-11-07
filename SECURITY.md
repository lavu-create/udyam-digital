# Security & Privacy Policy

## 1. Project Security Overview

**Project Udyam Digital** was architected for **Airtel SYNC 2026 – Digital Track** with strict data privacy and security controls. The platform is designed to demonstrate how enterprise telecom onboarding can operate without forwarding sensitive customer identity documents (PII) to external third-party AI APIs.

---

## 2. Technical Alignment with India's DPDP Act, 2023

The application implements concrete software engineering controls reflecting the statutory principles of India's *Digital Personal Data Protection (DPDP) Act, 2023*:

1. **Unbundled Affirmative Consent (Section 6):**
   - Consent is captured via explicit, granular checkboxes (statutory verification, physical feasibility, and operational alerts).
   - Notices are rendered in vernacular language (English and Hindi).
   - Zero pre-checked boxes or bundled deceptive consent patterns.

2. **Immutable Audit Logging:**
   - Every consent event captures an ISO 8601 UTC timestamp and a one-way SHA-256 hash of the client IP address.
   - Audit tokens (`DPDP-{id}-{hash}`) are recorded in the persistence ledger.

3. **In-Memory Document Assessment:**
   - Document upload checks (`POST /api/v1/kyc/upload-check`) evaluate Laplacian blur variance, dimensions, and rotation in memory.
   - Documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs. Production deployment requires further security and retention assessment.

4. **No External Third-Party AI API Forwarding:**
   - Business needs assessment, catalog rule evaluation, and document checks run within the backend environment without forwarding customer data to external third-party AI APIs.

---

## 3. Disclosures on Demonstration & Synthetic Data

To safeguard privacy and prevent any accidental disclosure of real business or individual data:
- **Synthetic Registry Datasets:** The application queries synthetic datasets (`mock_gstin_registry.csv` with 3,534 records and `mock_udyam_registry.csv` with 2,723 records). All business names, addresses, and registration numbers are demonstration fixtures.
- **Simulated Order Milestones:** Order progression milestones (`KYC_VERIFIED` → `FEASIBILITY_CLEARED` → `EQUIPMENT_DISPATCHED` → `INSTALLATION_SCHEDULED` → `SERVICE_ACTIVE`) and assigned technician contacts (*Simulated Field Tech, Demo Node #402, +91 98000 00000*) are demonstration simulations.
- **Document Freshness Rule:** The 90-day utility bill threshold is a case-study validation rule evaluated against anchor date `2026-07-15`.

---

## 4. Production Hardening Roadmap

For commercial telecom production, the following additional security layers are specified:
- Hardware Security Module (HSM) key management with per-tenant envelope encryption (AES-256-GCM).
- Automated cryptographic shredder cron daemon enforcing 30-day document purge post-activation.
- Secure GSP (GST Suvidha Provider) integration with mutual TLS (mTLS) for live government GSTN / MCA21 lookup.
- Role-Based Access Control (RBAC) separating field technician views from underlying applicant identity data.

---

## 5. Reporting a Security Vulnerability

If you discover a security vulnerability or sensitive data exposure within this repository:
1. Please **do not** open a public GitHub issue.
2. Report the vulnerability privately to the project maintainers via the competition submission portal or repository maintainer contact.
3. Include detailed reproduction steps and affected components.
4. We will review and remediate verified security issues promptly.

