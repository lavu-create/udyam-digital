import React from 'react';
import { Language, translations } from '../i18n/translations';
import { Globe, RefreshCw, ShieldCheck } from 'lucide-react';

interface HeaderProps {
  language: Language;
  onLanguageChange: (lang: Language) => void;
  onReset: () => void;
  currentStep: number;
}

export const Header: React.FC<HeaderProps> = ({
  language,
  onLanguageChange,
  onReset,
  currentStep
}) => {
  const t = translations[language];

  return (
    <header className="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm">
      <div className="max-w-4xl mx-auto px-4 h-16 flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center space-x-3 cursor-pointer" onClick={onReset}>
          <div className="w-10 h-10 rounded-full bg-airtel-red flex items-center justify-center text-white font-black text-xl shadow-md">
            airtel
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h1 className="font-bold text-base text-slate-900 tracking-tight leading-none">
                {t.appTitle}
              </h1>
              <span className="text-[10px] font-semibold bg-red-100 text-airtel-red px-1.5 py-0.5 rounded">
                SYNC 2026
              </span>
            </div>
            <p className="text-xs text-slate-500 font-medium hidden sm:block">
              {t.appSubtitle}
            </p>
          </div>
        </div>

        {/* Controls */}
        <div className="flex items-center space-x-3">
          {/* DPDP Badge */}
          <div className="hidden md:flex items-center space-x-1 text-xs text-emerald-700 bg-emerald-50 px-2 py-1 rounded-md border border-emerald-200 font-medium">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>DPDP 2023 Aligned</span>
          </div>

          {/* Language Switcher */}
          <div className="flex items-center bg-slate-100 p-0.5 rounded-lg border border-slate-200">
            <button
              onClick={() => onLanguageChange('en')}
              className={`px-2.5 py-1 text-xs font-semibold rounded-md transition-all ${
                language === 'en'
                  ? 'bg-white text-airtel-red shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              EN
            </button>
            <button
              onClick={() => onLanguageChange('hi')}
              className={`px-2.5 py-1 text-xs font-semibold rounded-md transition-all ${
                language === 'hi'
                  ? 'bg-white text-airtel-red shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              हिंदी
            </button>
          </div>

          {/* Reset */}
          {currentStep > 0 && (
            <button
              onClick={onReset}
              title="Reset Journey"
              className="p-1.5 text-slate-400 hover:text-slate-600 rounded-lg hover:bg-slate-100 transition-colors"
            >
              <RefreshCw className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>
    </header>
  );
};

