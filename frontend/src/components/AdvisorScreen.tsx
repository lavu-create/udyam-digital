import React, { useState } from 'react';
import { Language, translations } from '../i18n/translations';
import { Bot, Send, Sparkles, ArrowRight, Check } from 'lucide-react';

interface Message {
  sender: 'ai' | 'user';
  text: string;
  chips?: string[];
  recommendedTier?: string;
  recommendedProductIds?: string[];
}

interface AdvisorScreenProps {
  language: Language;
  profile: {
    legal_name: string;
    segment: string;
    employee_count: number;
    site_count: number;
  };
  onSelectBundle: (tier: string, productIds: string[]) => void;
  onNext: () => void;
}

export const AdvisorScreen: React.FC<AdvisorScreenProps> = ({
  language,
  profile,
  onSelectBundle,
  onNext
}) => {
  const t = translations[language];

  const initialGreeting = language === 'hi'
    ? `नमस्ते! मैं आपका एयरटेल उद्यम डिजिटल सलाहकार हूँ। मैंने देखा कि आप ${profile.legal_name || 'अपने व्यवसाय'} (${profile.employee_count} कर्मचारी, ${profile.site_count} साइट) के लिए कनेक्टिविटी देख रहे हैं। क्या आपकी प्राथमिक आवश्यकता ब्रॉडबैंड, सीसीटीवी सुरक्षा, या मल्टी-साइट नेटवर्किंग है?`
    : `Namaste! I am your Airtel Udyam Digital AI Advisor. I see you are setting up connectivity for ${profile.legal_name || 'your enterprise'} with ${profile.employee_count} staff and ${profile.site_count} location(s). Are you looking for high-speed fibre, security cameras, or multi-site branch networking?`;

  const [messages, setMessages] = useState<Message[]>([
    {
      sender: 'ai',
      text: initialGreeting,
      chips: language === 'hi' 
        ? ['300 Mbps क्लीनिक प्लान', 'क्लाउड सीसीटीवी सुरक्षा', 'मल्टी-ब्रांच SD-WAN', 'किराना / रिटेल स्टार्टर']
        : ['300 Mbps Clinic Growth', 'Cloud CCTV Cameras', 'Multi-Site SD-WAN', 'Retail / Shop Starter'],
      recommendedTier: profile.segment === 'multi' ? 'pro' : profile.segment === 'prof' ? 'growth' : 'starter',
      recommendedProductIds: profile.segment === 'multi' ? ['P03', 'P10', 'P12', 'P21'] : profile.segment === 'prof' ? ['P02', 'P11', 'P23', 'P17'] : ['P01', 'P07']
    }
  ]);

  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [selectedPlan, setSelectedPlan] = useState<string | null>(
    profile.segment === 'multi' ? 'pro' : profile.segment === 'prof' ? 'growth' : 'starter'
  );

  const sendMessage = async (textToSend: string) => {
    if (!textToSend.trim()) return;

    const userMsg: Message = { sender: 'user', text: textToSend };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch('/api/v1/advisor/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: textToSend,
          language: language,
          conversation_state: { ...profile }
        })
      });
      const data = await res.json();

      const aiMsg: Message = {
        sender: 'ai',
        text: data.reply,
        chips: data.suggested_chips,
        recommendedTier: data.recommended_tier,
        recommendedProductIds: data.recommended_product_ids
      };

      setMessages((prev) => [...prev, aiMsg]);
      if (data.recommended_tier) {
        setSelectedPlan(data.recommended_tier);
        onSelectBundle(data.recommended_tier, data.recommended_product_ids);
      }
    } catch (err) {
      // Offline fallback
      setMessages((prev) => [
        ...prev,
        {
          sender: 'ai',
          text: language === 'hi' 
            ? 'आपके व्यवसाय के लिए हमने उद्यम ग्रोथ बंडल (300 Mbps + सीसीटीवी) तैयार किया है।'
            : 'Based on your needs, we have configured the Airtel Udyam Growth Bundle (300 Mbps + Cloud CCTV).',
          recommendedTier: 'growth',
          recommendedProductIds: ['P02', 'P11', 'P23', 'P17']
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="py-6 px-4 max-w-2xl mx-auto space-y-4 animate-fadeIn">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 rounded-full bg-red-100 flex items-center justify-center text-airtel-red">
            <Bot className="w-5 h-5" />
          </div>
          <div>
            <h2 className="text-base font-bold text-slate-900 leading-tight">
              {t.advisorTitle}
            </h2>
            <div className="flex items-center space-x-1.5">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              <span className="text-[11px] text-emerald-700 font-medium">Deterministic Rule Fallback Active</span>
            </div>
          </div>
        </div>

        <button
          onClick={onNext}
          className="inline-flex items-center space-x-1 text-xs font-bold text-airtel-red hover:underline"
        >
          <span>Skip to Bundles</span>
          <ArrowRight className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Chat Container */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs flex flex-col h-[460px] overflow-hidden">
        {/* Messages */}
        <div className="flex-1 p-4 overflow-y-auto space-y-3 bg-slate-50/50">
          {messages.map((m, idx) => (
            <div
              key={idx}
              className={`flex flex-col ${m.sender === 'user' ? 'items-end' : 'items-start'}`}
            >
              <div
                className={`max-w-[85%] rounded-2xl px-4 py-2.5 text-xs sm:text-sm leading-relaxed ${
                  m.sender === 'user'
                    ? 'bg-airtel-red text-white rounded-br-xs'
                    : 'bg-white border border-slate-200 text-slate-800 shadow-2xs rounded-bl-xs'
                }`}
              >
                {m.text}

                {/* Plan Recommendation Badge inside bubble */}
                {m.recommendedTier && m.sender === 'ai' && (
                  <div className="mt-2.5 pt-2 border-t border-slate-100 flex items-center justify-between">
                    <span className="text-[10px] uppercase font-bold tracking-wider text-airtel-red flex items-center space-x-1">
                      <Sparkles className="w-3 h-3" />
                      <span>Recommended: {m.recommendedTier.toUpperCase()} BUNDLE</span>
                    </span>
                    <button
                      onClick={() => {
                        setSelectedPlan(m.recommendedTier!);
                        onSelectBundle(m.recommendedTier!, m.recommendedProductIds || []);
                        onNext();
                      }}
                      className="text-[11px] font-bold text-slate-900 bg-red-50 hover:bg-red-100 px-2 py-1 rounded transition-colors"
                    >
                      Apply & Continue →
                    </button>
                  </div>
                )}
              </div>

              {/* Chips below AI message */}
              {m.chips && m.chips.length > 0 && (
                <div className="flex flex-wrap gap-1.5 mt-2 max-w-[90%]">
                  {m.chips.map((chip, cIdx) => (
                    <button
                      key={cIdx}
                      onClick={() => sendMessage(chip)}
                      className="text-[11px] font-medium bg-white hover:bg-red-50 hover:text-airtel-red hover:border-red-200 text-slate-600 border border-slate-200 px-2.5 py-1 rounded-full transition-all"
                    >
                      {chip}
                    </button>
                  ))}
                </div>
              )}
            </div>
          ))}

          {loading && (
            <div className="flex items-center space-x-1.5 text-xs text-slate-400 p-2">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce"></span>
              <span className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce [animation-delay:0.2s]"></span>
              <span className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce [animation-delay:0.4s]"></span>
            </div>
          )}
        </div>

        {/* Input Bar */}
        <div className="p-3 bg-white border-t border-slate-200">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              sendMessage(input);
            }}
            className="flex items-center space-x-2"
          >
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder={t.advisorPlaceholder}
              className="flex-1 px-3.5 py-2 text-xs sm:text-sm bg-slate-50 border border-slate-200 rounded-xl focus:bg-white focus:border-airtel-red outline-none"
            />
            <button
              type="submit"
              disabled={!input.trim()}
              className="p-2.5 bg-airtel-red hover:bg-airtel-darkRed disabled:opacity-40 text-white rounded-xl shadow-xs transition-colors"
            >
              <Send className="w-4 h-4" />
            </button>
          </form>
        </div>
      </div>

      {/* Bottom Action */}
      <div className="flex justify-end pt-2">
        <button
          onClick={onNext}
          className="inline-flex items-center space-x-2 bg-slate-900 hover:bg-slate-800 text-white px-5 py-2.5 rounded-xl text-xs font-bold shadow-sm transition-all"
        >
          <span>Review Recommended Bundles</span>
          <ArrowRight className="w-3.5 h-3.5" />
        </button>
      </div>
    </div>
  );
};

