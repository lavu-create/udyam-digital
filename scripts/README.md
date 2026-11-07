# Submission & Compliance Build Tooling

This directory contains standalone Python generator scripts for reproducing the Airtel SYNC 2026 competition deliverables.

> **Note:** Official compiled submission artifacts are already built, verified, and tracked in [`../submission/`](../submission/). Re-running these scripts is not required to evaluate or run Project Udyam Digital.

---

## 1. Scripts Overview

| Script | Output Deliverable | Dependencies |
|---|---|---|
| [`build_presentation.py`](build_presentation.py) | `submission/Project_Udyam_Digital.pptx`<br/>`submission/Project_Udyam_Digital.pdf` | `python-pptx`, `reportlab`, `pypdf`, `qrcode` |
| [`generate_dpdp_pdf.py`](generate_dpdp_pdf.py) | `submission/DPDP_Privacy_Security_Note.pdf` | `reportlab` |

---

## 2. Invocation Instructions

Both scripts dynamically resolve the repository root and can be invoked either from the root or from within the `scripts/` directory:

### Run from Repository Root:
```bash
python3 scripts/build_presentation.py
python3 scripts/generate_dpdp_pdf.py
```

### Run from `scripts/` Directory:
```bash
cd scripts
python3 build_presentation.py
python3 generate_dpdp_pdf.py
```
