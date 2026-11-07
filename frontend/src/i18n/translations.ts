export type Language = 'en' | 'hi';

export const translations = {
  en: {
    appTitle: "Airtel Udyam Digital",
    appSubtitle: "India's MSME Connectivity Journey, Simplified",
    step: "Step",
    next: "Continue",
    back: "Back",
    startJourney: "Start 10-Minute Onboarding",
    heroHeading: "Get Your Business Connected in One Sitting",
    heroDesc: "AI-powered recommendations, transparent monthly pricing, sub-second digital KYC, and real-time installation tracking for 6.3 crore Indian small enterprises.",
    benefits: [
      { title: "No Paperwork", desc: "Instant digital KYC via GSTIN & Udyam" },
      { title: "Transparent Pricing", desc: "Consolidated bills with zero hidden setup traps" },
      { title: "Rapid Installation", desc: "Dedicated technician dispatched within 72 hours" }
    ],
    // Profile
    profileHeading: "Tell us about your business",
    profileSub: "We'll tailor telecom, cloud, and security solutions specifically for your operations.",
    bizName: "Business / Enterprise Name",
    bizSegment: "Primary Business Activity",
    segments: {
      micro: "Retail Shop / Trading / Micro Business",
      prof: "Healthcare Clinic / CA Firm / Consultancy",
      multi: "Multi-Branch Enterprise / Chain Store",
      mfg: "Manufacturing Plant / Factory"
    },
    employeeCount: "Staff & Employee Count",
    siteCount: "Number of Operating Locations / Sites",
    city: "City / Location",
    tier: "City Tier",
    // Advisor
    advisorTitle: "Airtel AI Business Advisor",
    advisorSub: "Conversational needs assessment grounded in real enterprise connectivity packages.",
    advisorPlaceholder: "Type your needs (e.g., 'I run a dental clinic with 8 staff')...",
    send: "Send",
    chipsTitle: "Quick Recommendations:",
    // Bundles
    recommendedTitle: "Tailored Udyam Connectivity Bundles",
    recommendedSub: "Curated packages calculated with transparent monthly rates and zero setup fees.",
    selectBundle: "Select This Bundle",
    customizeInQuote: "Customize in Quote Builder",
    perMonth: "/ month",
    zeroSetup: "Zero Setup Fee (Annual)",
    // Quote
    quoteTitle: "Interactive Quote Builder",
    quoteSub: "Add or remove modular cloud add-ons. Dependencies & GSTIN requirements are validated live.",
    monthlyTotal: "Consolidated Monthly Total",
    setupTotal: "One-Time Setup Fee",
    activeGSTRequired: "Active GSTIN Required for selected SKUs",
    proceedCheckout: "Proceed to Instant Checkout",
    // Checkout & KYC
    checkoutTitle: "Digital KYC & Verification",
    checkoutSub: "Sub-second verification against national registries with zero physical documents.",
    gstinLabel: "GSTIN Number (Optional for basic broadband)",
    udyamLabel: "Udyam Registration Number",
    verifyRegistry: "Verify Registry Status",
    docUploadTitle: "Upload Supporting Proofs",
    docUploadDesc: "Upload certificate images or test with pre-loaded case scenarios (K01–K12).",
    selectLeadPreset: "Select Test Specimen (K01–K12):",
    runVerification: "Run Smart KYC Validation",
    // Result
    kycPassed: "Digital KYC Successfully Verified",
    kycReview: "Manual Review Required by Exception Desk",
    kycRejected: "Document Rejected — Action Required",
    // Consent
    consentTitle: "DPDP Act, 2023 Statutory Consent",
    consentNotice: "In accordance with Section 6 of India's Digital Personal Data Protection Act, 2023, your personal and business data is processed solely for statutory telecom provisioning. Documents are processed in memory by the hosted backend and are not forwarded to external third-party AI APIs. Production deployment requires further security and retention assessment.",
    consentCheck1: "I authorize Airtel to verify registration details with GSTIN and Udyam databases.",
    consentCheck2: "I agree to premises verification for optical fiber installation.",
    confirmOrder: "Accept & Place Order",
    // Tracker
    orderSuccess: "Order Confirmed & Provisioning Initiated",
    orderId: "Order ID",
    technicianTitle: "Assigned Lead Technician [Simulated Demo]",
    technicianCall: "Simulate Call",
    estimatedInstall: "Scheduled Optical Drop [Simulated SLA: 72h]",
    liveTimeline: "Provisioning Milestone Tracker [Simulation Active]"
  },
  hi: {
    appTitle: "एयरटेल उद्यम डिजिटल",
    appSubtitle: "भारत के एमएसएमई के लिए डिजिटल कनेक्टिविटी",
    step: "चरण",
    next: "आगे बढ़ें",
    back: "पीछे जाएँ",
    startJourney: "10 मिनट में ऑनबोर्डिंग शुरू करें",
    heroHeading: "एक ही बैठक में अपने व्यवसाय को डिजिटल बनाएं",
    heroDesc: "एआई संचालित सिफारिशें, पारदर्शी मासिक मूल्य, सब-सेकंड डिजिटल केवाईसी और भारत के 6.3 करोड़ छोटे व्यवसायों के लिए त्वरित इंस्टॉलेशन।",
    benefits: [
      { title: "कागजी कार्रवाई मुक्त", desc: "जीएसटीआईएन और उद्यम द्वारा तुरंत सत्यापन" },
      { title: "पारदर्शी दरें", desc: "बिना किसी छिपे शुल्क के स्पष्ट मासिक बिल" },
      { title: "त्वरित इंस्टॉलेशन", desc: "72 घंटों के भीतर समर्पित तकनीशियन" }
    ],
    // Profile
    profileHeading: "अपने व्यवसाय के बारे में बताएं",
    profileSub: "हम आपकी आवश्यकताओं के अनुसार सर्वोत्तम ब्रॉडबैंड और क्लाउड प्लान तैयार करेंगे।",
    bizName: "व्यवसाय / प्रतिष्ठान का नाम",
    bizSegment: "मुख्य व्यावसायिक गतिविधि",
    segments: {
      micro: "रिटेल दुकान / किराना / छोटा व्यापार",
      prof: "डॉक्टर क्लिनिक / सीए फर्म / कंसल्टेंसी",
      multi: "मल्टी-ब्रांच प्रतिष्ठान / चेन स्टोर",
      mfg: "मैन्युफैक्चरिंग प्लांट / कारखाना"
    },
    employeeCount: "कर्मचारियों की संख्या",
    siteCount: "दुकान / शाखाओं की संख्या",
    city: "शहर",
    tier: "सिटी टियर",
    // Advisor
    advisorTitle: "एयरटेल एआई बिजनेस सलाहकार",
    advisorSub: "आपके व्यवसाय की आवश्यकतानुसार सही कनेक्टिविटी की तत्काल सलाह।",
    advisorPlaceholder: "अपनी आवश्यकता लिखें (उदा. 'मेरी 8 कर्मचारियों वाली क्लिनिक है')...",
    send: "भेजें",
    chipsTitle: "त्वरित सुझाव:",
    // Bundles
    recommendedTitle: "आपके लिए अनुशंसित उद्यम बंडल",
    recommendedSub: "बिना किसी छिपे शुल्क के पारदर्शी मासिक प्लान।",
    selectBundle: "यह बंडल चुनें",
    customizeInQuote: "कोटेशन में बदलाव करें",
    perMonth: "/ माह",
    zeroSetup: "शून्य सेटअप शुल्क (वार्षिक प्लान)",
    // Quote
    quoteTitle: "इंटरएक्टिव कोटेशन बिल्डर",
    quoteSub: "क्लाउड और सुरक्षा एड-ऑन जोड़ें या हटाएं।",
    monthlyTotal: "कुल मासिक राशि",
    setupTotal: "एकमुश्त सेटअप शुल्क",
    activeGSTRequired: "चयनित प्लान के लिए एक्टिव जीएसटी आवश्यक है",
    proceedCheckout: "चेकआउट की ओर बढ़ें",
    // Checkout & KYC
    checkoutTitle: "डिजिटल केवाईसी और सत्यापन",
    checkoutSub: "सरकारी रजिस्ट्री से तत्काल सत्यापन बिना किसी भौतिक दस्तावेज के।",
    gstinLabel: "जीएसटीआईएन नंबर (बेसिक ब्रॉडबैंड के लिए वैकल्पिक)",
    udyamLabel: "उद्यम पंजीकरण संख्या",
    verifyRegistry: "रजिस्ट्री की जांच करें",
    docUploadTitle: "दस्तावेज अपलोड करें",
    docUploadDesc: "प्रमाण पत्र अपलोड करें या टेस्ट सैंपल (K01–K12) चुनें।",
    selectLeadPreset: "टेस्ट सैंपल चुनें (K01–K12):",
    runVerification: "डिजिटल केवाईसी सत्यापित करें",
    // Result
    kycPassed: "डिजिटल केवाईसी सफलतापूर्वक सत्यापित",
    kycReview: "समीक्षा आवश्यक (बैक-ऑफिस सहायता)",
    kycRejected: "दस्तावेज अस्वीकृत — सुधार आवश्यक",
    // Consent
    consentTitle: "डीपीडीपी अधिनियम, 2023 वैधानिक सहमति",
    consentNotice: "भारत के डिजिटल व्यक्तिगत डेटा संरक्षण (डीपीडीपी) अधिनियम 2023 की धारा 6 के अनुसार, आपका डेटा केवल दूरसंचार कनेक्शन के लिए उपयोग किया जाता है। दस्तावेज़ होस्ट किए गए बैकएंड द्वारा मेमोरी में संसाधित किए जाते हैं और बाहरी तीसरे पक्ष के AI एपीआई को अग्रेषित नहीं किए जाते हैं। उत्पादन परिनियोजन के लिए आगे सुरक्षा और प्रतिधारण मूल्यांकन की आवश्यकता है।",
    consentCheck1: "मैं एयरटेल को जीएसटीआईएन और उद्यम डेटाबेस से विवरण सत्यापित करने की अनुमति देता हूँ।",
    consentCheck2: "मैं इंस्टॉलेशन हेतु परिसर सत्यापन की सहमति देता हूँ।",
    confirmOrder: "सहमति दें और ऑर्डर करें",
    // Tracker
    orderSuccess: "ऑर्डर स्वीकृत — सेवा सक्रियण जारी",
    orderId: "ऑर्डर संख्या",
    technicianTitle: "नियुक्त फील्ड इंजीनियर (डेमो)",
    technicianCall: "कॉल डेमो",
    estimatedInstall: "संभावित इंस्टॉलेशन समय (सिम्युलेटेड)",
    liveTimeline: "प्रोग्रेस टाइमलाइन (सिम्युलेशन)"
  }
};

