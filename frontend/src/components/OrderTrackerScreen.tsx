import React, { useState } from 'react';
import { Language, translations } from '../i18n/translations';
import { OrderState } from '../types';
import { CheckCircle2, Clock, Phone, User, Calendar, MapPin, Play, RefreshCw, ShieldCheck } from 'lucide-react';

interface OrderTrackerScreenProps {
  language: Language;
  order: OrderState;
  onAdvanceMilestone: () => void;
  onReset: () => void;
}

export const OrderTrackerScreen: React.FC<OrderTrackerScreenProps> = ({
  language,
  order,
  onAdvanceMilestone,
  onReset
}) => {
  const t = translations[language];
  const [advancing, setAdvancing] = useState(false);

  const handleAdvance = async () => {
    setAdvancing(true);
    await onAdvanceMilestone();
    setAdvancing(false);
  };

  return (
    <div className="py-6 px-4 max-w-2xl mx-auto space-y-6 animate-fadeIn">
      {/* Success Banner */}
      <div className="bg-emerald-500 text-white p-6 rounded-2xl shadow-md text-center space-y-2">
        <div className="w-12 h-12 rounded-full bg-white/20 flex items-center justify-center mx-auto mb-2">
          <CheckCircle2 className="w-8 h-8 text-white" />
        </div>
        <h2 className="text-xl sm:text-2xl font-black">
          {t.orderSuccess}
        </h2>
        <div className="inline-block bg-white/20 px-3 py-1 rounded-full text-xs font-mono font-bold tracking-wider">
          {t.orderId}: {order.order_id}
        </div>
      </div>

      {/* Technician Card */}
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-3">
        <div className="flex items-center justify-between pb-3 border-b border-slate-100">
          <div className="flex items-center space-x-2">
            <div className="w-9 h-9 rounded-full bg-red-50 text-airtel-red flex items-center justify-center font-bold">
              <User className="w-5 h-5" />
            </div>
            <div>
              <div className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
                {t.technicianTitle}
              </div>
              <div className="text-sm font-black text-slate-900">
                {order.technician_name}
              </div>
            </div>
          </div>

          <a
            href={`tel:${order.technician_phone}`}
            className="inline-flex items-center space-x-1.5 bg-slate-900 hover:bg-slate-800 text-white px-3.5 py-2 rounded-xl text-xs font-bold shadow-xs transition-colors"
          >
            <Phone className="w-3.5 h-3.5" />
            <span>{t.technicianCall}</span>
          </a>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-600 pt-1">
          <div className="flex items-center space-x-2">
            <Calendar className="w-4 h-4 text-slate-400 shrink-0" />
            <span>Scheduled: <b className="text-slate-800">{order.scheduled_install_date}</b></span>
          </div>
          <div className="flex items-center space-x-2">
            <MapPin className="w-4 h-4 text-slate-400 shrink-0" />
            <span className="truncate">{order.installation_address}</span>
          </div>
        </div>
      </div>

      {/* Milestones Visual Tracker */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-2xs space-y-5">
        <div className="flex items-center justify-between">
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center space-x-1.5">
            <Clock className="w-4 h-4 text-airtel-red" />
            <span>{t.liveTimeline}</span>
          </h3>
          <span className="text-[10px] text-slate-400 font-medium">Real-Time Sync</span>
        </div>

        <div className="space-y-4">
          {order.milestones.map((m, idx) => {
            const isCompleted = m.status === 'COMPLETED';
            const isInProgress = m.status === 'IN_PROGRESS';
            const isLast = idx === order.milestones.length - 1;

            return (
              <div key={m.milestone} className="flex items-start space-x-3 relative">
                {/* Connecting Line */}
                {!isLast && (
                  <div
                    className={`absolute left-3.5 top-7 w-0.5 h-8 -ml-[1px] ${
                      isCompleted ? 'bg-emerald-500' : 'bg-slate-200'
                    }`}
                  ></div>
                )}

                {/* Status Dot */}
                <div
                  className={`w-7 h-7 rounded-full flex items-center justify-center shrink-0 text-xs font-bold transition-all z-10 ${
                    isCompleted
                      ? 'bg-emerald-500 text-white shadow-xs'
                      : isInProgress
                      ? 'bg-amber-500 text-white animate-pulse'
                      : 'bg-slate-100 text-slate-400 border border-slate-200'
                  }`}
                >
                  {isCompleted ? '✓' : idx + 1}
                </div>

                {/* Content */}
                <div className="flex-1 pt-0.5">
                  <div className="flex items-center justify-between">
                    <span
                      className={`text-xs font-bold ${
                        isCompleted
                          ? 'text-slate-900'
                          : isInProgress
                          ? 'text-amber-900 font-extrabold'
                          : 'text-slate-400'
                      }`}
                    >
                      {m.title}
                    </span>
                    <span
                      className={`text-[10px] font-semibold px-2 py-0.5 rounded ${
                        isCompleted
                          ? 'bg-emerald-50 text-emerald-700'
                          : isInProgress
                          ? 'bg-amber-50 text-amber-700'
                          : 'bg-slate-50 text-slate-400'
                      }`}
                    >
                      {m.status}
                    </span>
                  </div>
                  <p className="text-[11px] text-slate-500 mt-0.5 leading-relaxed">
                    {m.notes}
                  </p>
                </div>
              </div>
            );
          })}
        </div>

        {/* Demo Advance Milestone Button */}
        <div className="pt-4 border-t border-slate-100 flex flex-col sm:flex-row gap-2 justify-between items-center">
          <button
            onClick={handleAdvance}
            disabled={advancing}
            className="w-full sm:w-auto inline-flex items-center justify-center space-x-1.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 px-4 py-2 rounded-xl transition-all"
          >
            <Play className="w-3.5 h-3.5 text-airtel-red" />
            <span>Simulate Real-Time Milestone Advance</span>
          </button>

          <button
            onClick={onReset}
            className="w-full sm:w-auto inline-flex items-center justify-center space-x-1.5 text-xs font-bold text-slate-500 hover:text-slate-800 px-3 py-2 rounded-xl"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span>Start Another Order</span>
          </button>
        </div>
      </div>
    </div>
  );
};

