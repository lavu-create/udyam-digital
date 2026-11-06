import React from 'react';
import { Language, translations } from '../i18n/translations';
import { Bundle } from '../types';
import { Check, ArrowRight, SlidersHorizontal, Sparkles } from 'lucide-react';

interface BundleScreenProps {
  language: Language;
  bundles: Bundle[];
  selectedTier: string;
  onSelectTier: (tier: string, productIds: string[]) => void;
  onCustomize: () => void;
  onNext: () => void;
}

export const BundleScreen: React.FC<BundleScreenProps> = ({
  language,
  bundles,
  selectedTier,
  onSelectTier,
  onCustomize,
  onNext
}) => {
  const t = translations[language];

  return (
    <div className="py-6 px-4 max-w-4xl mx-auto space-y-6 animate-fadeIn">
      <div className="text-center">
        <span className="text-xs font-bold text-airtel-red uppercase tracking-wider">
          {t.step} 3 of 6
        </span>
        <h2 className="text-xl sm:text-2xl font-black text-slate-900 mt-1">
          {t.recommendedTitle}
        </h2>
        <p className="text-xs sm:text-sm text-slate-500 mt-1 max-w-xl mx-auto">
          {t.recommendedSub}
        </p>
      </div>

      {/* 3 Bundles Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        {bundles.map((b) => {
          const isSelected = selectedTier === b.tier;
          const isGrowth = b.tier === 'growth';

          return (
            <div
              key={b.tier}
              className={`rounded-2xl p-5 border transition-all flex flex-col justify-between relative ${
                isSelected
                  ? 'border-airtel-red bg-white ring-2 ring-airtel-red shadow-md'
                  : 'border-slate-200 bg-white hover:border-slate-300 shadow-2xs'
              }`}
            >
              {/* Badge */}
              {isGrowth && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-airtel-red text-white text-[10px] uppercase font-bold tracking-wider px-3 py-0.5 rounded-full shadow-xs flex items-center space-x-1">
                  <Sparkles className="w-3 h-3" />
                  <span>Most Popular for MSMEs</span>
                </div>
              )}

              <div>
                <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">
                  {b.badge}
                </div>
                <h3 className="text-base font-extrabold text-slate-900 mt-1">
                  {b.title}
                </h3>
                <p className="text-xs text-slate-500 mt-1 leading-relaxed">
                  {b.description}
                </p>

                {/* Price */}
                <div className="mt-4 pt-4 border-t border-slate-100">
                  <div className="flex items-baseline space-x-1">
                    <span className="text-2xl font-black text-slate-900">
                      ₹{b.monthly_price.toLocaleString('en-IN')}
                    </span>
                    <span className="text-xs text-slate-400">{t.perMonth}</span>
                  </div>
                  <div className="text-[11px] font-semibold text-emerald-600 mt-0.5">
                    {t.zeroSetup}
                  </div>
                </div>

                {/* Highlights */}
                <div className="mt-4 space-y-2">
                  {b.highlights.map((h, i) => (
                    <div key={i} className="flex items-start space-x-2 text-xs text-slate-700">
                      <Check className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                      <span>{h}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Action */}
              <div className="mt-6 pt-4 border-t border-slate-100">
                <button
                  onClick={() => {
                    onSelectTier(b.tier, b.product_ids);
                  }}
                  className={`w-full py-2.5 rounded-xl text-xs font-bold transition-all ${
                    isSelected
                      ? 'bg-airtel-red text-white shadow-sm'
                      : 'bg-slate-100 hover:bg-slate-200 text-slate-800'
                  }`}
                >
                  {isSelected ? '✓ Selected' : t.selectBundle}
                </button>
              </div>
            </div>
          );
        })}
      </div>

      {/* Navigation Options */}
      <div className="flex flex-col sm:flex-row items-center justify-between pt-4 border-t border-slate-200 gap-3">
        <button
          onClick={onCustomize}
          className="inline-flex items-center space-x-2 text-xs font-bold text-slate-700 bg-white hover:bg-slate-50 border border-slate-200 px-4 py-2.5 rounded-xl shadow-2xs transition-all w-full sm:w-auto justify-center"
        >
          <SlidersHorizontal className="w-4 h-4 text-airtel-red" />
          <span>{t.customizeInQuote}</span>
        </button>

        <button
          onClick={onNext}
          className="inline-flex items-center space-x-2 bg-airtel-red hover:bg-airtel-darkRed text-white px-6 py-2.5 rounded-xl text-xs font-bold shadow-sm transition-all w-full sm:w-auto justify-center"
        >
          <span>{t.proceedCheckout}</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

