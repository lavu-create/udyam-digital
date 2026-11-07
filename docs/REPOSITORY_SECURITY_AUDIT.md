# Repository Privacy & Security Audit Report

**Project:** Udyam Digital — Airtel SYNC 2026 (Digital Track)  
**Target Repository:** [https://github.com/lavu-create/udyam-digital](https://github.com/lavu-create/udyam-digital)  
**Audit Date:** November 6, 2026  
**Auditor:** Senior GitHub Repository Maintainer & Security Reviewer  
**Audit Scope:** All tracked repository files, entire commit history (`378a606` to `e2aba2d`), datasets, deployment configs, and environment templates.

---

## 1. Executive Summary

A comprehensive privacy and security audit was conducted on the public GitHub repository for **Project Udyam Digital**. The audit verified that **no production secrets, private encryption keys, cloud credentials, database binaries, or real-world customer identity documents exist** in either the working tree or the Git commit history.

The codebase demonstrates strong software engineering hygiene:
- Zero raw KYC specimen images or customer PII are tracked in git.
- Zero live government GSTN / MCA21 API keys or cloud tokens are committed.
- All registry queries execute against synthetic test datasets (`mock_gstin_registry.csv` and `mock_udyam_registry.csv`).
- Documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs. Production deployment requires further security and retention assessment.

This report documents findings categorized by severity, identifies non-critical metadata exposures (such as local machine hostname in Git committer headers), and provides specific remediation recommendations for user approval.

---

## 2. Tracked Files Inventory Audit (`git ls-files`)

The repository currently tracks 60 files across code, configuration, documentation, and submission deliverables:

| Category | Tracked Files | Privacy & Security Verification |
|---|---|---|
| **Root Configs** | `.dockerignore`, `.env.example`, `.gitignore`, `.vercelignore`, `Dockerfile`, `render.yaml`, `vercel.json`, `requirements.txt` | **CLEAN.** `.env.example` contains only empty template comments. No secrets. `.gitignore` comprehensively ignores `.env*`, `*.db`, `node_modules/`, `python_libs/`, `extracted/`. |
| **Backend Code** | `api/index.py`, `backend/config.py`, `backend/database.py`, `backend/main.py`, `backend/models/*.py`, `backend/services/*.py`, `backend/tests/test_system.py` | **CLEAN.** No hardcoded passwords, tokens, or private keys. Local `python_libs` check is safely optional. File uploads processed in memory. |
| **Frontend Code** | `frontend/src/**/*.{ts,tsx,css}`, `frontend/package.json`, `frontend/package-lock.json`, `frontend/vite.config.ts`, etc. | **CLEAN.** Pure client-side React 18 code. No API keys or external telemetry trackers. |
| **Datasets** | `data/product_catalogue.csv`, `data/mock_gstin_registry.csv`, `data/mock_udyam_registry.csv` | **VERIFIED SYNTHETIC.** All company names and addresses are mock demonstration entities. |
| **Submission Files** | `submission/Project_Udyam_Digital.pptx` (1.31 MB), `submission/Project_Udyam_Digital.pdf` (1.64 MB), `submission/DPDP_Privacy_Security_Note.pdf` (5.3 KB), `submission/github_qr.png` | **CLEAN.** Preserved within the 20 MB hackathon limit. Zero private metadata. |
| **Documentation** | `README.md`, `SECURITY.md`, `docs/*.md` | **AUDITED.** Corrected all unsupported percentage claims, clarified simulations, and removed broken badges. |
| **Build Scripts** | `scripts/build_presentation.py`, `scripts/generate_dpdp_pdf.py` | **ORGANIZED.** Consolidated into `scripts/`. Pre-compiled outputs are tracked in `submission/`. |

---

## 3. Git History Deep-Scan Audit

A deep commit-by-commit diff audit was performed across all three repository commits:
1. `378a606` — *feat: initial public release of Project Udyam Digital MVP (Airtel SYNC 2026)*
2. `afc0e02` — *ci/deploy: add multi-stage Dockerfile, Render Blueprint, Vercel serverless deployment, and live demo URL*
3. `e2aba2d` — *docs/ui: align landing metrics with audited dataset baselines (₹15,053 CAC, 17.62d velocity) and update video storyboard*

### Findings:
- **No Secrets in History:** A regex pattern scan (`PRIVATE KEY`, `BEGIN RSA`, `api_key=`, `secret=`, `password=`) across `git log -p` returned zero instances of leaked credentials.
- **No Database Dumps:** No `.db`, `.sqlite`, `.sql`, or `.dump` files were ever committed to Git history.
- **No Raw KYC Image Scans:** Raw specimen images (`kyc_documents/*.png`) were excluded before the initial commit.
- **Committer Metadata (LOW Severity):** The Git committer email in existing commits is set to:  
  `Lavanya <lavanya36914gmail.com@Lavanya-MacBook-Air.local>`  
  This metadata reveals the local macOS hostname (`Lavanya-MacBook-Air.local`) and username.

---

## 4. Dataset Audit & Redistribution Review

| File | Rows | Contents | Redistribution Risk | Recommendation |
|---|---|---|---|---|
| `data/product_catalogue.csv` | 25 SKUs | Product names, specifications, prices, and dependency rules. | **LOW.** Core application logic required by the backend. | **Retain.** |
| `data/mock_gstin_registry.csv` | 3,534 records | Synthetic business names, mock GSTINs, synthetic addresses. | **LOW.** Clearly titled "mock", required for offline registry search demonstration. | **Retain.** |
| `data/mock_udyam_registry.csv` | 2,723 records | Synthetic enterprise names, mock Udyam IDs, activity classifications. | **LOW.** Synthetic hackathon benchmark dataset. | **Retain.** |
| `extracted/kyc_documents/` | 12 case sets | Case specimen scans (PAN cards, GST certificates, utility bills). | **HIGH.** Original competition archives. | **Excluded via `.gitignore`. NOT tracked in Git.** |

---

## 5. Review of Build & Standalone Scripts

The repository consolidates optional standalone generation tooling into `scripts/`:
- **`scripts/build_presentation.py`:** Generates the official 7-slide PPTX and matching PDF from scratch, embedding verified resource hyperlinks and QR codes.
- **`scripts/generate_dpdp_pdf.py`:** Generates the 1-page DPDP compliance note using ReportLab.
- Legacy draft `build_full_submission.py` has been superseded and archived locally.

### Assessment:
1. Both scripts produce reproducible artifacts; their official compiled outputs are tracked in `submission/`.
2. A third party cloning the repository can run `scripts/generate_dpdp_pdf.py` directly; running `scripts/build_presentation.py` requires competition template fixtures.
3. Pre-compiled deliverables are preserved and tracked in `submission/`.

---

## 6. Categorized Findings & Vulnerability Matrix

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           FINDINGS CLASSIFICATION MATRIX                                │
├──────────┬────────────────────────────────────────────────────────┬─────────────────────┤
│ Severity │ Description                                            │ Current Status      │
├──────────┼────────────────────────────────────────────────────────┼─────────────────────┤
│ CRITICAL │ Exposed credentials, API keys, private keys, passwords │ NONE (0 Found)      │
│ HIGH     │ Raw KYC documents, confidential customer scans, .env   │ NONE (0 Found)      │
│ MEDIUM   │ Standalone build scripts with external dependencies    │ IDENTIFIED (Task 4) │
│ LOW      │ Local machine hostname in Git committer email headers  │ IDENTIFIED          │
│ LOW      │ Documentation over-claims (70% CAC, 100% DPDP)         │ REMEDIATED (Task 1) │
└──────────┴────────────────────────────────────────────────────────┴─────────────────────┘
```

### Detailed Breakdown:

#### CRITICAL (0 Issues)
- No active or historic secrets found.

#### HIGH (0 Issues)
- No personal documents, identity scans, or unencrypted database files found in Git.

#### REMEDIATED
- **Standalone Build Scripts:** Relocated to `scripts/build_presentation.py` and `scripts/generate_dpdp_pdf.py` with compiled deliverables tracked in `submission/`. Legacy drafts archived locally.

#### LOW (2 Issues)
- **Local Committer Identity:** Commits `378a606`, `afc0e02`, and `e2aba2d` contain `@Lavanya-MacBook-Air.local` in committer email metadata.
  - *Risk:* Cosmetic exposure of local macOS computer name in public commit logs.
  - *Remediation Note:* If the maintainer wishes to redact this, it would require a Git history rewrite (`git filter-repo` / `git commit --amend` with `git push --force`). Because the user instructions strictly state **"Do not rewrite Git history. Do not force push."**, this is logged as an informational finding. For future commits, set:
    `git config user.email "lavanya36914@gmail.com"` (or GitHub's private `no-reply` address).
- **Documentation Claims:** Previous README drafts stated "-70% CAC Reduction", "100% DPDP Compliance", and "2.5x Funnel Lift" without qualification.
  - *Remediation:* Fully resolved in `README.md` and `docs/DEMO_VIDEO_STORYBOARD.md` by labeling figures as baseline metrics, proposed targets, product visions, or architectural specifications.

---

## 7. Recommended Actions & Next Steps

1. **Keep Git History Intact:** Do not force push or rewrite history.
2. **Add CI Workflow:** Enable `.github/workflows/ci.yml` to automatically verify backend tests and frontend builds on pull requests.
3. **Commit Updated Documentation:** Stage the audited `README.md`, `SECURITY.md`, `docs/DEPLOYMENT.md`, and this audit report.
4. **License Clarity:** Maintain the explicit proprietary disclaimer in Section 10 of `README.md` (no open-source license granted without explicit authorization).

*Audit completed and submitted for repository maintainer review.*

