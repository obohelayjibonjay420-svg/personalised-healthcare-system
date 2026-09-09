import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Personalised Healthcare",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CUSTOM CSS — modern dashboard
# ============================================================
st.markdown("""
<style>
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    .hero {
        padding: 1.5rem 1.7rem;
        border-radius: 22px;
        background: linear-gradient(135deg, #eef5ff 0%, #f8fbff 55%, #f4efff 100%);
        border: 1px solid rgba(80,100,150,.12);
        margin-bottom: 1.2rem;
    }

    .hero-title {
        font-size: 2.25rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -.04em;
    }

    .hero-sub {
        color: #5f6b7a;
        margin-top: .35rem;
        font-size: 1rem;
    }

    .section-card {
        padding: 1rem 1.1rem;
        border-radius: 16px;
        border: 1px solid rgba(80,100,150,.13);
        background: rgba(255,255,255,.72);
        margin-bottom: .8rem;
    }

    .mini-label {
        font-size: .78rem;
        color: #697586;
        text-transform: uppercase;
        letter-spacing: .07em;
        font-weight: 700;
    }

    .mini-value {
        font-size: 1.55rem;
        font-weight: 800;
        margin-top: .15rem;
    }

    .meaning {
        color: #667085;
        font-size: .78rem;
        line-height: 1.35;
        margin-top: -.25rem;
        margin-bottom: .25rem;
    }

    .ref {
        color: #475467;
        font-size: .73rem;
        line-height: 1.35;
    }

    .risk-high {
        padding: 1.25rem;
        border-radius: 18px;
        background: #fff0f0;
        border: 1px solid #f2b8b8;
    }

    .risk-mod {
        padding: 1.25rem;
        border-radius: 18px;
        background: #fff8e8;
        border: 1px solid #ead19a;
    }

    .risk-low {
        padding: 1.25rem;
        border-radius: 18px;
        background: #effaf3;
        border: 1px solid #b8dfc3;
    }

    .risk-number {
        font-size: 2.1rem;
        font-weight: 850;
        line-height: 1;
    }

    .risk-name {
        font-size: .82rem;
        font-weight: 700;
        letter-spacing: .08em;
        margin-top: .45rem;
    }

    .badge {
        display: inline-block;
        padding: .25rem .55rem;
        border-radius: 999px;
        font-size: .72rem;
        font-weight: 700;
        background: #f2f4f7;
        color: #475467;
    }

    .footer-note {
        color: #667085;
        font-size: .75rem;
        text-align: center;
        padding: 1rem 0 .2rem;
    }

    [data-testid="stMetric"] {
        border: 1px solid rgba(80,100,150,.12);
        padding: .7rem;
        border-radius: 14px;
        background: rgba(255,255,255,.72);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# MODEL
# ============================================================
@st.cache_resource
def load_model():
    model = joblib.load("final_model_artifacts/calibrated_final_model.pkl")
    with open("final_model_artifacts/model_config.json", encoding="utf-8") as f:
        config = json.load(f)
    return model, config

model, config = load_model()
features = config["features"]

# ============================================================
# METADATA
# ============================================================
META = {
    "Age": ("বয়স", "Age in completed years / পূর্ণ বয়স", "years",
            "Adult input; model-specific relationship"),
    "BMI": ("বডি মাস ইনডেক্স", "Weight relative to height / ওজন-উচ্চতার অনুপাত", "kg/m²",
            "<18.5 underweight | 18.5–24.9 healthy | 25–29.9 overweight | ≥30 obesity"),
    "Cholesterol": ("মোট কোলেস্টেরল", "Total blood cholesterol / রক্তের মোট কোলেস্টেরল", "mg/dL",
                    "<200 generally desirable"),
    "Glucose_Level": ("রক্তের গ্লুকোজ", "Blood glucose / রক্তে শর্করার মাত্রা", "mg/dL",
                      "Fasting: ~70–99 normal; fasting status matters"),
    "HbA1c": ("এইচবিএ১সি", "Average glucose marker over ~2–3 months / গত ২–৩ মাসের গড় শর্করার সূচক", "%",
              "<5.7% normal | 5.7–6.4% prediabetes range | ≥6.5% diabetes range"),
    "Systolic_BP": ("সিস্টোলিক BP", "Pressure when heart contracts / হৃদপিণ্ড সংকোচনের সময়ের চাপ", "mmHg",
                    "<120 normal | 120–129 elevated | ≥130 higher"),
    "Diastolic_BP": ("ডায়াস্টোলিক BP", "Pressure when heart relaxes / হৃদপিণ্ড শিথিল অবস্থার চাপ", "mmHg",
                     "<80 normal | ≥80 higher"),
    "LDL": ("এলডিএল", "Low-density lipoprotein; often called 'bad' cholesterol / খারাপ কোলেস্টেরল", "mg/dL",
            "<100 generally desirable; target varies by risk"),
    "HDL": ("এইচডিএল", "High-density lipoprotein; often called 'good' cholesterol / ভালো কোলেস্টেরল", "mg/dL",
            "≥60 best; low thresholds differ by sex"),
    "Triglycerides": ("ট্রাইগ্লিসারাইড", "A major blood fat / রক্তের এক ধরনের চর্বি", "mg/dL",
                      "<150 normal | 150–199 borderline high | ≥200 high"),
    "CRP": ("সি-রিঅ্যাকটিভ প্রোটিন", "Inflammation-related biomarker / প্রদাহের সঙ্গে সম্পর্কিত সূচক", "mg/L",
            "Assay/context dependent; hs-CRP uses separate categories"),
    "eGFR": ("কিডনি ফিল্টারিং রেট", "Estimated kidney filtration / কিডনির আনুমানিক filtration", "mL/min/1.73m²",
             "≥90 usually normal; 60–89 mildly decreased; <60 reduced"),
    "Waist_Circumference": ("কোমরের পরিধি", "Waist circumference / কোমরের চারপাশের মাপ", "cm",
                            "Risk cutoffs vary by sex and population"),
    "Resting_Heart_Rate": ("বিশ্রামকালীন হার্ট রেট", "Heart beats per minute at rest / বিশ্রামে হৃদস্পন্দন", "bpm",
                           "Typical adult resting range ~60–100"),
    "HRV": ("হার্ট রেট ভ্যারিয়েবিলিটি", "Variation between heartbeats / পরপর হৃদস্পন্দনের সময়ের পরিবর্তন",
            "device-dependent", "No single universal clinical reference"),
    "Sleep_Hours": ("ঘুমের সময়", "Average sleep duration / প্রতিদিন গড় ঘুম", "hours/day",
                    "Adults commonly recommended ~7–9 h/night"),
    "PRS_Cardiometabolic": ("কার্ডিওমেটাবলিক PRS", "Polygenic susceptibility score / জেনেটিক susceptibility score",
                            "model score", "No universal clinical range; model-specific"),
    "PRS_Type2Diabetes": ("টাইপ-২ ডায়াবেটিস PRS", "Polygenic susceptibility score / জেনেটিক susceptibility score",
                          "model score", "No universal clinical range; model-specific"),
    "APOE_e4_Carrier": ("APOE-e4 carrier", "Presence of APOE ε4 allele / APOE ε4 allele আছে কি না", "0/1",
                        "0 = No | 1 = Yes"),
    "BRCA_Pathogenic_Variant": ("BRCA pathogenic variant", "Pathogenic BRCA variant / pathogenic variant আছে কি না",
                                "0/1", "0 = No | 1 = Yes"),
    "Family_History_CVD": ("পরিবারে CVD ইতিহাস", "Family history of cardiovascular disease / পরিবারের হৃদ্‌রোগের ইতিহাস",
                           "0/1", "0 = No | 1 = Yes"),
    "Family_History_T2D": ("পরিবারে T2D ইতিহাস", "Family history of type 2 diabetes / পরিবারের টাইপ-২ ডায়াবেটিসের ইতিহাস",
                           "0/1", "0 = No | 1 = Yes"),
}

CATS = {
    "Gender": ["Female", "Male"],
    "Smoking_Status": ["Non-smoker", "Former smoker", "Current smoker"],
    "Alcohol_Consumption": ["Low", "Moderate", "High", "Unknown"],
    "Physical_Activity_Level": ["Sedentary", "Lightly Active", "Moderately Active", "Highly Active"],
    "Diet_Type": ["Balanced", "High Protein", "Keto", "Mediterranean", "Vegan", "Vegetarian"],
    "Sleep_Quality": ["Excellent", "Good", "Fair", "Poor"],
}

DEFAULTS = {
    "Age": 40.0, "BMI": 24.0, "Cholesterol": 190.0, "Glucose_Level": 90.0,
    "HbA1c": 5.4, "Systolic_BP": 120.0, "Diastolic_BP": 80.0,
    "LDL": 100.0, "HDL": 50.0, "Triglycerides": 120.0, "CRP": 1.0,
    "eGFR": 90.0, "Waist_Circumference": 85.0, "Resting_Heart_Rate": 70.0,
    "HRV": 50.0, "Sleep_Hours": 7.0, "PRS_Cardiometabolic": 0.0,
    "PRS_Type2Diabetes": 0.0, "APOE_e4_Carrier": 0, "BRCA_Pathogenic_Variant": 0,
    "Family_History_CVD": 0, "Family_History_T2D": 0,
}

# ============================================================
# HELPERS
# ============================================================
def meta_text(feature):
    bn, meaning, unit, ref = META.get(
        feature, (feature, "Model input / মডেল ইনপুট", "", "No universal reference")
    )
    return bn, meaning, unit, ref

def numeric_input(feature, key_prefix="p"):
    bn, meaning, unit, ref = meta_text(feature)
    return st.number_input(
        f"{feature} — {bn}",
        value=float(DEFAULTS.get(feature, 0.0)),
        step=0.1,
        help=f"Meaning / অর্থ: {meaning}\nReference: {ref}",
        key=f"{key_prefix}_{feature}",
    )

def select_input(feature, key_prefix="p"):
    bn, meaning, unit, ref = meta_text(feature)
    return st.selectbox(
        f"{feature} — {bn}",
        CATS[feature],
        help=f"Meaning / অর্থ: {meaning}\nReference: {ref}",
        key=f"{key_prefix}_{feature}",
    )

def yes_no_input(feature, key_prefix="p"):
    bn, meaning, unit, ref = meta_text(feature)
    return st.selectbox(
        f"{feature} — {bn}",
        [0, 1],
        format_func=lambda x: "No / না" if x == 0 else "Yes / হ্যাঁ",
        help=f"Meaning / অর্থ: {meaning}\nReference: {ref}",
        key=f"{key_prefix}_{feature}",
    )

def status_bmi(v):
    if v < 18.5: return "Underweight / কম ওজন"
    if v < 25: return "Healthy range / স্বাভাবিক"
    if v < 30: return "Overweight / অতিরিক্ত ওজন"
    return "Obesity range / স্থূলতা"

def status_bp(sys, dia):
    if sys < 120 and dia < 80: return "Normal / স্বাভাবিক"
    if sys < 130 and dia < 80: return "Elevated / কিছুটা বেশি"
    if sys < 140 or dia < 90: return "Higher / বেশি"
    return "High / উচ্চ"

def status_ldl(v):
    if v < 100: return "Generally desirable"
    if v < 130: return "Near/above desirable"
    if v < 160: return "Borderline high"
    if v < 190: return "High"
    return "Very high"

def status_tg(v):
    if v < 150: return "Normal"
    if v < 200: return "Borderline high"
    if v < 500: return "High"
    return "Very high"

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="hero">
  <div class="mini-label">RESEARCH • AI • PERSONAL HEALTH</div>
  <div class="hero-title">Personalised Healthcare Risk Assessment</div>
  <div class="hero-sub">ব্যক্তিকেন্দ্রিক স্বাস্থ্যঝুঁকি মূল্যায়ন • Interactive bilingual research prototype</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
with st.sidebar:
    st.markdown("## 🩺 Health Assessment")
    st.caption("বাংলা + English")
    page = st.radio(
        "Navigate / নেভিগেট",
        ["Dashboard", "Patient Input", "Risk Results", "Reference Guide"],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown("**Model status**")
    st.success("Loaded • Ready")
    st.caption(f"{len(features)} model input features")
    st.divider()
    st.caption("Research prototype only. Not for diagnosis or treatment.")

# ============================================================
# PATIENT INPUT
# ============================================================
if "patient_data" not in st.session_state:
    st.session_state.patient_data = None
if "result" not in st.session_state:
    st.session_state.result = None

if page == "Dashboard":
    st.subheader("Welcome / স্বাগতম")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Model Inputs", len(features))
    c2.metric("Risk Classes", len(model.classes_))
    c3.metric("Interface", "Bilingual")
    c4.metric("Mode", "Research")

    st.markdown("### Assessment workflow / মূল্যায়নের ধাপ")
    a, b, c = st.columns(3)
    with a:
        st.markdown('<div class="section-card"><b>01 • Enter</b><br>রোগীর clinical, lifestyle & genetic information দিন।</div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="section-card"><b>02 • Assess</b><br>Model probability ও predicted risk দেখুন।</div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="section-card"><b>03 • Interpret</b><br>Reference values ও model output একসাথে review করুন।</div>', unsafe_allow_html=True)

    st.info("Go to **Patient Input** from the left sidebar to start. / শুরু করতে বাম পাশের Patient Input নির্বাচন করুন।")

elif page == "Patient Input":
    st.subheader("Patient Input / রোগীর তথ্য")
    st.caption("Each field includes meaning, unit and a reference note. / প্রতিটি ফিল্ডে অর্থ, unit ও reference note দেওয়া আছে।")

    with st.form("advanced_patient_form"):
        tab1, tab2, tab3, tab4 = st.tabs([
            "👤 Profile / প্রোফাইল",
            "❤️ Clinical / ক্লিনিক্যাল",
            "🏃 Lifestyle / জীবনযাপন",
            "🧬 Genetics / জেনেটিক"
        ])

        patient = {}

        with tab1:
            x1, x2 = st.columns(2)
            with x1:
                if "Age" in features: patient["Age"] = numeric_input("Age")
                if "Gender" in features: patient["Gender"] = select_input("Gender")
                if "BMI" in features: patient["BMI"] = numeric_input("BMI")
                if "Waist_Circumference" in features: patient["Waist_Circumference"] = numeric_input("Waist_Circumference")
            with x2:
                if "Smoking_Status" in features: patient["Smoking_Status"] = select_input("Smoking_Status")
                if "Alcohol_Consumption" in features: patient["Alcohol_Consumption"] = select_input("Alcohol_Consumption")
                if "Sleep_Quality" in features: patient["Sleep_Quality"] = select_input("Sleep_Quality")
                if "Sleep_Hours" in features: patient["Sleep_Hours"] = numeric_input("Sleep_Hours")

        with tab2:
            x1, x2 = st.columns(2)
            clinical = [
                "Cholesterol", "Glucose_Level", "HbA1c", "Systolic_BP",
                "Diastolic_BP", "LDL", "HDL", "Triglycerides", "CRP",
                "eGFR", "Resting_Heart_Rate", "HRV"
            ]
            for i, f in enumerate([x for x in clinical if x in features]):
                with (x1 if i % 2 == 0 else x2):
                    patient[f] = numeric_input(f)

        with tab3:
            x1, x2 = st.columns(2)
            if "Physical_Activity_Level" in features:
                with x1: patient["Physical_Activity_Level"] = select_input("Physical_Activity_Level")
            if "Diet_Type" in features:
                with x2: patient["Diet_Type"] = select_input("Diet_Type")

            for f in ["Stress_Level", "Depression_Score", "Anxiety_Score", "Social_Isolation_Index"]:
                if f in features:
                    patient[f] = numeric_input(f)

        with tab4:
            st.caption("Genetic variables are susceptibility indicators, not diagnoses. / জেনেটিক ভ্যারিয়েবল susceptibility বোঝায়, রোগ নির্ণয় নয়।")
            x1, x2 = st.columns(2)
            genetic = [
                "PRS_Cardiometabolic", "PRS_Type2Diabetes",
                "APOE_e4_Carrier", "BRCA_Pathogenic_Variant",
                "Family_History_CVD", "Family_History_T2D"
            ]
            for i, f in enumerate([x for x in genetic if x in features]):
                with (x1 if i % 2 == 0 else x2):
                    if f in ["APOE_e4_Carrier", "BRCA_Pathogenic_Variant",
                             "Family_History_CVD", "Family_History_T2D"]:
                        patient[f] = yes_no_input(f)
                    else:
                        patient[f] = numeric_input(f)

        submitted = st.form_submit_button(
            "🔎 Assess Risk / স্বাস্থ্যঝুঁকি মূল্যায়ন",
            use_container_width=True,
            type="primary"
        )

    if submitted:
        # Ensure exact feature order
        X = pd.DataFrame([{f: patient.get(f, DEFAULTS.get(f, 0)) for f in features}])[features]
        try:
            pred = model.predict(X)[0]
            probs = model.predict_proba(X)[0]
            st.session_state.patient_data = patient
            st.session_state.result = {
                "prediction": pred,
                "probabilities": {c: float(p) for c, p in zip(model.classes_, probs)}
            }
            st.success("Assessment completed / মূল্যায়ন সম্পন্ন হয়েছে। Go to Risk Results.")
        except Exception as e:
            st.error("Prediction failed / Prediction সম্পন্ন হয়নি।")
            st.code(str(e))

    # Live clinical snapshot
    if st.session_state.patient_data:
        p = st.session_state.patient_data
        st.divider()
        st.markdown("### Quick clinical snapshot / দ্রুত ক্লিনিক্যাল সারাংশ")
        cards = []
        if "BMI" in p: cards.append(("BMI", p["BMI"], status_bmi(p["BMI"])))
        if "Systolic_BP" in p and "Diastolic_BP" in p:
            cards.append(("BP", f"{p['Systolic_BP']:.0f}/{p['Diastolic_BP']:.0f}", status_bp(p["Systolic_BP"], p["Diastolic_BP"])))
        if "LDL" in p: cards.append(("LDL", f"{p['LDL']:.1f}", status_ldl(p["LDL"])))
        if "Triglycerides" in p: cards.append(("Triglycerides", f"{p['Triglycerides']:.1f}", status_tg(p["Triglycerides"])))

        cols = st.columns(len(cards) if cards else 1)
        for col, (name, value, status) in zip(cols, cards):
            with col:
                st.markdown(f'<div class="section-card"><div class="mini-label">{name}</div><div class="mini-value">{value}</div><div class="badge">{status}</div></div>', unsafe_allow_html=True)

elif page == "Risk Results":
    st.subheader("Risk Results / ঝুঁকির ফলাফল")

    if not st.session_state.result:
        st.warning("No assessment yet. Please complete Patient Input first.")
    else:
        result = st.session_state.result
        pred = result["prediction"]
        probs = result["probabilities"]

        if pred == "High":
            st.markdown('<div class="risk-high"><div class="risk-number">HIGH</div><div class="risk-name">উচ্চ ঝুঁকি</div><p>Model-predicted class. This is not a diagnosis.</p></div>', unsafe_allow_html=True)
        elif pred == "Moderate":
            st.markdown('<div class="risk-mod"><div class="risk-number">MODERATE</div><div class="risk-name">মাঝারি ঝুঁকি</div><p>Model-predicted class. This is not a diagnosis.</p></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="risk-low"><div class="risk-number">LOW</div><div class="risk-name">কম ঝুঁকি</div><p>Model-predicted class. This is not a diagnosis.</p></div>', unsafe_allow_html=True)

        st.markdown("### Model probability / মডেল probability")
        cols = st.columns(3)
        for col, risk in zip(cols, ["High", "Moderate", "Low"]):
            with col:
                st.metric(risk, f"{probs.get(risk, 0):.2%}")

        prob_df = pd.DataFrame({
            "Risk": list(probs.keys()),
            "Probability": list(probs.values())
        }).sort_values("Probability", ascending=False)

        st.bar_chart(prob_df.set_index("Risk"), y="Probability", use_container_width=True)

        st.markdown("### Patient snapshot / রোগীর সারাংশ")
        p = st.session_state.patient_data or {}
        rows = []
        for f, v in p.items():
            bn, meaning, unit, ref = meta_text(f)
            rows.append({
                "Parameter": f,
                "বাংলা নাম": bn,
                "Value": v,
                "Unit": unit,
                "Reference / সাধারণ রেঞ্জ": ref
            })
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

        st.warning(
            "Research prototype only / শুধুমাত্র গবেষণার প্রোটোটাইপ। "
            "Model probabilities are statistical outputs and are not causal treatment effects."
        )

elif page == "Reference Guide":
    st.subheader("Reference Guide / রেফারেন্স গাইড")
    st.caption("General educational reference information. Individual clinical targets may differ.")

    ref_rows = []
    for f in features:
        bn, meaning, unit, ref = meta_text(f)
        ref_rows.append({
            "Term": f,
            "বাংলা": bn,
            "Meaning / অর্থ": meaning,
            "Unit": unit,
            "Reference": ref
        })

    st.dataframe(
        pd.DataFrame(ref_rows),
        use_container_width=True,
        hide_index=True,
        height=650
    )

    st.info(
        "Reference ranges are educational and context-dependent. "
        "Genetic/PRS variables do not have universal clinical reference intervals."
    )

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown(
    '<div class="footer-note">Personalised Healthcare Risk Assessment • '
    'Bilingual AI Research Prototype • Not a diagnostic or treatment system</div>',
    unsafe_allow_html=True
)
