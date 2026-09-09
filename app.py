import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title="Personalised Healthcare",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# PREMIUM NOTION-STYLE UI
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Bengali:wght@400;500;600;700;800&display=swap');

:root{
 --ink:#14213D; --ink2:#253858; --muted:#667085; --faint:#98A2B3;
 --line:rgba(148,163,184,.22); --white:rgba(255,255,255,.88);
 --blue:#2563EB; --cyan:#0891B2; --purple:#7C3AED;
 --green:#059669; --amber:#D97706; --red:#DC2626;
}

html,body,[class*="css"]{
 font-family:"Inter","Noto Sans Bengali",sans-serif;
}
.stApp{
 color:var(--ink);
 background:
   radial-gradient(circle at 8% 8%,rgba(37,99,235,.10),transparent 22%),
   radial-gradient(circle at 92% 8%,rgba(124,58,237,.10),transparent 24%),
   radial-gradient(circle at 78% 88%,rgba(8,145,178,.07),transparent 22%),
   linear-gradient(135deg,#F8FBFF 0%,#F6F7FB 52%,#FBF9FF 100%);
 background-attachment:fixed;
}
.stApp:before{
 content:""; position:fixed; inset:0; pointer-events:none; z-index:0;
 opacity:.28;
 background-image:
   linear-gradient(rgba(37,99,235,.035) 1px,transparent 1px),
   linear-gradient(90deg,rgba(37,99,235,.035) 1px,transparent 1px);
 background-size:38px 38px;
 mask-image:linear-gradient(to bottom,black,transparent 85%);
}
.block-container{
 max-width:1500px; padding:1rem 2rem 2.5rem; position:relative; z-index:1;
}
h1,h2,h3,h4{color:var(--ink)!important;letter-spacing:-.03em;}
p,span,label,div{scrollbar-width:thin;}

.hero{
 position:relative; overflow:hidden; padding:2.2rem 2.3rem;
 border:1px solid rgba(255,255,255,.75); border-radius:28px;
 background:
   linear-gradient(120deg,rgba(255,255,255,.94),rgba(247,250,255,.90) 55%,rgba(249,246,255,.94));
 box-shadow:0 24px 70px rgba(16,24,40,.09),inset 0 1px 0 rgba(255,255,255,.95);
 margin-bottom:1.35rem;
}
.hero:after{
 content:""; position:absolute; width:220px;height:220px;right:-70px;top:-90px;
 border-radius:50%;
 background:linear-gradient(135deg,rgba(37,99,235,.18),rgba(124,58,237,.08));
 filter:blur(2px); animation:floatOrb 7s ease-in-out infinite;
}
.hero:before{
 content:""; position:absolute; width:110px;height:110px;right:180px;bottom:-55px;
 border-radius:50%; background:rgba(8,145,178,.10); filter:blur(3px);
 animation:floatOrb2 9s ease-in-out infinite;
}
.eyebrow{
 color:#526681; font-size:.72rem; font-weight:800;
 letter-spacing:.15em; text-transform:uppercase;
}
.hero-title{
 position:relative; z-index:1; margin:.3rem 0 0;
 font-size:clamp(1.9rem,3.8vw,2.9rem); font-weight:800;
 letter-spacing:-.055em; color:var(--ink)!important;
}
.hero-sub{
 position:relative; z-index:1; margin-top:.55rem;
 color:#64748B; font-size:1rem; font-weight:500;
}

.card,.metric-card{
 background:var(--white); border:1px solid var(--line); border-radius:19px;
 box-shadow:0 10px 32px rgba(15,23,42,.055);
 backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
 transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease;
}
.card{padding:1.15rem 1.2rem;}
.metric-card{padding:1rem 1.1rem;min-height:112px;}
.card:hover,.metric-card:hover{
 transform:translateY(-2px); box-shadow:0 16px 38px rgba(15,23,42,.08);
 border-color:rgba(37,99,235,.18);
}
.metric-label{
 color:#667085;font-size:.72rem;font-weight:800;
 text-transform:uppercase;letter-spacing:.09em;
}
.metric-value{color:var(--ink);font-size:1.7rem;font-weight:800;margin-top:.25rem;}
.metric-note{color:#98A2B3;font-size:.73rem;margin-top:.15rem;}
.section-kicker{
 color:#667085;font-size:.72rem;font-weight:800;
 text-transform:uppercase;letter-spacing:.12em;margin-bottom:.25rem;
}
.info-chip{
 display:inline-block;padding:.3rem .68rem;border-radius:999px;
 background:#F2F5FA;border:1px solid #E4E9F1;color:#475467;
 font-size:.71rem;font-weight:750;margin:.12rem .18rem .12rem 0;
}
.risk-card{
 padding:1.5rem;border-radius:23px;border:1px solid;
 box-shadow:0 16px 42px rgba(15,23,42,.07);
}
.risk-high{background:linear-gradient(135deg,#FFF7F7,#FFFFFF);border-color:#FECACA;}
.risk-moderate{background:linear-gradient(135deg,#FFFCF2,#FFFFFF);border-color:#FDE68A;}
.risk-low{background:linear-gradient(135deg,#F1FCF7,#FFFFFF);border-color:#BBF7D0;}
.risk-number{font-size:2.55rem;font-weight:850;letter-spacing:-.055em;color:var(--ink);margin-top:.25rem;}
.risk-title{font-size:.72rem;font-weight:800;letter-spacing:.12em;color:#667085;text-transform:uppercase;}

div[data-testid="stForm"]{
 background:rgba(255,255,255,.92); border:1px solid var(--line);
 border-radius:23px;padding:1.15rem;
 box-shadow:0 16px 45px rgba(15,23,42,.065);
}
[data-baseweb="input"]>div,[data-baseweb="select"]>div{
 border-radius:12px!important; border-color:#DDE4EE!important;
}
label{color:var(--ink)!important;font-weight:650!important;}
.stTabs [data-baseweb="tab-list"]{
 background:rgba(237,242,248,.92);padding:.38rem;border-radius:15px;gap:.35rem;
}
.stTabs [data-baseweb="tab"]{
 border-radius:11px;padding:.68rem .95rem;font-weight:750;color:#58677A;
}
.stTabs [aria-selected="true"]{
 background:#fff!important;color:var(--blue)!important;
 box-shadow:0 4px 15px rgba(15,23,42,.08);
}
.stButton>button,.stDownloadButton>button{
 border-radius:12px!important;min-height:2.8rem;font-weight:800!important;
 transition:transform .15s ease,box-shadow .15s ease;
}
.stButton>button:hover,.stDownloadButton>button:hover{
 transform:translateY(-1px);box-shadow:0 10px 22px rgba(37,99,235,.16);
}
[data-testid="stMetric"]{
 background:rgba(255,255,255,.90);border:1px solid var(--line);
 border-radius:17px;box-shadow:0 8px 24px rgba(15,23,42,.05);
}
[data-testid="stSidebar"]{
 background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(246,249,253,.96));
 border-right:1px solid var(--line);
}
[data-testid="stDataFrame"]{border:1px solid var(--line);border-radius:16px;overflow:hidden;}
div[data-testid="stAlert"]{border-radius:15px;}
.footer{color:#98A2B3;text-align:center;font-size:.72rem;padding:1rem 0 .2rem;}

@keyframes floatOrb{0%,100%{transform:translate3d(0,0,0) scale(1)}50%{transform:translate3d(-15px,12px,0) scale(1.06)}}
@keyframes floatOrb2{0%,100%{transform:translate3d(0,0,0)}50%{transform:translate3d(18px,-10px,0)}}

@media(max-width:760px){
 .block-container{padding:.65rem .72rem 1.5rem;}
 .hero{padding:1.35rem;border-radius:21px;}
 .hero-title{font-size:1.85rem;line-height:1.15;}
 .hero-sub{font-size:.9rem;line-height:1.5;}
 .metric-card{min-height:96px;}
 .metric-value{font-size:1.35rem;}
 .card{padding:.95rem;}
 .risk-number{font-size:2.05rem;}
 .stTabs [data-baseweb="tab"]{padding:.58rem .65rem;font-size:.78rem;}
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD MODEL
# ============================================================
@st.cache_resource
def load_model():
    model = joblib.load("final_model_artifacts/calibrated_final_model.pkl")
    with open("final_model_artifacts/model_config.json", encoding="utf-8") as f:
        config = json.load(f)
    return model, config

model, config = load_model()
features = config["features"]
classes = list(model.classes_)

# ============================================================
# METADATA
# ============================================================
META = {
"Age":("বয়স","Age in completed years / পূর্ণ বয়স","years","Adult input; model-specific"),
"BMI":("বডি মাস ইনডেক্স","Weight relative to height / ওজন-উচ্চতার অনুপাত","kg/m²","<18.5 underweight | 18.5–24.9 healthy | 25–29.9 overweight | ≥30 obesity"),
"Cholesterol":("মোট কোলেস্টেরল","Total blood cholesterol / রক্তের মোট কোলেস্টেরল","mg/dL","<200 generally desirable"),
"Glucose_Level":("রক্তের গ্লুকোজ","Blood glucose / রক্তে শর্করা","mg/dL","Fasting ~70–99 mg/dL is generally normal"),
"HbA1c":("এইচবিএ১সি","Average glucose marker / গত ২–৩ মাসের গড় শর্করার সূচক","%","<5.7% normal | 5.7–6.4% prediabetes range | ≥6.5% diabetes range"),
"Systolic_BP":("সিস্টোলিক BP","Pressure during heart contraction / সংকোচনের সময়ের চাপ","mmHg","<120 normal | 120–129 elevated | ≥130 higher"),
"Diastolic_BP":("ডায়াস্টোলিক BP","Pressure during heart relaxation / শিথিল অবস্থার চাপ","mmHg","<80 normal | ≥80 higher"),
"LDL":("এলডিএল","Low-density lipoprotein / 'bad' cholesterol","mg/dL","<100 generally desirable; target varies by risk"),
"HDL":("এইচডিএল","High-density lipoprotein / 'good' cholesterol","mg/dL","≥60 best; low thresholds differ by sex"),
"Triglycerides":("ট্রাইগ্লিসারাইড","Major blood fat / রক্তের এক ধরনের চর্বি","mg/dL","<150 normal | 150–199 borderline high | ≥200 high"),
"CRP":("সি-রিঅ্যাকটিভ প্রোটিন","Inflammation-related biomarker / প্রদাহের সূচক","mg/L","Assay/context dependent"),
"eGFR":("কিডনি ফিল্টারিং রেট","Estimated kidney filtration / কিডনির filtration capacity","mL/min/1.73m²","≥90 usually normal; 60–89 mildly decreased; <60 reduced"),
"Waist_Circumference":("কোমরের পরিধি","Waist circumference / কোমরের মাপ","cm","Cutoffs vary by sex and population"),
"Resting_Heart_Rate":("বিশ্রামকালীন হার্ট রেট","Heart beats at rest / বিশ্রামে হৃদস্পন্দন","bpm","Typical adult resting range ~60–100"),
"HRV":("হার্ট রেট ভ্যারিয়েবিলিটি","Beat-to-beat variation / হৃদস্পন্দনের সময়ের পরিবর্তন","device-dependent","No single universal reference"),
"Sleep_Hours":("ঘুমের সময়","Average sleep duration / গড় ঘুমের সময়","hours/day","Adults commonly recommended ~7–9 h/night"),
"PRS_Cardiometabolic":("কার্ডিওমেটাবলিক PRS","Polygenic susceptibility score / জেনেটিক susceptibility","model score","No universal clinical range; model-specific"),
"PRS_Type2Diabetes":("টাইপ-২ ডায়াবেটিস PRS","Polygenic susceptibility score / জেনেটিক susceptibility","model score","No universal clinical range; model-specific"),
"APOE_e4_Carrier":("APOE-e4 carrier","Presence of APOE ε4 allele / APOE ε4 allele আছে কি না","0/1","0 = No | 1 = Yes"),
"BRCA_Pathogenic_Variant":("BRCA pathogenic variant","Pathogenic BRCA variant / pathogenic variant আছে কি না","0/1","0 = No | 1 = Yes"),
"Family_History_CVD":("পরিবারে CVD ইতিহাস","Family history of cardiovascular disease / পরিবারের হৃদ্‌রোগের ইতিহাস","0/1","0 = No | 1 = Yes"),
"Family_History_T2D":("পরিবারে T2D ইতিহাস","Family history of type 2 diabetes / পরিবারের ডায়াবেটিসের ইতিহাস","0/1","0 = No | 1 = Yes"),
}

CATS={
"Gender":["Female","Male"],
"Smoking_Status":["Non-smoker","Former smoker","Current smoker"],
"Alcohol_Consumption":["Low","Moderate","High","Unknown"],
"Physical_Activity_Level":["Sedentary","Lightly Active","Moderately Active","Highly Active"],
"Diet_Type":["Balanced","High Protein","Keto","Mediterranean","Vegan","Vegetarian"],
"Sleep_Quality":["Excellent","Good","Fair","Poor"],
}

DEFAULTS={
"Age":40.0,"BMI":24.0,"Cholesterol":190.0,"Glucose_Level":90.0,"HbA1c":5.4,
"Systolic_BP":120.0,"Diastolic_BP":80.0,"LDL":100.0,"HDL":50.0,
"Triglycerides":120.0,"CRP":1.0,"eGFR":90.0,"Waist_Circumference":85.0,
"Resting_Heart_Rate":70.0,"HRV":50.0,"Sleep_Hours":7.0,
"PRS_Cardiometabolic":0.0,"PRS_Type2Diabetes":0.0,
"APOE_e4_Carrier":0,"BRCA_Pathogenic_Variant":0,
"Family_History_CVD":0,"Family_History_T2D":0,
}

# ============================================================
# STATE
# ============================================================
if "patient_data" not in st.session_state:
    st.session_state.patient_data=None
if "result" not in st.session_state:
    st.session_state.result=None

# ============================================================
# HELPERS
# ============================================================
def info(f):
    return META.get(f,(f,f,"","No universal reference"))

def numeric_control(f,prefix="input"):
    bn,meaning,unit,ref=info(f)
    return st.number_input(
        f"{f} — {bn}",
        value=float(DEFAULTS.get(f,0.0)),
        step=0.1,
        help=f"Meaning / অর্থ: {meaning}\nUnit: {unit}\nReference: {ref}",
        key=f"{prefix}_{f}"
    )

def select_control(f,prefix="input"):
    bn,meaning,unit,ref=info(f)
    return st.selectbox(
        f"{f} — {bn}",CATS[f],
        help=f"Meaning / অর্থ: {meaning}\nReference: {ref}",
        key=f"{prefix}_{f}"
    )

def binary_control(f,prefix="input"):
    bn,meaning,unit,ref=info(f)
    return st.selectbox(
        f"{f} — {bn}",[0,1],
        format_func=lambda x:"No / না" if x==0 else "Yes / হ্যাঁ",
        help=f"Meaning / অর্থ: {meaning}\nReference: {ref}",
        key=f"{prefix}_{f}"
    )

def clinical_flags(p):
    flags=[]
    if "BMI" in p:
        if p["BMI"]>=30: flags.append(("BMI","Obesity range / স্থূলতার range","red"))
        elif p["BMI"]>=25: flags.append(("BMI","Overweight range / অতিরিক্ত ওজন","amber"))
    if "Systolic_BP" in p and "Diastolic_BP" in p:
        if p["Systolic_BP"]>=140 or p["Diastolic_BP"]>=90: flags.append(("BP","High range / উচ্চ","red"))
        elif p["Systolic_BP"]>=130 or p["Diastolic_BP"]>=80: flags.append(("BP","Above normal / স্বাভাবিকের বেশি","amber"))
    if "LDL" in p and p["LDL"]>=130: flags.append(("LDL","Above desirable / কাঙ্ক্ষিতের বেশি","amber"))
    if "Triglycerides" in p and p["Triglycerides"]>=150: flags.append(("TG","Above normal / বেশি","amber"))
    if "HbA1c" in p and p["HbA1c"]>=5.7: flags.append(("HbA1c","Above normal range / স্বাভাবিকের বেশি","amber"))
    if "eGFR" in p and p["eGFR"]<60: flags.append(("eGFR","Reduced / কম","red"))
    return flags

def report_text():
    if not st.session_state.result:
        return ""
    r=st.session_state.result
    p=st.session_state.patient_data or {}
    lines=[
        "PERSONALISED HEALTHCARE RISK ASSESSMENT",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"Predicted Risk: {r['prediction']}",
        "Risk Probabilities:"
    ]
    for c,v in r["probabilities"].items():
        lines.append(f"  {c}: {v:.2%}")
    lines += ["","Clinical Snapshot:"]
    for f,v in p.items():
        lines.append(f"  {f}: {v}")
    lines += [
        "",
        "SAFETY NOTE:",
        "Research prototype only. Model output is not a diagnosis or treatment recommendation.",
        "What-if changes represent model sensitivity, not causal treatment effects."
    ]
    return "\n".join(lines)

# ============================================================
# HERO
# ============================================================
st.markdown("""
<div class="hero">
  <div class="eyebrow">AI • PERSONAL HEALTH • RESEARCH</div>
  <div class="hero-title">Personalised Healthcare Risk Assessment</div>
  <div class="hero-sub">ব্যক্তিকেন্দ্রিক স্বাস্থ্যঝুঁকি মূল্যায়ন · Bilingual intelligent research dashboard</div>
</div>
""",unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## 🩺 Health Assessment")
    st.caption("বাংলা + English")
    page=st.radio(
        "Navigation / নেভিগেশন",
        ["Overview / Dashboard","Patient Assessment","Risk Results","What-if Simulator","Reference Guide"],
        label_visibility="collapsed"
    )
    st.divider()
    st.markdown("**System status**")
    st.success("Model loaded • Ready")
    st.caption(f"{len(features)} model input features")
    st.caption("3 risk classes")
    st.markdown(
        '<div style="display:flex;align-items:center;gap:7px;color:#667085;font-size:.74rem">'
        '<span style="width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.10)"></span>'
        'System online · Model ready</div>',
        unsafe_allow_html=True
    )
    st.divider()
    st.caption("Research prototype • Not for diagnosis")

# ============================================================
# OVERVIEW
# ============================================================
if page=="Overview / Dashboard":
    st.subheader("Overview / সারসংক্ষেপ")
    st.caption("A quick view of the assessment workflow and model interface.")

    cols=st.columns(4)
    metrics=[
        ("Model Inputs",len(features),"features"),
        ("Risk Classes",len(classes),"High • Moderate • Low"),
        ("Interface","BI","Bilingual"),
        ("Mode","Research","Prototype"),
    ]
    for col,(a,b,c) in zip(cols,metrics):
        with col:
            st.markdown(f'<div class="metric-card"><div class="metric-label">{a}</div><div class="metric-value">{b}</div><div class="metric-note">{c}</div></div>',unsafe_allow_html=True)

    st.markdown(
        '<div class="card" style="margin:.2rem 0 1.15rem">'
        '<div class="section-kicker">LIVE SYSTEM</div>'
        '<b style="font-size:1.05rem">● Model engine ready</b>'
        '<span style="color:#667085;margin-left:10px">Secure local inference · No retraining during assessment</span>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown("### Assessment workflow / মূল্যায়নের ধাপ")
    a,b,c=st.columns(3)
    cards=[
        ("01","ENTER / ইনপুট","Clinical, lifestyle and genetic information দিন।"),
        ("02","ASSESS / মূল্যায়ন","Model predicted class ও probabilities দেখুন।"),
        ("03","UNDERSTAND / বুঝুন","Reference values, flags ও what-if sensitivity review করুন।")
    ]
    for col,(n,t,d) in zip([a,b,c],cards):
        with col:
            st.markdown(f'<div class="card"><div class="section-kicker">{n}</div><h3>{t}</h3><p style="color:#667085">{d}</p></div>',unsafe_allow_html=True)

    st.markdown("### Built for / কার জন্য")
    st.markdown(
        '<span class="info-chip">Research</span><span class="info-chip">Public Health</span>'
        '<span class="info-chip">Clinical Education</span><span class="info-chip">Health Analytics</span>'
        '<span class="info-chip">AI/ML Prototype</span>',
        unsafe_allow_html=True
    )

# ============================================================
# PATIENT ASSESSMENT
# ============================================================
elif page=="Patient Assessment":
    st.subheader("Patient Assessment / রোগীর মূল্যায়ন")
    st.caption("Enter available information. Each field provides meaning, unit and reference guidance.")

    with st.form("assessment_form"):
        tab1,tab2,tab3,tab4=st.tabs([
            "👤 Profile / প্রোফাইল",
            "❤️ Clinical / ক্লিনিক্যাল",
            "🏃 Lifestyle / জীবনযাপন",
            "🧬 Genetics / জেনেটিক"
        ])
        patient={}

        with tab1:
            a,b=st.columns(2)
            if "Age" in features:
                with a: patient["Age"]=numeric_control("Age")
            if "Gender" in features:
                with b: patient["Gender"]=select_control("Gender")
            if "BMI" in features:
                with a: patient["BMI"]=numeric_control("BMI")
            if "Waist_Circumference" in features:
                with b: patient["Waist_Circumference"]=numeric_control("Waist_Circumference")
            if "Smoking_Status" in features:
                with a: patient["Smoking_Status"]=select_control("Smoking_Status")
            if "Alcohol_Consumption" in features:
                with b: patient["Alcohol_Consumption"]=select_control("Alcohol_Consumption")

        with tab2:
            clinical=["Cholesterol","Glucose_Level","HbA1c","Systolic_BP","Diastolic_BP",
                      "LDL","HDL","Triglycerides","CRP","eGFR","Resting_Heart_Rate","HRV"]
            available=[f for f in clinical if f in features]
            a,b=st.columns(2)
            for i,f in enumerate(available):
                with (a if i%2==0 else b):
                    patient[f]=numeric_control(f)

        with tab3:
            a,b=st.columns(2)
            if "Physical_Activity_Level" in features:
                with a: patient["Physical_Activity_Level"]=select_control("Physical_Activity_Level")
            if "Diet_Type" in features:
                with b: patient["Diet_Type"]=select_control("Diet_Type")
            if "Sleep_Quality" in features:
                with a: patient["Sleep_Quality"]=select_control("Sleep_Quality")
            if "Sleep_Hours" in features:
                with b: patient["Sleep_Hours"]=numeric_control("Sleep_Hours")

            for f in ["Stress_Level","Depression_Score","Anxiety_Score","Social_Isolation_Index"]:
                if f in features:
                    patient[f]=numeric_control(f)

        with tab4:
            st.info("Genetic inputs represent susceptibility information. / জেনেটিক ইনপুট susceptibility বোঝায়; diagnosis নয়।")
            genetic=["PRS_Cardiometabolic","PRS_Type2Diabetes","APOE_e4_Carrier",
                     "BRCA_Pathogenic_Variant","Family_History_CVD","Family_History_T2D"]
            a,b=st.columns(2)
            for i,f in enumerate([x for x in genetic if x in features]):
                with (a if i%2==0 else b):
                    if f in ["APOE_e4_Carrier","BRCA_Pathogenic_Variant","Family_History_CVD","Family_History_T2D"]:
                        patient[f]=binary_control(f)
                    else:
                        patient[f]=numeric_control(f)

        submitted=st.form_submit_button(
            "🔎 Assess Health Risk / স্বাস্থ্যঝুঁকি মূল্যায়ন",
            use_container_width=True,
            type="primary"
        )

    if submitted:
        X=pd.DataFrame([{f:patient.get(f,DEFAULTS.get(f,0)) for f in features}])[features]
        try:
            pred=model.predict(X)[0]
            probs=model.predict_proba(X)[0]
            st.session_state.patient_data=patient
            st.session_state.result={
                "prediction":pred,
                "probabilities":{c:float(v) for c,v in zip(classes,probs)}
            }
            st.success("Assessment completed / মূল্যায়ন সম্পন্ন হয়েছে। Open Risk Results.")
        except Exception as e:
            st.error("Prediction failed / Prediction সম্পন্ন হয়নি।")
            st.code(str(e))

    if st.session_state.patient_data:
        p=st.session_state.patient_data
        flags=clinical_flags(p)
        st.markdown("### Instant clinical flags / দ্রুত clinical flags")
        if flags:
            fcols=st.columns(min(4,len(flags)))
            for col,(name,msg,kind) in zip(fcols,flags):
                with col:
                    symbol="●"
                    st.markdown(f'<div class="card"><div class="section-kicker">{symbol} {name}</div><b>{msg}</b></div>',unsafe_allow_html=True)
        else:
            st.success("No predefined reference flag triggered / কোনো predefined reference flag trigger হয়নি।")

# ============================================================
# RISK RESULTS
# ============================================================
elif page=="Risk Results":
    st.subheader("Risk Results / ঝুঁকির ফলাফল")
    r=st.session_state.result

    if not r:
        st.info("Complete Patient Assessment first. / আগে Patient Assessment সম্পন্ন করুন।")
    else:
        pred=r["prediction"]
        probs=r["probabilities"]
        cls_name={"High":"HIGH RISK / উচ্চ ঝুঁকি","Moderate":"MODERATE RISK / মাঝারি ঝুঁকি","Low":"LOW RISK / কম ঝুঁকি"}.get(pred,pred)

        css_class={"High":"risk-high","Moderate":"risk-moderate","Low":"risk-low"}.get(pred,"risk-moderate")
        st.markdown(
            f'<div class="risk-card {css_class}"><div class="risk-title">MODEL PREDICTION / মডেল পূর্বাভাস</div>'
            f'<div class="risk-number">{cls_name}</div>'
            f'<p style="color:#667085;margin-bottom:0">Statistical model output • Not a diagnosis</p></div>',
            unsafe_allow_html=True
        )

        st.markdown("### Probability profile / Probability প্রোফাইল")
        c1,c2,c3=st.columns(3)
        for col,risk in zip([c1,c2,c3],["High","Moderate","Low"]):
            with col:
                st.metric(f"{risk} Risk",f"{probs.get(risk,0):.2%}")

        pdf=pd.DataFrame({"Risk":list(probs.keys()),"Probability":list(probs.values())}).sort_values("Probability",ascending=False)
        st.bar_chart(pdf.set_index("Risk"),y="Probability",use_container_width=True)

        st.markdown("### Patient snapshot / রোগীর সারাংশ")
        p=st.session_state.patient_data or {}
        rows=[]
        for f,v in p.items():
            bn,meaning,unit,ref=info(f)
            rows.append({"Parameter":f,"বাংলা":bn,"Value":v,"Unit":unit,"Reference":ref})
        st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)

        flags=clinical_flags(p)
        if flags:
            st.markdown("### Reference-based flags / Reference অনুযায়ী flags")
            for name,msg,kind in flags:
                if kind=="red": st.error(f"{name}: {msg}")
                else: st.warning(f"{name}: {msg}")

        st.markdown("### Export / রিপোর্ট সংরক্ষণ")
        st.download_button(
            "⬇️ Download assessment report",
            data=report_text(),
            file_name="personalised_healthcare_assessment.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.warning(
            "Research prototype only / শুধুমাত্র গবেষণার প্রোটোটাইপ। "
            "Model probabilities are statistical outputs and should not be used alone for diagnosis or treatment."
        )

# ============================================================
# WHAT-IF SIMULATOR
# ============================================================
elif page=="What-if Simulator":
    st.subheader("What-if Simulator / What-if বিশ্লেষণ")
    st.caption("Explore model sensitivity by changing selected inputs. This is NOT a causal treatment simulator.")

    r=st.session_state.result
    p=st.session_state.patient_data

    if not r or not p:
        st.info("Complete a patient assessment first. / আগে patient assessment সম্পন্ন করুন।")
    else:
        st.markdown(
            f'<div class="card"><div class="section-kicker">CURRENT MODEL OUTPUT</div>'
            f'<h3>{r["prediction"]} Risk</h3>'
            f'<p style="color:#667085">Change selected variables and compare the model output.</p></div>',
            unsafe_allow_html=True
        )

        scenario=dict(p)
        numeric_candidates=[f for f in ["LDL","HDL","Triglycerides","BMI","Systolic_BP","Diastolic_BP","Sleep_Hours","Physical_Activity_Level","Smoking_Status"] if f in features and f in p]

        if not numeric_candidates:
            st.info("No supported what-if variables are available in this model configuration.")
        else:
            a,b=st.columns(2)

            if "LDL" in numeric_candidates:
                with a:
                    scenario["LDL"]=st.number_input("LDL — What-if / LDL পরিবর্তন",value=float(p["LDL"]),step=1.0,key="wf_ldl")
            if "Triglycerides" in numeric_candidates:
                with b:
                    scenario["Triglycerides"]=st.number_input("Triglycerides — What-if / TG পরিবর্তন",value=float(p["Triglycerides"]),step=1.0,key="wf_tg")
            if "BMI" in numeric_candidates:
                with a:
                    scenario["BMI"]=st.number_input("BMI — What-if / BMI পরিবর্তন",value=float(p["BMI"]),step=.1,key="wf_bmi")
            if "Systolic_BP" in numeric_candidates:
                with b:
                    scenario["Systolic_BP"]=st.number_input("Systolic BP — What-if / BP পরিবর্তন",value=float(p["Systolic_BP"]),step=1.0,key="wf_sbp")
            if "Smoking_Status" in numeric_candidates:
                with a:
                    scenario["Smoking_Status"]=st.selectbox("Smoking Status — What-if",CATS["Smoking_Status"],index=CATS["Smoking_Status"].index(p["Smoking_Status"]) if p["Smoking_Status"] in CATS["Smoking_Status"] else 0,key="wf_smoke")
            if "Physical_Activity_Level" in numeric_candidates:
                with b:
                    scenario["Physical_Activity_Level"]=st.selectbox("Activity — What-if / সক্রিয়তা",CATS["Physical_Activity_Level"],index=CATS["Physical_Activity_Level"].index(p["Physical_Activity_Level"]) if p["Physical_Activity_Level"] in CATS["Physical_Activity_Level"] else 0,key="wf_activity")

            X0=pd.DataFrame([{f:p.get(f,DEFAULTS.get(f,0)) for f in features}])[features]
            X1=pd.DataFrame([{f:scenario.get(f,DEFAULTS.get(f,0)) for f in features}])[features]
            base_probs=model.predict_proba(X0)[0]
            new_probs=model.predict_proba(X1)[0]
            base={c:float(v) for c,v in zip(classes,base_probs)}
            new={c:float(v) for c,v in zip(classes,new_probs)}

            st.markdown("### Before vs What-if / আগে বনাম পরিবর্তনের পর")
            cols=st.columns(3)
            for col,c in zip(cols,["High","Moderate","Low"]):
                delta=(new.get(c,0)-base.get(c,0))*100
                with col:
                    st.metric(c,f"{new.get(c,0):.2%}",f"{delta:+.2f} pp")

            compare=pd.DataFrame({
                "Risk":classes,
                "Baseline": [base.get(c,0) for c in classes],
                "What-if":[new.get(c,0) for c in classes]
            }).set_index("Risk")
            st.bar_chart(compare,use_container_width=True)

            st.info(
                "Interpretation / ব্যাখ্যা: the displayed change is model sensitivity under altered inputs. "
                "It does not establish that changing a variable will cause a clinical outcome."
            )

# ============================================================
# REFERENCE GUIDE
# ============================================================
elif page=="Reference Guide":
    st.subheader("Reference Guide / রেফারেন্স গাইড")
    st.caption("General educational references. Clinical interpretation can vary by person, laboratory, sex and context.")

    search=st.text_input("Search term / টার্ম খুঁজুন",placeholder="e.g. LDL, BMI, blood pressure...")
    rows=[]
    for f in features:
        bn,meaning,unit,ref=info(f)
        rows.append({"Term":f,"বাংলা":bn,"Meaning / অর্থ":meaning,"Unit":unit,"Reference":ref})
    ref_df=pd.DataFrame(rows)
    if search:
        mask=ref_df.astype(str).apply(lambda x:x.str.contains(search,case=False,na=False)).any(axis=1)
        ref_df=ref_df[mask]
    st.dataframe(ref_df,use_container_width=True,hide_index=True,height=650)

    st.markdown("### Important terminology / গুরুত্বপূর্ণ টার্ম")
    st.markdown("""
    **PRS — Polygenic Risk Score:** multiple genetic variants combined into a statistical susceptibility score.  
    **CVD — Cardiovascular Disease:** diseases affecting the heart and blood vessels / হৃদ্‌যন্ত্র ও রক্তনালীর রোগসমূহ।  
    **T2D — Type 2 Diabetes:** a common form of diabetes / টাইপ-২ ডায়াবেটিস।  
    **eGFR — estimated Glomerular Filtration Rate:** an estimate of kidney filtration.  
    **HRV — Heart Rate Variability:** variation in time between heartbeats.
    """)

    st.warning(
        "Reference ranges are educational and not a substitute for clinical assessment. "
        "PRS/genetic variables have no universal clinical reference interval in this prototype."
    )

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown(
    '<div class="footer">Personalised Healthcare Risk Assessment · AI/ML Research Prototype · '
    'Bilingual Interface · Not a diagnostic or treatment system</div>',
    unsafe_allow_html=True
)
