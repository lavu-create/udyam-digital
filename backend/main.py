import os
import sys

# Ensure python_libs is on sys.path
libs_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "python_libs"))
if libs_path not in sys.path:
    sys.path.insert(0, libs_path)

from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from typing import List, Dict, Any

from backend.database import engine, Base, SessionLocal
from backend.models.orm import Product as ORMProduct
from backend.models.schemas import (
    ProductSchema,
    QuoteValidationRequest,
    QuoteValidationResponse,
    AdvisorChatRequest,
    AdvisorChatResponse,
    AdvisorRecommendRequest,
    AdvisorRecommendResponse,
    RegistryLookupResponse,
    KYCVerifyPackRequest,
    KYCVerifyPackResponse,
    ConsentRequest,
    ConsentResponse,
    OrderCreateRequest,
    OrderResponse
)
from backend.services.catalog_service import catalog_service
from backend.services.advisor_service import advisor_service
from backend.services.registry_service import registry_service
from backend.services.ocr_service import ocr_service
from backend.services.consent_service import consent_service
from backend.services.order_service import order_service

# Create database tables
Base.metadata.create_all(bind=engine)

# Seed products into SQLite if empty
def seed_products():
    db = SessionLocal()
    try:
        count = db.query(ORMProduct).count()
        if count == 0:
            for p in catalog_service.get_all_products():
                orm_p = ORMProduct(
                    product_id=p["product_id"],
                    category=p["category"],
                    product_name=p["product_name"],
                    description=p["description"],
                    unit=p["unit"],
                    price_min_inr_per_month=p["price_min_inr_per_month"],
                    price_max_inr_per_month=p["price_max_inr_per_month"],
                    one_time_setup_inr=p["one_time_setup_inr"],
                    min_contract_months=p["min_contract_months"],
                    available_city_tiers=p["available_city_tiers"],
                    min_employees=p["min_employees"],
                    min_sites=p["min_sites"],
                    requires_gstin=p["requires_gstin"],
                    requires_one_of=p["requires_one_of"],
                    typical_install_days=p["typical_install_days"],
                    target_segments=p["target_segments"]
                )
                db.add(orm_p)
            db.commit()
    finally:
        db.close()

seed_products()

app = FastAPI(
    title="Project Udyam Digital API",
    description="Airtel SYNC 2026 - AI-Powered MSME Digital Acquisition & Onboarding Service",
    version="1.0.0"
)

# Enable CORS for local Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Project Udyam Digital API",
        "version": "1.0.0",
        "environment": "demonstration_sandbox",
        "catalog_skus_loaded": len(catalog_service.products),
        "gstin_registry_indexed": len(registry_service.gstin_index),
        "udyam_registry_indexed": len(registry_service.udyam_index),
        "ocr_status": "LOCAL_IMAGE_QUALITY_AND_SYNTHETIC_VERIFIER",
        "dpdp_alignment": "TECHNICAL_CONTROLS_ACTIVE",
        "simulation_mode": True
    }

# ----------------- CATALOGUE & QUOTE -----------------
@app.get("/api/v1/catalog/products", response_model=List[ProductSchema])
def list_products():
    return catalog_service.get_all_products()

@app.post("/api/v1/catalog/validate-quote", response_model=QuoteValidationResponse)
def validate_quote(req: QuoteValidationRequest):
    result = catalog_service.validate_and_quote(
        product_ids=req.product_ids,
        has_active_gstin=req.has_active_gstin,
        site_count=req.site_count,
        employee_count=req.employee_count
    )
    return result

# ----------------- ADVISOR -----------------
@app.post("/api/v1/advisor/chat", response_model=AdvisorChatResponse)
def advisor_chat(req: AdvisorChatRequest):
    return advisor_service.chat(
        message=req.message,
        language=req.language,
        state=req.conversation_state
    )

@app.post("/api/v1/advisor/recommend", response_model=AdvisorRecommendResponse)
def advisor_recommend(req: AdvisorRecommendRequest):
    return advisor_service.recommend(
        segment=req.segment,
        employee_count=req.employee_count,
        site_count=req.site_count,
        needs_cctv=req.needs_cctv,
        needs_static_ip=req.needs_static_ip,
        needs_telephony=req.needs_telephony,
        needs_backup=req.needs_backup
    )

# ----------------- MOCK REGISTRIES -----------------
@app.get("/api/v1/registry/gstin/{gstin}", response_model=RegistryLookupResponse)
def lookup_gstin(gstin: str):
    return registry_service.lookup_gstin(gstin)

@app.get("/api/v1/registry/udyam/{udyam_number}", response_model=RegistryLookupResponse)
def lookup_udyam(udyam_number: str):
    return registry_service.lookup_udyam(udyam_number)

# ----------------- SMART KYC & OCR -----------------
@app.post("/api/v1/kyc/verify-pack", response_model=KYCVerifyPackResponse)
def verify_kyc_pack(req: KYCVerifyPackRequest):
    lead_id = req.lead_id or "K03"
    result = ocr_service.verify_lead_pack(lead_id=lead_id, consent_given=req.consent_given)
    return result

@app.post("/api/v1/kyc/upload-check")
async def check_uploaded_document(file: UploadFile = File(...)):
    # 1. Enforce 5MB size limit
    content = await file.read()
    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size exceeds maximum 5MB limit.")

    # 2. Enforce strict image/pdf MIME types
    allowed_types = ["image/png", "image/jpeg", "image/webp", "application/pdf"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail=f"Unsupported file format '{file.content_type}'. Please upload PNG, JPEG or PDF.")

    # 3. Local in-memory Computer Vision quality assessment (zero cloud API leakage, zero disk persistence)
    quality = ocr_service.assess_image_quality(content)
    is_passed = not quality.get("is_blurry", False)

    return {
        "filename": file.filename,
        "size_bytes": len(content),
        "content_type": file.content_type,
        "quality_metrics": quality,
        "is_blurry": quality.get("is_blurry", False),
        "status": "PASSED" if is_passed else "FLAGGED_BLURRY",
        "notes": "Processed 100% in local memory; no file written to persistent storage."
    }

# ----------------- DPDP ACT CONSENT -----------------
@app.post("/api/v1/consent/record", response_model=ConsentResponse)
def record_consent(req: ConsentRequest, request: Request):
    client_ip = request.client.host if request.client else "127.0.0.1"
    return consent_service.record_consent(
        purpose=req.purpose,
        language=req.language,
        business_id=req.business_id,
        order_id=req.order_id,
        client_ip=client_ip
    )

# ----------------- ORDER MANAGEMENT -----------------
@app.post("/api/v1/orders/create", response_model=OrderResponse)
def create_order(req: OrderCreateRequest):
    return order_service.create_order(
        product_ids=req.product_ids,
        business_name=req.business_name,
        contact_name=req.contact_name,
        contact_phone=req.contact_phone,
        installation_address=req.installation_address,
        monthly_price=req.monthly_price,
        setup_fee=req.setup_fee,
        quote_id=req.quote_id,
        gstin=req.gstin,
        udyam_number=req.udyam_number
    )

@app.get("/api/v1/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: str):
    order = order_service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.post("/api/v1/orders/{order_id}/advance", response_model=OrderResponse)
def advance_order_status(order_id: str):
    order = order_service.advance_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Mount built React frontend if available
candidate_dists = [
    os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend", "dist")),
    os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "dist")),
    os.path.abspath("./frontend/dist"),
    os.path.abspath("./dist")
]
frontend_dist = next((d for d in candidate_dists if os.path.exists(d)), None)

if frontend_dist:
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="static")

    @app.exception_handler(404)
    async def spa_404_handler(request: Request, exc: Exception):
        if request.url.path.startswith("/api/"):
            return JSONResponse(status_code=404, content={"detail": f"API route '{request.url.path}' not found"})
        index_file = os.path.join(frontend_dist, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return JSONResponse(status_code=404, content={"detail": "Not found"})
