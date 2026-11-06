# API Specification & Endpoint Catalogue
## Project Udyam Digital: RESTful Interface Standard

**Document Version:** 1.0 (OpenAPI / Implementation-Ready)  
**Protocol:** HTTP/1.1 & HTTP/2 over TLS 1.3  
**Base URL:** `http://localhost:8000/api/v1` (Production: `https://udyam-digital.airtel.in/api/v1`)  
**Data Format:** JSON (`application/json`) / Multipart Form (`multipart/form-data`)  

---

## 1. Authentication & Security Architecture

- **Merchant Session State:** Stateless Session Token (`X-Session-ID: uuid4`) issued on initial landing page load and carried in request headers.
- **Partner / Admin Console:** Bearer API Token (`Authorization: Bearer <PARTNER_KEY>`) for sales co-pilot and drop recovery endpoints.
- **Data Protection:** All payloads carrying identifiers (GSTIN, Udyam, phone numbers) are masked in server log output.

---

## 2. Standard Error Response Format

All error responses return HTTP status codes in the 4xx or 5xx range with a predictable JSON envelope:

```json
{
  "success": false,
  "error_code": "GSTIN_STATUS_INVALID",
  "message": "The provided GSTIN is Cancelled in government tax records.",
  "details": {
    "gstin": "37IHKXV5167L1ZS",
    "status": "Cancelled",
    "suggested_action": "Please provide an active GSTIN or proceed using Udyam registration."
  },
  "timestamp": "2026-11-06T19:30:00Z"
}
```

Common Error Codes:
- `SCHEMA_VALIDATION_ERROR` (422)
- `GSTIN_NOT_FOUND` (404)
- `GSTIN_STATUS_INVALID` (400)
- `UDYAM_NOT_FOUND` (404)
- `DOCUMENT_BLURRY` (400)
- `DOCUMENT_EXPIRED` (400)
- `NAME_MISMATCH` (400)
- `DEPENDENCY_UNSATISFIED` (400)
- `GSTIN_REQUIRED_FOR_SKU` (400)

---

## 3. Core API Endpoint Catalogue

### 3.1 AI Advisor & Needs Discovery

#### `POST /api/v1/advisor/chat`
Handles conversational turn between the MSME owner and the GenAI Advisor.

- **Request Payload:**
```json
{
  "session_id": "sess-908123-ab",
  "language": "hi",
  "message": "मेरी जयपुर में 4 लोगों की सैलून की दुकान है। मुझे यूपीआई पेमेंट के लिए अच्छा इंटरनेट चाहिए।",
  "business_context": {
    "business_name": "Saffron Unisex Salon",
    "city": "Jaipur",
    "city_tier": 2,
    "employee_count": 4,
    "current_internet": "Mobile Hotspot"
  }
}
```

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "reply": "नमस्ते! आपके सैलून में यूपीआई पेमेंट और कस्टमर वाई-फाई के लिए 'Biz Fibre 100' सबसे बेहतरीन रहेगा। इसमें बिना रुके हाई-स्पीड इंटरनेट मिलता है ताकि क्यूआर कोड स्कैन तुरंत हो सके। क्या आपको सैलून की सुरक्षा के लिए सीसीटीवी कैमरा भी चाहिए?",
  "detected_needs": {
    "primary_connectivity": "Fibre",
    "bandwidth_mbps": 100,
    "recommended_skus": ["P01", "P07", "P22"]
  },
  "recommended_bundles": [
    {
      "bundle_id": "starter_micro",
      "name": "Essential Salon Pack",
      "monthly_inr": 1298.0,
      "products": ["P01", "P07"]
    },
    {
      "bundle_id": "growth_micro",
      "name": "Smart Salon Growth Pack",
      "monthly_inr": 1697.0,
      "products": ["P01", "P07", "P22"]
    }
  ]
}
```

---

### 3.2 Product Catalogue & Quote Engine

#### `GET /api/v1/catalog/products`
Returns all 25 active enterprise products with dependencies and rules.

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "total_products": 25,
  "products": [
    {
      "product_id": "P01",
      "category": "Connectivity",
      "product_name": "Biz Fibre 100",
      "description": "Business fibre broadband, 100 Mbps, unlimited data",
      "price_min_inr_per_month": 999.0,
      "price_max_inr_per_month": 1199.0,
      "one_time_setup_inr": 0.0,
      "requires_gstin": "N",
      "requires_one_of": null,
      "typical_install_days": 5
    },
    {
      "product_id": "P10",
      "category": "Connectivity",
      "product_name": "Managed SD-WAN",
      "description": "Multi-site secure SD-WAN edge router",
      "price_min_inr_per_month": 2500.0,
      "price_max_inr_per_month": 3500.0,
      "one_time_setup_inr": 5000.0,
      "requires_gstin": "Y",
      "requires_one_of": "P01|P02|P03|P05|P06",
      "typical_install_days": 14
    }
  ]
}
```

#### `POST /api/v1/quotes/calculate`
Validates dependencies and computes accurate single monthly pricing.

- **Request Payload:**
```json
{
  "business_id": "biz-8821",
  "has_gstin": true,
  "selected_items": [
    { "product_id": "P01", "quantity": 1 },
    { "product_id": "P07", "quantity": 2 },
    { "product_id": "P22", "quantity": 1 }
  ]
}
```

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "quote": {
    "quote_id": "QUO-2026-9901",
    "total_monthly_recurring_inr": 1996.0,
    "one_time_setup_fee_inr": 1000.0,
    "estimated_tax_inr": 359.28,
    "total_first_month_inr": 3355.28,
    "contract_duration_months": 12,
    "line_items": [
      { "product_id": "P01", "name": "Biz Fibre 100", "qty": 1, "monthly_inr": 999.0, "setup_inr": 0.0 },
      { "product_id": "P07", "name": "Business Postpaid 299", "qty": 2, "monthly_inr": 598.0, "setup_inr": 0.0 },
      { "product_id": "P22", "name": "Secure Wi-Fi", "qty": 1, "monthly_inr": 399.0, "setup_inr": 1000.0 }
    ],
    "dependency_validation": { "status": "PASSED", "violations": [] },
    "gstin_validation": { "status": "PASSED" }
  }
}
```

---

### 3.3 Smart KYC & Registry Verification

#### `POST /api/v1/verification/gstin`
Verifies GSTIN against `mock_gstin_registry.csv` and checks active status.

- **Request Payload:**
```json
{
  "gstin": "19EOGXH4115Y1ZL"
}
```

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "status": "Active",
  "data": {
    "gstin": "19EOGXH4115Y1ZL",
    "legal_name": "Joseph Shah (Prop. Harmony Dental Care)",
    "trade_name": "Harmony Dental Care",
    "constitution": "Proprietorship",
    "principal_place_of_business": "Shop/Unit 199, Station Road, Kolkata, West Bengal - 347550",
    "state": "West Bengal",
    "registration_date": "2022-04-17"
  }
}
```

#### `POST /api/v1/verification/udyam`
Verifies Udyam registration against `mock_udyam_registry.csv`.

- **Request Payload:**
```json
{
  "udyam_number": "UDYAM-WB-00-5053330"
}
```

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "data": {
    "udyam_number": "UDYAM-WB-00-5053330",
    "enterprise_name": "Harmony Dental Care",
    "enterprise_type": "Small",
    "major_activity": "Services",
    "nic_description": "Dental clinic",
    "state": "West Bengal",
    "city": "Kolkata",
    "date_of_registration": "2022-09-27"
  }
}
```

#### `POST /api/v1/verification/upload-document`
Ingests an image document, applies blur pre-check, auto-deskews, and extracts fields.

- **Request Payload (Multipart Form Data):**
  - `file`: binary image/png
  - `doc_type`: `address_proof` | `gst_certificate` | `udyam_certificate` | `signatory_id`
  - `applicant_ref`: `K01` (optional for benchmark testing)

- **Response Payload (200 OK — Valid Document):**
```json
{
  "success": true,
  "document_id": "doc-881290",
  "quality_assessment": {
    "blur_score": 342.5,
    "is_sharp": true,
    "rotation_detected_deg": 0.0
  },
  "extracted_data": {
    "consumer_number": "9790713533",
    "billed_to": "Harmony Dental Care",
    "supply_address": "Shop/Unit 199, Station Road, Kolkata, West Bengal - 347550",
    "bill_date": "2026-05-22",
    "units_consumed": 992
  },
  "compliance_validation": {
    "is_fresh": true,
    "days_old_from_anchor": 54,
    "status": "APPROVED"
  }
}
```

- **Response Payload (400 Bad Request — Trapping Expired Bill like K11):**
```json
{
  "success": false,
  "error_code": "DOCUMENT_EXPIRED",
  "message": "Electricity bill is dated 2025-10-31 which is 257 days old (exceeds 90-day threshold).",
  "details": {
    "bill_date": "2025-10-31",
    "anchor_date": "2026-07-15",
    "days_elapsed": 257,
    "allowed_max_days": 90
  }
}
```

---

### 3.4 Consent & Order Management

#### `POST /api/v1/consent/record`
Captures affirmative DPDP Act 2023 consent.

- **Request Payload:**
```json
{
  "business_id": "biz-8821",
  "consent_items": [
    { "type": "REGISTRY_LOOKUP", "agreed": true },
    { "type": "ADDRESS_VERIFICATION", "agreed": true },
    { "type": "SERVICE_PROVISIONING", "agreed": true }
  ],
  "language": "hi",
  "signature_token": "sig-hash-771290"
}
```

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "consent_id": "CNS-2026-1109",
  "timestamp": "2026-11-06T19:30:15Z",
  "audit_receipt": "AUD-DPDP-OK"
}
```

#### `POST /api/v1/orders/create`
Finalizes onboarding and initiates provisioning state machine.

- **Request Payload:**
```json
{
  "business_id": "biz-8821",
  "quote_id": "QUO-2026-9901",
  "consent_id": "CNS-2026-1109"
}
```

- **Response Payload (201 Created):**
```json
{
  "success": true,
  "order": {
    "order_id": "ORD-2026-KOL-1029",
    "status": "KYC_VERIFIED",
    "estimated_installation_days": 5,
    "estimated_install_date": "2026-11-11",
    "monthly_bill_inr": 1996.0,
    "tracking_url": "/track/ORD-2026-KOL-1029"
  }
}
```

#### `GET /api/v1/orders/{order_id}/status`
Returns real-time milestone progress.

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "order_id": "ORD-2026-KOL-1029",
  "business_name": "Harmony Dental Care",
  "current_status": "FEASIBILITY_CLEARED",
  "progress_percentage": 50,
  "milestones": [
    { "code": "KYC_VERIFIED", "name": "KYC & Legal Approval", "status": "COMPLETED", "date": "2026-11-06T19:30Z" },
    { "code": "FEASIBILITY_CLEARED", "name": "Fibre Node Checked", "status": "COMPLETED", "date": "2026-11-06T19:32Z" },
    { "code": "DISPATCHED", "name": "CPE Router Dispatched", "status": "IN_PROGRESS", "date": null },
    { "code": "SCHEDULED", "name": "Technician Appointment", "status": "PENDING", "date": null },
    { "code": "ACTIVE", "name": "Service Active", "status": "PENDING", "date": null }
  ],
  "technician_details": {
    "name": "Amit Sharma",
    "phone_masked": "XXXXXX9821",
    "scheduled_slot": "2026-11-10 10:00 AM - 12:00 PM"
  }
}
```

---

### 3.5 Partner & Sales Co-Pilot Endpoints

#### `GET /api/v1/partner/leads`
Lists leads with drop-risk propensity scores for partner follow-up.

- **Response Payload (200 OK):**
```json
{
  "success": true,
  "total_open_leads": 12,
  "leads": [
    {
      "lead_id": "L03571",
      "business_name": "Ganesh Woodcraft",
      "city": "Nagpur",
      "stage_reached": "KYC complete",
      "drop_reason": "First payment failed",
      "propensity_score": 0.89,
      "recommended_action": "High-value lead; retry digital payment link via WhatsApp"
    }
  ]
}
```

