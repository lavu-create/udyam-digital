import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DATA_DIR = os.path.join(BASE_DIR, "data")
EXTRACTED_DATA_DIR = os.path.join(BASE_DIR, "extracted", "udyam_digital_data")

DATA_DIR = REPO_DATA_DIR if os.path.exists(REPO_DATA_DIR) else EXTRACTED_DATA_DIR

CATALOGUE_CSV = os.path.join(DATA_DIR, "product_catalogue.csv")
GSTIN_REGISTRY_CSV = os.path.join(DATA_DIR, "mock_gstin_registry.csv")
UDYAM_REGISTRY_CSV = os.path.join(DATA_DIR, "mock_udyam_registry.csv")
KYC_DOCS_DIR = os.path.join(EXTRACTED_DATA_DIR, "kyc_documents")

# Database location (automatically falls back to /tmp on serverless environments like Vercel)
IS_VERCEL = bool(os.getenv("VERCEL"))
DEFAULT_DB_PATH = "/tmp/udyam_digital.db" if IS_VERCEL else os.path.join(BASE_DIR, "udyam_digital.db")
DB_PATH = os.getenv("DB_PATH", DEFAULT_DB_PATH)
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")

# Server configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

# Statutory Anchor Date for KYC verification (from case dataset)
ANCHOR_DATE = os.getenv("ANCHOR_DATE", "2026-07-15")
MAX_BILL_AGE_DAYS = int(os.getenv("MAX_BILL_AGE_DAYS", "90"))
BLUR_LAPLACIAN_THRESHOLD = float(os.getenv("BLUR_LAPLACIAN_THRESHOLD", "250.0"))

