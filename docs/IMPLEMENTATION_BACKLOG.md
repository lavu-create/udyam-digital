# Technical Implementation Backlog
## Project Udyam Digital: Granular, Ordered Development Plan

**Document Version:** 1.0 (Implementation-Ready Backlog)  
**Strategy:** End-to-End Vertical Slice First (Functional MVP -> Robust Verification -> Polish)  

---

## Sprint Overview & Phase Sequence

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              DEVELOPMENT MILESTONES                                    │
├─────────┬──────────────────────────┬───────────────────────────────────────────────────┤
│ Sprint  │ Focus Area               │ Core Deliverable                                  │
├─────────┼──────────────────────────┼───────────────────────────────────────────────────┤
│ Track 1 │ Foundation & Data Engine │ SQLite DB, 25-SKU Catalog, & Mock Registries      │
│ Track 2 │ Backend Core Services    │ FastAPI Router, Rules Engine, KYC Verification    │
│ Track 3 │ Frontend Core Journey    │ React App: Advisor, Quote Builder, KYC, & Tracker │
│ Track 4 │ Smart KYC & OCR Harness  │ Image Pre-check, Deskew, Date Check (K01–K12)     │
│ Track 5 │ Polish & Stretch Goals   │ i18n Hindi/English, Partner Console, Containerize │
└─────────┴──────────────────────────┴───────────────────────────────────────────────────┘
```

---

## Detailed Task Breakdown

### Milestone 1: Foundation, Database & Catalog Engine

#### `TASK-01`: Project Scaffolding & Virtual Environment
- **Description:** Initialize backend project layout (`backend/`), configure Python virtual environment, install FastAPI, Uvicorn, SQLAlchemy, Pydantic, Pillow, and pytest.
- **Files/Modules:** `backend/requirements.txt`, `backend/main.py`, `backend/config.py`
- **Dependencies:** None
- **Acceptance Criteria:** FastAPI server boots and returns `{"status": "healthy"}` at `GET /health`.
- **Testing:** `curl http://localhost:8000/health` returns HTTP 200.

#### `TASK-02`: Database Models & SQLite Persistence
- **Description:** Implement SQLAlchemy models for `businesses`, `products`, `quotes`, `quote_items`, `kyc_verifications`, `kyc_documents`, `orders`, `order_milestones`, `consent_records`, and `audit_logs`.
- **Files/Modules:** `backend/models/database.py`, `backend/services/database.py`
- **Dependencies:** `TASK-01`
- **Acceptance Criteria:** `init_db()` automatically creates all tables in `udyam_digital.db`.
- **Testing:** Pytest script verifying table schema generation and CRUD operations.

#### `TASK-03`: Catalog Ingestion & Dependency Engine
- **Description:** Ingest `product_catalogue.csv` (25 SKUs) into the database on startup. Implement the dependency evaluation engine verifying `requires_one_of` and `requires_gstin == 'Y'`.
- **Files/Modules:** `backend/services/catalog_service.py`, `backend/routers/catalog.py`
- **Dependencies:** `TASK-02`
- **Acceptance Criteria:** `GET /api/v1/catalog/products` returns 25 SKUs. Adding `P10` (SD-WAN) without base broadband throws `DEPENDENCY_UNSATISFIED`.
- **Testing:** Unit tests verifying all 7 dependency combinations and 10 GSTIN-mandatory SKUs.

---

### Milestone 2: Mock Registries & Smart KYC Engine

#### `TASK-04`: Mock GSTIN & Mock Udyam Registry Services
- **Description:** Implement lookup endpoints querying `mock_gstin_registry.csv` (3,534 records) and `mock_udyam_registry.csv` (2,723 records).
- **Files/Modules:** `backend/services/registry_service.py`, `backend/routers/kyc.py`
- **Dependencies:** `TASK-01`
- **Acceptance Criteria:**
  - Querying `19EOGXH4115Y1ZL` returns Harmony Dental Care (`Active`).
  - Querying `37IHKXV5167L1ZS` returns `Cancelled` status.
- **Testing:** Unit tests verifying active, cancelled, and not-found lookups with <10ms latency.

#### `TASK-05`: Local Image Pre-check & OCR Validation Engine
- **Description:** Implement document quality assessment (Laplacian blur variance), orientation/deskewing, and field extraction (Bill Date, Address, Consumer No).
- **Files/Modules:** `backend/services/ocr_engine.py`
- **Dependencies:** `TASK-01`
- **Acceptance Criteria:**
  - Traps blurred image `K04_gst_certificate.png` with `DOCUMENT_BLURRY`.
  - Auto-deskews `K02_gst_certificate.png`.
  - Rejects `K11_address_proof.png` (bill date `2025-10-31` exceeds 90-day threshold against anchor `2026-07-15`).
- **Testing:** Automated test suite running across all 47 specimen images in `kyc_documents/`.

#### `TASK-06`: Comprehensive KYC Orchestration & DPDP Consent
- **Description:** Implement unified KYC validation endpoint cross-matching OCR results against registry data and capturing affirmative DPDP Act 2023 consent.
- **Files/Modules:** `backend/services/kyc_orchestrator.py`, `backend/routers/kyc.py`
- **Dependencies:** `TASK-04`, `TASK-05`
- **Acceptance Criteria:** Traps legal name mismatch in `K07` ("Shri Physio Clinic" vs "Neelgiri Physio Clinic") and missing document in `K05`.
- **Testing:** Assertion matrix covering scenarios `K01` through `K12`.

---

### Milestone 3: AI Advisor & Order Tracker Services

#### `TASK-07`: GenAI Advisor Service with Rule-Based Fallback
- **Description:** Build the conversational advisor with prompt grounding in the 25-SKU catalogue, bilingual support (English/Hindi), and deterministic rule-based fallback.
- **Files/Modules:** `backend/services/advisor_service.py`, `backend/routers/advisor.py`
- **Dependencies:** `TASK-03`
- **Acceptance Criteria:**
  - Chat returns plain-language bundle recommendations.
  - Returns identical valid responses when LLM API keys are absent.
- **Testing:** Test cases for salon, dental clinic, retail chain, and textile factory inputs.

#### `TASK-08`: Order Management & Milestone Provisioning Engine
- **Description:** Create order fulfillment engine, calculate estimated install date from `typical_install_days`, and manage milestone progression state machine.
- **Files/Modules:** `backend/services/order_service.py`, `backend/routers/orders.py`
- **Dependencies:** `TASK-02`, `TASK-03`
- **Acceptance Criteria:** Creating an order produces a valid Order ID and initializes milestones (`KYC_VERIFIED`, `FEASIBILITY_CLEARED`, etc.).
- **Testing:** State transition tests for order progression.

---

### Milestone 4: Mobile-First Frontend Application

#### `TASK-09`: React App Setup, Brand Theming & i18n
- **Description:** Scaffold React 18 TypeScript application using Vite and Tailwind CSS. Implement Airtel Red (`#E40000`) theme and bilingual dictionary switcher (EN/HI).
- **Files/Modules:** `frontend/package.json`, `frontend/src/i18n/`, `frontend/tailwind.config.js`
- **Dependencies:** None
- **Acceptance Criteria:** Toggle button seamlessly switches all UI copy between English and Hindi without page refresh.
- **Testing:** Cypress / Jest rendering tests for language switching.

#### `TASK-10`: Conversational Advisor UI
- **Description:** Build WhatsApp-style chat interface with speech-to-text input, quick-reply suggestion chips, and audio playback.
- **Files/Modules:** `frontend/src/components/AdvisorChat.tsx`
- **Dependencies:** `TASK-07`, `TASK-09`
- **Acceptance Criteria:** Interactive messaging flow sending user prompts to backend and displaying recommended bundles.
- **Testing:** UI interaction tests.

#### `TASK-11`: Interactive Quote Builder & Checkout UI
- **Description:** Build the dynamic bundle customizer with add-on toggles, quantity sliders, setup fee badges, and consolidated monthly pricing.
- **Files/Modules:** `frontend/src/components/QuoteBuilder.tsx`
- **Dependencies:** `TASK-03`, `TASK-09`
- **Acceptance Criteria:** Toggling add-ons updates the monthly total and setup fee in real time.
- **Testing:** State updates and pricing calculation checks.

#### `TASK-12`: Smart KYC Upload & Verification Screen
- **Description:** Build document upload dropzones, instant GSTIN/Udyam lookup cards, error alert modals, and DPDP affirmative consent checkboxes.
- **Files/Modules:** `frontend/src/components/KYCVerification.tsx`
- **Dependencies:** `TASK-06`, `TASK-09`
- **Acceptance Criteria:** Shows real-time validation badges (Active/Cancelled) and gives user-friendly feedback on blurry or expired docs.
- **Testing:** File upload and error handling UI tests.

#### `TASK-13`: Real-Time Order Tracker UI
- **Description:** Build visual progress tracker displaying milestone states, technician appointment details, and SLA countdown.
- **Files/Modules:** `frontend/src/components/OrderTracker.tsx`
- **Dependencies:** `TASK-08`, `TASK-09`
- **Acceptance Criteria:** Renders progress timeline and technician contact card for active orders.
- **Testing:** Milestone visual rendering tests.

---

### Milestone 5: Stretch Goals, Containerization & Verification

#### `TASK-14`: Partner & Sales Co-Pilot Console
- **Description:** Build a lightweight partner view showing open leads, drop reasons, and propensity scores for assisted recovery.
- **Files/Modules:** `frontend/src/components/PartnerConsole.tsx`, `backend/routers/partner.py`
- **Dependencies:** `TASK-08`, `TASK-09`
- **Acceptance Criteria:** Displays list of dropped leads from `smb_leads.csv` with one-click "Escalate Callback" button.
- **Testing:** Propensity ranking and escalation API tests.

#### `TASK-15`: Docker Containerization & Single-Command Runner
- **Description:** Create multi-stage `Dockerfile` and `docker-compose.yml` for unified local/cloud execution, along with a `run_local.sh` fallback script.
- **Files/Modules:** `Dockerfile`, `docker-compose.yml`, `run_local.sh`
- **Dependencies:** All previous tasks
- **Acceptance Criteria:** Application boots via `./run_local.sh` or `docker-compose up` with zero manual intervention.
- **Testing:** Clean environment container boot and end-to-end user journey test.

