import React from 'react';
import { Language, translations } from '../i18n/translations';
import { Building2, Users, MapPin, Layers, ArrowRight } from 'lucide-react';

interface ProfileScreenProps {
  language: Language;
  profile: {
    legal_name: string;
    segment: string;
    employee_count: number;
    site_count: number;
    city: string;
    city_tier: number;
  };
  onChange: (field: string, value: any) => void;
  onNext: () => void;
}

export const ProfileScreen: React.FC<ProfileScreenProps> = ({
  language,
  profile,
  onChange,
  onNext
}) => {
  const t = translations[language];

  return (
    <div className="py-6 px-4 max-w-xl mx-auto space-y-6 animate-fadeIn">
      <div className="text-center sm:text-left">
        <span className="text-xs font-bold text-airtel-red uppercase tracking-wider">
          {t.step} 1 of 6
        </span>
        <h2 className="text-xl sm:text-2xl font-black text-slate-900 mt-1">
          {t.profileHeading}
        </h2>
        <p className="text-xs sm:text-sm text-slate-500 mt-1">
          {t.profileSub}
        </p>
      </div>

      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-5">
        {/* Business Name */}
        <div>
          <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
            {t.bizName}
          </label>
          <div className="relative">
            <Building2 className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
            <input
              type="text"
              value={profile.legal_name}
              onChange={(e) => onChange('legal_name', e.target.value)}
              placeholder="e.g. Harmony Dental Care, Saffron Bakers"
              className="w-full pl-9 pr-3 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:bg-white focus:border-airtel-red focus:ring-1 focus:ring-airtel-red outline-none transition-all"
            />
          </div>
        </div>

        {/* Business Segment */}
        <div>
          <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
            {t.bizSegment}
          </label>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            {[
              { id: 'micro', label: t.segments.micro, desc: '1–5 staff, standalone' },
              { id: 'prof', label: t.segments.prof, desc: 'Clinics, CA, legal' },
              { id: 'multi', label: t.segments.multi, desc: 'Retail chains, branches' },
              { id: 'mfg', label: t.segments.mfg, desc: 'Units, industrial setups' }
            ].map((seg) => (
              <button
                key={seg.id}
                type="button"
                onClick={() => onChange('segment', seg.id)}
                className={`p-3 text-left rounded-xl border transition-all ${
                  profile.segment === seg.id
                    ? 'border-airtel-red bg-red-50/50 text-slate-900 ring-1 ring-airtel-red'
                    : 'border-slate-200 hover:border-slate-300 text-slate-700 bg-white'
                }`}
              >
                <div className="text-xs font-bold">{seg.label}</div>
                <div className="text-[10px] text-slate-400 mt-0.5">{seg.desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Staff & Sites Sliders */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
          <div>
            <div className="flex justify-between items-center mb-1">
              <label className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center space-x-1">
                <Users className="w-3.5 h-3.5 text-slate-400" />
                <span>{t.employeeCount}</span>
              </label>
              <span className="text-xs font-bold text-airtel-red bg-red-50 px-2 py-0.5 rounded">
                {profile.employee_count}
              </span>
            </div>
            <input
              type="range"
              min="1"
              max="50"
              value={profile.employee_count}
              onChange={(e) => onChange('employee_count', parseInt(e.target.value))}
              className="w-full accent-airtel-red cursor-pointer"
            />
          </div>

          <div>
            <div className="flex justify-between items-center mb-1">
              <label className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center space-x-1">
                <Layers className="w-3.5 h-3.5 text-slate-400" />
                <span>{t.siteCount}</span>
              </label>
              <span className="text-xs font-bold text-airtel-red bg-red-50 px-2 py-0.5 rounded">
                {profile.site_count} {profile.site_count > 1 ? 'Sites' : 'Site'}
              </span>
            </div>
            <input
              type="range"
              min="1"
              max="10"
              value={profile.site_count}
              onChange={(e) => onChange('site_count', parseInt(e.target.value))}
              className="w-full accent-airtel-red cursor-pointer"
            />
          </div>
        </div>

        {/* City & Tier */}
        <div className="grid grid-cols-2 gap-3 pt-2">
          <div>
            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
              {t.city}
            </label>
            <div className="relative">
              <MapPin className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
              <input
                type="text"
                value={profile.city}
                onChange={(e) => onChange('city', e.target.value)}
                placeholder="Jaipur, Kolkata, Kochi"
                className="w-full pl-9 pr-3 py-2 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:bg-white focus:border-airtel-red outline-none"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
              {t.tier}
            </label>
            <div className="flex space-x-2">
              <button
                type="button"
                onClick={() => onChange('city_tier', 1)}
                className={`flex-1 py-2 text-xs font-bold rounded-xl border transition-all ${
                  profile.city_tier === 1
                    ? 'border-airtel-red bg-red-50 text-airtel-red'
                    : 'border-slate-200 text-slate-600 bg-white'
                }`}
              >
                Tier 1 Metro
              </button>
              <button
                type="button"
                onClick={() => onChange('city_tier', 2)}
                className={`flex-1 py-2 text-xs font-bold rounded-xl border transition-all ${
                  profile.city_tier === 2
                    ? 'border-airtel-red bg-red-50 text-airtel-red'
                    : 'border-slate-200 text-slate-600 bg-white'
                }`}
              >
                Tier 2 Cluster
              </button>
            </div>
          </div>
        </div>

        {/* Next Button */}
        <div className="pt-4">
          <button
            onClick={onNext}
            className="w-full flex items-center justify-center space-x-2 bg-airtel-red hover:bg-airtel-darkRed text-white py-3 rounded-xl font-bold text-sm shadow-md transition-all"
          >
            <span>Ask AI Advisor & Get Plan</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};

