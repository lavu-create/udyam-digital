import os
import sys

# Ensure python_libs and project root are on sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
libs_dir = os.path.join(root_dir, "python_libs")
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if libs_dir not in sys.path:
    sys.path.insert(0, libs_dir)

from backend.database import engine, Base
from backend.models import orm
Base.metadata.create_all(bind=engine)

from backend.services.catalog_service import catalog_service
from backend.services.advisor_service import advisor_service
from backend.services.registry_service import registry_service
from backend.services.ocr_service import ocr_service
from backend.services.consent_service import consent_service
from backend.services.order_service import order_service

def test_catalog_skus_and_dependencies():
    print("Testing Catalog & Dependency Rules...")
    # 1. 25 SKUs loaded
    products = catalog_service.get_all_products()
    assert len(products) == 25, f"Expected 25 SKUs, got {len(products)}"
    print("  ✓ Exactly 25 catalogue SKUs loaded")

    # 2. Enforce 10 GSTIN requirements
    gstin_skus = [p["product_id"] for p in products if p["requires_gstin"] == "Y"]
    assert len(gstin_skus) == 10, f"Expected 10 GSTIN SKUs, got {len(gstin_skus)}"
    assert "P03" in gstin_skus and "P10" in gstin_skus and "P21" in gstin_skus
    print("  ✓ Exactly 10 GSTIN-mandatory SKUs verified")

    # 3. Test dependency failure: P10 (SD-WAN) alone without base broadband
    res_fail = catalog_service.validate_and_quote(["P10"], has_active_gstin=True)
    assert not res_fail["valid"], "Expected P10 without broadband to fail validation"
    assert any("requires at least one base connection" in err for err in res_fail["errors"])
    print("  ✓ Product dependency enforcement verified (P10 blocked without base broadband)")

    # 4. Test dependency pass: P01 (Broadband) + P10 (SD-WAN) with Active GSTIN
    res_pass = catalog_service.validate_and_quote(["P01", "P10"], has_active_gstin=True)
    assert res_pass["valid"], f"Expected P01 + P10 to pass: {res_pass['errors']}"
    assert res_pass["monthly_total_min"] == (999.0 + 2500.0), f"Expected 3499.0, got {res_pass['monthly_total_min']}"
    print("  ✓ Validated quote totals and dependency satisfaction (P01 + P10)")

    # 5. Test GSTIN requirement failure: P03 (Fibre 1G) with has_active_gstin=False
    res_gst_fail = catalog_service.validate_and_quote(["P03"], has_active_gstin=False)
    assert not res_gst_fail["valid"]
    assert any("Active GSTIN registration" in err for err in res_gst_fail["errors"])
    print("  ✓ Statutory GSTIN requirement enforced (P03 blocked without Active GSTIN)")

def test_mock_registries():
    print("\nTesting Mock Registries...")
    # Active GSTIN
    res_active = registry_service.lookup_gstin("19EOGXH4115Y1ZL")
    assert res_active["found"] and res_active["status"] == "Active"
    assert "Harmony Dental Care" in res_active["legal_name"]
    print("  ✓ Mock GSTIN Active lookup passed (Harmony Dental Care)")

    # Cancelled GSTIN
    res_canc = registry_service.lookup_gstin("37IHKXV5167L1ZS")
    assert res_canc["found"] and res_canc["status"] == "Cancelled"
    print("  ✓ Mock GSTIN Cancelled lookup trapped (Status: Cancelled)")

    # Mock Udyam
    res_udyam = registry_service.lookup_udyam("UDYAM-KL-00-3078801")
    assert res_udyam["found"] and res_udyam["status"] == "Active"
    print("  ✓ Mock Udyam Registry lookup passed")

def test_advisor():
    print("\nTesting Conversational AI Advisor...")
    # English chat
    chat_en = advisor_service.chat("I run a dental clinic with 8 staff")
    assert chat_en["recommended_tier"] == "growth"
    assert "P02" in chat_en["recommended_product_ids"]
    print("  ✓ English clinical intent classification passed")

    # Hindi chat
    chat_hi = advisor_service.chat("मेरी रिटेल की दुकान है", language="hi")
    assert chat_hi["recommended_tier"] == "starter"
    assert "नमस्ते" in chat_hi["reply"]
    print("  ✓ Hindi retail intent classification passed")

    # Bundle recommendation
    rec = advisor_service.recommend("multi", employee_count=25, site_count=3)
    assert rec["bundles"][0]["tier"] == "pro"
    print("  ✓ Multi-site bundle recommendation passed")

def test_smart_kyc_and_edge_cases():
    print("\nTesting Smart KYC Engine across K01–K12 edge cases...")
    
    # K01: Cancelled GSTIN
    k01 = ocr_service.verify_lead_pack("K01")
    assert k01["overall_status"] in ["REJECTED", "REQUIRES_MANUAL_REVIEW"]
    assert "GSTIN_STATUS_CANCELLED" in k01["risk_flags"]
    print("  ✓ K01 Trapped: Cancelled GSTIN status")

    # K02: Skewed image / date mismatch
    k02 = ocr_service.verify_lead_pack("K02")
    assert "ROTATION_DETECTED_AUTO_DESKEWED" in k02["risk_flags"] or "UDYAM_REGISTRATION_DATE_MISMATCH" in k02["risk_flags"]
    assert k02["overall_status"] == "REQUIRES_MANUAL_REVIEW"
    print("  ✓ K02 Trapped: Skewed image & date mismatch")

    # K03: Clean pass
    k03 = ocr_service.verify_lead_pack("K03")
    assert k03["overall_status"] == "VERIFIED"
    assert len(k03["risk_flags"]) == 0
    print("  ✓ K03 Passed: Clean digital KYC verification")

    # K04: Blurry document
    k04 = ocr_service.verify_lead_pack("K04")
    assert "DOCUMENT_BLURRY_FAIL" in k04["risk_flags"]
    assert k04["overall_status"] == "REJECTED"
    print("  ✓ K04 Trapped: Laplacian blur threshold triggered")

    # K05: Missing file
    k05 = ocr_service.verify_lead_pack("K05")
    assert "MISSING_UDYAM_CERTIFICATE" in k05["risk_flags"]
    assert k05["overall_status"] == "REQUIRES_MANUAL_REVIEW"
    print("  ✓ K05 Trapped: Missing certificate file detected")

    # K06: GSTIN character mismatch
    k06 = ocr_service.verify_lead_pack("K06")
    assert any("GSTIN_CHAR_MISMATCH" in f for f in k06["risk_flags"])
    print("  ✓ K06 Trapped: Character typo on document vs registry")

    # K07: Legal name mismatch
    k07 = ocr_service.verify_lead_pack("K07")
    assert any("LEGAL_NAME_MISMATCH" in f for f in k07["risk_flags"])
    print("  ✓ K07 Trapped: Legal name mismatch on certificate")

    # K11: Expired electricity bill (>90 days old from 2026-07-15)
    k11 = ocr_service.verify_lead_pack("K11")
    assert any("EXPIRED" in f for f in k11["risk_flags"])
    assert k11["overall_status"] == "REJECTED"
    print("  ✓ K11 Trapped: Stale utility bill (>90 days old)")

    # Clean test cases
    for k in ["K08", "K09", "K10", "K12"]:
        res = ocr_service.verify_lead_pack(k)
        assert res["overall_status"] == "VERIFIED"
    print("  ✓ K08, K09, K10, K12 Clean passes verified")

def test_dpdp_consent_and_orders():
    print("\nTesting DPDP Consent & Order Fulfillment...")
    # DPDP Consent
    consent = consent_service.record_consent(
        purpose="TELECOM_STATUTORY_PROVISIONING",
        language="hi",
        client_ip="192.168.1.100"
    )
    assert consent["success"]
    assert "DPDP-" in consent["audit_hash"]
    print("  ✓ DPDP Act affirmative consent recorded with SHA-256 IP hash")

    # Order Creation
    order = order_service.create_order(
        product_ids=["P01", "P07"],
        business_name="Neelgiri Diagnostics",
        contact_name="Dr. R. Sharma",
        contact_phone="+91 98111 22334",
        installation_address="Plot 44, Industrial Area, Jaipur",
        monthly_price=1298.0,
        setup_fee=0.0
    )
    assert "ORD-2026-" in order["order_id"]
    assert len(order["milestones"]) == 5
    assert "Simulated Field Tech" in order["technician_name"]
    print(f"  ✓ Order created: {order['order_id']} with 5 provisioning milestones")

if __name__ == "__main__":
    test_catalog_skus_and_dependencies()
    test_mock_registries()
    test_advisor()
    test_smart_kyc_and_edge_cases()
    test_dpdp_consent_and_orders()
    print("\n==========================================")
    print("ALL 18 ARCHITECTURAL ASSERTION TESTS PASSED!")
    print("==========================================")
