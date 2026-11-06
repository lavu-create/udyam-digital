import React, { useState } from 'react';
import { Language, translations } from '../i18n/translations';
import { Check, ShieldCheck, AlertTriangle, Upload, Search, FileText, CheckCircle2 } from 'lucide-react';

interface CheckoutScreenProps {
  language: Language;
  businessName: string;
  monthlyTotal: number;
  setupFee: number;
  gstin: string;
  udyamNumber: string;
  onGstinChange: (val: string) => void;
  onUdyamChange: (val: string) => void;
  onVerifyPack: (leadId: string) => void;
  kycResult: any;
  loadingKyc: boolean;
  onNext: () => void;
}

export const CheckoutScreen: React.FC<CheckoutScreenProps> = ({
  language,
  businessName,
  monthlyTotal,
  setupFee,
  gstin,
  udyamNumber,
  onGstinChange,
  onUdyamChange,
  onVerifyPack,
  kycResult,
  loadingKyc,
  onNext
}) => {
  const t = translations[language];
  const [selectedLead, setSelectedLead] = useState('K03');
  const [gstinLookup, setGstinLookup] = useState<any>(null);
  const [lookingUp, setLookingUp] = useState(false);

  const handleLookupGstin = async () => {
    if (!gstin.trim()) return;
    setLookingUp(true);
    try {
      const res = await fetch(`/api/v1/registry/gstin/${gstin.trim()}`);
      const data = await res.json();
      setGstinLookup(data);
    } catch (e) {
      setGstinLookup({ found: false, status: 'NETWORK_ERROR' });
    } finally {
      setLookingUp(false);
    }
  };

  return (
    <div className="py-6 px-4 max-w-2xl mx-auto space-y-6 animate-fadeIn">
      {/* Header */}
      <div>
        <span className="text-xs font-bold text-airtel-red uppercase tracking-wider">
          {t.step} 5 of 6
        </span>
        <h2 className="text-xl sm:text-2xl font-black text-slate-900 mt-1">
          {t.checkoutTitle}
        </h2>
        <p className="text-xs sm:text-sm text-slate-500 mt-1">
          {t.checkoutSub}
        </p>
      </div>

      {/* Plan Summary Card */}
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs flex items-center justify-between">
        <div>
          <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
            Selected Configuration
          </span>
          <h3 className="font-extrabold text-slate-900 text-sm mt-0.5">
            {businessName || 'Business Solution Pack'}
          </h3>
          <p className="text-xs text-slate-500 mt-0.5">
            Zero setup fee • Standard 12-month business commitment
          </p>
        </div>
        <div className="text-right">
          <div className="text-xl font-black text-slate-900">
            ₹{monthlyTotal.toLocaleString('en-IN')}
            <span className="text-xs font-normal text-slate-400"> /mo</span>
          </div>
          <span className="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded">
            DPDP Compliant
          </span>
        </div>
      </div>

      {/* Registry Lookup Box */}
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-700 flex items-center space-x-1.5">
          <ShieldCheck className="w-4 h-4 text-emerald-600" />
          <span>Statutory Registry Lookups (Mock Indexed)</span>
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {/* GSTIN Field */}
          <div>
            <label className="block text-[11px] font-bold text-slate-600 mb-1">
              {t.gstinLabel}
            </label>
            <div className="flex space-x-1.5">
              <input
                type="text"
                value={gstin}
                onChange={(e) => onGstinChange(e.target.value.toUpperCase())}
                placeholder="19EOGXH4115Y1ZL"
                className="flex-1 px-3 py-2 text-xs font-mono bg-slate-50 border border-slate-200 rounded-xl focus:bg-white focus:border-airtel-red outline-none"
              />
              <button
                type="button"
                onClick={handleLookupGstin}
                disabled={lookingUp}
                className="px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold rounded-xl transition-colors shrink-0"
              >
                {lookingUp ? '...' : <Search className="w-3.5 h-3.5" />}
              </button>
            </div>
          </div>

          {/* Udyam Field */}
          <div>
            <label className="block text-[11px] font-bold text-slate-600 mb-1">
              {t.udyamLabel}
            </label>
            <input
              type="text"
              value={udyamNumber}
              onChange={(e) => onUdyamChange(e.target.value.toUpperCase())}
              placeholder="UDYAM-WB-00-1123456"
              className="w-full px-3 py-2 text-xs font-mono bg-slate-50 border border-slate-200 rounded-xl focus:bg-white focus:border-airtel-red outline-none"
            />
          </div>
        </div>

        {/* GSTIN Result Badge */}
        {gstinLookup && (
          <div className={`p-3 rounded-xl border text-xs flex items-start space-x-2 ${
            gstinLookup.status === 'Active'
              ? 'bg-emerald-50 border-emerald-200 text-emerald-800'
              : 'bg-red-50 border-red-200 text-red-800'
          }`}>
            {gstinLookup.status === 'Active' ? (
              <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
            ) : (
              <AlertTriangle className="w-4 h-4 text-red-600 shrink-0 mt-0.5" />
            )}
            <div>
              <div className="font-bold">
                {gstinLookup.status === 'Active' ? 'Active GSTIN Verified' : `GSTIN Status: ${gstinLookup.status}`}
              </div>
              {gstinLookup.legal_name && (
                <div className="text-[11px] mt-0.5">
                  Legal Name: <span className="font-semibold">{gstinLookup.legal_name}</span> • {gstinLookup.address}
                </div>
              )}
            </div>
          </div>
        )}
      </div>

      {/* Smart KYC Engine & Test Specimen Harness */}
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-4">
        <div>
          <h3 className="font-bold text-xs uppercase tracking-wider text-slate-700 flex items-center space-x-1.5">
            <Upload className="w-4 h-4 text-airtel-red" />
            <span>Smart KYC Quality & Synthetic Verification (Local Vision Engine)</span>
          </h3>
          <p className="text-xs text-slate-500 mt-1">
            Local computer vision checks image quality (Laplacian blur variance and rotation) and evaluates synthetic registry benchmarks across test scenarios (K01–K12).
          </p>
        </div>

        {/* Specimen Dropdown Picker */}
        <div className="bg-slate-50 p-3.5 rounded-xl border border-slate-200">
          <label className="block text-[11px] font-bold text-slate-700 mb-1.5">
            {t.selectLeadPreset}
          </label>
          <div className="flex flex-col sm:flex-row gap-2">
            <select
              value={selectedLead}
              onChange={(e) => setSelectedLead(e.target.value)}
              className="flex-1 bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-medium text-slate-800 outline-none"
            >
              <option value="K03">K03 — Harmony Dental Care (Clean Valid Pass)</option>
              <option value="K01">K01 — Sita Handlooms (Cancelled GSTIN / Blank Udyam)</option>
              <option value="K02">K02 — Apex Diagnostics (Rotated Skew / Date Mismatch)</option>
              <option value="K04">K04 — Metro Retailers (Blurry Image Laplacian Trap)</option>
              <option value="K05">K05 — Silicon Micro Tech (Missing Certificate File)</option>
              <option value="K06">K06 — Marwar Logistics (GSTIN Character Typo)</option>
              <option value="K07">K07 — Shri Physio Clinic (Legal Name Mismatch)</option>
              <option value="K11">K11 — Ganga Auto Spares (Expired Bill &gt;90 Days)</option>
              <option value="K08">K08 — Karnal Agro Mills (Clean Valid Pass)</option>
              <option value="K09">K09 — Narmada Pharma Lab (Clean Valid Pass)</option>
              <option value="K10">K10 — Surat Diamond Polishing (Clean Valid Pass)</option>
              <option value="K12">K12 — Patna Cold Storage (Clean Valid Pass)</option>
            </select>

            <button
              type="button"
              onClick={() => onVerifyPack(selectedLead)}
              disabled={loadingKyc}
              className="px-4 py-2 bg-airtel-red hover:bg-airtel-darkRed text-white text-xs font-bold rounded-xl shadow-xs transition-all shrink-0 flex items-center justify-center space-x-1.5"
            >
              <FileText className="w-3.5 h-3.5" />
              <span>{loadingKyc ? 'Analyzing...' : t.runVerification}</span>
            </button>
          </div>
        </div>

        {/* Live KYC Verification Output Card */}
        {kycResult && (
          <div className={`p-4 rounded-xl border text-xs space-y-2 animate-fadeIn ${
            kycResult.overall_status === 'VERIFIED'
              ? 'bg-emerald-50/70 border-emerald-200 text-emerald-900'
              : kycResult.overall_status === 'REQUIRES_MANUAL_REVIEW'
              ? 'bg-amber-50/70 border-amber-200 text-amber-900'
              : 'bg-red-50/70 border-red-200 text-red-900'
          }`}>
            <div className="flex items-center justify-between pb-2 border-b border-slate-200/50">
              <div className="flex items-center space-x-1.5 font-bold">
                {kycResult.overall_status === 'VERIFIED' ? (
                  <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                ) : (
                  <AlertTriangle className="w-4 h-4 text-amber-600" />
                )}
                <span>Status: {kycResult.overall_status}</span>
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 bg-white/80 rounded border font-semibold">
                Confidence: {Math.round(kycResult.confidence_score * 100)}%
              </span>
            </div>

            <p className="text-[11px] leading-relaxed">
              <b>Recommendation:</b> {kycResult.recommendation}
            </p>

            {/* Risk Flags */}
            {kycResult.risk_flags && kycResult.risk_flags.length > 0 && (
              <div className="space-y-1 pt-1">
                <span className="font-bold text-[10px] uppercase tracking-wider block">
                  Identified Discrepancies / Flags:
                </span>
                {kycResult.risk_flags.map((flag: string, idx: number) => (
                  <div key={idx} className="text-[11px] font-mono bg-white/70 px-2 py-0.5 rounded border leading-tight">
                    • {flag}
                  </div>
                ))}
              </div>
            )}

            {/* Vision Quality Stats */}
            {kycResult.ocr_checks && (
              <div className="pt-2 text-[10px] text-slate-500 border-t border-slate-200/50 flex flex-wrap gap-2">
                <span>Engine: <b>{kycResult.ocr_checks.engine_status}</b></span>
                {kycResult.ocr_checks.gst_quality?.laplacian_variance && (
                  <span>Laplacian Blur Variance: <b>{kycResult.ocr_checks.gst_quality.laplacian_variance}</b></span>
                )}
                <span>Bill Age: <b>{kycResult.ocr_checks.bill_age_days} days</b></span>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Navigation */}
      <div className="flex justify-end pt-2">
        <button
          onClick={onNext}
          disabled={!kycResult}
          className="inline-flex items-center space-x-2 bg-airtel-red hover:bg-airtel-darkRed disabled:opacity-40 text-white px-6 py-3 rounded-xl text-xs font-bold shadow-md transition-all"
        >
          <span>Proceed to Consent & Placement</span>
          <Check className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

