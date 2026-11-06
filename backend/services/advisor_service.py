from typing import List, Dict, Any, Optional

class AdvisorService:
    def __init__(self):
        self.bundles = {
            "micro": {
                "tier": "starter",
                "title": "Airtel Udyam Starter Bundle",
                "badge": "Best for Micro Retail & Standalone Shops",
                "monthly_price": 1298.0,
                "description": "High-speed optical fibre broadband with unlimited data and a business mobile connection for billing & POS payments.",
                "product_ids": ["P01", "P07"],
                "highlights": [
                    "100 Mbps Unlimited Fibre Broadband (P01)",
                    "Biz Mobile Postpaid with 30GB & Unlimited Calling (P07)",
                    "Zero Setup Fee with 12-Month Commitment",
                    "No GSTIN Required for Instant Activation"
                ]
            },
            "prof": {
                "tier": "growth",
                "title": "Airtel Udyam Growth Bundle",
                "badge": "Best for Clinics, CA Firms & Consultancies",
                "monthly_price": 2597.0,
                "description": "Ultra-reliable 300 Mbps broadband with static IP for EHR/tally hosting, AI cloud CCTV, and automated cloud backup.",
                "product_ids": ["P02", "P11", "P23", "P17"],
                "highlights": [
                    "300 Mbps Commercial Fibre Connection (P02)",
                    "Static IP for Secure Server / Camera Access (P11)",
                    "AI Cloud CCTV 1080p with 7-Day Cloud Vault (P23)",
                    "1TB Automated Offsite Cloud Backup (P17)",
                    "Priority 4-Hour Fault Restoration SLA"
                ]
            },
            "multi": {
                "tier": "pro",
                "title": "Airtel Udyam Pro Multi-Site Bundle",
                "badge": "Best for Multi-Site Chains & Manufacturing",
                "monthly_price": 6896.0,
                "description": "Gigabit enterprise fibre with zero-touch SD-WAN, unified cloud telephony, and enterprise-grade managed perimeter firewall.",
                "product_ids": ["P03", "P10", "P12", "P21"],
                "highlights": [
                    "1 Gbps Symmetrical Enterprise Fibre (P03)",
                    "Managed SD-WAN for Seamless Multi-Branch Mesh (P10)",
                    "Cloud Telephony & Smart IVR Receptionist (P12)",
                    "Managed Unified Threat Management Firewall (P21)",
                    "99.5% Uptime Guarantee with Dedicated Account Lead"
                ]
            }
        }

    def recommend(
        self,
        segment: str,
        employee_count: int = 5,
        site_count: int = 1,
        needs_cctv: bool = False,
        needs_static_ip: bool = False,
        needs_telephony: bool = False,
        needs_backup: bool = False
    ) -> Dict[str, Any]:
        target = segment.lower()
        if site_count > 1 or target in ["multi", "mfg", "manufacturing", "chain"]:
            primary_key = "multi"
            rationale = (
                f"For your multi-location operations ({site_count} sites) and team of {employee_count}, "
                "we recommend the Udyam Pro Bundle featuring 1 Gbps fibre and SD-WAN for inter-branch connectivity."
            )
        elif target in ["prof", "clinic", "dental", "consultancy", "office"] or employee_count > 5:
            primary_key = "prof"
            rationale = (
                f"For your professional practice with {employee_count} staff, the Udyam Growth Bundle "
                "delivers 300 Mbps bandwidth, dedicated Static IP, and Cloud CCTV surveillance."
            )
        else:
            primary_key = "micro"
            rationale = (
                f"For your standalone business ({employee_count} staff), the Udyam Starter Bundle "
                "provides high-speed 100 Mbps broadband with business mobile backup at the most cost-effective price."
            )

        bundles_list = [
            self.bundles[primary_key],
            self.bundles["prof"] if primary_key != "prof" else self.bundles["micro"],
            self.bundles["multi"] if primary_key != "multi" else self.bundles["prof"]
        ]

        return {
            "bundles": bundles_list,
            "rationale": rationale
        }

    def chat(self, message: str, language: str = "en", state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        msg = message.lower()
        lang = language.lower()
        context = state or {}

        # Default Hindi vs English prompt responses
        if "clinic" in msg or "doctor" in msg or "dental" in msg or "hospital" in msg or "मरीज" in msg or "क्लीनिक" in msg:
            context["segment"] = "prof"
            if lang == "hi":
                reply = (
                    "नमस्ते डॉक्टर साहब! क्लिनिक और हेल्थकेयर सेंटर्स के लिए हम एयरटेल उद्यम ग्रोथ बंडल की सिफारिश करते हैं। "
                    "इसमें 300 Mbps ब्रॉडबैंड, पेशेंट रिकॉर्ड्स के लिए स्टेटिक आईपी, और परिसर सुरक्षा के लिए क्लाउड सीसीटीवी शामिल है। "
                    "क्या आपके क्लिनिक में कितने डॉक्टर और स्टाफ सदस्य हैं?"
                )
                chips = ["1-5 कर्मचारी", "6-15 कर्मचारी", "क्लाउड सीसीटीवी चाहिए", "प्लान चुनें"]
            else:
                reply = (
                    "Welcome! For clinics and healthcare practices, we recommend the Airtel Udyam Growth Bundle. "
                    "It includes 300 Mbps Biz Fibre, Static IP for EHR/imaging hosting, and Cloud CCTV for clinic security. "
                    "How many doctors and staff work at your facility?"
                )
                chips = ["1-5 Staff", "6-15 Staff", "Need Cloud CCTV", "View Recommended Plans"]
            return {
                "reply": reply,
                "language": lang,
                "suggested_chips": chips,
                "recommended_tier": "growth",
                "recommended_product_ids": ["P02", "P11", "P23", "P17"],
                "business_context": context
            }

        elif "retail" in msg or "shop" in msg or "store" in msg or "bakery" in msg or "दुकान" in msg or "व्यापार" in msg:
            context["segment"] = "micro"
            if lang == "hi":
                reply = (
                    "नमस्ते! रिटेल स्टोर्स और दुकानों के लिए एयरटेल उद्यम स्टार्टर बंडल सबसे लोकप्रिय है। "
                    "मात्र ₹1,298/माह में आपको 100 Mbps अनलिमिटेड फाइबर और बिलिंग/POS के लिए बिजनेस मोबाइल मिलता है—बिना किसी सेटअप शुल्क के।"
                )
                chips = ["सुरक्षा कैमरा जोड़ें", "स्टेटिक आईपी चाहिए", "सीधे कोटेशन देखें", "ऑर्डर शुरू करें"]
            else:
                reply = (
                    "Hello! For retail shops and trading businesses, the Airtel Udyam Starter Bundle is our most popular choice. "
                    "At just ₹1,298/mo, you get 100 Mbps unlimited fibre plus a business postpaid SIM for POS & digital payments—zero setup fee."
                )
                chips = ["Add Security Camera", "Need Static IP", "View Instant Quote", "Start Onboarding"]
            return {
                "reply": reply,
                "language": lang,
                "suggested_chips": chips,
                "recommended_tier": "starter",
                "recommended_product_ids": ["P01", "P07"],
                "business_context": context
            }

        elif "factory" in msg or "manufacturing" in msg or "branch" in msg or "multi" in msg or "कारखाना" in msg or "ब्रांच" in msg:
            context["segment"] = "multi"
            if lang == "hi":
                reply = (
                    "नमस्ते! मल्टी-साइट और मैन्युफैक्चरिंग व्यवसायों के लिए हम एयरटेल उद्यम प्रो बंडल प्रदान करते हैं। "
                    "इसमें 1 Gbps एंटरप्राइज फाइबर, मल्टी-ब्रांच के लिए मैनेज्ड SD-WAN, स्मार्ट क्लाउड टेलीफोनी और फायरवॉल सुरक्षा शामिल है।"
                )
                chips = ["कोट कस्टमाइज़ करें", "जीएसटीआईएन वेरिफाई करें", "प्लान जोड़ें"]
            else:
                reply = (
                    "Greetings! For manufacturing units and multi-branch operations, we configure the Airtel Udyam Pro Multi-Site Bundle. "
                    "This features 1 Gbps enterprise fibre, SD-WAN interconnectivity, cloud telephony, and managed cyber-firewall."
                )
                chips = ["Customize Quote", "Verify GSTIN", "Configure Plan"]
            return {
                "reply": reply,
                "language": lang,
                "suggested_chips": chips,
                "recommended_tier": "pro",
                "recommended_product_ids": ["P03", "P10", "P12", "P21"],
                "business_context": context
            }

        else:
            # General Greeting
            if lang == "hi":
                reply = (
                    "नमस्ते! मैं आपका एयरटेल उद्यम डिजिटल सलाहकार हूँ। "
                    "मैं आपके व्यवसाय के लिए सही ब्रॉडबैंड, क्लाउड और टेलीकॉम समाधान खोजने में आपकी सहायता करूँगा। "
                    "आपका व्यवसाय किस प्रकार का है?"
                )
                chips = ["रिटेल दुकान / स्टोर", "डॉक्टर / क्लिनिक", "प्रोफेशनल ऑफिस", "फैक्ट्री / मल्टी-साइट"]
            else:
                reply = (
                    "Namaste! I am your Airtel Udyam Digital AI Advisor. "
                    "I will help you configure the perfect telecom, cloud and security bundle for your business in minutes. "
                    "What type of business do you run?"
                )
                chips = ["Retail Shop / Store", "Doctor / Clinic", "Professional Office", "Factory / Multi-Branch"]

            return {
                "reply": reply,
                "language": lang,
                "suggested_chips": chips,
                "recommended_tier": "starter",
                "recommended_product_ids": ["P01", "P07"],
                "business_context": context
            }

advisor_service = AdvisorService()

