import os
import sys

# Ensure local python_libs is prioritized
sys.path.insert(0, os.path.abspath('./python_libs'))

import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
import pypdf

os.makedirs('submission', exist_ok=True)

pptx_out = 'submission/Project_Udyam_Digital.pptx'
pdf_out = 'submission/Project_Udyam_Digital.pdf'

# Brand Colors
RED = RGBColor(228, 0, 0)            # #E40000
DARK = RGBColor(31, 41, 55)          # #1F2937
SLATE = RGBColor(17, 24, 39)         # #111827
GRAY = RGBColor(107, 114, 128)       # #6B7280
LIGHT_GRAY = RGBColor(243, 244, 246) # #F3F4F6
WHITE = RGBColor(255, 255, 255)      # #FFFFFF
GREEN = RGBColor(5, 150, 105)        # #059669
AMBER = RGBColor(217, 119, 6)        # #D97706
BORDER = RGBColor(229, 231, 235)     # #E5E7EB

HEX_RED = HexColor('#E40000')
HEX_DARK = HexColor('#1F2937')
HEX_SLATE = HexColor('#111827')
HEX_GRAY = HexColor('#6B7280')
HEX_LIGHT_GRAY = HexColor('#F3F4F6')
HEX_WHITE = HexColor('#FFFFFF')
HEX_GREEN = HexColor('#059669')
HEX_AMBER = HexColor('#D97706')
HEX_BORDER = HexColor('#E5E7EB')
HEX_LIGHT_RED = HexColor('#FEE2E2')

print("Starting generation of competition-ready 7-slide deck...")

# -------------------------------------------------------------
# PART 1: GENERATE PPTX VIA PYTHON-PPTX
# -------------------------------------------------------------
template_path = 'extracted/airtel_sync/Submission Template_Sync.pptx'
prs = pptx.Presentation(template_path)
prs.slide_width = Inches(10.0)
prs.slide_height = Inches(5.625)

slide1 = prs.slides[0]
slide2 = prs.slides[1]

blank_layout = prs.slide_layouts[6]
content_bg = 'extracted/pptx_media/ppt/media/image1.jpg'

for _ in range(5):
    s = prs.slides.add_slide(blank_layout)
    s.shapes.add_picture(content_bg, Inches(0), Inches(0), width=Inches(10.0), height=Inches(5.625))

slides = list(prs.slides)
slide3 = slides[2]
slide4 = slides[3]
slide5 = slides[4]
slide6 = slides[5]
slide7 = slides[6]

def add_header(slide, tag_text, title_text, subtitle_text):
    tb = slide.shapes.add_textbox(Inches(1.3), Inches(0.2), Inches(7.4), Inches(0.95))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p0 = tf.paragraphs[0]
    p0.text = tag_text.upper()
    p0.font.name = 'Arial'
    p0.font.size = Pt(8.5)
    p0.font.bold = True
    p0.font.color.rgb = RED
    p0.space_after = Pt(2)
    
    p1 = tf.add_paragraph()
    p1.text = title_text
    p1.font.name = 'Arial'
    p1.font.size = Pt(17)
    p1.font.bold = True
    p1.font.color.rgb = DARK
    p1.space_after = Pt(2)
    
    p2 = tf.add_paragraph()
    p2.text = subtitle_text
    p2.font.name = 'Arial'
    p2.font.size = Pt(10)
    p2.font.color.rgb = GRAY

# ----------------- SLIDE 1: PROJECT VISION (PPTX) -----------------
# Header block above SYNC logo
t_box = slide1.shapes.add_textbox(Inches(1.8), Inches(0.4), Inches(4.5), Inches(1.8))
tf1 = t_box.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

p = tf1.paragraphs[0]
p.text = "AIRTEL SYNC 2026 · DIGITAL TRACK (ENTERPRISE TRACK A)"
p.font.name = 'Arial'
p.font.size = Pt(8.5)
p.font.bold = True
p.font.color.rgb = RED
p.space_after = Pt(4)

p = tf1.add_paragraph()
p.text = "Project Udyam Digital"
p.font.name = 'Arial'
p.font.size = Pt(30)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_after = Pt(3)

p = tf1.add_paragraph()
p.text = "India's MSME Connectivity Journey, Simplified."
p.font.name = 'Arial'
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RGBColor(229, 231, 235)
p.space_after = Pt(4)

p = tf1.add_paragraph()
p.text = "Making Small Businesses Go Digital in One Sitting (<10 Minutes)"
p.font.name = 'Arial'
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = RED

# Journey Card below SYNC logo
j_bg = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(3.2), Inches(4.7), Inches(1.85))
j_bg.fill.solid()
j_bg.fill.fore_color.rgb = RGBColor(20, 24, 33)
j_bg.line.color.rgb = RED
j_bg.line.width = Pt(1.5)

j_tb = slide1.shapes.add_textbox(Inches(0.75), Inches(3.28), Inches(4.4), Inches(1.7))
j_tf = j_tb.text_frame
j_tf.word_wrap = True
jp0 = j_tf.paragraphs[0]
jp0.text = "THE 10-MINUTE DIGITAL ONBOARDING JOURNEY:"
jp0.font.name = 'Arial'
jp0.font.size = Pt(9.5)
jp0.font.bold = True
jp0.font.color.rgb = WHITE
jp0.space_after = Pt(4)

steps = [
    "1. Multilingual AI Advisor  ->  Vernacular needs discovery (Hindi & English)",
    "2. Right-Fit Bundling       ->  Broadband, SIMs, Cloud & CCTV in one bill",
    "3. Instant Smart KYC        ->  <60s GSTIN & Udyam lookup with local OCR",
    "4. Proactive Live Tracker   ->  Real-time milestone visibility (Zero chase calls)"
]
for st in steps:
    jp = j_tf.add_paragraph()
    jp.text = st
    jp.font.name = 'Arial'
    jp.font.size = Pt(8)
    jp.font.color.rgb = RGBColor(209, 213, 219)
    jp.space_after = Pt(2)

c_box = slide1.shapes.add_textbox(Inches(0.6), Inches(5.1), Inches(6.0), Inches(0.35))
c_tf = c_box.text_frame
cp = c_tf.paragraphs[0]
cp.text = "Empowering 6.3 Crore MSMEs | Transforming 17.6-day procurement into 10 minutes | Unstop Partner"
cp.font.name = 'Arial'
cp.font.size = Pt(8)
cp.font.color.rgb = RGBColor(156, 163, 175)

# ----------------- SLIDE 2: PROBLEM & DATA OPPORTUNITY (PPTX) -----------------
add_header(slide2, "The MSME Acquisition Bottleneck", 
           "Current MSME Acquisition: High Friction, Low Conversion", 
           "Forensic analysis of 5,000 SMB leads reveals a broken sales cycle where 92.6% of interested leads drop out.")

# 3 Top KPI Cards
kpis = [
    ("7.36% ACTIVATION RATE", "Only 368 of 5,000 leads activate", RED),
    ("Rs. 15,053 BLENDED CAC", "Rs. 5.54M total sales spend across cohort", DARK),
    ("17.62 DAYS VELOCITY", "Average 3.01 customer status chase calls", AMBER)
]
card_w = Inches(2.8)
for idx, (title, sub, col) in enumerate(kpis):
    x = Inches(0.6) + idx * Inches(2.95)
    box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.2), card_w, Inches(0.7))
    box.fill.solid()
    box.fill.fore_color.rgb = LIGHT_GRAY
    box.line.color.rgb = col
    box.line.width = Pt(1.5)
    
    tb = slide2.shapes.add_textbox(x + Inches(0.1), Inches(1.23), card_w - Inches(0.2), Inches(0.6))
    tf = tb.text_frame
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = 'Arial'
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = col
    
    p1 = tf.add_paragraph()
    p1.text = sub
    p1.font.name = 'Arial'
    p1.font.size = Pt(8.5)
    p1.font.color.rgb = DARK

# Left Box: Funnel Breakdown
f_box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(2.05), Inches(4.3), Inches(2.95))
f_box.fill.solid()
f_box.fill.fore_color.rgb = WHITE
f_box.line.color.rgb = BORDER
f_box.line.width = Pt(1)

f_tb = slide2.shapes.add_textbox(Inches(0.75), Inches(2.15), Inches(4.0), Inches(2.75))
f_tf = f_tb.text_frame
f_tf.word_wrap = True
fp0 = f_tf.paragraphs[0]
fp0.text = "ACTUAL MSME FUNNEL PROGRESSION (5,000 LEADS)"
fp0.font.name = 'Arial'
fp0.font.size = Pt(9.5)
fp0.font.bold = True
fp0.font.color.rgb = DARK
fp0.space_after = Pt(4)

funnel_rows = [
    ("1. Leads Generated:", "5,000", "100.0%  (Starting Cohort)"),
    ("2. Contacted:", "3,406", " 68.1%  (-1,594 unreachable / no time)"),
    ("3. Needs Assessed:", "1,974", " 58.0%  (-1,432 visit unscheduled)"),
    ("4. Quote Accepted:", "  861", " 43.6%  (-1,113 STEEPEST DROP!)"),
    ("5. KYC Complete:", "  588", " 68.3%  (-273 paperwork / doc trap)"),
    ("6. Fully Activated:", "  368", " 62.6%  (-220 install delay / cancel)")
]
for stage, cnt, pct in funnel_rows:
    p = f_tf.add_paragraph()
    p.text = f"{stage:<20} {cnt:>6}   |  {pct}"
    p.font.name = 'Arial'
    p.font.size = Pt(8)
    if "STEEPEST" in pct:
        p.font.bold = True
        p.font.color.rgb = RED
    else:
        p.font.color.rgb = DARK

f_note = f_tf.add_paragraph()
f_note.text = "\n* Steepest drop occurs from Needs Assessed to Quote Accepted (56.4% drop) due to 5-day quote delays & telco jargon."
f_note.font.name = 'Arial'
f_note.font.size = Pt(7.5)
f_note.font.color.rgb = GRAY

# Right Box: Drop Reason Categorization
d_box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.1), Inches(2.05), Inches(4.3), Inches(2.95))
d_box.fill.solid()
d_box.fill.fore_color.rgb = WHITE
d_box.line.color.rgb = BORDER
d_box.line.width = Pt(1)

d_tb = slide2.shapes.add_textbox(Inches(5.25), Inches(2.15), Inches(4.0), Inches(2.75))
d_tf = d_tb.text_frame
d_tf.word_wrap = True
dp0 = d_tf.paragraphs[0]
dp0.text = "ROOT-CAUSE OF 4,632 DROPPED LEADS"
dp0.font.name = 'Arial'
dp0.font.size = Pt(9.5)
dp0.font.bold = True
dp0.font.color.rgb = DARK
dp0.space_after = Pt(4)

reasons = [
    ("Scheduling Friction (827 leads):", "Owner had no time for visit (531), visit unscheduled by rep (296)."),
    ("Quote Delays & Jargon (385 leads):", "Quote too complex to decipher (206), took 3-5 days to arrive (179)."),
    ("KYC Documentation (273 leads):", "Missing GST/Udyam doc (94), paperwork too long (79), mismatches (47)."),
    ("Install Delays & Churn (220 leads):", "Install delayed >21 days (98), customer cancelled pre-install (53).")
]
for cat, desc in reasons:
    p = d_tf.add_paragraph()
    p.text = cat
    p.font.name = 'Arial'
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = RED
    
    p2 = d_tf.add_paragraph()
    p2.text = desc
    p2.font.name = 'Arial'
    p2.font.size = Pt(8)
    p2.font.color.rgb = DARK
    p2.space_after = Pt(2)

opp = d_tf.add_paragraph()
opp.text = "KEY TAKEAWAY: 48.8% of drops (2,264 leads) stem purely from manual sales scheduling and documentation friction."
opp.font.name = 'Arial'
opp.font.size = Pt(8)
opp.font.bold = True
opp.font.color.rgb = GREEN

# ----------------- SLIDE 3: OUR SOLUTION (PPTX) -----------------
add_header(slide3, "Core Product Architecture",
           "Project Udyam Digital: Architecture of Frictionless Acquisition",
           "Replacing multi-week sales cycles with an intelligent, self-service 10-minute digital onboarding journey.")

pillars = [
    ("1. Conversational AI Advisor", 
     "Vernacular Needs Discovery",
     ["• Discovers needs in plain Hindi & English",
      "• Translates shopkeeper needs into tech",
      "• Recommends tailored 3-tier bundles",
      "• Offline deterministic rule fallback"]),
    ("2. Dynamic Bundle Engine", 
     "Transparent Pricing & Rules",
     ["• Powers 25 enterprise SKUs from catalogue",
      "• Enforces strict dependency graph rules",
      "• Validates GSTIN requirement across 10 SKUs",
      "• Single consolidated monthly bill + setup"]),
    ("3. Instant Smart KYC", 
     "Sub-Second Verification",
     ["• Instant mock GSTIN & Udyam API lookup",
      "• Auto-deskews & checks image blur (K04)",
      "• Freshness check (<90 days anchor 2026)",
      "• DPDP 2023 affirmative consent & purge"]),
    ("4. Post-Order Tracker", 
     "Proactive Milestone SLA",
     ["• 5-stage provisioning state machine",
      "• Live technician contact & scheduled slot",
      "• Automated WhatsApp milestone webhooks",
      "• Eliminates 3.01 customer chase calls"])
]

pw = Inches(2.1)
for idx, (p_title, p_sub, points) in enumerate(pillars):
    x = Inches(0.6) + idx * Inches(2.23)
    p_box = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.25), pw, Inches(2.65))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = WHITE
    p_box.line.color.rgb = RED if idx == 0 else BORDER
    p_box.line.width = Pt(1.5 if idx == 0 else 1)
    
    tb = slide3.shapes.add_textbox(x + Inches(0.1), Inches(1.3), pw - Inches(0.2), Inches(2.55))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = p_title
    p0.font.name = 'Arial'
    p0.font.size = Pt(10)
    p0.font.bold = True
    p0.font.color.rgb = RED
    
    p1 = tf.add_paragraph()
    p1.text = p_sub
    p1.font.name = 'Arial'
    p1.font.size = Pt(8.5)
    p1.font.bold = True
    p1.font.color.rgb = DARK
    p1.space_after = Pt(4)
    
    for pt in points:
        p = tf.add_paragraph()
        p.text = pt
        p.font.name = 'Arial'
        p.font.size = Pt(7.8)
        p.font.color.rgb = DARK
        p.space_after = Pt(2)

pt_box = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(4.05), Inches(8.8), Inches(0.95))
pt_box.fill.solid()
pt_box.fill.fore_color.rgb = LIGHT_GRAY
pt_box.line.color.rgb = DARK
pt_box.line.width = Pt(1)

pt_tb = slide3.shapes.add_textbox(Inches(0.75), Inches(4.1), Inches(8.5), Inches(0.85))
pt_tf = pt_tb.text_frame
pt_tf.word_wrap = True
pt_p0 = pt_tf.paragraphs[0]
pt_p0.text = "O2O CHANNEL PARTNER & FIELD FORCE SYNERGY (ASSISTED DIGITAL MODEL)"
pt_p0.font.name = 'Arial'
pt_p0.font.size = Pt(9.5)
pt_p0.font.bold = True
pt_p0.font.color.rgb = RED

pt_p1 = pt_tf.add_paragraph()
pt_p1.text = "Instead of competing with local retail dealers and field agents, Project Udyam Digital equips them with digital attribution QR codes and back-office drop-recovery queues. Partners earn full recurring commissions while offloading manual documentation, shifting from paper pushers into trusted digital advisors."
pt_p1.font.name = 'Arial'
pt_p1.font.size = Pt(8.5)
pt_p1.font.color.rgb = DARK

# ----------------- SLIDE 4: PRODUCT EXPERIENCE (PPTX) -----------------
add_header(slide4, "User Experience & Prototype Design",
           "Intuitive, Mobile-First Prototype Experience",
           "Proposed prototype screen designs engineered for 375px mobile viewports with bilingual Hindi/English support.")

screens = [
    ("1. AI Conversational Advisor", "WhatsApp-style bilingual chat: 'Namaste! How many staff work at your clinic?' Quick suggestion chips for zero typing."),
    ("2. Recommended Bundles", "3 transparent cards (Starter Rs. 1,298, Growth Rs. 2,597, Pro Rs. 6,896) with plain-language business rationales."),
    ("3. Modular Quote Builder", "Interactive toggles for add-ons: Cloud CCTV (+Rs. 249), Static IP (+Rs. 200). Live total updates; zero hidden clauses."),
    ("4. Instant Registry Check", "GSTIN & Udyam entry triggers sub-second lookup; displays green 'Active' badge and auto-fills business details."),
    ("5. Smart KYC & Blur Trap", "Auto-deskews tilted photos (K02); intercepts blurry docs (K04) and expired electricity bills (K11 >90 days)."),
    ("6. Live Order Tracker", "5-stage visual progress timeline: Assigned technician Amit Sharma, contact card, and scheduled appointment.")
]

sw = Inches(2.8)
sh = Inches(1.65)
for idx, (title, desc) in enumerate(screens):
    row = idx // 3
    col = idx % 3
    x = Inches(0.6) + col * Inches(2.95)
    y = Inches(1.25) + row * Inches(1.8)
    
    s_box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, sw, sh)
    s_box.fill.solid()
    s_box.fill.fore_color.rgb = WHITE
    s_box.line.color.rgb = RED if idx == 0 else BORDER
    s_box.line.width = Pt(1.5 if idx == 0 else 1)
    
    tb = slide4.shapes.add_textbox(x + Inches(0.1), y + Inches(0.08), sw - Inches(0.2), sh - Inches(0.15))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = 'Arial'
    p0.font.size = Pt(9.5)
    p0.font.bold = True
    p0.font.color.rgb = RED if idx == 0 else DARK
    p0.space_after = Pt(2)
    
    p1 = tf.add_paragraph()
    p1.text = desc
    p1.font.name = 'Arial'
    p1.font.size = Pt(8)
    p1.font.color.rgb = DARK

proto_note = slide4.shapes.add_textbox(Inches(0.6), Inches(4.9), Inches(8.8), Inches(0.3))
pn_tf = proto_note.text_frame
pn_p = pn_tf.paragraphs[0]
pn_p.text = "* Proposed prototype interface specifications. Designed for zero-training adoption by non-technical Indian proprietors."
pn_p.font.name = 'Arial'
pn_p.font.size = Pt(8)
pn_p.font.italic = True
pn_p.font.color.rgb = GRAY

# ----------------- SLIDE 5: TECHNICAL ARCHITECTURE & TRUST (PPTX) -----------------
add_header(slide5, "System Architecture & Privacy",
           "Modular Monolith Architecture with Privacy-by-Design",
           "Decoupled FastAPI backend, local vision OCR processing, and strict DPDP Act 2023 compliance.")

# Left Box: Tech Architecture
a_box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.25), Inches(4.3), Inches(3.7))
a_box.fill.solid()
a_box.fill.fore_color.rgb = WHITE
a_box.line.color.rgb = BORDER
a_box.line.width = Pt(1)

a_tb = slide5.shapes.add_textbox(Inches(0.75), Inches(1.35), Inches(4.0), Inches(3.5))
a_tf = a_tb.text_frame
a_tf.word_wrap = True
ap0 = a_tf.paragraphs[0]
ap0.text = "SYSTEM COMPONENT TOPOLOGY"
ap0.font.name = 'Arial'
ap0.font.size = Pt(9.5)
ap0.font.bold = True
ap0.font.color.rgb = DARK
ap0.space_after = Pt(4)

arch_layers = [
    ("Presentation Tier:", "React 18, TypeScript, Tailwind CSS, Bilingual i18n"),
    ("API Gateway Tier:", "Python FastAPI, CORS middleware, Pydantic validation"),
    ("Core Service Modules:", "Advisor Adapter (with offline rule fallback), Catalog Engine (25 SKUs), Smart KYC Orchestrator, Order State Machine, Partner Co-Pilot"),
    ("Offline Registry Engines:", "Indexed Mock GSTIN (3,534 records), Mock Udyam (2,723 records), Local OCR Pipeline (Laplacian blur variance + deskew)"),
    ("Persistence & Vault:", "SQLite (Local MVP) / PostgreSQL (Cloud), AES-256 Encrypted 30-Day Vault, Immutable DPDP Audit Ledger")
]
for layer, desc in arch_layers:
    p = a_tf.add_paragraph()
    p.text = layer
    p.font.name = 'Arial'
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = RED
    
    p2 = a_tf.add_paragraph()
    p2.text = desc
    p2.font.name = 'Arial'
    p2.font.size = Pt(8)
    p2.font.color.rgb = DARK
    p2.space_after = Pt(2)

# Right Box: DPDP Act Controls
t_box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.1), Inches(1.25), Inches(4.3), Inches(3.7))
t_box.fill.solid()
t_box.fill.fore_color.rgb = WHITE
t_box.line.color.rgb = BORDER
t_box.line.width = Pt(1)

t_tb = slide5.shapes.add_textbox(Inches(5.25), Inches(1.35), Inches(4.0), Inches(3.5))
t_tf = t_tb.text_frame
t_tf.word_wrap = True
tp0 = t_tf.paragraphs[0]
tp0.text = "DPDP ACT, 2023 TRUST & PRIVACY CONTROLS"
tp0.font.name = 'Arial'
tp0.font.size = Pt(9.5)
tp0.font.bold = True
tp0.font.color.rgb = DARK
tp0.space_after = Pt(4)

dpdp_points = [
    ("Affirmative Consent (Sec 6):", "Unbundled, explicit checkboxes in Hindi & English; immutable consent timestamp and IP hash logging."),
    ("Purpose Limitation (Sec 5):", "KYC data processed strictly for statutory telecom provisioning; zero secondary commercial monetization."),
    ("Data Minimisation (Sec 6(1)):", "No GSTIN required for retail broadband; only minimum statutory ID and supply address captured."),
    ("Zero Cloud PII Leakage:", "100% local OCR execution; customer documents are never transmitted to external third-party AI APIs."),
    ("Storage Limitation (Sec 8):", "Automated 30-day purge of document images post-activation; encrypted AES-256 storage."),
    ("PII Masking & Sanitation:", "Signatory IDs and phone numbers masked in UI, logs, and partner views (e.g. XXXXXX9821).")
]
for title, desc in dpdp_points:
    p = t_tf.add_paragraph()
    p.text = title
    p.font.name = 'Arial'
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = GREEN
    
    p2 = t_tf.add_paragraph()
    p2.text = desc
    p2.font.name = 'Arial'
    p2.font.size = Pt(7.8)
    p2.font.color.rgb = DARK
    p2.space_after = Pt(2)

# ----------------- SLIDE 6: BUSINESS MODEL & IMPACT (PPTX) -----------------
add_header(slide6, "Unit Economics & Value Creation",
           "Sustainable Unit Economics & Quantified Business Impact",
           "Slashing customer acquisition costs by 70% while accelerating conversion and recurring ARPU.")

# Top Comparison Matrix (Facts vs Targets)
m_box = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.25), Inches(8.8), Inches(1.8))
m_box.fill.solid()
m_box.fill.fore_color.rgb = WHITE
m_box.line.color.rgb = BORDER
m_box.line.width = Pt(1)

m_tb = slide6.shapes.add_textbox(Inches(0.75), Inches(1.3), Inches(8.5), Inches(1.7))
m_tf = m_tb.text_frame
m_tf.word_wrap = True
mp0 = m_tf.paragraphs[0]
mp0.text = "BASELINE FUNNEL (ACTUAL DATASET) VS. PROJECT UDYAM DIGITAL TARGETS"
mp0.font.name = 'Arial'
mp0.font.size = Pt(9.5)
mp0.font.bold = True
mp0.font.color.rgb = DARK
mp0.space_after = Pt(4)

matrix = [
    ("Funnel Conversion Rate:", "7.36% (368 / 5,000 leads)", "18.5% – 22.0% (+2.5x lift)", "Removes visit scheduling friction & 5-day quote wait"),
    ("Blended CAC per Activated SMB:", "Rs. 15,053 per activation", "Rs. 4,200 – Rs. 4,500 (-70%)", "Shifts from feet-on-street to zero-touch digital self-serve"),
    ("Average Activation Velocity:", "17.62 Days (Median: 17d)", "2.5 – 3.5 Days (-80%)", "Sub-second digital KYC pass-through & instant scheduling"),
    ("Status Chasing Inbound Calls:", "3.01 Calls per customer", "< 0.5 Calls (-83%)", "Live visual milestone tracker & automated WhatsApp updates"),
    ("6-Month Customer Churn:", "15.22% (56 / 368 churned)", "< 7.5% (-50%)", "Needs-based right-fit recommendation vs sales quota pitching")
]
for metric, base, tgt, lever in matrix:
    p = m_tf.add_paragraph()
    p.text = f"{metric:<28} | Base: {base:<22} -> Target: {tgt:<24} | {lever}"
    p.font.name = 'Arial'
    p.font.size = Pt(8)
    p.font.color.rgb = DARK
    p.space_after = Pt(1)

# Bottom 3 Value Pillars
v_pillars = [
    ("Recurring ARPU Expansion", 
     "Broadband + SaaS Subscriptions", 
     "Generates predictable monthly cash flows: Micro retail averages Rs. 2,470/mo, professional offices average Rs. 6,796/mo, multi-site businesses reach Rs. 31,233/mo on a single bill."),
    ("High-Margin Cross-Selling", 
     "SaaS, Security & CCTV Add-ons", 
     "Modular upsells like Cloud Backup (P17), Endpoint Security (P20), and Cloud CCTV (P23) deliver >70% gross margin with zero incremental field visit costs."),
    ("Assisted Digital O2O Synergy", 
     "Channel Partner Commissioning", 
     "Local retail dealers and field agents earn a 12% recurring revenue share on digital QR sign-ups. Payback period drops from 6.1 months to 1.8 months.")
]
vw = Inches(2.8)
for idx, (title, sub, desc) in enumerate(v_pillars):
    x = Inches(0.6) + idx * Inches(2.95)
    v_box = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(3.2), vw, Inches(1.75))
    v_box.fill.solid()
    v_box.fill.fore_color.rgb = LIGHT_GRAY
    v_box.line.color.rgb = RED if idx == 0 else BORDER
    v_box.line.width = Pt(1.5 if idx == 0 else 1)
    
    tb = slide6.shapes.add_textbox(x + Inches(0.1), Inches(3.28), vw - Inches(0.2), Inches(1.6))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = 'Arial'
    p0.font.size = Pt(9.5)
    p0.font.bold = True
    p0.font.color.rgb = RED if idx == 0 else DARK
    
    p1 = tf.add_paragraph()
    p1.text = sub
    p1.font.name = 'Arial'
    p1.font.size = Pt(8.5)
    p1.font.bold = True
    p1.font.color.rgb = DARK
    p1.space_after = Pt(3)
    
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.name = 'Arial'
    p2.font.size = Pt(8)
    p2.font.color.rgb = DARK

# ----------------- SLIDE 7: EXECUTION ROADMAP & CONCLUSION (PPTX) -----------------
add_header(slide7, "Roadmap & Strategic Vision",
           "90-Day Execution Roadmap & Vision for India's MSMEs",
           "Structured rollout roadmap delivering enterprise-scale digital adoption across Tier 1 and Tier 2 clusters.")

phases = [
    ("Phase 1: Days 1–30", "Core MVP Foundation", [
        "• Deploy FastAPI modular backend",
        "• Ingest 25 SKUs & dependency rules",
        "• Index mock GSTIN & Udyam registries",
        "• Build mobile React wizard with i18n"
    ]),
    ("Phase 2: Days 31–60", "Smart KYC & Vision", [
        "• Local blur detection & auto-deskew",
        "• DPDP 30-day vault purge automation",
        "• Pass K01-K12 assertion test harness",
        "• Order state machine & milestone API"
    ]),
    ("Phase 3: Days 61–90", "Pilot & Partner Co-Pilot", [
        "• 2-city pilot (Jaipur Tier 2 & Kolkata)",
        "• Deploy Partner attribution QR console",
        "• Drop-recovery queue for field reps",
        "• Measure conversion & CAC lift"
    ])
]
rw = Inches(2.8)
for idx, (title, sub, tasks) in enumerate(phases):
    x = Inches(0.6) + idx * Inches(2.95)
    r_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.25), rw, Inches(1.85))
    r_box.fill.solid()
    r_box.fill.fore_color.rgb = WHITE
    r_box.line.color.rgb = RED if idx == 0 else BORDER
    r_box.line.width = Pt(1.5 if idx == 0 else 1)
    
    tb = slide7.shapes.add_textbox(x + Inches(0.1), Inches(1.3), rw - Inches(0.2), Inches(1.75))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = 'Arial'
    p0.font.size = Pt(9.5)
    p0.font.bold = True
    p0.font.color.rgb = RED
    
    p1 = tf.add_paragraph()
    p1.text = sub
    p1.font.name = 'Arial'
    p1.font.size = Pt(8.5)
    p1.font.bold = True
    p1.font.color.rgb = DARK
    p1.space_after = Pt(2)
    
    for tk in tasks:
        p = tf.add_paragraph()
        p.text = tk
        p.font.name = 'Arial'
        p.font.size = Pt(7.8)
        p.font.color.rgb = DARK
        p.space_after = Pt(1)

# Bottom Left Box: Strategic Vision
c_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(3.2), Inches(5.1), Inches(1.8))
c_box.fill.solid()
c_box.fill.fore_color.rgb = RGBColor(24, 28, 36)
c_box.line.color.rgb = RED
c_box.line.width = Pt(1.5)

c_tb = slide7.shapes.add_textbox(Inches(0.75), Inches(3.28), Inches(4.8), Inches(1.65))
c_tf = c_tb.text_frame
c_tf.word_wrap = True

cp0 = c_tf.paragraphs[0]
cp0.text = "WHY PROJECT UDYAM DIGITAL MATTERS"
cp0.font.name = 'Arial'
cp0.font.size = Pt(10)
cp0.font.bold = True
cp0.font.color.rgb = WHITE
cp0.space_after = Pt(3)

cp1 = c_tf.add_paragraph()
cp1.text = "Project Udyam Digital bridges enterprise telecom and 6.3 crore MSMEs. By replacing paper friction with conversational AI and multi-week delays with instant digital trust, we convert high-friction acquisition into a 10-minute reality."
cp1.font.name = 'Arial'
cp1.font.size = Pt(8)
cp1.font.color.rgb = RGBColor(229, 231, 235)
cp1.space_after = Pt(4)

cp2 = c_tf.add_paragraph()
cp2.text = "Key Outcomes:  [ 6.3 Cr MSMEs Empowered ]   [ 70% CAC Cut ]\n                [ 10-Min Onboarding ]   [ 100% DPDP Act Compliant ]"
cp2.font.name = 'Arial'
cp2.font.size = Pt(7.8)
cp2.font.bold = True
cp2.font.color.rgb = RED

# Bottom Right Box: Project Resources & Submission Artifacts
res_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.85), Inches(3.2), Inches(3.55), Inches(1.8))
res_box.fill.solid()
res_box.fill.fore_color.rgb = WHITE
res_box.line.color.rgb = BORDER
res_box.line.width = Pt(1)

# Resources Title
rtb = slide7.shapes.add_textbox(Inches(5.95), Inches(3.25), Inches(3.35), Inches(0.3))
rtf = rtb.text_frame
rp0 = rtf.paragraphs[0]
rp0.text = "PROJECT RESOURCES & SUBMISSION ARTIFACTS"
rp0.font.name = 'Arial'
rp0.font.size = Pt(8.5)
rp0.font.bold = True
rp0.font.color.rgb = DARK

# GitHub QR Code
qr_path = "submission/github_qr.png"
if os.path.exists(qr_path):
    slide7.shapes.add_picture(qr_path, Inches(5.95), Inches(3.58), width=Inches(0.85), height=Inches(0.85))

# GitHub Info & Hyperlink
gtb = slide7.shapes.add_textbox(Inches(6.88), Inches(3.55), Inches(2.45), Inches(0.88))
gtf = gtb.text_frame
gtf.word_wrap = True

gp0 = gtf.paragraphs[0]
gp0.text = "GitHub Repository"
gp0.font.name = 'Arial'
gp0.font.size = Pt(8)
gp0.font.bold = True
gp0.font.color.rgb = RED

gp1 = gtf.add_paragraph()
gp1.text = "Explore the Source Code"
gp1.font.name = 'Arial'
gp1.font.size = Pt(7)
gp1.font.color.rgb = GRAY
gp1.space_after = Pt(2)

gp2 = gtf.add_paragraph()
grun = gp2.add_run()
grun.text = "github.com/lavu-create/udyam-digital"
grun.font.name = 'Arial'
grun.font.size = Pt(6.8)
grun.font.bold = True
grun.font.underline = True
grun.font.color.rgb = DARK
grun.hyperlink.address = "https://github.com/lavu-create/udyam-digital"

# Demo Video Placeholder Container
v_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.95), Inches(4.5), Inches(3.35), Inches(0.43))
v_box.fill.solid()
v_box.fill.fore_color.rgb = LIGHT_GRAY
v_box.line.color.rgb = BORDER
v_box.line.width = Pt(0.75)

vtb = slide7.shapes.add_textbox(Inches(6.0), Inches(4.5), Inches(3.25), Inches(0.42))
vtf = vtb.text_frame
vtf.word_wrap = True

vp0 = vtf.paragraphs[0]
vp0.text = "Demo Video (Max 3m): [ Link Pending Upload ]"
vp0.font.name = 'Arial'
vp0.font.size = Pt(7)
vp0.font.bold = True
vp0.font.color.rgb = DARK

vp1 = vtf.add_paragraph()
vp1.text = "Walkthrough pitch link & QR will be added upon video upload."
vp1.font.name = 'Arial'
vp1.font.size = Pt(6)
vp1.font.italic = True
vp1.font.color.rgb = GRAY

prs.save(pptx_out)
print(f"PPTX successfully created at: {pptx_out}")

# -------------------------------------------------------------
# PART 2: GENERATE IDENTICAL HIGH-RES PDF VIA REPORTLAB
# -------------------------------------------------------------
print("Generating PDF...")
c = canvas.Canvas(pdf_out, pagesize=(720, 405))

def draw_card(c, x, y, w, h, fill_col, border_col, border_w=1, r=6):
    c.saveState()
    c.setFillColor(fill_col)
    c.setStrokeColor(border_col)
    c.setLineWidth(border_w)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1)
    c.restoreState()

def draw_header_pdf(c, tag, title, subtitle):
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_RED)
    c.drawString(95, 385, tag.upper())
    
    c.setFont('Helvetica-Bold', 14)
    c.setFillColor(HEX_DARK)
    c.drawString(95, 368, title)
    
    c.setFont('Helvetica', 8)
    c.setFillColor(HEX_GRAY)
    c.drawString(95, 354, subtitle)

# --- PDF PAGE 1: VISION ---
c.drawImage('extracted/pptx_media/ppt/media/image2.jpg', 0, 0, width=720, height=405)

# Title Block placed above the SYNC logo (Airtel logo is to the left)
c.setFont('Helvetica-Bold', 8)
c.setFillColor(HEX_RED)
c.drawString(135, 360, "AIRTEL SYNC 2026 · DIGITAL TRACK (ENTERPRISE TRACK A)")

c.setFont('Helvetica-Bold', 26)
c.setFillColor(HEX_WHITE)
c.drawString(135, 332, "Project Udyam Digital")

c.setFont('Helvetica-Bold', 12)
c.setFillColor(HexColor('#E5E7EB'))
c.drawString(135, 314, "India's MSME Connectivity Journey, Simplified.")

c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_RED)
c.drawString(135, 298, "Making Small Businesses Go Digital in One Sitting (<10 Minutes)")

# 4-Step Journey Card placed below the SYNC logo (y=35..165)
draw_card(c, 45, 35, 330, 130, HexColor('#141821'), HEX_RED, border_w=1.5, r=6)
c.setFont('Helvetica-Bold', 8)
c.setFillColor(HEX_WHITE)
c.drawString(55, 148, "THE 10-MINUTE DIGITAL ONBOARDING JOURNEY:")

c.setFont('Helvetica', 7)
c.setFillColor(HexColor('#D1D5DB'))
c.drawString(55, 132, "1. Vernacular AI Advisor  -> Plain-language needs discovery (Hindi/English)")
c.drawString(55, 118, "2. Smart Dynamic Bundles  -> Broadband, SIMs, Cloud & CCTV in one bill")
c.drawString(55, 104, "3. Instant Smart KYC      -> <60s GSTIN & Udyam lookup with local OCR")
c.drawString(55, 90,  "4. Post-Order Tracker     -> Real-time milestone visibility (Zero chase calls)")

c.setFont('Helvetica-Oblique', 6.8)
c.setFillColor(HexColor('#9CA3AF'))
c.drawString(55, 66, "Empowering 6.3 Crore MSMEs | Transforming 17.6-day procurement into 10 minutes | Unstop Partner")

c.showPage()

# --- PDF PAGE 2: PROBLEM & DATA OPPORTUNITY ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "The MSME Acquisition Bottleneck", 
               "Current MSME Acquisition: High Friction, Low Conversion", 
               "Forensic analysis of 5,000 SMB leads reveals a broken sales cycle where 92.6% of interested leads drop out.")

# 3 Top KPI Cards
draw_card(c, 45, 290, 195, 50, HEX_LIGHT_GRAY, HEX_RED, border_w=1.5)
c.setFont('Helvetica-Bold', 9.5)
c.setFillColor(HEX_RED)
c.drawString(55, 324, "7.36% ACTIVATION RATE")
c.setFont('Helvetica', 7.5)
c.setFillColor(HEX_DARK)
c.drawString(55, 306, "Only 368 of 5,000 leads activate")

draw_card(c, 255, 290, 195, 50, HEX_LIGHT_GRAY, HEX_DARK, border_w=1.5)
c.setFont('Helvetica-Bold', 9.5)
c.setFillColor(HEX_DARK)
c.drawString(265, 324, "Rs. 15,053 BLENDED CAC")
c.setFont('Helvetica', 7.5)
c.setFillColor(HEX_DARK)
c.drawString(265, 306, "Rs. 5.54M total sales spend across cohort")

draw_card(c, 465, 290, 195, 50, HEX_LIGHT_GRAY, HEX_AMBER, border_w=1.5)
c.setFont('Helvetica-Bold', 9.5)
c.setFillColor(HEX_AMBER)
c.drawString(475, 324, "17.62 DAYS VELOCITY")
c.setFont('Helvetica', 7.5)
c.setFillColor(HEX_DARK)
c.drawString(475, 306, "Average 3.01 customer status chase calls")

# Left: Funnel
draw_card(c, 45, 60, 300, 215, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(55, 258, "ACTUAL MSME FUNNEL PROGRESSION (5,000 LEADS)")

funnel_p = [
    ("1. Leads Generated:", "5,000", "100.0%  (Starting Cohort)", False),
    ("2. Contacted:", "3,406", " 68.1%  (-1,594 unreachable / no time)", False),
    ("3. Needs Assessed:", "1,974", " 58.0%  (-1,432 visit unscheduled)", False),
    ("4. Quote Accepted:", "  861", " 43.6%  (-1,113 STEEPEST DROP!)", True),
    ("5. KYC Complete:", "  588", " 68.3%  (-273 paperwork / doc trap)", False),
    ("6. Fully Activated:", "  368", " 62.6%  (-220 install delay / cancel)", False)
]
for idx, (stg, cnt, pct, is_bold) in enumerate(funnel_p):
    y = 236 - idx * 24
    c.setFont('Helvetica-Bold' if is_bold else 'Helvetica', 7.5)
    c.setFillColor(HEX_RED if is_bold else HEX_DARK)
    c.drawString(55, y, f"{stg:<20} {cnt:>6}   |  {pct}")

c.setFont('Helvetica-Oblique', 6.8)
c.setFillColor(HEX_GRAY)
c.drawString(55, 78, "* Steepest drop: Needs Assessed to Quote Accepted (-56.4%) due to 5-day wait & jargon.")

# Right: Drop Reasons
draw_card(c, 360, 60, 300, 215, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(370, 258, "ROOT-CAUSE OF 4,632 DROPPED LEADS")

reasons_p = [
    ("Scheduling Friction (827 leads):", "Owner had no time for visit (531), visit unscheduled (296)."),
    ("Quote Delays & Jargon (385 leads):", "Quote too complex to decipher (206), took 3-5 days to arrive (179)."),
    ("KYC Documentation (273 leads):", "Missing GST/Udyam doc (94), paperwork too long (79), mismatches (47)."),
    ("Install Delays & Churn (220 leads):", "Install delayed >21 days (98), customer cancelled pre-install (53).")
]
for idx, (cat, desc) in enumerate(reasons_p):
    y = 238 - idx * 38
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_RED)
    c.drawString(370, y, cat)
    c.setFont('Helvetica', 7)
    c.setFillColor(HEX_DARK)
    c.drawString(370, y - 11, desc)

c.setFont('Helvetica-Bold', 7.2)
c.setFillColor(HEX_GREEN)
c.drawString(370, 80, "TAKEAWAY: 48.8% of drops (2,264 leads) stem from manual sales & paperwork friction.")

c.showPage()

# --- PDF PAGE 3: OUR SOLUTION (4 PILLARS) ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "Core Product Architecture",
               "Project Udyam Digital: Architecture of Frictionless Acquisition",
               "Replacing multi-week sales cycles with an intelligent, self-service 10-minute digital onboarding journey.")

pillars_p = [
    ("1. Conversational Advisor", "Vernacular Needs Discovery", [
        "• Plain Hindi & English discovery",
        "• Demystifies complex telco jargon",
        "• Recommends 3-tier smart bundles",
        "• Offline deterministic rule fallback"
    ]),
    ("2. Dynamic Bundle Engine", "Transparent Pricing & Rules", [
        "• Powers 25 enterprise SKUs",
        "• Enforces dependency graph rules",
        "• Validates GSTIN across 10 SKUs",
        "• Single monthly bill + setup fees"
    ]),
    ("3. Instant Smart KYC", "Sub-Second Verification", [
        "• Mock GSTIN & Udyam API lookups",
        "• Auto-deskews & checks blur (K04)",
        "• Freshness check (<90d anchor 2026)",
        "• DPDP 2023 consent & 30-day purge"
    ]),
    ("4. Post-Order Tracker", "Proactive Milestone SLA", [
        "• 5-stage provisioning state machine",
        "• Live technician contact & schedule",
        "• Automated WhatsApp webhooks",
        "• Eliminates 3.01 customer calls"
    ])
]
for idx, (p_t, p_s, pts) in enumerate(pillars_p):
    x = 45 + idx * 155
    draw_card(c, x, 130, 145, 195, HEX_WHITE, HEX_RED if idx == 0 else HEX_BORDER, border_w=1.5 if idx == 0 else 1)
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(HEX_RED if idx == 0 else HEX_DARK)
    c.drawString(x + 8, 308, p_t)
    
    c.setFont('Helvetica-Bold', 7)
    c.setFillColor(HEX_DARK)
    c.drawString(x + 8, 294, p_s)
    
    for p_idx, pt in enumerate(pts):
        c.setFont('Helvetica', 6.8)
        c.drawString(x + 8, 276 - p_idx * 15, pt)

draw_card(c, 45, 55, 620, 65, HEX_LIGHT_GRAY, HEX_DARK, border_w=1)
c.setFont('Helvetica-Bold', 8)
c.setFillColor(HEX_RED)
c.drawString(55, 102, "O2O CHANNEL PARTNER & FIELD FORCE SYNERGY (ASSISTED DIGITAL MODEL)")

c.setFont('Helvetica', 7.2)
c.setFillColor(HEX_DARK)
c.drawString(55, 87, "Instead of competing with local retail dealers and field agents, Project Udyam Digital equips them with digital attribution")
c.drawString(55, 75, "QR codes and back-office drop-recovery queues. Partners earn full recurring commissions while offloading manual documentation,")
c.drawString(55, 63, "transforming them from paper pushers into trusted digital advisors.")

c.showPage()

# --- PDF PAGE 4: PRODUCT EXPERIENCE (MOCKUPS) ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "User Experience & Prototype Design",
               "Intuitive, Mobile-First Prototype Experience",
               "Proposed prototype screen designs engineered for 375px mobile viewports with bilingual Hindi/English support.")

screens_p = [
    ("1. AI Conversational Advisor", "WhatsApp-style bilingual chat: 'Namaste! How many staff work at your clinic?' Quick suggestion chips for zero typing."),
    ("2. Recommended Bundles", "3 transparent cards (Starter Rs. 1,298, Growth Rs. 2,597, Pro Rs. 6,896) with plain-language business rationales."),
    ("3. Modular Quote Builder", "Interactive toggles for add-ons: Cloud CCTV (+Rs. 249), Static IP (+Rs. 200). Live total updates; zero hidden clauses."),
    ("4. Instant Registry Check", "GSTIN & Udyam entry triggers sub-second lookup; displays green 'Active' badge and auto-fills business details."),
    ("5. Smart KYC & Blur Trap", "Auto-deskews tilted photos (K02); intercepts blurry docs (K04) and expired electricity bills (K11 >90 days)."),
    ("6. Live Order Tracker", "5-stage visual progress timeline: Assigned technician Amit Sharma, contact card, and scheduled appointment.")
]

for idx, (title, desc) in enumerate(screens_p):
    row = idx // 3
    col = idx % 3
    x = 45 + col * 210
    y = 205 - row * 130
    
    draw_card(c, x, y, 198, 120, HEX_WHITE, HEX_RED if idx == 0 else HEX_BORDER, border_w=1.5 if idx == 0 else 1)
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(HEX_RED if idx == 0 else HEX_DARK)
    c.drawString(x + 10, y + 104, title)
    
    words = desc.split(' ')
    line1 = " ".join(words[:7])
    line2 = " ".join(words[7:14])
    line3 = " ".join(words[14:21])
    line4 = " ".join(words[21:])
    
    c.setFont('Helvetica', 7)
    c.setFillColor(HEX_DARK)
    curr_y = y + 88
    for l in [line1, line2, line3, line4]:
        if l:
            c.drawString(x + 10, curr_y, l)
            curr_y -= 13

c.setFont('Helvetica-Oblique', 7)
c.setFillColor(HEX_GRAY)
c.drawString(45, 60, "* Proposed prototype interface specifications. Designed for zero-training adoption by non-technical Indian proprietors.")

c.showPage()

# --- PDF PAGE 5: TECHNICAL ARCHITECTURE & TRUST ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "System Architecture & Privacy",
               "Modular Monolith Architecture with Privacy-by-Design",
               "Decoupled FastAPI backend, local vision OCR processing, and strict DPDP Act 2023 compliance.")

# Left: System Topology
draw_card(c, 45, 60, 300, 265, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(55, 308, "SYSTEM COMPONENT TOPOLOGY")

layers_p = [
    ("Presentation Tier:", "React 18, TypeScript, Tailwind CSS, Bilingual i18n"),
    ("API Gateway Tier:", "Python FastAPI, CORS middleware, Pydantic validation"),
    ("Core Service Modules:", "Advisor Adapter (with offline rule fallback), Catalog Engine (25 SKUs), Smart KYC Orchestrator, Order State Machine, Partner Co-Pilot"),
    ("Offline Registry Engines:", "Indexed Mock GSTIN (3,534 records), Mock Udyam (2,723 records), Local OCR Pipeline (Laplacian blur variance + deskew)"),
    ("Persistence & Vault:", "SQLite (Local MVP) / PostgreSQL (Cloud), AES-256 Encrypted 30-Day Vault, Immutable DPDP Audit Ledger")
]
curr_y = 292
for l_title, l_desc in layers_p:
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_RED)
    c.drawString(55, curr_y, l_title)
    c.setFont('Helvetica', 6.8)
    c.setFillColor(HEX_DARK)
    
    words = l_desc.split(' ')
    l1 = " ".join(words[:8])
    l2 = " ".join(words[8:])
    c.drawString(55, curr_y - 10, l1)
    if l2:
        c.drawString(55, curr_y - 19, l2)
        curr_y -= 31
    else:
        curr_y -= 22

# Right: DPDP Act Controls
draw_card(c, 360, 60, 305, 265, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(370, 308, "DPDP ACT, 2023 TRUST & PRIVACY CONTROLS")

dpdp_p = [
    ("Affirmative Consent (Sec 6):", "Unbundled checkboxes in Hindi & English; immutable consent timestamp & IP hash."),
    ("Purpose Limitation (Sec 5):", "KYC data processed strictly for statutory telecom onboarding; zero secondary use."),
    ("Data Minimisation (Sec 6(1)):", "No GSTIN required for retail broadband; only minimum statutory ID & address captured."),
    ("Zero Cloud PII Leakage:", "100% local OCR execution; customer documents are never sent to external AI APIs."),
    ("Storage Limitation (Sec 8):", "Automated 30-day purge of document images post-activation; encrypted vault."),
    ("PII Masking & Sanitation:", "Signatory IDs and phone numbers masked in UI and logs (e.g. XXXXXX9821).")
]
curr_y = 292
for d_title, d_desc in dpdp_p:
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_GREEN)
    c.drawString(370, curr_y, d_title)
    c.setFont('Helvetica', 6.8)
    c.setFillColor(HEX_DARK)
    
    words = d_desc.split(' ')
    l1 = " ".join(words[:8])
    l2 = " ".join(words[8:])
    c.drawString(370, curr_y - 10, l1)
    if l2:
        c.drawString(370, curr_y - 19, l2)
        curr_y -= 31
    else:
        curr_y -= 22

c.showPage()

# --- PDF PAGE 6: BUSINESS MODEL & IMPACT ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "Unit Economics & Value Creation",
               "Sustainable Unit Economics & Quantified Business Impact",
               "Slashing customer acquisition costs by 70% while accelerating conversion and recurring ARPU.")

# Top Comparison Matrix
draw_card(c, 45, 195, 620, 130, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(55, 310, "BASELINE FUNNEL (ACTUAL DATASET) VS. PROJECT UDYAM DIGITAL TARGETS")

matrix_p = [
    ("Funnel Conversion Rate:", "7.36% (368 / 5,000 leads)", "18.5% – 22.0% (+2.5x lift)", "Removes visit scheduling friction & 5-day quote wait"),
    ("Blended CAC per Activated SMB:", "Rs. 15,053 per activation", "Rs. 4,200 – Rs. 4,500 (-70%)", "Shifts from feet-on-street to zero-touch digital self-serve"),
    ("Average Activation Velocity:", "17.62 Days (Median: 17d)", "2.5 – 3.5 Days (-80%)", "Sub-second digital KYC pass-through & instant scheduling"),
    ("Status Chasing Inbound Calls:", "3.01 Calls per customer", "< 0.5 Calls (-83%)", "Live visual milestone tracker & automated WhatsApp updates"),
    ("6-Month Customer Churn:", "15.22% (56 / 368 churned)", "< 7.5% (-50%)", "Needs-based right-fit recommendation vs sales quota pitching")
]
for idx, (metric, base, tgt, lever) in enumerate(matrix_p):
    y = 290 - idx * 18
    c.setFont('Courier-Bold', 6.8)
    c.setFillColor(HEX_DARK)
    c.drawString(55, y, f"{metric:<28} | Base: {base:<22} -> Target: {tgt:<24} | {lever}")

# Bottom 3 Pillars
v_p = [
    ("Recurring ARPU Expansion", "Broadband + SaaS Subscriptions", 
     "Generates predictable monthly cash flows: Micro retail averages Rs. 2,470/mo, professional offices average Rs. 6,796/mo, multi-site businesses reach Rs. 31,233/mo on a single bill."),
    ("High-Margin Cross-Selling", "SaaS, Security & CCTV Add-ons", 
     "Modular upsells like Cloud Backup (P17), Endpoint Security (P20), and Cloud CCTV (P23) deliver >70% gross margin with zero incremental field visit costs."),
    ("Assisted Digital O2O Synergy", "Channel Partner Commissioning", 
     "Local retail dealers and field agents earn a 12% recurring revenue share on digital QR sign-ups. Payback period drops from 6.1 months to 1.8 months.")
]
for idx, (title, sub, desc) in enumerate(v_p):
    x = 45 + idx * 210
    draw_card(c, x, 60, 200, 125, HEX_LIGHT_GRAY, HEX_RED if idx == 0 else HEX_BORDER, border_w=1.5 if idx == 0 else 1)
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(HEX_RED if idx == 0 else HEX_DARK)
    c.drawString(x + 8, 170, title)
    
    c.setFont('Helvetica-Bold', 7)
    c.setFillColor(HEX_DARK)
    c.drawString(x + 8, 157, sub)
    
    words = desc.split(' ')
    l1 = " ".join(words[:8])
    l2 = " ".join(words[8:16])
    l3 = " ".join(words[16:24])
    l4 = " ".join(words[24:])
    c.setFont('Helvetica', 6.8)
    c.drawString(x + 8, 142, l1)
    c.drawString(x + 8, 131, l2)
    c.drawString(x + 8, 120, l3)
    if l4:
        c.drawString(x + 8, 109, l4)

c.showPage()

# --- PDF PAGE 7: EXECUTION ROADMAP & CONCLUSION ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "Roadmap & Strategic Vision",
               "90-Day Execution Roadmap & Vision for India's MSMEs",
               "Structured rollout roadmap delivering enterprise-scale digital adoption across Tier 1 and Tier 2 clusters.")

phases_p = [
    ("Phase 1: Days 1–30", "Core MVP Foundation", [
        "• Deploy FastAPI modular backend",
        "• Ingest 25 SKUs & dependency rules",
        "• Index mock GSTIN & Udyam registries",
        "• Build mobile React wizard with i18n"
    ]),
    ("Phase 2: Days 31–60", "Smart KYC & Vision", [
        "• Local blur detection & auto-deskew",
        "• DPDP 30-day vault purge automation",
        "• Pass K01-K12 assertion test harness",
        "• Order state machine & milestone API"
    ]),
    ("Phase 3: Days 61–90", "Pilot & Partner Co-Pilot", [
        "• 2-city pilot (Jaipur Tier 2 & Kolkata)",
        "• Deploy Partner attribution QR console",
        "• Drop-recovery queue for field reps",
        "• Measure conversion & CAC lift"
    ])
]
for idx, (title, sub, tasks) in enumerate(phases_p):
    x = 45 + idx * 210
    draw_card(c, x, 185, 200, 140, HEX_WHITE, HEX_RED if idx == 0 else HEX_BORDER, border_w=1.5 if idx == 0 else 1)
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(HEX_RED)
    c.drawString(x + 8, 310, title)
    
    c.setFont('Helvetica-Bold', 7)
    c.setFillColor(HEX_DARK)
    c.drawString(x + 8, 297, sub)
    
    for t_idx, tk in enumerate(tasks):
        c.setFont('Helvetica', 6.8)
        c.setFillColor(HEX_DARK)
        c.drawString(x + 8, 281 - t_idx * 13, tk)

# Concluding Bottom Left Box: Strategic Vision
draw_card(c, 45, 50, 360, 125, HexColor('#181C24'), HEX_RED, border_w=1.5)
c.setFont('Helvetica-Bold', 9)
c.setFillColor(HEX_WHITE)
c.drawString(55, 160, "WHY PROJECT UDYAM DIGITAL MATTERS")

c.setFont('Helvetica', 7.2)
c.setFillColor(HexColor('#E5E7EB'))
c.drawString(55, 144, "Project Udyam Digital bridges the gap between India's enterprise telecom")
c.drawString(55, 132, "infrastructure and 6.3 crore MSMEs. By replacing physical paperwork with AI")
c.drawString(55, 120, "and multi-week delays with instant trust, we convert friction into a 10-minute reality.")

c.setFont('Helvetica-Bold', 7.2)
c.setFillColor(HEX_RED)
c.drawString(55, 98, "Key Outcomes:  [ 6.3 Cr MSMEs Empowered ]   [ 70% CAC Cut ]")
c.drawString(55, 86, "                 [ 10-Minute Onboarding ]       [ 100% DPDP Act Compliant ]")

# Concluding Bottom Right Box: Project Resources & Submission Artifacts
draw_card(c, 415, 50, 255, 125, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 7.5)
c.setFillColor(HEX_DARK)
c.drawString(425, 162, "PROJECT RESOURCES & SUBMISSION ARTIFACTS")

# GitHub QR Code & Link
if os.path.exists('submission/github_qr.png'):
    c.drawImage('submission/github_qr.png', 425, 96, width=46, height=46)

c.setFont('Helvetica-Bold', 7.5)
c.setFillColor(HEX_RED)
c.drawString(478, 132, "GitHub Repository")

c.setFont('Helvetica', 6.5)
c.setFillColor(HexColor('#6B7280'))
c.drawString(478, 121, "Explore the Source Code")

c.setFont('Helvetica-Bold', 6.2)
c.setFillColor(HEX_DARK)
c.drawString(478, 108, "github.com/lavu-create/udyam-digital")
c.linkURL('https://github.com/lavu-create/udyam-digital', (425, 96, 660, 150), relative=0)

# Demo Video Placeholder Container
draw_card(c, 425, 58, 235, 30, HEX_LIGHT_GRAY, HEX_BORDER, border_w=0.8, r=4)
c.setFont('Helvetica-Bold', 6.5)
c.setFillColor(HEX_DARK)
c.drawString(432, 75, "Demo Video (Max 3m): [ Link Pending Upload ]")

c.setFont('Helvetica-Oblique', 5.8)
c.setFillColor(HexColor('#6B7280'))
c.drawString(432, 64, "Walkthrough pitch link & QR will be added upon video upload.")

c.showPage()
c.save()

print(f"PDF successfully created at: {pdf_out}")

# Verification
pptx_prs = pptx.Presentation(pptx_out)
pdf_reader = pypdf.PdfReader(pdf_out)

print("\n--- FINAL VERIFICATION REPORT ---")
print(f"PPTX Slide Count: {len(pptx_prs.slides)} slides (Requirement: EXACTLY 7)")
print(f"PDF Page Count: {len(pdf_reader.pages)} pages (Requirement: EXACTLY 7)")
print(f"PPTX File Size: {os.path.getsize(pptx_out)/1024/1024:.2f} MB (Requirement: < 20 MB)")
print(f"PDF File Size: {os.path.getsize(pdf_out)/1024/1024:.2f} MB (Requirement: < 20 MB)")

