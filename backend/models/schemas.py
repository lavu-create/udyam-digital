from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ProductSchema(BaseModel):
    product_id: str
    category: str
    product_name: str
    description: Optional[str] = None
    unit: Optional[str] = None
    price_min_inr_per_month: float
    price_max_inr_per_month: float
    one_time_setup_inr: float = 0.0
    min_contract_months: int = 12
    available_city_tiers: Optional[str] = None
    min_employees: int = 1
    min_sites: int = 1
    requires_gstin: str = "N"
    requires_one_of: Optional[str] = None
    typical_install_days: int = 5
    target_segments: Optional[str] = None

class QuoteValidationRequest(BaseModel):
    product_ids: List[str]
    has_active_gstin: bool = False
    site_count: int = 1
    employee_count: int = 5

class QuoteItemResponse(BaseModel):
    product_id: str
    product_name: str
    category: str
    price_min: float
    price_max: float
    setup_fee: float

class QuoteValidationResponse(BaseModel):
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []
    monthly_total_min: float
    monthly_total_max: float
    setup_fee_total: float
    requires_gstin: bool
    gstin_satisfied: bool
    items: List[QuoteItemResponse]

class AdvisorChatRequest(BaseModel):
    message: str
    language: str = "en"
    conversation_state: Optional[Dict[str, Any]] = None

class AdvisorChatResponse(BaseModel):
    reply: str
    language: str
    suggested_chips: List[str]
    recommended_tier: Optional[str] = None
    recommended_product_ids: List[str] = []
    business_context: Dict[str, Any] = {}

class AdvisorRecommendRequest(BaseModel):
    segment: str  # micro, prof, multi, mfg
    employee_count: int = 5
    site_count: int = 1
    needs_cctv: bool = False
    needs_static_ip: bool = False
    needs_telephony: bool = False
    needs_backup: bool = False

class RecommendedBundle(BaseModel):
    tier: str
    title: str
    badge: str
    monthly_price: float
    description: str
    product_ids: List[str]
    highlights: List[str]

class AdvisorRecommendResponse(BaseModel):
    bundles: List[RecommendedBundle]
    rationale: str

class RegistryLookupResponse(BaseModel):
    found: bool
    registry: str
    status: str
    legal_name: Optional[str] = None
    trade_name: Optional[str] = None
    address: Optional[str] = None
    registration_date: Optional[str] = None
    details: Dict[str, Any] = {}

class KYCVerifyPackRequest(BaseModel):
    lead_id: Optional[str] = "K03"  # K01 - K12
    gstin: Optional[str] = None
    udyam_number: Optional[str] = None
    consent_given: bool = True

class KYCVerifyPackResponse(BaseModel):
    lead_id: str
    overall_status: str  # VERIFIED, REQUIRES_MANUAL_REVIEW, REJECTED
    confidence_score: float
    gstin_result: Dict[str, Any]
    udyam_result: Dict[str, Any]
    ocr_checks: Dict[str, Any]
    risk_flags: List[str]
    recommendation: str

class ConsentRequest(BaseModel):
    business_id: Optional[int] = None
    order_id: Optional[str] = None
    purpose: str = "TELECOM_STATUTORY_PROVISIONING"
    language: str = "en"
    accepted: bool = True

class ConsentResponse(BaseModel):
    success: bool
    consent_id: int
    timestamp: str
    language: str
    audit_hash: str

class OrderCreateRequest(BaseModel):
    quote_id: Optional[str] = None
    product_ids: List[str]
    business_name: str
    contact_name: str
    contact_phone: str
    installation_address: str
    gstin: Optional[str] = None
    udyam_number: Optional[str] = None
    monthly_price: float
    setup_fee: float = 0.0

class OrderResponse(BaseModel):
    order_id: str
    status: str
    business_name: str
    installation_address: str
    monthly_recurring_inr: float
    setup_fee_inr: float
    technician_name: str
    technician_phone: str
    scheduled_install_date: str
    milestones: List[Dict[str, Any]]

