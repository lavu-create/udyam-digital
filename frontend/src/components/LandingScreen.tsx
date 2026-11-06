import React from 'react';
import { Language, translations } from '../i18n/translations';
import { ArrowRight, Zap, CheckCircle2, Shield, Users, Clock, TrendingDown } from 'lucide-react';

interface LandingScreenProps {
  language: Language;
  onStart: () => void;
}

export const LandingScreen: React.FC<LandingScreenProps> = ({ language, onStart }) => {
  const t = translations[language];

  return (
    <div className="py-8 px-4 max-w-4xl mx-auto space-y-8 animate-fadeIn">
      {/* Hero Box */}
      <div className="bg-gradient-to-br from-white to-red-50/40 rounded-2xl p-6 sm:p-10 border border-red-100 shadow-sm relative overflow-hidden">
        <div className="absolute top-0 right-0 -mt-10 -mr-10 w-48 h-48 bg-red-100 rounded-full blur-3xl opacity-50 pointer-events-none"></div>

        <div className="inline-flex items-center space-x-2 bg-red-50 text-airtel-red border border-red-200 px-3 py-1 rounded-full text-xs font-semibold mb-4">
          <Zap className="w-3.5 h-3.5" />
          <span>Airtel SYNC 2026 Enterprise Innovation</span>
        </div>

        <h2 className="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight max-w-2xl">
          {t.heroHeading}
        </h2>

        <p className="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed max-w-2xl">
          {t.heroDesc}
        </p>

        {/* CTA */}
        <div className="mt-6 flex flex-col sm:flex-row items-stretch sm:items-center space-y-3 sm:space-y-0 sm:space-x-4">
          <button
            onClick={onStart}
            className="inline-flex items-center justify-center space-x-2 bg-airtel-red hover:bg-airtel-darkRed text-white px-6 py-3.5 rounded-xl font-bold text-sm shadow-md hover:shadow-lg transition-all"
          >
            <span>{t.startJourney}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
          <div className="flex items-center space-x-2 text-xs text-slate-500 font-medium px-2">
            <Clock className="w-4 h-4 text-emerald-600" />
            <span>Average onboarding time: 10 mins (vs 17.6 days baseline)</span>
          </div>
        </div>

        {/* Key Metrics Grid */}
        <div className="mt-8 grid grid-cols-2 sm:grid-cols-4 gap-3 pt-6 border-t border-red-100">
          <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
            <div className="flex items-center space-x-1 text-slate-500 text-xs font-medium">
              <TrendingDown className="w-3.5 h-3.5 text-emerald-600" />
              <span>Acquisition Cost</span>
            </div>
            <div className="text-lg font-black text-slate-900 mt-1">-70% CAC</div>
            <div className="text-[10px] text-slate-400">₹15,053 → ₹4,200</div>
          </div>

          <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
            <div className="flex items-center space-x-1 text-slate-500 text-xs font-medium">
              <Clock className="w-3.5 h-3.5 text-emerald-600" />
              <span>Turnaround Velocity</span>
            </div>
            <div className="text-lg font-black text-slate-900 mt-1">2.5 Days</div>
            <div className="text-[10px] text-slate-400">Down from 17.6 days</div>
          </div>

          <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
            <div className="flex items-center space-x-1 text-slate-500 text-xs font-medium">
              <Shield className="w-3.5 h-3.5 text-emerald-600" />
              <span>Privacy & Trust</span>
            </div>
            <div className="text-lg font-black text-slate-900 mt-1">100% Local</div>
            <div className="text-[10px] text-slate-400">Zero cloud PII leakage</div>
          </div>

          <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
            <div className="flex items-center space-x-1 text-slate-500 text-xs font-medium">
              <Users className="w-3.5 h-3.5 text-emerald-600" />
              <span>Target Market</span>
            </div>
            <div className="text-lg font-black text-slate-900 mt-1">6.3 Cr</div>
            <div className="text-[10px] text-slate-400">Indian MSMEs</div>
          </div>
        </div>
      </div>

      {/* 3 Pillar Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        {t.benefits.map((b, i) => (
          <div key={i} className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs hover:border-red-200 transition-colors">
            <div className="w-8 h-8 rounded-lg bg-red-50 text-airtel-red flex items-center justify-center font-bold text-sm mb-3">
              0{i+1}
            </div>
            <h3 className="font-bold text-slate-900 text-sm">{b.title}</h3>
            <p className="text-xs text-slate-500 mt-1 leading-relaxed">{b.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

