import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

st.set_page_config(
    page_title="Personalised Healthcare Risk Assessment",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Load model
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("final_model_artifacts/calibrated_final_model.pkl")
    with open("final_model_artifacts/model_config.json", encoding="utf-8") as f:
        config = json.load(f)
    return model, config

model, config = load_model()
features = config["features"]

# -----------------------------
# UI dictionaries
# -----------------------------
META = {
    "Age": {
        "bn": "বয়স",
        "unit": "years",
        "meaning": "Age in completed years / পূর্ণ বয়স",
        "ref": "Adult input; model-specific risk relationship"
    },
    "BMI": {
        "bn": "বডি মাস ইনডেক্স",
        "unit": "kg/m²",
        "meaning": "Body Mass Index = weight relative to height / ওজন-উচ্চতার অনুপাত",
        "ref": "<18.5 underweight | 18.5–24.9 healthy | 25–29.9 overweight | ≥30 obesity"
    },
    "Cholesterol": {
        "bn": "মোট কোলেস্টেরল",
        "unit": "mg/dL",
        "meaning": "Total cholesterol in blood / রক্তের মোট কোলেস্টেরল",
        "ref": "<200 desirable"
    },
    "Glucose_Level": {
        "bn": "রক্তের গ্লুকোজ",
        "unit": "mg/dL",
        "meaning": "Blood glucose level / রক্তে শর্করার মাত্রা",
        "ref": "If fasting: ~70–99 normal; interpretation depends on fasting status"
    },
    "HbA1c": {
        "bn": "এইচবিএ১সি",
        "unit": "%",
        "meaning": "Approximate average blood glucose over ~2–3 months / গত ২–৩ মাসের গড় রক্তশর্করার সূচক",
        "ref": "<5.7% generally normal; 5.7–6.4% prediabetes range; ≥6.5% diabetes range"
    },
    "Systolic_BP": {
        "bn": "সিস্টোলিক রক্তচাপ",
        "unit": "mmHg",
        "meaning": "Pressure when the heart contracts / হৃদপিণ্ড সংকোচনের সময়ের চাপ",
        "ref": "<120 normal | 120–129 elevated | 130–139 stage 1 | ≥140 stage 2"
    },
    "Diastolic_BP": {
        "bn": "ডায়াস্টোলিক রক্তচাপ",
        "unit": "mmHg",
        "meaning": "Pressure when the heart relaxes / হৃদপিণ্ড শিথিল অবস্থার চাপ",
        "ref": "<80 normal | 80–89 stage 1 | ≥90 stage 2"
    },
    "LDL": {
        "bn": "এলডিএল কোলেস্টেরল",
        "unit": "mg/dL",
        "meaning": "Low-density lipoprotein; often called 'bad' cholesterol / ধমনিতে plaque জমার সঙ্গে সম্পর্কিত কোলেস্টেরল",
        "ref": "<100 generally desirable; personal targets vary by risk"
    },
    "HDL": {
        "bn": "এইচডিএল কোলেস্টেরল",
        "unit": "mg/dL",
        "meaning": "High-density lipoprotein; often called 'good' cholesterol / রক্ত থেকে cholesterol transport-এ সহায়ক",
        "ref": "≥60 best; <40 low in men; <50 low in women",
    },
    "Triglycerides": {
        "bn": "ট্রাইগ্লিসারাইড",
        "unit": "mg/dL",
        "meaning": "A major blood fat / রক্তের এক ধরনের চর্বি",
        "ref": "<150 normal | 150–199 borderline high | ≥200 high"
    },
    "CRP": {
        "bn": "সি-রিঅ্যাকটিভ প্রোটিন",
        "unit": "mg/L",
        "meaning": "Inflammation-related biomarker / প্রদাহের সঙ্গে সম্পর্কিত সূচক",
        "ref": "Lab- and assay-dependent; hs-CRP uses different cardiovascular categories",
    },
    "eGFR": {
        "bn": "কিডনি ফিল্টারিং রেট",
        "unit": "mL/min/1.73m²",
        "meaning": "Estimated kidney filtration capacity / কিডনির আনুমানিক filtration ক্ষমতা",
        "ref": "≥90 usually normal; 60–89 mildly decreased; <60 may indicate reduced kidney function"
    },
    "Waist_Circumference": {
        "bn": "কোমরের পরিধি",
        "unit": "cm",
        "meaning": "Waist circumference / কোমরের চারপাশের মাপ",
        "ref": "Risk cutoffs vary by sex and population"
    },
    "Resting_Heart_Rate": {
        "bn": "বিশ্রামকালীন হার্ট রেট",
        "unit": "bpm",
        "meaning": "Heart beats per minute at rest / বিশ্রামে প্রতি মিনিটে হৃদস্পন্দন",
        "ref": "Typical adult resting range ~60–100 bpm"
    },
    "HRV": {
        "bn": "হার্ট রেট ভ্যারিয়েবিলিটি",
        "unit": "device-dependent",
        "meaning": "Variation between successive heartbeats / পরপর হৃদস্পন্দনের সময়ের পরিবর্তন",
        "ref": "No single universal clinical reference; depends on method, age and device"
    },
    "Smoking_Status": {
        "bn": "ধূমপানের অবস্থা",
        "unit": "",
        "meaning": "Current smoking status / বর্তমান ধূমপানের অবস্থা",
        "ref": "Non-smoker | Former smoker | Current smoker"
    },
    "Alcohol_Consumption": {
        "bn": "অ্যালকোহল গ্রহণ",
        "unit": "",
        "meaning": "Reported alcohol-consumption category / অ্যালকোহল গ্রহণের শ্রেণি",
        "ref": "Low | Moderate | High | Unknown"
    },
    "Physical_Activity_Level": {
        "bn": "শারীরিক সক্রিয়তার মাত্রা",
        "unit": "",
        "meaning": "Usual physical-activity category / দৈনন্দিন শারীরিক সক্রিয়তার মাত্রা",
        "ref": "Sedentary | Lightly Active | Moderately Active | Highly Active"
    },
    "Diet_Type": {
        "bn": "খাদ্যাভ্যাসের ধরন",
        "unit": "",
        "meaning": "Self-reported diet pattern / খাদ্যাভ্যাসের ধরন",
        "ref": "Balanced | High Protein | Keto | Mediterranean | Vegan | Vegetarian"
    },
    "Sleep_Quality": {
        "bn": "ঘুমের মান",
        "unit": "",
        "meaning": "Self-reported sleep quality / ব্যক্তির নিজের মূল্যায়ন করা ঘুমের মান",
        "ref": "Excellent | Good | Fair | Poor"
    },
    "Sleep_Hours": {
        "bn": "ঘুমের সময়",
        "unit": "hours/day",
        "meaning": "Average sleep duration per day / প্রতিদিন গড়ে কত ঘণ্টা ঘুম",
        "ref": "Adults commonly recommended ~7–9 hours/night"
    },
    "PRS_Cardiometabolic": {
        "bn": "কার্ডিওমেটাবলিক পলিজেনিক রিস্ক স্কোর",
        "unit": "model score",
        "meaning": "Polygenic susceptibility score for cardiometabolic risk / জেনেটিক susceptibility-এর মডেল স্কোর",
        "ref": "No universal clinical reference; interpretation is dataset/model-specific"
    },
    "PRS_Type2Diabetes": {
        "bn": "টাইপ-২ ডায়াবেটিস পলিজেনিক রিস্ক স্কোর",
        "unit": "model score",
        "meaning": "Polygenic susceptibility score for type 2 diabetes / জেনেটিক susceptibility-এর মডেল স্কোর",
        "ref": "No universal clinical reference; interpretation is dataset/model-specific"
    },
    "APOE_e4_Carrier": {
        "bn": "APOE-e4 carrier status",
        "unit": "0/1",
        "meaning": "Whether an APOE ε4 allele is present / APOE ε4 allele আছে কি না",
        "ref": "0 = No | 1 = Yes"
    },
    "BRCA_Pathogenic_Variant": {
        "bn": "BRCA pathogenic variant",
        "unit": "0/1",
        "meaning": "Presence of a pathogenic BRCA variant / pathogenic BRCA variant আছে কি না",
        "ref": "0 = No | 1 = Yes"
    },
    "Family_History_CVD": {
        "bn": "পরিবারে CVD-এর ইতিহাস",
        "unit": "0/1",
        "meaning": "Family history of cardiovascular disease / পরিবারের হৃদ্‌রোগের ইতিহাস",
        "ref": "0 = No | 1 = Yes"
    },
    "Family_History_T2D": {
        "bn": "পরিবারে টাইপ-২ ডায়াবেটিসের ইতিহাস",
        "unit": "0/1",
        "meaning": "Family history of type 2 diabetes / পরিবারের টাইপ-২ ডায়াবেটিসের ইতিহাস",
        "ref": "0 = No | 1 = Yes"
    },
}

CATEGORIES = {
    "Smoking_Status": ["Non-smoker", "Former smoker", "Current smoker"],
    "Alcohol_Consumption": ["Low", "Moderate", "High", "Unknown"],
    "Physical_Activity_Level": ["Sedentary", "Lightly Active", "Moderately Active", "Highly Active"],
    "Diet_Type": ["Balanced", "High Protein", "Keto", "Mediterranean", "Vegan", "Vegetarian"],
    "Sleep_Quality": ["Excellent", "Good", "Fair", "Poor"],
}

# -----------------------------
# Header
# -----------------------------
st.title("🩺 Personalised Healthcare Risk Assessment")
st.markdown("### ব্যক্তিকেন্দ্রিক স্বাস্থ্যঝুঁকি মূল্যায়ন")
st.caption(
    "Research Prototype • গবেষণা-ভিত্তিক প্রোটোটাইপ • Not a diagnosis or treatment system"
)

with st.expander("ℹ️ How to use / কীভাবে ব্যবহার করবেন", expanded=True):
    st.markdown(
        """
        **English:** Enter the patient's available information. Each field shows its
        unit, meaning, and a general reference range where a standard exists.

        **বাংলা:** রোগীর তথ্য দিন। প্রতিটি ফিল্ডের পাশে unit, term-এর অর্থ এবং
        প্রযোজ্য ক্ষেত্রে সাধারণ reference range দেখানো হয়েছে।

        **Important:** The model prediction is a statistical model output. It does
        not prove that changing one variable will cause the predicted risk to change.
        """
    )

# -----------------------------
# Input form
# -----------------------------
patient = {}

with st.form("patient_form"):
    st.subheader("1. Patient Profile / রোগীর প্রাথমিক তথ্য")
    cols = st.columns(2)

    for i, feature in enumerate(features):
        meta = META.get(feature, {
            "bn": feature,
            "unit": "",
            "meaning": "",
            "ref": "No reference range available"
        })

        with cols[i % 2]:
            label = f"{feature} — {meta['bn']}"
            help_text = (
                f"Meaning / অর্থ: {meta['meaning']}\n"
                f"Reference / সাধারণ রেঞ্জ: {meta['ref']}"
            )

            if feature in CATEGORIES:
                patient[feature] = st.selectbox(
                    label,
                    CATEGORIES[feature],
                    help=help_text,
                    key=f"input_{feature}",
                )

            elif feature in [
                "APOE_e4_Carrier",
                "BRCA_Pathogenic_Variant",
                "Family_History_CVD",
                "Family_History_T2D",
            ]:
                patient[feature] = st.selectbox(
                    label,
                    [0, 1],
                    format_func=lambda x: "No / না (0)" if x == 0 else "Yes / হ্যাঁ (1)",
                    help=help_text,
                    key=f"input_{feature}",
                )

            else:
                default = 0.0
                if feature == "Age":
                    default = 40.0
                elif feature == "BMI":
                    default = 24.0
                elif feature == "Cholesterol":
                    default = 190.0
                elif feature == "Glucose_Level":
                    default = 90.0
                elif feature == "HbA1c":
                    default = 5.4
                elif feature == "Systolic_BP":
                    default = 120.0
                elif feature == "Diastolic_BP":
                    default = 80.0
                elif feature == "LDL":
                    default = 100.0
                elif feature == "HDL":
                    default = 50.0
                elif feature == "Triglycerides":
                    default = 120.0
                elif feature == "eGFR":
                    default = 90.0
                elif feature == "Sleep_Hours":
                    default = 7.0
                elif feature == "Resting_Heart_Rate":
                    default = 70.0
                elif feature == "Waist_Circumference":
                    default = 85.0
                elif feature == "HRV":
                    default = 50.0

                patient[feature] = st.number_input(
                    label,
                    value=float(default),
                    step=0.1,
                    help=help_text,
                    key=f"input_{feature}",
                )

            st.caption(
                f"**Meaning:** {meta['meaning']}  \n"
                f"**Reference:** {meta['ref']}"
            )

    submitted = st.form_submit_button(
        "🔎 Assess Health Risk / স্বাস্থ্যঝুঁকি মূল্যায়ন",
        use_container_width=True,
        type="primary",
    )

# -----------------------------
# Prediction
# -----------------------------
if submitted:
    X = pd.DataFrame([patient])[features]

    try:
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]

        prob = {
            cls: float(p)
            for cls, p in zip(model.classes_, probabilities)
        }

        st.divider()
        st.subheader("2. Risk Assessment / ঝুঁকি মূল্যায়ন")

        if prediction == "High":
            st.error("🔴 HIGH RISK / উচ্চ ঝুঁকি")
        elif prediction == "Moderate":
            st.warning("🟠 MODERATE RISK / মাঝারি ঝুঁকি")
        else:
            st.success("🟢 LOW RISK / কম ঝুঁকি")

        # Probability cards
        card_cols = st.columns(3)
        for col, risk in zip(card_cols, ["High", "Moderate", "Low"]):
            with col:
                st.metric(
                    f"{risk} Risk",
                    f"{prob.get(risk, 0):.2%}"
                )

        st.subheader("Risk Probability / ঝুঁকির সম্ভাবনা")
        prob_df = pd.DataFrame({
            "Risk Category": list(prob.keys()),
            "Probability": list(prob.values()),
        }).sort_values("Probability", ascending=False)

        st.bar_chart(
            prob_df.set_index("Risk Category"),
            y="Probability",
            use_container_width=True,
        )

        # Patient snapshot
        st.subheader("3. Clinical Snapshot / রোগীর সারাংশ")

        snapshot_features = [
            "BMI", "Cholesterol", "Glucose_Level", "HbA1c",
            "Systolic_BP", "Diastolic_BP", "LDL", "HDL",
            "Triglycerides", "eGFR", "Sleep_Hours"
        ]

        snapshot = []
        for f in snapshot_features:
            if f in patient:
                meta = META[f]
                snapshot.append({
                    "Parameter / প্যারামিটার": f"{f} ({meta['bn']})",
                    "Value / মান": patient[f],
                    "Unit": meta["unit"],
                    "Reference / সাধারণ রেঞ্জ": meta["ref"],
                })

        st.dataframe(
            pd.DataFrame(snapshot),
            use_container_width=True,
            hide_index=True,
        )

        # Research interpretation
        st.subheader("4. Interpretation / ব্যাখ্যা")

        st.info(
            "The probability values describe the model's estimated class probabilities. "
            "They are not the probability that the patient will definitely develop a disease. "
            "These results should not be used alone for diagnosis, treatment, or medication decisions."
        )

        st.markdown(
            "**বাংলা:** এই probability হলো মডেলের class prediction probability। "
            "এটি রোগী নিশ্চিতভাবে ভবিষ্যতে রোগে আক্রান্ত হবেন—এমন সম্ভাবনা নয়। "
            "Diagnosis, treatment বা medication decision-এর জন্য এই ফল একা ব্যবহার করা যাবে না।"
        )

        # Reference notes
        with st.expander("📚 Reference ranges & terminology / রেফারেন্স রেঞ্জ ও টার্ম"):
            st.markdown(
                """
                - **BMI:** <18.5 underweight; 18.5–24.9 healthy; 25–29.9 overweight; ≥30 obesity.
                - **Blood pressure:** normal <120/<80; elevated systolic 120–129 with diastolic <80;
                  stage 1 ≥130 or ≥80; stage 2 ≥140 or ≥90.
                - **Total cholesterol:** <200 mg/dL is generally desirable.
                - **LDL:** <100 mg/dL is generally desirable for many adults, but individual targets vary.
                - **Triglycerides:** <150 mg/dL is generally normal.
                - **HDL:** ≥60 mg/dL is considered optimal; low thresholds differ by sex.
                - **eGFR:** ≥90 is generally normal; interpretation depends on the clinical context.
                - **Genetic/PRS variables:** no universal clinical reference range; model/dataset-specific.
                """
            )

        st.warning(
            "⚠️ Research prototype only / শুধুমাত্র গবেষণার প্রোটোটাইপ। "
            "Not a diagnostic or treatment system / এটি diagnosis বা treatment system নয়."
        )

    except Exception as e:
        st.error("Prediction failed / Prediction সম্পন্ন হয়নি.")
        st.code(str(e))

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption(
    "Personalised Healthcare Risk Assessment • Research Prototype • "
    "Use validated clinical assessment and professional judgement for real-world care."
)
