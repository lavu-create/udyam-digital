# Data Privacy & Security Architecture
## Compliance Design Aligned with the Digital Personal Data Protection (DPDP) Act, 2023

**Document Version:** 1.0 (Implementation-Ready Privacy Blueprint)  
**Regulatory Anchor:** Digital Personal Data Protection Act, 2023 (Republic of India)  
**Application Scope:** Project Udyam Digital — MSME Digital Acquisition & Onboarding  

---

## 1. Regulatory Context & Engineering Commitment

The **Digital Personal Data Protection (DPDP) Act, 2023** establishes obligations for Data Fiduciaries collecting and processing digital personal data in India. 

> [!IMPORTANT]
> **DISCLAIMER ON COMPLIANCE SCOPE:**  
> This document specifies **concrete technical and software engineering controls** implemented in the Project Udyam Digital prototype to align with DPDP Act principles. It does not constitute a formal legal opinion or statutory legal certification. All data processed within this platform uses synthetic test registries and fictional applicant documents.

---

## 2. Core DPDP Act Principles & Implemented Technical Controls

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DPDP ACT 2023 CONTROL MAPPING                                   │
├──────────────────────────┬────────────────────────────┬────────────────────────────────┤
│ DPDP Statutory Principle │ Legal Intent               │ Implemented Technical Control  │
├──────────────────────────┼────────────────────────────┼────────────────────────────────┤
│ 1. Notice & Affirmative  │ Clear, multilingual notice │ Explicit, unbundled checkboxes │
│    Consent (Section 6)   │ before data collection;    │ in Hindi & English; granular   │
│                          │ voluntary & affirmative    │ per-purpose consent recording. │
├──────────────────────────┼────────────────────────────┼────────────────────────────────┤
│ 2. Purpose Limitation    │ Data processed strictly for│ KYC data collected solely for  │
│    (Section 5)           │ specified telecom service  │ statutory telecom provisioning;│
│                          │ onboarding purpose.        │ zero secondary marketing use.  │
├──────────────────────────┼────────────────────────────┼────────────────────────────────┤
│ 3. Data Minimisation     │ Collect only minimum data  │ No GSTIN requested for retail  │
│    (Section 6(1))        │ necessary for product pack.│ broadband; only statutory ID   │
│                          │                            │ and supply address collected.  │
├──────────────────────────┼────────────────────────────┼────────────────────────────────┤
│ 4. Storage Limitation    │ Retain personal data only  │ Ephemeral in-memory processing;│
│    & Deletion (Sec 8(7)) │ as long as required.       │ no external AI API forwarding; │
│                          │                            │ roadmap 30-day purge policy.   │
├──────────────────────────┼────────────────────────────┼────────────────────────────────┤
│ 5. Reasonable Security   │ Protect against data leaks │ TLS 1.3 in transit; local CV;  │
│    Safeguards (Sec 8(5)) │ or unauthorized access.    │ no external AI API forwarding; │
│                          │                            │ PII masking in logs & UI.      │
└──────────────────────────┴────────────────────────────┴────────────────────────────────┘
```

---

## 3. Deep Dive: Implemented Privacy Controls

### 3.1 Affirmative & Multilingual Consent Flow (`Section 6`)
- **Unbundled Notice:** Consent is never hidden inside broad Terms of Service. It is presented on a standalone, dedicated verification screen (`Step 13`).
- **Vernacular Language Support:** Notices are provided in the proprietor’s selected language (Hindi and English).
- **Granular Consent Items:**
  1. *Registry Verification:* "I authorize Airtel to verify my business registration details with government GSTIN and Udyam databases."
  2. *Site Feasibility:* "I authorize verification of my electricity/utility bill strictly for installation premises feasibility."
  3. *Operational Messaging:* "I agree to receive provisioning updates via SMS and WhatsApp."
- **Immutable Consent Logging:** Each consent transaction records:
  - `business_id`
  - `timestamp` (UTC ISO 8601)
  - `consent_items_accepted`
  - `language`
  - `ip_hash` (One-way SHA-256 hash of client IP)

### 3.2 Purpose Limitation & Data Minimisation (`Section 5 & 6(1)`)
- **Catalogue-Driven Data Minimisation:**
  - If a proprietor orders basic broadband (`P01` Biz Fibre 100) or mobile SIMs (`P07`), which do not mandate statutory GST registration (`requires_gstin == 'N'`), the application **does not prompt for or require a GST certificate**.
  - GSTIN is requested *only* when the selected bundle includes enterprise-tier products (`P03`, `P05`, `P10`, `P21`) where commercial tax compliance is statutorily required.
- **Selective Field Extraction:**
  - The OCR engine extracts strictly required fields: Consumer No, Supply Address, and Bill Date. Unrelated fields (such as meter reading history or tariff calculations) are discarded immediately from memory.

### 3.3 No External Third-Party AI API Forwarding & In-Memory Vision Processing
- **Critical Architecture Boundary:** Documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs. Production deployment requires further security and retention assessment.
- **Local Vision Engine:** Image preprocessing (Laplacian blur assessment, rotation/deskewing) and validation checks are executed in memory by the backend application runtime.
- **Advisor Isolation:** The Conversational Advisor is strictly confined to business needs conversation. It never receives or processes document images or KYC payloads.

### 3.4 PII Masking & Redaction Standards
To prevent exposure in application logs, customer service interfaces, or partner views:
- **Aadhaar / Signatory ID:** Redacted to display only the last 4 characters (`XXXX-XXXX-1234`).
- **Phone Numbers:** Masked in status views (`XXXXXX9821`).
- **PAN / GSTIN:** Embedded PAN characters are masked in public tracker screens.
- **Log Sanitation:** A custom logging middleware inspects all outbound logs and strips JSON fields matching sensitive keys (`tax_id`, `signatory_id`, `phone`, `document_bytes`).

### 3.5 Storage Limitation & Deletion Policy (`Section 8(7)`)
- **Ephemeral In-Memory Verification (Prototype Implementation):**
  - Documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs. Production deployment requires further security and retention assessment.
  - Raw document binary payloads are evaluated ephemerally in memory during request execution rather than written to persistent application databases.
  - Verification tokens and audit timestamps are logged without storing raw document binary files.
- **Production Roadmap Specification (Commercial Scale):**
  - For commercial production rollout, documents will reside in an HSM-backed AES-256-GCM encrypted volume with a background cryptographic shredder enforcing automated hard-deletion at T+30 days post-activation (`SERVICE_ACTIVE`).
  - Statutory Department of Telecommunications (DoT) compliance hashes will be retained in the audit ledger per telecom licensing requirements.

### 3.6 Access Control & Role-Based Authorization
- **Customer View:** Authenticated strictly by active session or OTP-verified Order ID. Customers can only view their own order status.
- **Partner / Sales View:** Channel partners and field executives access an aggregated console. Sensitive customer PII is masked; partners can only trigger callback requests or view progress states.

---

## 4. Privacy Audit Ledger Architecture

The system maintains an append-only audit trail (`audit_logs` table) recording every operation touching identity data:

```sql
-- Audit record generated on every registry lookup or document verification
INSERT INTO audit_logs (action, entity_type, entity_id, masked_details, ip_hash, timestamp)
VALUES (
    'GSTIN_LOOKUP',
    'BUSINESS',
    'biz-8821',
    '{"gstin": "19EOXXXXXXX1ZL", "status": "Active", "source": "MOCK_REGISTRY"}',
    'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    '2026-11-06T19:30:00Z'
);
```

This guarantees full auditability for regulatory compliance reviews without unnecessarily persisting unencrypted personal data in log streams.

