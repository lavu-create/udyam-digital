import React from 'react';
import { Language, translations } from '../i18n/translations';
import { Product, QuoteValidation } from '../types';
import { Check, AlertCircle, ArrowRight, ShieldAlert, Sparkles } from 'lucide-react';

interface QuoteBuilderScreenProps {
  language: Language;
  allProducts: Product[];
  selectedProductIds: string[];
  quoteValidation: QuoteValidation | null;
  hasActiveGstin: boolean;
  onToggleProduct: (productId: string) => void;
  onToggleGstinStatus: (hasGstin: boolean) => void;
  onProceed: () => void;
}

export const QuoteBuilderScreen: React.FC<QuoteBuilderScreenProps> = ({
  language,
  allProducts,
  selectedProductIds,
  quoteValidation,
  hasActiveGstin,
  onToggleProduct,
  onToggleGstinStatus,
  onProceed
}) => {
  const t = translations[language];

  // Group products by category
  const categories = Array.from(new Set(allProducts.map((p) => p.category)));

  return (
    <div className="py-6 px-4 max-w-4xl mx-auto space-y-6 animate-fadeIn">
      {/* Header */}
      <div>
        <span className="text-xs font-bold text-airtel-red uppercase tracking-wider">
          {t.step} 4 of 6
        </span>
        <h2 className="text-xl sm:text-2xl font-black text-slate-900 mt-1">
          {t.quoteTitle}
        </h2>
        <p className="text-xs sm:text-sm text-slate-500 mt-1">
          {t.quoteSub}
        </p>
      </div>

      {/* Main Grid: Left Products, Right Sticky Quote Card */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left: Product Catalogue */}
        <div className="lg:col-span-2 space-y-6">
          {categories.map((cat) => (
            <div key={cat} className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-2xs">
              <div className="bg-slate-50 px-4 py-2.5 border-b border-slate-200 font-bold text-xs uppercase tracking-wider text-slate-600">
                {cat} Solutions
              </div>
              <div className="divide-y divide-slate-100">
                {allProducts
                  .filter((p) => p.category === cat)
                  .map((p) => {
                    const isSelected = selectedProductIds.includes(p.product_id);
                    return (
                      <div
                        key={p.product_id}
                        onClick={() => onToggleProduct(p.product_id)}
                        className={`p-3.5 flex items-start justify-between cursor-pointer transition-colors ${
                          isSelected ? 'bg-red-50/30' : 'hover:bg-slate-50'
                        }`}
                      >
                        <div className="flex items-start space-x-3">
                          <input
                            type="checkbox"
                            checked={isSelected}
                            onChange={() => {}} // handled by parent onClick
                            className="mt-1 w-4 h-4 accent-airtel-red rounded cursor-pointer"
                          />
                          <div>
                            <div className="flex items-center space-x-2">
                              <span className="font-bold text-xs text-slate-900">
                                {p.product_name}
                              </span>
                              <span className="text-[10px] font-mono text-slate-400">
                                ({p.product_id})
                              </span>
                              {p.requires_gstin === 'Y' && (
                                <span className="text-[9px] font-semibold bg-amber-50 text-amber-700 border border-amber-200 px-1.5 py-0.2 rounded">
                                  GSTIN Req
                                </span>
                              )}
                            </div>
                            <p className="text-[11px] text-slate-500 mt-0.5 max-w-md">
                              {p.description}
                            </p>
                            {p.requires_one_of && (
                              <p className="text-[10px] text-slate-400 mt-1 italic">
                                Requires base connection: {p.requires_one_of}
                              </p>
                            )}
                          </div>
                        </div>

                        <div className="text-right shrink-0 ml-3">
                          <span className="text-xs font-bold text-slate-900">
                            ₹{p.price_min_inr_per_month}
                          </span>
                          <span className="text-[10px] text-slate-400 block">/mo</span>
                        </div>
                      </div>
                    );
                  })}
              </div>
            </div>
          ))}
        </div>

        {/* Right: Sticky Live Quote Summary */}
        <div className="space-y-4">
          <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm sticky top-20 space-y-4">
            <h3 className="font-extrabold text-sm text-slate-900 pb-3 border-b border-slate-100 flex items-center justify-between">
              <span>{t.monthlyTotal}</span>
              <span className="text-xs text-slate-400 font-normal">
                {selectedProductIds.length} {selectedProductIds.length === 1 ? 'item' : 'items'}
              </span>
            </h3>

            {/* Price Box */}
            <div className="bg-slate-50 p-4 rounded-xl border border-slate-200/80">
              <div className="text-xs text-slate-500 font-medium">Estimated Monthly Recurring</div>
              <div className="text-2xl font-black text-slate-900 mt-0.5">
                ₹{quoteValidation ? quoteValidation.monthly_total_min.toLocaleString('en-IN') : '0'}
                <span className="text-xs text-slate-400 font-normal"> /mo + GST</span>
              </div>
              <div className="text-[11px] text-slate-500 mt-1">
                Setup Fee: <span className="font-semibold text-slate-700">₹{quoteValidation?.setup_fee_total || 0}</span>
              </div>
            </div>

            {/* GSTIN Toggle Helper */}
            <div className="bg-amber-50/60 p-3 rounded-xl border border-amber-200/60 space-y-1.5">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-amber-900 flex items-center space-x-1">
                  <ShieldAlert className="w-3.5 h-3.5 text-amber-600" />
                  <span>GSTIN Status</span>
                </span>
                <label className="flex items-center space-x-1.5 text-xs text-slate-700 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={hasActiveGstin}
                    onChange={(e) => onToggleGstinStatus(e.target.checked)}
                    className="accent-airtel-red w-3.5 h-3.5"
                  />
                  <span>Active</span>
                </label>
              </div>
              <p className="text-[10px] text-amber-800 leading-tight">
                {quoteValidation?.requires_gstin
                  ? 'One or more selected SKUs require active commercial GSTIN registration.'
                  : 'Basic broadband does not mandate GSTIN.'}
              </p>
            </div>

            {/* Errors / Warnings */}
            {quoteValidation && !quoteValidation.valid && (
              <div className="bg-red-50 p-3 rounded-xl border border-red-200 space-y-1 text-xs text-red-700">
                <div className="font-bold flex items-center space-x-1">
                  <AlertCircle className="w-3.5 h-3.5" />
                  <span>Dependency Alert</span>
                </div>
                {quoteValidation.errors.map((err, idx) => (
                  <p key={idx} className="text-[11px] leading-tight">• {err}</p>
                ))}
              </div>
            )}

            {/* Selected Items List */}
            <div className="max-h-48 overflow-y-auto divide-y divide-slate-100 text-xs">
              {quoteValidation?.items.map((it) => (
                <div key={it.product_id} className="py-1.5 flex justify-between text-slate-600">
                  <span className="truncate pr-2">{it.product_name}</span>
                  <span className="font-semibold shrink-0">₹{it.price_min}</span>
                </div>
              ))}
            </div>

            {/* Proceed Action */}
            <button
              onClick={onProceed}
              disabled={quoteValidation ? !quoteValidation.valid : false}
              className="w-full bg-airtel-red hover:bg-airtel-darkRed disabled:opacity-40 text-white py-3 rounded-xl font-bold text-xs shadow-md transition-all flex items-center justify-center space-x-2"
            >
              <span>{t.proceedCheckout}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

