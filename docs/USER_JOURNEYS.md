# Detailed User Journey Specification
## Project Udyam Digital: 15-Step Mobile-First Onboarding Experience

**Document Version:** 1.0 (Implementation-Ready UX Flow)  
**Target User:** Non-technical Indian MSME Proprietors & Clinic / Office Admins  
**Languages:** English & Hindi (Bilingual Architecture)  

---

## Overview & UX Guiding Principles

1. **One-Sitting Completion (<10 Minutes):** Every friction point that traditionally delayed the sale by days (sales executive visits, 5-day quote generation, physical document collection) is compressed into an immediate, mobile-first step.
2. **Vernacular & Plain-Language Communication:** Eliminates telco technical jargon ("PRI lines", "CIR", "Static subnets", "ONT ports"). Speaks in terms the merchant understands: "Fast Internet for POS/UPI", "Office Email", "Security Cameras".
3. **No Dead Ends / Actionable Feedback:** When a verification fails (e.g., blurred image, expired electricity bill, cancelled GSTIN), the user is never stranded with an ambiguous error code. The system clearly explains what is wrong and provides an immediate remediation path.

---

## Detailed 15-Step User Journey

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE 15-STEP ONBOARDING JOURNEY                        │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│ PHASE 1: DISCOVERY       │ PHASE 2: CONFIGURATION   │ PHASE 3: VERIFICATION │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ 1. Landing Page          │ 5. Bundle Recommendation │ 9. GSTIN Verification │
│ 2. Business Info Form    │ 6. Interactive Quote     │ 10. Udyam Verification│
│ 3. Conversational Advisor│ 7. Transparent Monthly   │ 11. Document Upload   │
│ 4. Needs Assessment      │ 8. Order Checkout Review │ 12. KYC Exception Trap│
├──────────────────────────┴──────────────────────────┴───────────────────────┤
│ PHASE 4: CONFIRMATION & LIFECYCLE                                           │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│ 13. DPDP Consent Screen  │ 14. Order Confirmation   │ 15. Real-Time Tracker │
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

---

### Step 1: Landing Page
- **Screen View:** Mobile viewport (Airtel Corporate Red banner with SYNC badge).
- **Language Switcher:** Prominent toggle on header: `[ English | हिन्दी ]`.
- **Value Proposition Hero:**  
  *EN:* "Get your business digital in one sitting. High-speed broadband, business SIMs, cloud email & CCTV with one single bill."  
  *HI:* "सिर्फ एक बैठक में अपने व्यवसाय को डिजिटल बनाएं। हाई-स्पीड इंटरनेट, बिजनेस सिम, क्लाउड ईमेल और सीसीटीवी — एक ही बिल में।"
- **Primary CTA:** Large button: **"Start Digital Onboarding (10 mins) / शुरू करें"**.
- **Secondary CTA:** "Enter Partner / Agent Referral Code (सहयोगी कोड डालें)".

### Step 2: Business Information Collection
- **Input Fields:**
  - Business Name (e.g., "Harmony Dental Care")
  - Business Type Dropdown: Kirana / Retail, Clinic / Healthcare, Professional Office (CA/Legal), Restaurant / Cafe, Manufacturing Unit.
  - City & City Tier (Auto-detected or selected: Tier 1 / Tier 2).
  - Number of Employees & Number of Operational Sites.
- **Micro-Copy:** "We only ask for details needed to tailor your internet and software package."

### Step 3: Conversational AI Advisor
- **Chat Interface:** WhatsApp-style conversational thread with audio playback toggle.
- **Advisor Welcome Message:**  
  *EN:* "Namaste! I am your Airtel Digital Advisor. To recommend the best package for your clinic, tell me: how do you currently connect to the internet, and do you experience payment or phone call drops?"  
  *HI:* "नमस्ते! मैं आपका एयरटेल डिजिटल सलाहकार हूँ। आपके क्लिनिक के लिए सही पैकेज चुनने के लिए, कृपया बताएं: अभी आप इंटरनेट कैसे चलाते हैं, और क्या आपके पेमेंट या कॉल कटते हैं?"
- **Quick-Reply Chips:**  
  - "Using Mobile Hotspot / मोबाइल हॉटस्पॉट"
  - "Home Broadband / घरेलू ब्रॉडबैंड"
  - "Local Leased Line / लोकल केबल ऑपरेटर"
- **Speech-to-Text Input:** Built-in microphone button allowing proprietor to speak their reply in Hindi/English.

### Step 4: Business Needs Assessment
- **Assessment Logic:** The advisor translates user replies into exact capability requirements:
  - If mobile hotspot used -> Flag need for dedicated Fibre (`P01` or `P02`).
  - If multiple staff or patient records -> Flag need for Cloud Backup (`P17`) & Endpoint Antivirus (`P20`).
  - If customer payment drops reported -> Flag need for 4G/5G Failover Backup (`P09`).

### Step 5: Recommended Telecom and Cloud Bundles
- **Presentation:** 3 structured cards highlighting value:
  1. **Essential Starter Pack:** Biz Fibre 100 + 1 Business Postpaid SIM (Starting at ₹1,298/mo).
  2. **Recommended Growth Pack (Popular):** Biz Fibre 300 + 2 Business SIMs + Cloud Email + Wi-Fi Guest Network (₹2,597/mo).
  3. **Enterprise Pro Pack:** Biz Fibre 1G + Managed Firewall + 1TB Cloud Backup + CCTV Security (₹6,896/mo).
- **Plain-Language Explanation:** "Why this fits: Gives your dental clinic guaranteed high-speed internet for digital X-rays and patient billing, with automatic 4G backup so your UPI payments never freeze."

### Step 6: Interactive Quote Configuration
- **Modular Toggle Controls:**
  - Switch broadband tier (`Biz Fibre 100` vs `300` vs `1 Gbps`).
  - Toggle Add-Ons:
    - [x] Cloud CCTV Security (+₹249/mo)
    - [ ] Static IP Address (+₹200/mo)
    - [x] Secure Guest Wi-Fi (+₹399/mo)
- **Dependency Guardrails:** If a user selects `Static IP`, system automatically verifies that a valid broadband plan is selected (`P01|P02|P03`).

### Step 7: Transparent Monthly Pricing
- **Consolidated Billing Box:**
  - Monthly Recurring Charges (Internet + SIMs + Cloud): **₹2,846 / month**
  - Applicable Taxes (GST 18%): **₹512**
  - Total Monthly Bill: **₹3,358 / month**
- **One-Time Charges:**
  - Installation & Router Setup: **₹0 (Free under Annual Plan)**
  - Security Deposit: **₹0**
- **Trust Badge:** "No hidden surcharges. Single monthly invoice for all services."

### Step 8: Checkout Review
- **Order Summary Card:** Visual recap of selected products, contract duration (12 months), and installation address.
- **Button:** "Proceed to Instant KYC Verification (तुरंत सत्यापन करें)".

### Step 9: GSTIN Verification
- **Input:** 15-character GSTIN.
- **Instant Lookup Action:** Calls `POST /api/v1/verification/gstin`.
- **Status Validation:**
  - If `Active`: Success badge displayed; auto-fills Legal Entity Name, Trade Name, Registered Address.
  - If `Cancelled` or `Suspended`: Alert modal: "This GSTIN is marked Cancelled/Suspended in government records. Please enter an active GSTIN or proceed with Udyam verification."

### Step 10: Udyam Registration Verification
- **Input:** Udyam Registration Number (`UDYAM-XX-00-XXXXXXX`).
- **Instant Lookup Action:** Calls `POST /api/v1/verification/udyam`.
- **Autofill:** Micro/Small/Medium classification badge displayed; NIC industry code mapped.

### Step 11: Document Upload & Quality Pre-Check
- **Upload Dropzones:**
  1. Address Proof (Electricity Bill / Water Bill / Rent Agreement).
  2. Signatory Photo ID (Aadhaar / Voter ID / Driving License).
- **Real-Time Pre-Check Feedback:**
  - Blur Detection: If user uploads an out-of-focus image (like `K04`), instantly prompts: "Image is too blurry for automated verification. Please take a clearer photo."
  - Orientation Detection: Automatically corrects tilted/skewed documents (like `K02`).

### Step 12: KYC Validation & Exception Handling
- **Automated Validation Rules:**
  - **Freshness Rule:** Bill date must be within 90 days of anchor date (`2026-07-15`). If expired (like `K11` dated 2025-10-31), displays: "Document expired. Electricity bill must be less than 90 days old."
  - **Entity Cross-Match:** Document name must match GSTIN trade/legal name. If mismatched (like `K07`), flags discrepancy for manual review.
- **Remediation Options:** "Upload Alternative Document" or "Request Assisted Field Agent Visit".

### Step 13: Customer Consent (DPDP Act, 2023 Compliance)
- **Notice Presentation:** Plain-language affirmative consent screen in Hindi/English.
- **Granular Checkboxes:**
  - [x] "I consent to Airtel verifying my GSTIN and Udyam business details."
  - [x] "I consent to my installation address proof being verified for network connectivity."
  - [x] "I understand that document verification is processed strictly for statutory telecom onboarding."
- **Verification:** Proprietor OTP verification or mobile e-signature confirmation.

### Step 14: Order Confirmation & Provisioning Kickoff
- **Success Screen:** High-contrast celebration animation.
- **Order Metadata Displayed:**
  - Order Reference: `ORD-2026-DEL-8921`
  - Account Number: `ACCT-771209`
  - Estimated Installation: **3 Business Days**
- **Action Buttons:** "Download Official Quote PDF" and "Track Live Order Progress".

### Step 15: Real-Time Order Tracking
- **Milestone Progress Bar:**
  1. [DONE] KYC & Identity Verification
  2. [DONE] Network Feasibility Approved (Fibre Node Cleared)
  3. [ACTIVE] Hardware Router Dispatched (Tracking ID: BLR-EXP-9921)
  4. [PENDING] Field Technician Appointment: Scheduled for Thursday, 10:00 AM
  5. [PENDING] Final Connection & Unified Billing Active
- **Status Chase Call Eliminator:** Live technician contact card + "Reschedule Slot" button eliminates customer uncertainty and inbound chase calls.

---

## 6. Bilingual Localization Architecture (English / Hindi)

The frontend implements a unified i18n translation dictionary structure:

```typescript
// Example i18n Dictionary Structure
export const translations = {
  en: {
    heroTitle: "Get Your Business Digital in One Sitting",
    heroSubtitle: "High-speed broadband, business SIMs, cloud email & security in one single bill.",
    startBtn: "Start Digital Onboarding",
    advisorTitle: "Airtel Digital Business Advisor",
    advisorPlaceholder: "Describe your business needs or ask a question...",
    monthlyTotal: "Consolidated Monthly Total",
    setupFee: "One-Time Setup Fee",
    kycHeading: "Instant Smart KYC Verification",
    gstinLabel: "GSTIN (15 Digits)",
    udyamLabel: "Udyam Registration Number",
    consentText: "I consent to the collection and verification of my business credentials under the DPDP Act 2023.",
    trackHeading: "Live Order & Installation Tracker"
  },
  hi: {
    heroTitle: "सिर्फ एक बैठक में अपने व्यवसाय को डिजिटल बनाएं",
    heroSubtitle: "हाई-स्पीड इंटरनेट, बिजनेस सिम, क्लाउड ईमेल और सुरक्षा — एक ही बिल में।",
    startBtn: "डिजिटल ऑनबोर्डिंग शुरू करें",
    advisorTitle: "एयरटेल डिजिटल व्यापार सलाहकार",
    advisorPlaceholder: "अपने व्यवसाय की जरूरतें बताएं या सवाल पूछें...",
    monthlyTotal: "कुल मासिक शुल्क",
    setupFee: "एकमुश्त सेटअप शुल्क",
    kycHeading: "त्वरित स्मार्ट केवाईसी सत्यापन",
    gstinLabel: "जीएसटीआईएन (15 अंक)",
    udyamLabel: "उद्यम पंजीकरण संख्या",
    consentText: "मैं डीपीडीपी अधिनियम 2023 के तहत अपने व्यावसायिक विवरण के सत्यापन की सहमति देता हूँ।",
    trackHeading: "लाइव ऑर्डर और इंस्टॉलेशन ट्रैकर"
  }
};
```

