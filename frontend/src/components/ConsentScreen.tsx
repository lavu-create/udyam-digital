import React, { useState } from 'react';
import { Language, translations } from '../i18n/translations';
import { ShieldCheck, Lock, CheckCircle2, ArrowRight } from 'lucide-react';

interface ConsentScreenProps {
  language: Language;
  businessName: string;
  monthlyTotal: number;
  onConfirmOrder: (consentGiven: boolean) => void;
  loading: boolean;
}

export const ConsentScreen: React.FC<ConsentScreenProps> = ({
  language,
  businessName,
  monthlyTotal,
  onConfirmOrder,
  loading
}) => {
  const t = translations[language];
  const [check1, setCheck1] = useState(true);
  const [check2, setCheck2] = useState(true);
  const [check3, setCheck3] = useState(true);

  const allAccepted = check1 && check2 && check3;

  return (
    <div className="py-6 px-4 max-w-xl mx-auto space-y-6 animate-fadeIn">
      {/* Header */}
      <div>
        <span className="text-xs font-bold text-airtel-red uppercase tracking-wider">
          {t.step} 6 of 6
        </span>
        <h2 className="text-xl sm:text-2xl font-black text-slate-900 mt-1">
          {t.consentTitle}
        </h2>
        <p className="text-xs sm:text-sm text-slate-500 mt-1">
          Purpose-limited processing under Indian privacy law.
        </p>
      </div>

      {/* Notice Card */}
      <div className="bg-emerald-50/70 p-5 rounded-2xl border border-emerald-200 text-xs text-emerald-900 space-y-3">
        <div className="flex items-center space-x-2 font-bold text-sm text-emerald-800">
          <ShieldCheck className="w-5 h-5 text-emerald-600" />
          <span>Statutory Data Fiduciary Notice (Section 6)</span>
        </div>
        <p className="text-xs leading-relaxed text-emerald-800">
          {t.consentNotice}
        </p>
        <div className="pt-2 border-t border-emerald-200/60 text-[11px] text-emerald-700 flex flex-wrap gap-2">
          <span>• 30-Day Automated Vault Purge</span>
          <span>• Zero Cloud LLM Document Leakage</span>
          <span>• PII Masking Active</span>
        </div>
      </div>

      {/* Checkboxes Card */}
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-4">
        <label className="flex items-start space-x-3 cursor-pointer">
          <input
            type="checkbox"
            checked={check1}
            onChange={(e) => setCheck1(e.target.checked)}
            className="mt-0.5 w-4 h-4 accent-airtel-red rounded"
          />
          <span className="text-xs text-slate-700 leading-snug">
            {t.consentCheck1}
          </span>
        </label>

        <label className="flex items-start space-x-3 cursor-pointer">
          <input
            type="checkbox"
            checked={check2}
            onChange={(e) => setCheck2(e.target.checked)}
            className="mt-0.5 w-4 h-4 accent-airtel-red rounded"
          />
          <span className="text-xs text-slate-700 leading-snug">
            {t.consentCheck2}
          </span>
        </label>

        <label className="flex items-start space-x-3 cursor-pointer">
          <input
            type="checkbox"
            checked={check3}
            onChange={(e) => setCheck3(e.target.checked)}
            className="mt-0.5 w-4 h-4 accent-airtel-red rounded"
          />
          <span className="text-xs text-slate-700 leading-snug">
            I agree to receive operational provisioning and technician appointment alerts via SMS and WhatsApp.
          </span>
        </label>
      </div>

      {/* Confirmation Button */}
      <div className="pt-2">
        <button
          onClick={() => onConfirmOrder(allAccepted)}
          disabled={!allAccepted || loading}
          className="w-full flex items-center justify-center space-x-2 bg-airtel-red hover:bg-airtel-darkRed disabled:opacity-40 text-white py-3.5 rounded-xl font-bold text-sm shadow-md transition-all"
        >
          <Lock className="w-4 h-4" />
          <span>{loading ? 'Recording Consent & Provisioning...' : t.confirmOrder}</span>
        </button>
      </div>
    </div>
  );
};

