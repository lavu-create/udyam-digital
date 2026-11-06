import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DATA_DIR = os.path.join(BASE_DIR, "data")
EXTRACTED_DATA_DIR = os.path.join(BASE_DIR, "extracted", "udyam_digital_data")

DATA_DIR = REPO_DATA_DIR if os.path.exists(REPO_DATA_DIR) else EXTRACTED_DATA_DIR

CATALOGUE_CSV = os.path.join(DATA_DIR, "product_catalogue.csv")
GSTIN_REGISTRY_CSV = os.path.join(DATA_DIR, "mock_gstin_registry.csv")
UDYAM_REGISTRY_CSV = os.path.join(DATA_DIR, "mock_udyam_registry.csv")
KYC_DOCS_DIR = os.path.join(EXTRACTED_DATA_DIR, "kyc_documents")

DB_PATH = os.path.join(BASE_DIR, "udyam_digital.db")
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")

# Statutory Anchor Date for KYC verification (from case dataset)
ANCHOR_DATE = os.getenv("ANCHOR_DATE", "2026-07-15")
MAX_BILL_AGE_DAYS = int(os.getenv("MAX_BILL_AGE_DAYS", "90"))
BLUR_LAPLACIAN_THRESHOLD = float(os.getenv("BLUR_LAPLACIAN_THRESHOLD", "250.0"))

