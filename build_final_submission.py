import os
import sys

# Optional local library fallback
libs_path = os.path.abspath('./python_libs')
if os.path.exists(libs_path) and libs_path not in sys.path:
    sys.path.insert(0, libs_path)

import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
import pypdf
import qrcode

os.makedirs('submission', exist_ok=True)

pptx_out = 'submission/Project_Udyam_Digital_FINAL.pptx'
pdf_out = 'submission/Project_Udyam_Digital_FINAL.pdf'

# Brand Colors (Airtel SYNC Guidelines)
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

# Verified URLs
URL_LIVE_APP = "https://udyam-digital-rho.vercel.app"
URL_GITHUB = "https://github.com/lavu-create/udyam-digital"
URL_DEMO_VIDEO = "https://drive.google.com/file/d/1fxyMlvrPGGqDVeVV4CQsYVr7FWekat4_/view?usp=sharing"

# Generate High-Resolution QR Codes
qr_specs = [
    ("submission/qr_live_app.png", URL_LIVE_APP),
    ("submission/qr_github.png", URL_GITHUB),
    ("submission/qr_demo_video.png", URL_DEMO_VIDEO),
]

for qr_file, url_val in qr_specs:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url_val)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_file)
    print(f"Verified QR saved: {qr_file} -> {url_val}")

print("\nStarting generation of official 7-slide final submission deck...")

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
p.text = "Product Vision: Connecting MSMEs in a Single Sitting (~10 Minutes)"
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
jp0.text = "THE SINGLE-SITTING ONBOARDING JOURNEY (PRODUCT VISION):"
jp0.font.name = 'Arial'
jp0.font.size = Pt(9.5)
jp0.font.bold = True
jp0.font.color.rgb = WHITE
jp0.space_after = Pt(4)

steps = [
    "1. Rule-Grounded AI Advisor -> Vernacular needs discovery (Hindi & English)",
    "2. Right-Fit Bundling       -> Broadband, SIMs, Cloud & CCTV in one bill",
    "3. Instant Smart KYC        -> Sub-second GSTIN lookup with local vision QA",
    "4. Provisioning Tracker     -> 5-stage milestone simulation (demonstration model)"
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
cp.text = "Empowering 6.3 Crore MSMEs | Addressing 17.6-day sales cycle via digital self-serve | Unstop Partner"
cp.font.name = 'Arial'
cp.font.size = Pt(7.8)
cp.font.color.rgb = GRAY

# ----------------- SLIDE 2: PROBLEM & DATA OPPORTUNITY (PPTX) -----------------
add_header(slide2, "The MSME Acquisition Bottleneck", 
           "Current MSME Acquisition: High Friction, Low Conversion", 
           "Forensic analysis of 5,000 SMB leads reveals a broken sales cycle where 92.6% of interested leads drop out.")

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
           "Replacing multi-week sales cycles with an intelligent, self-service single-sitting onboarding journey.")

pillars = [
    ("1. Rule-Grounded AI Advisor", 
     "Vernacular Needs Discovery",
     ["• Discovers needs in plain Hindi & English",
      "• Translates shopkeeper needs into tech",
      "• Recommends tailored 3-tier bundles",
      "• Deterministic rule engine matching needs"]),
    ("2. Dynamic Bundle Engine", 
     "Transparent Pricing & Rules",
     ["• Powers 25 enterprise SKUs from catalogue",
      "• Enforces strict dependency graph rules",
      "• Validates GSTIN requirement across 10 SKUs",
      "• Single consolidated monthly bill + setup"]),
    ("3. Instant Smart KYC", 
     "Local Vision Pre-Checks",
     ["• Instant mock GSTIN & Udyam API lookup",
      "• Laplacian blur variance filter (K04)",
      "• Freshness validation (<90 days case rule)",
      "• DPDP 2023 affirmative consent & in-memory QA"]),
    ("4. Post-Order Tracker", 
     "Proactive Milestone SLA",
     ["• 5-stage provisioning state machine simulation",
      "• Simulated technician assignment & slot",
      "• Automated WhatsApp milestone simulation",
      "• Proactive transparency on 3.01 chase calls"])
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
    ("1. Conversational AI Advisor", "WhatsApp-style bilingual chat: 'Namaste! How many staff work at your clinic?' Quick suggestion chips for zero typing."),
    ("2. Recommended Bundles", "3 transparent cards (Starter Rs. 1,298, Growth Rs. 2,597, Pro Rs. 6,896) with plain-language business rationales."),
    ("3. Modular Quote Builder", "Interactive toggles for add-ons: Cloud CCTV (+Rs. 249), Static IP (+Rs. 200). Live total updates; zero hidden clauses."),
    ("4. Instant Registry Check", "GSTIN & Udyam entry triggers sub-second lookup; displays green 'Active' badge and auto-fills business details."),
    ("5. Smart KYC Image Quality", "Auto-checks orientation (K02); intercepts blurry docs via Laplacian filter (K04) and expired bills (K11 >90-day case rule)."),
    ("6. Provisioning Tracker", "5-stage visual progress timeline simulation with demonstration technician assignment and appointment slot.")
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
           "Decoupled FastAPI backend, local vision image-quality pre-checks, and DPDP Act 2023 technical alignment.")

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
    ("Core Service Modules:", "Advisor Adapter (deterministic rule mapping), Catalog Engine (25 SKUs), Smart KYC Orchestrator, Order State Machine Simulation"),
    ("Offline Registry Engines:", "Indexed Mock GSTIN (3,534 records), Mock Udyam (2,723 records), Local Computer Vision Pre-Checks (Laplacian blur variance + aspect QA)"),
    ("Persistence & Privacy:", "SQLite (Local MVP) / PostgreSQL (Cloud), Ephemeral in-memory document processing, ISO 8601 UTC audit logging")
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
tp0.text = "DPDP ACT, 2023 PRIVACY ALIGNMENT CONTROLS"
tp0.font.name = 'Arial'
tp0.font.size = Pt(9.5)
tp0.font.bold = True
tp0.font.color.rgb = DARK
tp0.space_after = Pt(4)

dpdp_points = [
    ("Affirmative Consent (Sec 6):", "Unbundled, explicit checkboxes in Hindi & English; immutable consent timestamp and SHA-256 IP hash logging."),
    ("Purpose Limitation (Sec 5):", "KYC data processed strictly for statutory telecom provisioning; zero secondary commercial monetization."),
    ("Data Minimisation (Sec 6(1)):", "No GSTIN required for retail broadband; only minimum statutory ID and supply address captured."),
    ("No External AI Forwarding:", "Documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs."),
    ("Storage Limitation (Sec 8):", "Ephemeral in-memory verification model without persistent storage of unnecessary sensitive document images."),
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
           "Targeting customer acquisition cost optimization while accelerating self-serve conversion and recurring ARPU.")

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
    ("Funnel Conversion Rate:", "7.36% (368 / 5,000 leads)", "18.5% – 22.0% (Projected)", "Removes visit scheduling friction & 5-day quote wait"),
    ("Blended CAC per Activated SMB:", "Rs. 15,053 per activation", "Rs. 4,200 – Rs. 4,500 (Target)", "Shifts from feet-on-street to zero-touch digital self-serve"),
    ("Average Activation Velocity:", "17.62 Days (Median: 17d)", "2.5 – 3.5 Days (Target)", "Sub-second digital KYC pass-through & instant scheduling"),
    ("Status Chasing Inbound Calls:", "3.01 Calls per customer", "< 0.5 Calls (Target)", "Live visual milestone tracker & automated WhatsApp updates"),
    ("6-Month Customer Churn:", "15.22% (56 / 368 churned)", "< 7.5% (Projected)", "Needs-based right-fit recommendation vs sales quota pitching")
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

# ----------------- SLIDE 7: EXECUTION ROADMAP & RESOURCES (PPTX) -----------------
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
        "• Local blur detection (Laplacian QA)",
        "• In-memory ephemeral verification",
        "• Pass K01-K12 synthetic test harness",
        "• Order state machine simulation API"
    ]),
    ("Phase 3: Days 61–90", "Pilot & Partner Co-Pilot", [
        "• 2-city pilot (Jaipur Tier 2 & Kolkata)",
        "• Deploy Partner attribution QR console",
        "• Drop-recovery queue for field reps",
        "• Measure self-serve adoption & lift"
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

# Bottom Left Box: Strategic Vision (Width: 4.2 Inches)
c_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(3.2), Inches(4.2), Inches(1.85))
c_box.fill.solid()
c_box.fill.fore_color.rgb = RGBColor(24, 28, 36)
c_box.line.color.rgb = RED
c_box.line.width = Pt(1.5)

c_tb = slide7.shapes.add_textbox(Inches(0.72), Inches(3.28), Inches(3.96), Inches(1.7))
c_tf = c_tb.text_frame
c_tf.word_wrap = True

cp0 = c_tf.paragraphs[0]
cp0.text = "WHY PROJECT UDYAM DIGITAL MATTERS"
cp0.font.name = 'Arial'
cp0.font.size = Pt(9.5)
cp0.font.bold = True
cp0.font.color.rgb = WHITE
cp0.space_after = Pt(3)

cp1 = c_tf.add_paragraph()
cp1.text = "Project Udyam Digital bridges enterprise telecom and 6.3 crore MSMEs. By replacing paper friction with conversational discovery and multi-week delays with instant digital trust, we convert high-friction acquisition into a single-sitting reality."
cp1.font.name = 'Arial'
cp1.font.size = Pt(7.8)
cp1.font.color.rgb = RGBColor(229, 231, 235)
cp1.space_after = Pt(4)

cp2 = c_tf.add_paragraph()
cp2.text = "Key Outcomes:  [ 6.3 Cr MSMEs Empowered ]   [ Product Vision: ~10-Min Onboarding ]\n                [ Rule-Grounded Needs Mapping ]   [ DPDP Act 2023 Technical Alignment ]"
cp2.font.name = 'Arial'
cp2.font.size = Pt(7.2)
cp2.font.bold = True
cp2.font.color.rgb = RED

# Bottom Right Box: PROJECT RESOURCES (Width: 4.5 Inches)
res_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.95), Inches(3.2), Inches(4.45), Inches(1.85))
res_box.fill.solid()
res_box.fill.fore_color.rgb = WHITE
res_box.line.color.rgb = BORDER
res_box.line.width = Pt(1)

# Section Header
rtb = slide7.shapes.add_textbox(Inches(5.05), Inches(3.24), Inches(4.25), Inches(0.35))
rtf = rtb.text_frame
rtf.word_wrap = True
rtf.margin_left = rtf.margin_top = rtf.margin_right = rtf.margin_bottom = 0

rp0 = rtf.paragraphs[0]
rp0.text = "PROJECT RESOURCES"
rp0.font.name = 'Arial'
rp0.font.size = Pt(9.0)
rp0.font.bold = True
rp0.font.color.rgb = RED

rp1 = rtf.add_paragraph()
rp1.text = "Scan QR code or click resource label to access live assets."
rp1.font.name = 'Arial'
rp1.font.size = Pt(6.8)
rp1.font.color.rgb = GRAY

# 3 Column Resource Cards
resources_data = [
    {
        "title": "LIVE APPLICATION",
        "label": "Explore the Live Prototype",
        "url": URL_LIVE_APP,
        "qr": "submission/qr_live_app.png",
        "x": Inches(5.05)
    },
    {
        "title": "SOURCE CODE",
        "label": "Explore the GitHub Repository",
        "url": URL_GITHUB,
        "qr": "submission/qr_github.png",
        "x": Inches(6.50)
    },
    {
        "title": "PRODUCT DEMO",
        "label": "Watch the 3-Minute Product Demo",
        "url": URL_DEMO_VIDEO,
        "qr": "submission/qr_demo_video.png",
        "x": Inches(7.95)
    }
]

col_w = Inches(1.35)
card_h = Inches(1.38)
card_y = Inches(3.60)

for res in resources_data:
    x_pos = res["x"]
    
    # Outer Card for Column
    col_card = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_pos, card_y, col_w, card_h)
    col_card.fill.solid()
    col_card.fill.fore_color.rgb = LIGHT_GRAY
    col_card.line.color.rgb = BORDER
    col_card.line.width = Pt(0.75)
    
    # Header inside card
    thb = slide7.shapes.add_textbox(x_pos, card_y + Inches(0.04), col_w, Inches(0.18))
    thf = thb.text_frame
    thf.word_wrap = True
    thf.margin_left = thf.margin_top = thf.margin_right = thf.margin_bottom = 0
    tp = thf.paragraphs[0]
    tp.alignment = PP_ALIGN.CENTER
    tp.text = res["title"]
    tp.font.name = 'Arial'
    tp.font.size = Pt(6.5)
    tp.font.bold = True
    tp.font.color.rgb = DARK
    
    # QR Code image (0.68" x 0.68")
    qr_size = Inches(0.68)
    qr_x = x_pos + (col_w - qr_size) / 2
    qr_y = card_y + Inches(0.22)
    if os.path.exists(res["qr"]):
        slide7.shapes.add_picture(res["qr"], qr_x, qr_y, width=qr_size, height=qr_size)
    
    # Clickable Label with Hyperlink
    tlb = slide7.shapes.add_textbox(x_pos + Inches(0.04), card_y + Inches(0.92), col_w - Inches(0.08), Inches(0.42))
    tlf = tlb.text_frame
    tlf.word_wrap = True
    tlf.margin_left = tlf.margin_top = tlf.margin_right = tlf.margin_bottom = 0
    lp = tlf.paragraphs[0]
    lp.alignment = PP_ALIGN.CENTER
    
    run = lp.add_run()
    run.text = res["label"]
    run.font.name = 'Arial'
    run.font.size = Pt(6.2)
    run.font.bold = True
    run.font.underline = True
    run.font.color.rgb = RED
    run.hyperlink.address = res["url"]

prs.save(pptx_out)
print(f"PPTX successfully created at: {pptx_out}")


# -------------------------------------------------------------
# PART 2: GENERATE REPORTLAB PDF WITH IDENTICAL ARTWORK & HYPERLINKS
# -------------------------------------------------------------
c = canvas.Canvas(pdf_out, pagesize=(720, 405)) # 16:9 widescreen @ 72 dpi (10" x 5.625")

def draw_card(c, x, y, w, h, fill_col, border_col, border_w=1, r=6):
    c.saveState()
    c.setFillColor(fill_col)
    c.setStrokeColor(border_col)
    c.setLineWidth(border_w)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1)
    c.restoreState()

def draw_header_pdf(c, tag, title, subtitle):
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_RED)
    c.drawString(95, 375, tag.upper())
    
    c.setFont('Helvetica-Bold', 15)
    c.setFillColor(HEX_DARK)
    c.drawString(95, 356, title)
    
    c.setFont('Helvetica', 8.5)
    c.setFillColor(HEX_GRAY)
    c.drawString(95, 342, subtitle)

# --- PDF PAGE 1: TITLE SLIDE ---
c.drawImage('extracted/pptx_media/ppt/media/image2.jpg', 0, 0, width=720, height=405)

c.setFont('Helvetica-Bold', 7.5)
c.setFillColor(HEX_RED)
c.drawString(130, 365, "AIRTEL SYNC 2026 · DIGITAL TRACK (ENTERPRISE TRACK A)")

c.setFont('Helvetica-Bold', 26)
c.setFillColor(HEX_WHITE)
c.drawString(130, 332, "Project Udyam Digital")

c.setFont('Helvetica-Bold', 12)
c.setFillColor(HexColor('#E5E7EB'))
c.drawString(130, 312, "India's MSME Connectivity Journey, Simplified.")

c.setFont('Helvetica-Bold', 8)
c.setFillColor(HEX_RED)
c.drawString(130, 296, "Product Vision: Connecting MSMEs in a Single Sitting (~10 Minutes)")

# Journey Box
draw_card(c, 45, 55, 340, 135, HexColor('#141821'), HEX_RED, border_w=1.5, r=6)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_WHITE)
c.drawString(55, 172, "THE SINGLE-SITTING ONBOARDING JOURNEY (PRODUCT VISION):")

pdf_steps = [
    "1. Rule-Grounded AI Advisor -> Vernacular needs discovery (Hindi & English)",
    "2. Right-Fit Bundling       -> Broadband, SIMs, Cloud & CCTV in one bill",
    "3. Instant Smart KYC        -> Sub-second GSTIN lookup with local vision QA",
    "4. Provisioning Tracker     -> 5-stage milestone progression simulation"
]
for idx, st in enumerate(pdf_steps):
    c.setFont('Helvetica', 7.5)
    c.setFillColor(HexColor('#D1D5DB'))
    c.drawString(55, 150 - idx * 16, st)

c.setFont('Helvetica', 6.8)
c.setFillColor(HexColor('#9CA3AF'))
c.drawString(45, 38, "Empowering 6.3 Crore MSMEs | Addressing 17.6-day sales cycle via digital self-serve | Unstop Partner")

c.showPage()

# --- PDF PAGE 2: PROBLEM & DATA OPPORTUNITY ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "The MSME Acquisition Bottleneck", 
               "Current MSME Acquisition: High Friction, Low Conversion", 
               "Forensic analysis of 5,000 SMB leads reveals a broken sales cycle where 92.6% of interested leads drop out.")

# 3 Top KPI Cards
kpis_pdf = [
    ("7.36% ACTIVATION RATE", "Only 368 of 5,000 leads activate", HEX_RED),
    ("Rs. 15,053 BLENDED CAC", "Rs. 5.54M total sales spend across cohort", HEX_DARK),
    ("17.62 DAYS VELOCITY", "Average 3.01 customer status chase calls", HEX_AMBER)
]
for idx, (title, sub, col) in enumerate(kpis_pdf):
    x = 45 + idx * 210
    draw_card(c, x, 275, 200, 50, HEX_LIGHT_GRAY, col, border_w=1.5)
    c.setFont('Helvetica-Bold', 9.5)
    c.setFillColor(col)
    c.drawString(x + 8, 305, title)
    
    c.setFont('Helvetica', 7.5)
    c.setFillColor(HEX_DARK)
    c.drawString(x + 8, 290, sub)

# Left Box: Funnel Progression
draw_card(c, 45, 55, 305, 210, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(55, 248, "ACTUAL MSME FUNNEL PROGRESSION (5,000 LEADS)")

for idx, (stage, cnt, pct) in enumerate(funnel_rows):
    y_pos = 228 - idx * 20
    c.setFont('Helvetica', 7.2)
    c.setFillColor(HEX_RED if "STEEPEST" in pct else HEX_DARK)
    c.drawString(55, y_pos, f"{stage:<20} {cnt:>6}   |  {pct}")

c.setFont('Helvetica', 6.2)
c.setFillColor(HexColor('#6B7280'))
c.drawString(55, 95, "* Steepest drop occurs from Needs Assessed to Quote Accepted (56.4% drop)")
c.drawString(55, 85, "  due to 5-day quote delays & telco jargon.")

# Right Box: Drop Reasons
draw_card(c, 360, 55, 315, 210, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(370, 248, "ROOT-CAUSE OF 4,632 DROPPED LEADS")

for idx, (cat, desc) in enumerate(reasons):
    y_pos = 228 - idx * 34
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_RED)
    c.drawString(370, y_pos, cat)
    
    c.setFont('Helvetica', 6.8)
    c.setFillColor(HEX_DARK)
    c.drawString(370, y_pos - 12, desc)

c.setFont('Helvetica-Bold', 6.8)
c.setFillColor(HEX_GREEN)
c.drawString(370, 80, "KEY TAKEAWAY: 48.8% of drops (2,264 leads) stem purely from")
c.drawString(370, 70, "manual sales scheduling and documentation friction.")

c.showPage()

# --- PDF PAGE 3: OUR SOLUTION ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "Core Product Architecture",
               "Project Udyam Digital: Architecture of Frictionless Acquisition",
               "Replacing multi-week sales cycles with an intelligent, self-service single-sitting onboarding journey.")

pillars_p = [
    ("1. Rule-Grounded Advisor", "Vernacular Discovery", [
        "• Needs in plain Hindi/English",
        "• Translates shop needs to tech",
        "• 3-tier tailored bundles",
        "• Deterministic rule mapping"
    ]),
    ("2. Dynamic Bundle Engine", "Transparent Rules", [
        "• 25 enterprise SKUs",
        "• Dependency graph rules",
        "• GSTIN checks on 10 SKUs",
        "• Single consolidated bill"
    ]),
    ("3. Instant Smart KYC", "Local Vision QA", [
        "• Mock GSTIN/Udyam lookup",
        "• Laplacian blur filter (K04)",
        "• Freshness check (<90d rule)",
        "• Ephemeral in-memory QA"
    ]),
    ("4. Post-Order Tracker", "Milestone SLA", [
        "• 5-stage simulation",
        "• Simulated technician slot",
        "• Automated WhatsApp webhooks",
        "• Transparent 3.01 chase calls"
    ])
]

for idx, (p_title, p_sub, p_pts) in enumerate(pillars_p):
    x = 45 + idx * 158
    draw_card(c, x, 135, 150, 190, HEX_WHITE, HEX_RED if idx == 0 else HEX_BORDER, border_w=1.5 if idx == 0 else 1)
    c.setFont('Helvetica-Bold', 8.5)
    c.setFillColor(HEX_RED)
    c.drawString(x + 6, 310, p_title)
    
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_DARK)
    c.drawString(x + 6, 296, p_sub)
    
    for pt_i, pt in enumerate(p_pts):
        c.setFont('Helvetica', 6.8)
        c.setFillColor(HEX_DARK)
        c.drawString(x + 6, 276 - pt_i * 15, pt)

# Bottom Partner Synergy Box
draw_card(c, 45, 55, 630, 68, HEX_LIGHT_GRAY, HEX_DARK, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_RED)
c.drawString(55, 107, "O2O CHANNEL PARTNER & FIELD FORCE SYNERGY (ASSISTED DIGITAL MODEL)")

c.setFont('Helvetica', 7.2)
c.setFillColor(HEX_DARK)
c.drawString(55, 92, "Instead of competing with local retail dealers and field agents, Project Udyam Digital equips them with digital attribution")
c.drawString(55, 80, "QR codes and drop-recovery queues. Partners earn full recurring commissions while offloading manual paperwork overhead.")

c.showPage()

# --- PDF PAGE 4: PRODUCT EXPERIENCE ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "User Experience & Prototype Design",
               "Intuitive, Mobile-First Prototype Experience",
               "Proposed prototype screen designs engineered for 375px mobile viewports with bilingual Hindi/English support.")

for idx, (title, desc) in enumerate(screens):
    r = idx // 3
    col = idx % 3
    x = 45 + col * 210
    y = 190 - r * 130
    draw_card(c, x, y, 200, 120, HEX_WHITE, HEX_RED if idx == 0 else HEX_BORDER, border_w=1.5 if idx == 0 else 1)
    
    c.setFont('Helvetica-Bold', 8.5)
    c.setFillColor(HEX_RED if idx == 0 else HEX_DARK)
    c.drawString(x + 8, y + 104, title)
    
    c.setFont('Helvetica', 7.0)
    c.setFillColor(HEX_DARK)
    
    words = desc.split()
    line1, line2, line3, line4 = "", "", "", ""
    for w in words:
        if len(line1 + w) < 36 and not line2:
            line1 += w + " "
        elif len(line2 + w) < 36 and not line3:
            line2 += w + " "
        elif len(line3 + w) < 36 and not line4:
            line3 += w + " "
        else:
            line4 += w + " "
    c.drawString(x + 8, y + 84, line1.strip())
    c.drawString(x + 8, y + 71, line2.strip())
    if line3: c.drawString(x + 8, y + 58, line3.strip())
    if line4: c.drawString(x + 8, y + 45, line4.strip())

c.setFont('Helvetica-Oblique', 6.8)
c.setFillColor(HexColor('#6B7280'))
c.drawString(45, 45, "* Proposed prototype interface specifications. Designed for zero-training adoption by non-technical Indian proprietors.")

c.showPage()

# --- PDF PAGE 5: TECHNICAL ARCHITECTURE & TRUST ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "System Architecture & Privacy",
               "Modular Monolith Architecture with Privacy-by-Design",
               "Decoupled FastAPI backend, local vision image-quality pre-checks, and DPDP Act 2023 technical alignment.")

# Left Tech Box
draw_card(c, 45, 50, 305, 275, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(55, 310, "SYSTEM COMPONENT TOPOLOGY")

for idx, (layer, desc) in enumerate(arch_layers):
    y_pos = 290 - idx * 46
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_RED)
    c.drawString(55, y_pos, layer)
    
    c.setFont('Helvetica', 6.8)
    c.setFillColor(HEX_DARK)
    words = desc.split()
    l1, l2 = "", ""
    for w in words:
        if len(l1 + w) < 42 and not l2:
            l1 += w + " "
        else:
            l2 += w + " "
    c.drawString(55, y_pos - 12, l1.strip())
    if l2: c.drawString(55, y_pos - 24, l2.strip())

# Right Trust Box
draw_card(c, 360, 50, 315, 275, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(370, 310, "DPDP ACT, 2023 PRIVACY ALIGNMENT CONTROLS")

for idx, (title, desc) in enumerate(dpdp_points):
    y_pos = 290 - idx * 39
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_GREEN)
    c.drawString(370, y_pos, title)
    
    c.setFont('Helvetica', 6.8)
    c.setFillColor(HEX_DARK)
    words = desc.split()
    l1, l2 = "", ""
    for w in words:
        if len(l1 + w) < 44 and not l2:
            l1 += w + " "
        else:
            l2 += w + " "
    c.drawString(370, y_pos - 12, l1.strip())
    if l2: c.drawString(370, y_pos - 24, l2.strip())

c.showPage()

# --- PDF PAGE 6: UNIT ECONOMICS & VALUE CREATION ---
c.drawImage('extracted/pptx_media/ppt/media/image1.jpg', 0, 0, width=720, height=405)
draw_header_pdf(c, "Unit Economics & Value Creation",
               "Sustainable Unit Economics & Quantified Business Impact",
               "Targeting customer acquisition cost optimization while accelerating self-serve conversion and recurring ARPU.")

# Matrix Box
draw_card(c, 45, 185, 630, 140, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_DARK)
c.drawString(55, 310, "BASELINE FUNNEL (ACTUAL DATASET) VS. PROJECT UDYAM DIGITAL TARGETS")

for idx, (metric, base, tgt, lever) in enumerate(matrix):
    y_pos = 290 - idx * 22
    c.setFont('Helvetica', 6.8)
    c.setFillColor(HEX_DARK)
    c.drawString(55, y_pos, f"{metric:<26} | Base: {base:<22} -> Target: {tgt:<24} | {lever}")

# Bottom 3 Value Pillars
for idx, (title, sub, desc) in enumerate(v_pillars):
    x = 45 + idx * 210
    draw_card(c, x, 50, 200, 125, HEX_LIGHT_GRAY, HEX_RED if idx == 0 else HEX_BORDER, border_w=1.5 if idx == 0 else 1)
    
    c.setFont('Helvetica-Bold', 8.5)
    c.setFillColor(HEX_RED if idx == 0 else HEX_DARK)
    c.drawString(x + 8, 160, title)
    
    c.setFont('Helvetica-Bold', 7.5)
    c.setFillColor(HEX_DARK)
    c.drawString(x + 8, 147, sub)
    
    c.setFont('Helvetica', 6.8)
    c.setFillColor(HEX_DARK)
    words = desc.split()
    l1, l2, l3, l4 = "", "", "", ""
    for w in words:
        if len(l1 + w) < 35 and not l2:
            l1 += w + " "
        elif len(l2 + w) < 35 and not l3:
            l2 += w + " "
        elif len(l3 + w) < 35 and not l4:
            l3 += w + " "
        else:
            l4 += w + " "
    c.drawString(x + 8, 131, l1.strip())
    c.drawString(x + 8, 118, l2.strip())
    if l3: c.drawString(x + 8, 105, l3.strip())
    if l4: c.drawString(x + 8, 92, l4.strip())

c.showPage()

# --- PDF PAGE 7: EXECUTION ROADMAP & RESOURCES ---
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
        "• Local blur detection (Laplacian QA)",
        "• In-memory ephemeral verification",
        "• Pass K01-K12 synthetic test harness",
        "• Order state machine simulation API"
    ]),
    ("Phase 3: Days 61–90", "Pilot & Partner Co-Pilot", [
        "• 2-city pilot (Jaipur Tier 2 & Kolkata)",
        "• Deploy Partner attribution QR console",
        "• Drop-recovery queue for field reps",
        "• Measure self-serve adoption & lift"
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

# Concluding Bottom Left Box: Strategic Vision (Width: 300)
draw_card(c, 45, 50, 300, 125, HexColor('#181C24'), HEX_RED, border_w=1.5)
c.setFont('Helvetica-Bold', 8.5)
c.setFillColor(HEX_WHITE)
c.drawString(55, 160, "WHY PROJECT UDYAM DIGITAL MATTERS")

c.setFont('Helvetica', 6.8)
c.setFillColor(HexColor('#E5E7EB'))
c.drawString(55, 144, "Project Udyam Digital bridges enterprise telecom and 6.3 crore MSMEs.")
c.drawString(55, 132, "By replacing paper friction with conversational discovery and multi-week delays")
c.drawString(55, 120, "with instant digital trust, we convert acquisition into a single-sitting reality.")

c.setFont('Helvetica-Bold', 6.5)
c.setFillColor(HEX_RED)
c.drawString(55, 96, "Key Outcomes:  [ 6.3 Cr MSMEs Empowered ]")
c.drawString(55, 84, "                 [ Product Vision: ~10-Min Onboarding ]")
c.drawString(55, 72, "                 [ Rule-Grounded Needs Mapping ]")
c.drawString(55, 60, "                 [ DPDP Act 2023 Technical Alignment ]")

# Concluding Bottom Right Box: PROJECT RESOURCES (Width: 320)
draw_card(c, 355, 50, 320, 125, HEX_WHITE, HEX_BORDER, border_w=1)
c.setFont('Helvetica-Bold', 8.0)
c.setFillColor(HEX_RED)
c.drawString(365, 162, "PROJECT RESOURCES")

c.setFont('Helvetica', 6.2)
c.setFillColor(HexColor('#6B7280'))
c.drawString(365, 151, "Scan QR code or click resource label to access live assets.")

# 3 Column Resource Cards in PDF
pdf_res_data = [
    {
        "title": "LIVE APPLICATION",
        "label": "Explore the Live Prototype",
        "url": URL_LIVE_APP,
        "qr": "submission/qr_live_app.png",
        "x": 365
    },
    {
        "title": "SOURCE CODE",
        "label": "Explore the GitHub Repository",
        "url": URL_GITHUB,
        "qr": "submission/qr_github.png",
        "x": 467
    },
    {
        "title": "PRODUCT DEMO",
        "label": "Watch the 3-Minute Product Demo",
        "url": URL_DEMO_VIDEO,
        "qr": "submission/qr_demo_video.png",
        "x": 569
    }
]

res_card_w = 96
res_card_h = 92
res_card_y = 55

for r_info in pdf_res_data:
    rx = r_info["x"]
    draw_card(c, rx, res_card_y, res_card_w, res_card_h, HEX_LIGHT_GRAY, HEX_BORDER, border_w=0.75, r=4)
    
    # Header inside card
    c.setFont('Helvetica-Bold', 5.5)
    c.setFillColor(HEX_DARK)
    c.drawCentredString(rx + res_card_w/2.0, res_card_y + 81, r_info["title"])
    
    # QR Code image (46 x 46)
    q_size = 46
    qx = rx + (res_card_w - q_size) / 2.0
    qy = res_card_y + 32
    if os.path.exists(r_info["qr"]):
        c.drawImage(r_info["qr"], qx, qy, width=q_size, height=q_size)
    
    # Clickable Label with Hyperlink
    c.setFont('Helvetica-Bold', 5.2)
    c.setFillColor(HEX_RED)
    
    # Split label into 2 lines for crisp centering
    words = r_info["label"].split()
    mid = len(words) // 2
    l1 = " ".join(words[:mid])
    l2 = " ".join(words[mid:])
    c.drawCentredString(rx + res_card_w/2.0, res_card_y + 19, l1)
    c.drawCentredString(rx + res_card_w/2.0, res_card_y + 10, l2)
    
    # Register active PDF clickable hyperlink covering the entire card
    c.linkURL(r_info["url"], (rx, res_card_y, rx + res_card_w, res_card_y + res_card_h), relative=0)

c.showPage()
c.save()

print(f"PDF successfully created at: {pdf_out}")

# Verification Check
pptx_prs = pptx.Presentation(pptx_out)
pdf_reader = pypdf.PdfReader(pdf_out)

print("\n--- FINAL VERIFICATION REPORT ---")
print(f"PPTX Slide Count: {len(pptx_prs.slides)} slides (Requirement: EXACTLY 7)")
print(f"PDF Page Count: {len(pdf_reader.pages)} pages (Requirement: EXACTLY 7)")
print(f"PPTX File Size: {os.path.getsize(pptx_out)/1024/1024:.2f} MB (Requirement: < 20 MB)")
print(f"PDF File Size: {os.path.getsize(pdf_out)/1024/1024:.2f} MB (Requirement: < 20 MB)")
