const I18N = {
  en: {
    home:"Home", heart:"Heart Risk", stroke:"Stroke Risk", cad:"CAD Risk", about:"About",
    title:"NiraVed", tagline:"Know Your Care Before You Pay",
    hero:"Check your heart and brain (stroke) risk in simple steps.",
    disclaimer:"Educational research prototype only. Not a medical device. Does not diagnose, prevent, or treat disease. Urgent symptoms require prompt professional care.",
    predict:"Predict Risk", result:"Result", risk_prob:"Risk probability",
    low:"Low", high:"High", back:"Back to Home",
    heart_desc:"Heart disease risk check", stroke_desc:"Brain stroke risk check", cad_desc:"Coronary artery disease (CAD) detailed check",
    about_text:"NiraVed is a student research prototype exploring heart disease and stroke risk from structured inputs. It is not a medical diagnostic service."
  },
  hi: {
    home:"होम", heart:"हृदय जोखिम", stroke:"स्ट्रोक जोखिम", cad:"CAD जोखिम", about:"जानकारी",
    title:"निरावेद", tagline:"भुगतान से पहले अपनी देखभाल जानें",
    hero:"सरल चरणों में अपना हृदय और मस्तिष्क (स्ट्रोक) जोखिम जांचें।",
    disclaimer:"केवल शैक्षिक अनुसंधान प्रोटोटाइप। चिकित्सा उपकरण नहीं। रोग का निदान, रोकथाम या इलाज नहीं करता। गंभीर लक्षणों पर तुरंत चिकित्सा सहायता लें।",
    predict:"जोखिम जांचें", result:"परिणाम", risk_prob:"जोखिम संभावना",
    low:"कम", high:"उच्च", back:"होम पर वापस",
    heart_desc:"हृदय रोग जोखिम जांच", stroke_desc:"मस्तिष्क स्ट्रोक जोखिम जांच", cad_desc:"कोरोनरी आर्टरी रोग (CAD) विस्तृत जांच",
    about_text:"निरावेद एक छात्र अनुसंधान प्रोटोटाइप है जो संरचित इनपुट से हृदय रोग और स्ट्रोक जोखिम का अन्वेषण करता है। यह चिकित्सा निदान सेवा नहीं है।"
  }
};
let LANG = localStorage.getItem("lang") || "en";
function t(k){ return (I18N[LANG] && I18N[LANG][k]) || I18N.en[k] || k; }
function applyI18n(){
  document.querySelectorAll("[data-i18n]").forEach(el=>{ el.textContent = t(el.getAttribute("data-i18n")); });
  const btn=document.getElementById("langBtn"); if(btn) btn.textContent = LANG==="en"?"हिंदी":"English";
}
function toggleLang(){ LANG = LANG==="en"?"hi":"en"; localStorage.setItem("lang",LANG); applyI18n(); }
document.addEventListener("DOMContentLoaded", applyI18n);
