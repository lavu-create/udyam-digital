# Product Requirements Document (PRD)
## Project Udyam Digital: Making Small Businesses Go Digital in One Sitting

**Competition:** Airtel SYNC 2026 — Digital Track  
**Track:** Enterprise Track A (Case: Project Udyam Digital)  
**Document Version:** 1.0 (Implementation-Ready Specification)  
**Target Audience:** Engineering, Product, Design, and Evaluation Board  

---

## 1. Executive Summary & Product Vision

### 1.1 Vision Statement
To empower every Indian Micro, Small, and Medium Enterprise (MSME) proprietor—from local kirana shop owners and clinic administrators to multi-branch restaurateurs and textile manufacturers—to discover, customize, legally onboard, and provision enterprise-grade telecom and digital productivity tools **in one sitting (<10 minutes)** on a mobile device in their native language.

### 1.2 Core Value Proposition
- **Zero-Touch Self-Service:** Replaces slow, high-friction field sales rep visits (which currently cause 827 dropped leads out of 5,000) with an intelligent, conversational GenAI advisor.
- **Unbundled Pricing Transparency:** Replaces confusing 5-day quote PDFs with instant, modular monthly billing where add-ons can be toggled in real time.
- **Instant Smart KYC:** Eliminates multi-week paperwork delays and documentation drop-offs (273 dropped leads) via sub-second lookups against official GSTIN and Udyam registries, automated OCR verification, and affirmative DPDP Act 2023 consent flows.
- **Proactive Post-Order Transparency:** Provides a real-time milestone visual tracker that eradicates the baseline average of 3.01 status-chasing phone calls per customer.
- **Synergistic Partner Co-Pilot:** Integrates channel partners and field reps through attribution QR codes and drop-recovery queues rather than cannibalizing existing retail networks.

---

## 2. Target User Personas & Segment Requirements

Based on empirical analysis of the 5,000-lead cohort in `smb_leads.csv`, the platform caters to four distinct personas:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   TARGET PERSONA MATRIX                                          │
├───────────────────┬──────────────┬───────────────┬──────────────────────┬────────────────────────┤
│ Persona Name      │ Share / Base │ Monthly Spend │ Primary Requirements │ Key Operational Pains  │
├───────────────────┼──────────────┼───────────────┼──────────────────────┼────────────────────────┤
│ 1. Kirana Ramesh  │ 54.2%        │ ₹1,500–₹3,000 │ 100% reliable UPI /  │ Dependent on mobile    │
│    (Micro Retail  │ (2,709 leads)│ (Avg: ₹2,504) │ POS connectivity,    │ hotspots; zero tech    │
│    & Services)    │              │               │ WhatsApp catalogue   │ literacy; high churn   │
├───────────────────┼──────────────┼───────────────┼──────────────────────┼────────────────────────┤
│ 2. Dr. Priya Rao  │ 24.9%        │ ₹5,000–₹9,000 │ 99.9% uptime, secure │ Using consumer Gmail;  │
│    (Professional  │ (1,247 leads)│ (Avg: ₹6,796) │ cloud storage, clinic│ data privacy worries;  │
│    Offices)       │              │               │ domain email, Wi-Fi  │ need single bill       │
├───────────────────┼──────────────┼───────────────┼──────────────────────┼────────────────────────┤
│ 3. Vikram Anand   │ 15.1%        │ ₹20k–₹45k     │ Central multi-branch │ Managing 5 different   │
│    (Small Multi-  │ (755 leads)  │ (Avg: ₹31,233)│ billing, SD-WAN,     │ local ISPs; no IT team;│
│    Site Retail)   │              │               │ cloud CCTV, failover │ high billing confusion │
├───────────────────┼──────────────┼───────────────┼──────────────────────┼────────────────────────┤
│ 4. Suresh Patel   │ 5.8%         │ ₹15k–₹35k     │ Leased Line (ILL),   │ Frequent line drops;   │
│    (Small Manufac-│ (289 leads)  │ (Avg: ₹19,980)│ machine IoT sensors, │ delayed fault recovery;│
│    turer)         │              │               │ ERP connectivity     │ high bandwidth needs   │
└───────────────────┴──────────────┴───────────────┴──────────────────────┴────────────────────────┘
```

---

## 3. High-Level Requirements & Feature Traceability

| Req ID | Case Requirement / Feature | Priority | Implementation Module | Source Document Trace |
| :--- | :--- | :---: | :--- | :--- |
| **FR-01** | Multilingual Mobile Landing Page | Mandatory | Frontend Client | Case Brief Page 3 |
| **FR-02** | Rapid Business Profiling | Mandatory | Advisor & Business Svc | Case Brief Page 3 |
| **FR-03** | Conversational GenAI Advisor | Mandatory | AI Advisor Service | Case Brief Page 3 (Build Challenge) |
| **FR-04** | Segment-Tailored Bundle Recommendation | Mandatory | Catalog & Quote Engine | Case Brief Page 3 (Q1 & Build) |
| **FR-05** | Real-Time Interactive Quote Builder | Mandatory | Catalog & Quote Engine | Case Brief Page 3 (Build Challenge) |
| **FR-06** | Product Dependency & GSTIN Validation | Mandatory | Catalog & Quote Engine | README.md / product_catalogue.csv |
| **FR-07** | GSTIN Instant Registry Verification | Mandatory | Smart KYC Engine | Case Brief Page 3 & mock_gstin |
| **FR-08** | Udyam Instant Registry Verification | Mandatory | Smart KYC Engine | Case Brief Page 3 & mock_udyam |
| **FR-09** | Document Upload, Pre-check & Local OCR | Mandatory | Smart KYC Engine | Case Brief Page 3 & kyc_documents/ |
| **FR-10** | KYC Validation & Edge-Case Trapping | Mandatory | Smart KYC Engine | README.md / K01–K12 Scenarios |
| **FR-11** | Affirmative DPDP Act 2023 Consent Flow | Mandatory | Consent & Security Svc | Case Brief Page 3 & 4 (Privacy Note) |
| **FR-12** | Instant Order Placement & Provisioning | Mandatory | Order Management Svc | Case Brief Page 3 |
| **FR-13** | Real-Time Visual Milestone Order Tracker | Mandatory | Tracker Service | Case Brief Page 3 (Build Challenge) |
| **FR-14** | Partner & Field Sales Co-Pilot Console | Stretch Goal | Admin / Partner Svc | Case Brief Page 3 (Stretch Goals) |
| **FR-15** | Lead Propensity & Drop Risk Scoring | Stretch Goal | Propensity ML Service | Case Brief Page 3 (Stretch Goals) |

---

## 4. Detailed Functional Requirements (Step-by-Step Journey)

### Step 1: Landing Page (`FR-01`)
- **F-1.1:** Mobile-responsive landing screen branded with Airtel Business visual elements (`#E40000`).
- **F-1.2:** Prominent language switcher supporting English and Hindi (extensible to Marathi, Tamil, Telugu, Bengali).
- **F-1.3:** Hero proposition: "Get Your Business Digital in One Sitting — Reliable Internet, Cloud, Security & Billing in Under 10 Minutes."
- **F-1.4:** Dual entry points: "Start Self-Serve Digital Journey" or "Partner Assisted Login" (via referral/dealer code).

### Step 2: Quick Business Profiling (`FR-02`)
- **F-2.1:** Capture minimal initial fields: Business Name, City, City Tier (1 or 2), Employee Count, and Branch Site Count.
- **F-2.2:** Non-blocking inputs: Allows immediate transition to the Conversational Advisor.

### Step 3: Conversational AI Advisor (`FR-03`)
- **F-3.1:** Chat interface embedded directly on the mobile screen with voice-to-text input support.
- **F-3.2:** Plain-language conversational flow in user’s chosen language (Hindi/English).
- **F-3.3:** Collects current connectivity setup (mobile hotspot vs home broadband vs leased line), current spend, and key operational pain points (e.g., payment drops, lack of storage, CCTV needs).
- **F-3.4:** LLM Provider-independent backend with deterministic rule-based fallback when offline.

### Step 4: Business Needs Assessment (`FR-04`)
- **F-4.1:** Automatically maps business profile to one of the 4 primary segments.
- **F-4.2:** Formulates 3 transparent bundle recommendations:
  1. **Essential Starter Pack:** Core connectivity for micro budgets.
  2. **Recommended Growth Pack:** Connectivity + Cloud Email + Wi-Fi Security.
  3. **Enterprise Pro Pack:** High-capacity line + SD-WAN + Cloud CCTV + Backup.

### Step 5 & 6: Interactive Quote Configuration (`FR-05`, `FR-06`)
- **F-5.1:** Dynamically renders the selected bundle from the official 25-SKU catalogue.
- **F-5.2:** Enforces strict catalogue dependency logic:
  - If `P09` (Failover), `P10` (SD-WAN), or `P21` (Firewall) is selected, requires a base broadband SKU (`P01|P02|P03|P05|P06`).
  - If `P11` (Static IP) is selected, requires `P01|P02|P03`.
  - If `P22` (Secure Wi-Fi) is selected, requires `P01|P02|P03|P04`.
  - If `P23` (CCTV) is selected, requires base broadband or AirFiber.
- **F-5.3:** Validates mandatory GSTIN requirement (`requires_gstin == 'Y'`). If the user has no GSTIN, disables or warns against adding `P03`, `P05`, `P06`, `P10`, `P12`, `P13`, `P14`, `P15`, `P21`, or `P24`.
- **F-5.4:** Allows interactive add-on quantity adjustment (e.g., number of SIMs, CCTV cameras).

### Step 7 & 8: Transparent Monthly Pricing & Checkout (`FR-05`)
- **F-7.1:** Consolidated Single Monthly Price: Aggregates recurring telecom and cloud costs into one transparent figure.
- **F-7.2:** Clear One-Time Setup Fee line item (e.g., ₹0 for Biz Fibre, ₹2,000 for SIP Trunk, ₹10,000 for Leased Line).
- **F-7.3:** Contract commitment transparency: Explicit display of minimum lock-in months (12 or 24 months).
- **F-7.4:** Checkout summary with itemized breakdown and zero hidden charges.

### Step 9: GSTIN Instant Verification (`FR-07`)
- **F-9.1:** Input field with real-time format validation (15-character alphanumeric, allowing character `X` at PAN position 4 per synthetic rules).
- **F-9.2:** Sub-second lookup against `mock_gstin_registry.csv` (3,534 records).
- **F-9.3:** Status validation: Immediately flags and halts onboarding if GSTIN status is `Cancelled` (167 records) or `Suspended` (101 records).
- **F-9.4:** Auto-populates Legal Name, Trade Name, Entity Constitution, and Registered Address upon active match.

### Step 10: Udyam Registration Verification (`FR-08`)
- **F-10.1:** Input field with format check (`UDYAM-<StateCode>-00-<7Digits>`).
- **F-10.2:** Lookup against `mock_udyam_registry.csv` (2,723 records).
- **F-10.3:** Auto-populates Enterprise Type (Micro, Small, Medium) and NIC activity description.

### Step 11: Document Upload, Quality Pre-check & OCR (`FR-09`)
- **F-11.1:** Mobile-friendly file uploader supporting PNG, JPG, and PDF.
- **F-11.2:** Image Quality Pre-check:
  - Blur Detection: Computes Laplacian variance. Rejects images below sharpness threshold (trapping blurry uploads like `K04`).
  - Auto-Deskewing: Detects orientation and rotation angles, correcting skewed documents like `K02`.
- **F-11.3:** In-Memory Vision & Verification Engine: Evaluates image quality (sharpness, rotation) and validates structured fields in memory without forwarding customer documents to external third-party AI APIs.

### Step 12: KYC Validation & Exception Handling (`FR-10`)
- **F-12.1:** Freshness Validation: Validates that address proof / electricity bills are dated within 90 days of the fixed baseline date **2026-07-15**. Rejects expired documents (trapping `K11` electricity bill dated 2025-10-31).
- **F-12.2:** Field Cross-Matching: Verifies that Trade Name / Legal Name extracted via OCR matches the registered GSTIN/Udyam data. Flags discrepancies (trapping `K07` where doc says "Shri Physio Clinic" but registry says "Neelgiri Physio Clinic").
- **F-12.3:** Incomplete Pack Detection: Traps missing mandatory documents (trapping `K05` where Udyam certificate is omitted).
- **F-12.4:** Graceful Exception UI: Provides clear, actionable failure explanations with a one-click "Upload Fresh Copy" or "Request Assisted Verification" button.

### Step 13: Affirmative DPDP Act 2023 Consent (`FR-11`)
- **F-13.1:** Presents clear, unbundled consent notice in the user's selected language.
- **F-13.2:** Explicit checkboxes for:
  1. Identity verification via GSTIN/Udyam registries.
  2. Installation address verification via utility bill.
  3. Service provisioning and communication via WhatsApp/SMS.
- **F-13.3:** Displays exact data processing notice (documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs; production roadmap specifies HSM encryption and 30-day purge post-activation).
- **F-13.4:** Digital signature or OTP verification capture.

### Step 14: Order Confirmation & Provisioning Kickoff (`FR-12`)
- **F-14.1:** Generates unique Order ID (e.g., `ORD-2026-XXXX`).
- **F-14.2:** Creates downloadable digital confirmation receipt and sends WhatsApp confirmation notification.
- **F-14.3:** Automatically schedules technician installation slot based on product install SLA (from `typical_install_days`).

### Step 15: Real-Time Visual Milestone Order Tracker (`FR-13`)
- **F-15.1:** Customer-facing progress tracker accessible via Order ID or registered mobile number.
- **F-15.2:** 5 distinct real-time milestone states:
  1. `KYC_VERIFIED`: Legal documents and registries approved.
  2. `FEASIBILITY_CLEARED`: Fibre loop and wireless signal verified.
  3. `HARDWARE_DISPATCHED`: Router / SIMs / CPE assigned and shipped.
  4. `ENGINEER_SCHEDULED`: Technician name and time slot confirmed.
  5. `SERVICE_ACTIVE`: Connection active, unified billing cycle initialized.
- **F-15.3:** Eliminates status-chasing phone calls by displaying current progress, technician contact, and expected activation date.

---

## 5. Non-Functional Requirements (NFR)

### 5.1 Performance & Latency
- **NFR-P1:** Initial page load under 1.5 seconds on a standard 4G mobile network.
- **NFR-P2:** Sub-second API responses (<300ms) for GSTIN and Udyam registry lookups.
- **NFR-P3:** Document OCR extraction and verification completed within 3.5 seconds.

### 5.2 Security & Privacy (DPDP Act, 2023)
- **NFR-S1:** TLS 1.3 encryption in transit for all client-server communications.
- **NFR-S2:** Documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs. Production deployment requires further security and retention assessment.
- **NFR-S3:** PII Data Masking: Aadhaar, PAN, and signatory IDs masked in logs and client UI.
- **NFR-S4:** No External AI Forwarding: Customer documents and PII are not forwarded to external third-party AI APIs.

### 5.3 Reliability & Local Execution
- **NFR-R1:** 100% self-contained local execution capability without requiring paid cloud API keys or external services.
- **NFR-R2:** Deterministic rule engine fallback if GenAI LLM API is unavailable.

### 5.4 Usability & Accessibility
- **NFR-A1:** Mobile-first responsive design compliant with WCAG 2.1 AA contrast standards.
- **NFR-A2:** Form inputs optimized for touch keyboards with numerical keypads for numbers and uppercase formatting for GSTINs.

