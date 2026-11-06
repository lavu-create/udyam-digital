import os
import sys

# Ensure python_libs is on path
libs_path = os.path.abspath("./python_libs")
if libs_path not in sys.path:
    sys.path.insert(0, libs_path)

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "submission/DPDP_Privacy_Security_Note.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Colors
C_RED = HexColor('#E40000')
C_DARK = HexColor('#111827')
C_GRAY = HexColor('#4B5563')
C_LIGHT = HexColor('#F9FAFB')
C_BORDER = HexColor('#E5E7EB')
C_GREEN = HexColor('#059669')

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    textColor=C_RED
)

sub_style = ParagraphStyle(
    'DocSub',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=C_DARK
)

meta_style = ParagraphStyle(
    'DocMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7.5,
    leading=11,
    textColor=C_GRAY
)

sec_title = ParagraphStyle(
    'SecTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=C_RED,
    spaceAfter=4,
    spaceBefore=6
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7.8,
    leading=11,
    textColor=C_DARK
)

bold_body = ParagraphStyle(
    'BoldBody',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.8,
    leading=11,
    textColor=C_DARK
)

disclaimer_style = ParagraphStyle(
    'DisclaimerText',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=7,
    leading=9.5,
    textColor=C_GRAY
)

story = []

# Title & Header
story.append(Paragraph("PROJECT UDYAM DIGITAL: DATA PRIVACY & SECURITY NOTE", title_style))
story.append(Paragraph("Architectural Alignment with India's Digital Personal Data Protection (DPDP) Act, 2023", sub_style))
story.append(Spacer(1, 3))

meta_text = "<b>Track:</b> Airtel SYNC 2026 – Digital Track &nbsp;|&nbsp; <b>Entity:</b> MSME Acquisition Engine &nbsp;|&nbsp; <b>Date:</b> November 2026 &nbsp;|&nbsp; <b>Status:</b> Technical Architecture Specification"
story.append(Paragraph(meta_text, meta_style))
story.append(Spacer(1, 6))

# Divider
story.append(Table([['']], colWidths=[540], rowHeights=[2], style=TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_RED),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
])))
story.append(Spacer(1, 6))

# Section 1: Executive Summary & Scope
story.append(Paragraph("1. EXECUTIVE SUMMARY & STATUTORY SCOPE", sec_title))
p1 = ("Project Udyam Digital is designed with a strict <b>Privacy-by-Design</b> architecture governed by the principles of "
      "India's <i>Digital Personal Data Protection (DPDP) Act, 2023</i>. The platform enables frictionless onboarding for "
      "Indian MSMEs while safeguarding proprietor personal data, statutory identity artifacts, and utility documents. "
      "<i><b>Engineering Disclaimer:</b> This document outlines concrete software controls implemented in the prototype; "
      "it does not constitute formal statutory legal certification. All test datasets utilize synthetic registries.</i>")
story.append(Paragraph(p1, body_style))
story.append(Spacer(1, 6))

# Section 2: DPDP Statutory Principle Mapping Table
story.append(Paragraph("2. STATUTORY PRINCIPLE TO TECHNICAL CONTROL MAPPING", sec_title))

table_data = [
    [
        Paragraph("<b>DPDP Act Principle</b>", bold_body),
        Paragraph("<b>Statutory Intent</b>", bold_body),
        Paragraph("<b>Implemented Technical Architecture Safeguard</b>", bold_body)
    ],
    [
        Paragraph("<b>Notice & Affirmative Consent</b><br/>(Section 6)", body_style),
        Paragraph("Clear, unbundled, multilingual notice prior to personal data collection.", body_style),
        Paragraph("Explicit opt-in checkboxes presented in proprietor's selected language (Hindi/English). Immutable consent logging with ISO 8601 UTC timestamp and SHA-256 IP hash.", body_style)
    ],
    [
        Paragraph("<b>Purpose Limitation</b><br/>(Section 5)", body_style),
        Paragraph("Data processed strictly for specified, lawful provisioning purpose.", body_style),
        Paragraph("KYC documents and registry data are processed strictly for statutory telecom KYC and premises feasibility. Data is strictly cordoned off from secondary advertising or commercial telemetry.", body_style)
    ],
    [
        Paragraph("<b>Data Minimisation</b><br/>(Section 6(1))", body_style),
        Paragraph("Collect solely the minimum necessary personal data.", body_style),
        Paragraph("No GST certificate is requested for retail broadband SKUs (where requires_gstin=='N'). OCR selectively extracts only Consumer No, Address, and Date, immediately discarding extraneous fields.", body_style)
    ],
    [
        Paragraph("<b>Storage Limitation</b><br/>(Section 8(7))", body_style),
        Paragraph("Retain personal data only as long as required for purpose.", body_style),
        Paragraph("Uploaded KYC document images are stored in an AES-256 encrypted temporary vault and automatically purged 30 days post-service activation, retaining only immutable regulatory reference tokens.", body_style)
    ],
    [
        Paragraph("<b>Reasonable Security</b><br/>(Section 8(5))", body_style),
        Paragraph("Protect against data leaks, breach, and unauthorized access.", body_style),
        Paragraph("Zero external cloud AI transmission of KYC documents; 100% local vision OCR execution. Mandatory PII masking (Aadhaar XXXX-XXXX-1234, phone XXXXXX9821) in all logs and UI views.", body_style)
    ]
]

t = Table(table_data, colWidths=[130, 150, 260])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), C_LIGHT),
    ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('RIGHTPADDING', (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(Spacer(1, 8))

# Section 3: Core Architectural Privacy Safeguards
story.append(Paragraph("3. CORE ARCHITECTURAL PRIVACY BOUNDARIES", sec_title))

p_safeguards = [
    ("A. Zero Cloud LLM Document Leakage (Air-Gapped KYC):", 
     "Under no circumstances are uploaded customer documents (GST certificates, Udyam registration, utility bills) transmitted to public third-party LLMs (such as OpenAI, Gemini, or Claude). The conversational AI Advisor is strictly isolated to commercial product guidance, while all document validation, deskewing, and blur detection execute entirely within the local application runtime."),
    ("B. Automated 30-Day Document Purge Lifecycle:",
     "Customer utility bills and identity documents reside in an AES-256 encrypted storage volume. Upon milestone progression to 'SERVICE_ACTIVE', a background worker schedules an automated hard-deletion of binary document files at T+30 days. Only Department of Telecommunications (DoT) audit hashes are permanently retained."),
    ("C. Comprehensive PII Masking & Log Sanitation:",
     "Customer phone numbers, Signatory Aadhaar references, and tax numbers are dynamically masked across all client-facing screens, partner/field consoles, and operational server logs. Middleware sanitizes all JSON output to prevent accidental exposure of raw personal data in application telemetry."),
    ("D. Granular Role-Based Access Control (RBAC):",
     "Proprietors access order status strictly via authenticated session tokens. Assisted digital channel partners and field executives view only aggregated drop-recovery queues and progress milestones, completely barred from viewing underlying customer identification files.")
]

for title, desc in p_safeguards:
    story.append(Paragraph(f"<b>{title}</b> {desc}", body_style))
    story.append(Spacer(1, 3))

story.append(Spacer(1, 4))

# Footer Box
footer_table = Table([[
    Paragraph("<b>Project Udyam Digital</b> | Airtel SYNC 2026 – Digital Track | Platform Partner: Unstop | 100% DPDP Act, 2023 Aligned Architecture", disclaimer_style)
]], colWidths=[540], style=TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_LIGHT),
    ('BOX', (0,0), (-1,-1), 0.5, C_BORDER),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(footer_table)

doc.build(story)
print(f"Successfully generated: {pdf_path}")

