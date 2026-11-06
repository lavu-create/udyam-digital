import React, { useState, useEffect } from 'react';
import { Language } from './i18n/translations';
import { Product, Bundle, QuoteValidation, OrderState } from './types';
import { Header } from './components/Header';
import { LandingScreen } from './components/LandingScreen';
import { ProfileScreen } from './components/ProfileScreen';
import { AdvisorScreen } from './components/AdvisorScreen';
import { BundleScreen } from './components/BundleScreen';
import { QuoteBuilderScreen } from './components/QuoteBuilderScreen';
import { CheckoutScreen } from './components/CheckoutScreen';
import { ConsentScreen } from './components/ConsentScreen';
import { OrderTrackerScreen } from './components/OrderTrackerScreen';

export function App() {
  const [language, setLanguage] = useState<Language>('en');
  const [step, setStep] = useState<number>(0);

  // Business Profile
  const [profile, setProfile] = useState({
    legal_name: 'Harmony Dental Care',
    segment: 'prof',
    employee_count: 8,
    site_count: 1,
    city: 'Jaipur',
    city_tier: 2
  });

  // Catalog & Quote
  const [allProducts, setAllProducts] = useState<Product[]>([]);
  const [bundles, setBundles] = useState<Bundle[]>([]);
  const [selectedTier, setSelectedTier] = useState<string>('growth');
  const [selectedProductIds, setSelectedProductIds] = useState<string[]>(['P02', 'P11', 'P23', 'P17']);
  const [hasActiveGstin, setHasActiveGstin] = useState<boolean>(true);
  const [quoteValidation, setQuoteValidation] = useState<QuoteValidation | null>(null);

  // KYC & Checkout
  const [gstin, setGstin] = useState<string>('19EOGXH4115Y1ZL');
  const [udyamNumber, setUdyamNumber] = useState<string>('UDYAM-WB-00-1123456');
  const [kycResult, setKycResult] = useState<any>(null);
  const [loadingKyc, setLoadingKyc] = useState<boolean>(false);

  // Order
  const [order, setOrder] = useState<OrderState | null>(null);
  const [placingOrder, setPlacingOrder] = useState<boolean>(false);

  // Fetch Products on boot
  useEffect(() => {
    fetch('/api/v1/catalog/products')
      .then((res) => res.json())
      .then((data) => setAllProducts(data))
      .catch((err) => console.error('Error fetching catalogue:', err));

    // Fetch initial recommendations
    fetchRecommendations('prof', 8, 1);
  }, []);

  // Validate Quote whenever products or GSTIN status change
  useEffect(() => {
    if (selectedProductIds.length === 0) return;

    fetch('/api/v1/catalog/validate-quote', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        product_ids: selectedProductIds,
        has_active_gstin: hasActiveGstin,
        site_count: profile.site_count,
        employee_count: profile.employee_count
      })
    })
      .then((res) => res.json())
      .then((data) => setQuoteValidation(data))
      .catch((err) => console.error('Error validating quote:', err));
  }, [selectedProductIds, hasActiveGstin, profile.site_count, profile.employee_count]);

  const fetchRecommendations = async (seg: string, emp: number, sites: number) => {
    try {
      const res = await fetch('/api/v1/advisor/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          segment: seg,
          employee_count: emp,
          site_count: sites
        })
      });
      const data = await res.json();
      setBundles(data.bundles);
    } catch (err) {
      console.error('Error fetching bundles:', err);
    }
  };

  const handleProfileChange = (field: string, value: any) => {
    const updated = { ...profile, [field]: value };
    setProfile(updated);
    if (field === 'segment' || field === 'employee_count' || field === 'site_count') {
      fetchRecommendations(updated.segment, updated.employee_count, updated.site_count);
    }
  };

  const handleSelectBundle = (tier: string, productIds: string[]) => {
    setSelectedTier(tier);
    setSelectedProductIds(productIds);
  };

  const handleToggleProduct = (pid: string) => {
    if (selectedProductIds.includes(pid)) {
      setSelectedProductIds(selectedProductIds.filter((id) => id !== pid));
    } else {
      setSelectedProductIds([...selectedProductIds, pid]);
    }
  };

  const handleVerifyKycPack = async (leadId: string) => {
    setLoadingKyc(true);
    try {
      const res = await fetch('/api/v1/kyc/verify-pack', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lead_id: leadId, consent_given: true })
      });
      const data = await res.json();
      setKycResult(data);
      if (data.gstin_result?.gstin) {
        setGstin(data.gstin_result.gstin);
      }
      if (data.udyam_result?.udyam_number) {
        setUdyamNumber(data.udyam_result.udyam_number);
      }
    } catch (err) {
      console.error('Error verifying KYC pack:', err);
    } finally {
      setLoadingKyc(false);
    }
  };

  const handleConfirmOrder = async (consentGiven: boolean) => {
    setPlacingOrder(true);
    try {
      // 1. Record DPDP consent
      await fetch('/api/v1/consent/record', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          purpose: 'TELECOM_STATUTORY_PROVISIONING',
          language: language,
          accepted: consentGiven
        })
      });

      // 2. Create Order
      const res = await fetch('/api/v1/orders/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          product_ids: selectedProductIds,
          business_name: profile.legal_name,
          contact_name: 'Proprietor',
          contact_phone: '+91 98765 43210',
          installation_address: `${profile.city}, Rajasthan`,
          gstin: gstin,
          udyam_number: udyamNumber,
          monthly_price: quoteValidation?.monthly_total_min || 2597.0,
          setup_fee: quoteValidation?.setup_fee_total || 0.0
        })
      });
      const orderData = await res.json();
      setOrder(orderData);
      setStep(7); // Go to Order Tracker
    } catch (err) {
      console.error('Error placing order:', err);
    } finally {
      setPlacingOrder(false);
    }
  };

  const handleAdvanceMilestone = async () => {
    if (!order) return;
    try {
      const res = await fetch(`/api/v1/orders/${order.order_id}/advance`, {
        method: 'POST'
      });
      const updated = await res.json();
      setOrder(updated);
    } catch (err) {
      console.error('Error advancing milestone:', err);
    }
  };

  const handleReset = () => {
    setStep(0);
    setOrder(null);
    setKycResult(null);
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900">
      <Header
        language={language}
        onLanguageChange={setLanguage}
        onReset={handleReset}
        currentStep={step}
      />

      <main className="flex-1 pb-16">
        {step === 0 && (
          <LandingScreen
            language={language}
            onStart={() => setStep(1)}
          />
        )}

        {step === 1 && (
          <ProfileScreen
            language={language}
            profile={profile}
            onChange={handleProfileChange}
            onNext={() => setStep(2)}
          />
        )}

        {step === 2 && (
          <AdvisorScreen
            language={language}
            profile={profile}
            onSelectBundle={handleSelectBundle}
            onNext={() => setStep(3)}
          />
        )}

        {step === 3 && (
          <BundleScreen
            language={language}
            bundles={bundles}
            selectedTier={selectedTier}
            onSelectTier={handleSelectBundle}
            onCustomize={() => setStep(4)}
            onNext={() => setStep(5)}
          />
        )}

        {step === 4 && (
          <QuoteBuilderScreen
            language={language}
            allProducts={allProducts}
            selectedProductIds={selectedProductIds}
            quoteValidation={quoteValidation}
            hasActiveGstin={hasActiveGstin}
            onToggleProduct={handleToggleProduct}
            onToggleGstinStatus={setHasActiveGstin}
            onProceed={() => setStep(5)}
          />
        )}

        {step === 5 && (
          <CheckoutScreen
            language={language}
            businessName={profile.legal_name}
            monthlyTotal={quoteValidation?.monthly_total_min || 2597.0}
            setupFee={quoteValidation?.setup_fee_total || 0.0}
            gstin={gstin}
            udyamNumber={udyamNumber}
            onGstinChange={setGstin}
            onUdyamChange={setUdyamNumber}
            onVerifyPack={handleVerifyKycPack}
            kycResult={kycResult}
            loadingKyc={loadingKyc}
            onNext={() => setStep(6)}
          />
        )}

        {step === 6 && (
          <ConsentScreen
            language={language}
            businessName={profile.legal_name}
            monthlyTotal={quoteValidation?.monthly_total_min || 2597.0}
            onConfirmOrder={handleConfirmOrder}
            loading={placingOrder}
          />
        )}

        {step === 7 && order && (
          <OrderTrackerScreen
            language={language}
            order={order}
            onAdvanceMilestone={handleAdvanceMilestone}
            onReset={handleReset}
          />
        )}
      </main>
    </div>
  );
}

export default App;

