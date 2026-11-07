# Deployment & Infrastructure Guide

**Project Udyam Digital**  
**Competition:** Airtel SYNC 2026 – Digital Track  
**Live Production URL:** [https://udyam-digital-rho.vercel.app](https://udyam-digital-rho.vercel.app)  

---

## 1. Architecture & Deployment Strategy

Project Udyam Digital is packaged as a **unified modular application** where the Python FastAPI backend serves the production-compiled React 18 single-page application (SPA) from `frontend/dist`. This eliminates cross-origin resource sharing (CORS) friction, simplifies certificate management, and allows the platform to deploy across multiple cloud platforms without requiring separate frontend and backend hosting providers.

```
┌────────────────────────────────────────────────────────────────────────┐
│               UNIFIED FULL-STACK DEPLOYMENT (Single Origin)             │
│                   https://udyam-digital-rho.vercel.app                 │
├───────────────────────────────────┬────────────────────────────────────┤
│         REACT 18 + VITE SPA       │         FASTAPI REST BACKEND       │
│  Static Assets in frontend/dist   │  Serverless ASGI / Container Run   │
│  • Client-side Bilingual i18n     │  • 25 Grounded Catalogue SKUs      │
│  • Airtel Red (#E40000) UI        │  • 3,534 Mock GSTINs Indexed       │
│  • 12-Screen MSME Onboarding Flow │  • 2,723 Mock Udyam Numbers        │
│  • Interactive Quote Engine       │  • Local Computer Vision Checks    │
│  • Simulated Milestone Tracker    │  • DPDP Act SHA-256 Consent Ledger │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 2. Deployment Targets

### Target A: Vercel Serverless Function (Live Production)

The live demonstration at **[https://udyam-digital-rho.vercel.app](https://udyam-digital-rho.vercel.app)** runs as a serverless ASGI function on Vercel.

**Key Configuration Files:**
- [`vercel.json`](../vercel.json): Defines routes and rewrites:
  - `/api/(.*)` routes directly to `api/index.py`.
  - `/((?!api/).*)` routes to the SPA entrypoint `/index.html`.
- [`api/index.py`](../api/index.py): Serverless ASGI wrapper importing `backend.main:app`.
- [`.vercelignore`](../.vercelignore): Excludes heavy non-runtime artifacts (virtual environments, local test archives, presentation source binaries) to stay well within Vercel's 225 MB function limit.
- **Ephemeral Database Handling:** In serverless Lambda environments where the root filesystem is read-only, `backend/config.py` automatically initializes SQLite in the writable `/tmp` directory (`/tmp/udyam_digital.db`).

---

### Target B: Multi-Stage Production Docker Container

A self-contained production Docker image compiles the React frontend and packages the FastAPI backend using official slim base images:

```bash
# 1. Build the multi-stage Docker image
docker build -t udyam-digital:latest .

# 2. Run container on host port 8000
docker run -d -p 8000:8000 --name udyam-app udyam-digital:latest
```

**Dockerfile Structure:**
- **Stage 1 (Frontend Builder):** Uses `node:20-alpine`, runs `npm ci` and `npm run build` to generate `frontend/dist`.
- **Stage 2 (Runtime Runner):** Uses `python:3.11-slim`, installs lean runtime dependencies from `requirements.txt`, copies built frontend assets into `/app/frontend/dist`, and launches Uvicorn on dynamic `${PORT:-8000}`.

---

### Target C: Render Web Service Blueprint

A 1-click cloud service configuration is provided in [`render.yaml`](../render.yaml):
- **Service Type:** Web Service (`env: docker`).
- **Plan:** Free tier compatible.
- **Health Check Endpoint:** `/health` (monitors SKU count and registry index status).
- **Auto-Deploy:** Git push to `main` triggers automatic container build and deployment.

---

### Target D: Local Development Run

For local development or jury evaluation:

```bash
# 1. Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install backend runtime dependencies
pip install -r requirements.txt

# 3. Build frontend production bundle
cd frontend
npm ci
npm run build
cd ..

# 4. Start unified server
python3 -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```
Open **[http://localhost:8000](http://localhost:8000)** in your browser.

To run with hot reloading during development:
```bash
# Terminal 1: Backend API
source .venv/bin/activate
uvicorn backend.main:app --reload --port 8000

# Terminal 2: Vite Dev Server
cd frontend
npm run dev
```

---

## 3. Environment Variables Reference

| Variable | Default Value | Description |
|---|---|---|
| `PORT` | `8000` | Port on which the Uvicorn server listens (injected automatically by cloud providers). |
| `HOST` | `0.0.0.0` | Network binding interface (must be `0.0.0.0` for containers and cloud hosting). |
| `DATABASE_URL` | `sqlite:///{DB_PATH}` | Database connection string. Supports PostgreSQL (`postgresql+psycopg2://...`) for production clustering. |
| `DB_PATH` | `/tmp/udyam_digital.db` (on Vercel) or `udyam_digital.db` | Local SQLite database file location. |
| `ANCHOR_DATE` | `2026-07-15` | Anchor date for case dataset KYC utility bill freshness validation. |
| `MAX_BILL_AGE_DAYS` | `90` | Maximum allowable utility bill age in days based on case validation rules. |
| `VERCEL` | `""` | Flag detected in Vercel serverless runtime to switch database storage to `/tmp`. |

---

## 4. Verification & Health Monitoring

To verify service health after deployment:

```bash
# Root health check (returns SKU count and registry index status)
curl -s https://udyam-digital-rho.vercel.app/health

# Catalog products endpoint
curl -s https://udyam-digital-rho.vercel.app/api/v1/catalog/products | head -c 200
```
Expected health response:
```json
{
  "status": "healthy",
  "service": "Project Udyam Digital API",
  "version": "1.0.0",
  "environment": "demonstration_sandbox",
  "catalog_skus_loaded": 25,
  "gstin_registry_indexed": 3534,
  "udyam_registry_indexed": 2723,
  "ocr_status": "LOCAL_IMAGE_QUALITY_AND_SYNTHETIC_VERIFIER",
  "dpdp_alignment": "TECHNICAL_CONTROLS_ACTIVE",
  "simulation_mode": true
}
```

