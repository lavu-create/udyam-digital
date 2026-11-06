# Database Schema & Data Model Specification
## Project Udyam Digital: Relational Entity Architecture

**Document Version:** 1.0 (Implementation-Ready Schema)  
**Database Engines:** SQLite (Local MVP) / PostgreSQL (Cloud Production)  
**ORM:** SQLAlchemy 2.0 (Python)  

---

## 1. Entity-Relationship Diagram (ERD)

```mermaid
erDiagram
    BUSINESS ||--o{ LEAD : "generates"
    BUSINESS ||--o{ QUOTE : "requests"
    BUSINESS ||--o{ KYC_VERIFICATION : "undergoes"
    BUSINESS ||--o{ ORDER : "places"
    BUSINESS ||--o{ CONSENT_RECORD : "grants"

    PRODUCT ||--o{ PRODUCT_DEPENDENCY : "has"
    PRODUCT ||--o{ BUNDLE_ITEM : "included_in"
    PRODUCT ||--o{ QUOTE_ITEM : "billed_in"

    BUNDLE ||--o{ BUNDLE_ITEM : "contains"
    BUNDLE ||--o{ QUOTE : "initiates"

    QUOTE ||--o{ QUOTE_ITEM : "itemizes"
    QUOTE ||--o| ORDER : "converts_to"

    KYC_VERIFICATION ||--o{ KYC_DOCUMENT : "verifies"
    ORDER ||--o{ ORDER_MILESTONE : "tracks"

    BUSINESS {
        string business_id PK
        string business_name
        string business_type
        string segment
        string city
        int city_tier
        string state
        string preferred_language
        int employee_count
        int num_sites
        string gstin
        string udyam_number
        datetime created_at
    }

    PRODUCT {
        string product_id PK
        string category
        string product_name
        string description
        string unit
        float price_min_inr
        float price_max_inr
        float setup_fee_inr
        int min_contract_months
        string available_tiers
        int min_employees
        int min_sites
        string requires_gstin
        int install_days
        string target_segments
    }

    PRODUCT_DEPENDENCY {
        int id PK
        string product_id FK
        string required_one_of_ids
    }

    QUOTE {
        string quote_id PK
        string business_id FK
        string bundle_id FK
        float total_monthly_inr
        float total_setup_inr
        int contract_months
        string status
        datetime created_at
    }

    QUOTE_ITEM {
        int id PK
        string quote_id FK
        string product_id FK
        int quantity
        float unit_monthly_inr
        float unit_setup_inr
    }

    KYC_VERIFICATION {
        string verification_id PK
        string business_id FK
        string gstin
        string gstin_status
        string udyam_number
        string udyam_status
        string overall_status
        string failure_reason
        datetime verified_at
    }

    KYC_DOCUMENT {
        string document_id PK
        string verification_id FK
        string doc_type
        string file_name
        string storage_path
        float blur_score
        float rotation_angle
        string extracted_date
        int is_date_valid
        string extracted_name
        int is_name_matched
        string validation_status
        datetime uploaded_at
    }

    ORDER {
        string order_id PK
        string business_id FK
        string quote_id FK
        string status
        float monthly_bundle_value
        float setup_fee_value
        string estimated_install_date
        string assigned_technician
        datetime created_at
    }

    ORDER_MILESTONE {
        int id PK
        string order_id FK
        string milestone_code
        string milestone_name
        string status
        datetime completed_at
        string remarks
    }

    CONSENT_RECORD {
        string consent_id PK
        string business_id FK
        string consent_type
        string language
        int is_affirmative
        string ip_hash
        datetime granted_at
    }

    AUDIT_LOG {
        int id PK
        string action
        string entity_type
        string entity_id
        string masked_details
        string ip_hash
        datetime timestamp
    }
```

---

## 2. Table Specifications & Schema Definitions

### 2.1 Table: `businesses`
Stores the legal and operational profile of the MSME entity.

```sql
CREATE TABLE businesses (
    business_id VARCHAR(36) PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    business_type VARCHAR(100) NOT NULL,
    segment VARCHAR(50) NOT NULL, -- 'Micro retail & services', 'Professional offices', etc.
    city VARCHAR(100) NOT NULL,
    city_tier INT NOT NULL CHECK (city_tier IN (1, 2)),
    state VARCHAR(100) NOT NULL,
    preferred_language VARCHAR(20) DEFAULT 'Hindi',
    employee_count INT DEFAULT 1,
    num_sites INT DEFAULT 1,
    gstin VARCHAR(15),
    udyam_number VARCHAR(30),
    contact_name VARCHAR(100),
    contact_role VARCHAR(50),
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_businesses_gstin ON businesses(gstin);
CREATE INDEX idx_businesses_udyam ON businesses(udyam_number);
```

### 2.2 Table: `products` (Seeded from `product_catalogue.csv`)
Stores the 25 official enterprise product SKUs.

```sql
CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY, -- 'P01' through 'P25'
    category VARCHAR(50) NOT NULL,       -- 'Connectivity', 'Communication', 'Cloud & Productivity', 'Security', 'IoT & Physical'
    product_name VARCHAR(150) NOT NULL,
    description TEXT,
    unit VARCHAR(50) DEFAULT 'per site',
    price_min_inr FLOAT NOT NULL,
    price_max_inr FLOAT NOT NULL,
    setup_fee_inr FLOAT DEFAULT 0.0,
    min_contract_months INT DEFAULT 12,
    available_tiers VARCHAR(20) DEFAULT '1;2',
    min_employees INT DEFAULT 1,
    min_sites INT DEFAULT 1,
    requires_gstin VARCHAR(1) DEFAULT 'N' CHECK (requires_gstin IN ('Y', 'N')),
    typical_install_days INT DEFAULT 5,
    target_segments VARCHAR(100)
);
```

### 2.3 Table: `product_dependencies`
Enforces dependency rules such as `requires_one_of`.

```sql
CREATE TABLE product_dependencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(10) NOT NULL REFERENCES products(product_id),
    required_one_of VARCHAR(100) NOT NULL -- e.g., 'P01|P02|P03|P05|P06'
);
```

### 2.4 Table: `quotes` & `quote_items`
Records customer quote calculations and line-item configurations.

```sql
CREATE TABLE quotes (
    quote_id VARCHAR(36) PRIMARY KEY,
    business_id VARCHAR(36) NOT NULL REFERENCES businesses(business_id),
    total_monthly_inr FLOAT NOT NULL,
    total_setup_inr FLOAT NOT NULL,
    contract_months INT DEFAULT 12,
    status VARCHAR(30) DEFAULT 'DRAFT', -- 'DRAFT', 'ACCEPTED', 'EXPIRED'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE quote_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote_id VARCHAR(36) NOT NULL REFERENCES quotes(quote_id) ON DELETE CASCADE,
    product_id VARCHAR(10) NOT NULL REFERENCES products(product_id),
    quantity INT DEFAULT 1,
    unit_monthly_inr FLOAT NOT NULL,
    unit_setup_inr FLOAT NOT NULL
);
```

### 2.5 Table: `kyc_verifications` & `kyc_documents`
Tracks registry verification outcomes and document OCR analysis.

```sql
CREATE TABLE kyc_verifications (
    verification_id VARCHAR(36) PRIMARY KEY,
    business_id VARCHAR(36) NOT NULL REFERENCES businesses(business_id),
    gstin VARCHAR(15),
    gstin_status VARCHAR(30), -- 'Active', 'Cancelled', 'Suspended', 'NotFound'
    udyam_number VARCHAR(30),
    udyam_status VARCHAR(30), -- 'Active', 'NotFound'
    overall_status VARCHAR(30) NOT NULL, -- 'PASSED', 'REJECTED', 'MANUAL_REVIEW'
    failure_reason TEXT,
    verified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE kyc_documents (
    document_id VARCHAR(36) PRIMARY KEY,
    verification_id VARCHAR(36) NOT NULL REFERENCES kyc_verifications(verification_id),
    doc_type VARCHAR(50) NOT NULL, -- 'address_proof', 'gst_certificate', 'udyam_certificate', 'signatory_id'
    file_name VARCHAR(255) NOT NULL,
    storage_path VARCHAR(500) NOT NULL,
    blur_score FLOAT,              -- Laplacian variance
    rotation_angle FLOAT DEFAULT 0.0,
    extracted_date VARCHAR(20),
    is_date_valid INT DEFAULT 1,   -- 1 = Fresh (<90 days from 2026-07-15), 0 = Expired
    extracted_name VARCHAR(255),
    is_name_matched INT DEFAULT 1,
    validation_status VARCHAR(30) NOT NULL, -- 'VALID', 'BLURRY', 'EXPIRED', 'MISMATCH', 'MISSING'
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2.6 Table: `orders` & `order_milestones`
Manages post-checkout fulfillment and tracking state machine.

```sql
CREATE TABLE orders (
    order_id VARCHAR(36) PRIMARY KEY,
    business_id VARCHAR(36) NOT NULL REFERENCES businesses(business_id),
    quote_id VARCHAR(36) NOT NULL REFERENCES quotes(quote_id),
    status VARCHAR(50) DEFAULT 'KYC_VERIFIED',
    monthly_bundle_value FLOAT NOT NULL,
    setup_fee_value FLOAT NOT NULL,
    estimated_install_date VARCHAR(20),
    assigned_technician VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_milestones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id VARCHAR(36) NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    milestone_code VARCHAR(50) NOT NULL, -- 'KYC_VERIFIED', 'FEASIBILITY_CLEARED', 'DISPATCHED', 'SCHEDULED', 'ACTIVE'
    milestone_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING', -- 'COMPLETED', 'IN_PROGRESS', 'PENDING'
    completed_at TIMESTAMP,
    remarks TEXT
);
```

### 2.7 Table: `consent_records` & `audit_logs`
DPDP Act 2023 compliance ledger.

```sql
CREATE TABLE consent_records (
    consent_id VARCHAR(36) PRIMARY KEY,
    business_id VARCHAR(36) NOT NULL REFERENCES businesses(business_id),
    consent_type VARCHAR(100) NOT NULL, -- 'KYC_VERIFICATION', 'SERVICE_PROVISIONING'
    language VARCHAR(20) DEFAULT 'Hindi',
    is_affirmative INT DEFAULT 1,
    ip_hash VARCHAR(64),
    granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action VARCHAR(100) NOT NULL, -- 'REGISTRY_LOOKUP', 'DOCUMENT_OCR', 'CONSENT_RECORDED'
    entity_type VARCHAR(50),
    entity_id VARCHAR(50),
    masked_details TEXT,
    ip_hash VARCHAR(64),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3. Database Migration & Compatibility Strategy

- **Local MVP Development:** The system uses SQLite (`udyam_digital.db`) stored in the application data directory. Zero installation, zero external port configuration.
- **Enterprise / Cloud Deployment:** Using SQLAlchemy models, the exact same schema deploys directly to PostgreSQL via standard environment variable:
  `DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/udyam_digital`
- **Seeding Script:** At startup, `services/database.py` executes `init_db()` which automatically verifies that tables exist and seeds the 25 SKUs from `product_catalogue.csv` and dependencies if the database is fresh.

