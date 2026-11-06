from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class Business(Base):
    __tablename__ = "businesses"
    id = Column(Integer, primary_key=True, index=True)
    legal_name = Column(String(255), nullable=False)
    trade_name = Column(String(255))
    segment = Column(String(50))  # micro, prof, multi, mfg
    city = Column(String(100))
    city_tier = Column(Integer, default=1)
    employee_count = Column(Integer, default=5)
    site_count = Column(Integer, default=1)
    gstin = Column(String(20), index=True)
    udyam_number = Column(String(30), index=True)
    contact_name = Column(String(100))
    contact_phone = Column(String(20))
    contact_email = Column(String(100))
    installation_address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Product(Base):
    __tablename__ = "products"
    product_id = Column(String(10), primary_key=True, index=True)
    category = Column(String(50), nullable=False)
    product_name = Column(String(255), nullable=False)
    description = Column(Text)
    unit = Column(String(50))
    price_min_inr_per_month = Column(Float, nullable=False)
    price_max_inr_per_month = Column(Float, nullable=False)
    one_time_setup_inr = Column(Float, default=0.0)
    min_contract_months = Column(Integer, default=12)
    available_city_tiers = Column(String(50))
    min_employees = Column(Integer, default=1)
    min_sites = Column(Integer, default=1)
    requires_gstin = Column(String(1), default="N")
    requires_one_of = Column(String(255))
    typical_install_days = Column(Integer, default=5)
    target_segments = Column(String(100))

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(String(50), primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=True)
    monthly_total_min = Column(Float, nullable=False)
    monthly_total_max = Column(Float, nullable=False)
    setup_fee_total = Column(Float, default=0.0)
    contract_months = Column(Integer, default=12)
    status = Column(String(50), default="DRAFT")  # DRAFT, ACCEPTED, EXPIRED
    created_at = Column(DateTime, default=datetime.utcnow)

class QuoteItem(Base):
    __tablename__ = "quote_items"
    id = Column(Integer, primary_key=True, index=True)
    quote_id = Column(String(50), ForeignKey("quotes.id"), nullable=False)
    product_id = Column(String(10), ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, default=1)
    monthly_price = Column(Float, nullable=False)

class KYCVerification(Base):
    __tablename__ = "kyc_verifications"
    id = Column(String(50), primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=True)
    gstin_verified = Column(Boolean, default=False)
    gstin_status = Column(String(50))
    udyam_verified = Column(Boolean, default=False)
    udyam_status = Column(String(50))
    overall_status = Column(String(50), default="PENDING")  # VERIFIED, REQUIRES_MANUAL_REVIEW, REJECTED
    risk_flags = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = "orders"
    id = Column(String(50), primary_key=True, index=True)
    quote_id = Column(String(50), ForeignKey("quotes.id"), nullable=False)
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=True)
    status = Column(String(50), default="KYC_VERIFIED")
    monthly_recurring_inr = Column(Float, nullable=False)
    setup_fee_inr = Column(Float, default=0.0)
    technician_name = Column(String(100), default="Simulated Field Tech (Demo Node #402)")
    technician_phone = Column(String(30), default="+91 98000 00000 (Demo)")
    scheduled_install_date = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class OrderMilestone(Base):
    __tablename__ = "order_milestones"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String(50), ForeignKey("orders.id"), nullable=False)
    milestone = Column(String(50), nullable=False)
    status = Column(String(50), default="PENDING")  # COMPLETED, IN_PROGRESS, PENDING
    completed_at = Column(DateTime)
    notes = Column(Text)

class ConsentRecord(Base):
    __tablename__ = "consent_records"
    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, nullable=True)
    order_id = Column(String(50), nullable=True)
    purpose = Column(String(100), nullable=False)
    language = Column(String(10), default="en")
    ip_hash = Column(String(64))
    accepted_at = Column(DateTime, default=datetime.utcnow)
    terms_version = Column(String(20), default="1.0-DPDP2023")

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String(50), nullable=False)
    entity_id = Column(String(50), nullable=False)
    action = Column(String(100), nullable=False)
    details = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

