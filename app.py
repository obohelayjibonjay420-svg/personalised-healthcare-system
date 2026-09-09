
import streamlit as st
import pandas as pd
import joblib
import json

# Load model
model = joblib.load("final_model_artifacts/calibrated_final_model.pkl")

with open("final_model_artifacts/model_config.json") as f:
    config = json.load(f)

features = config["features"]

st.title("Personalised Healthcare Risk Assessment")
st.caption("Research Prototype — Not a Diagnostic System")

st.header("Patient Information")

patient = {}

for feature in features:

    if feature in [
        "Smoking_Status",
        "Alcohol_Consumption",
        "Physical_Activity_Level",
        "Diet_Type",
        "Sleep_Quality"
    ]:
        patient[feature] = st.text_input(feature)

    elif feature in [
        "APOE_e4_Carrier",
        "BRCA_Pathogenic_Variant",
        "Family_History_CVD",
        "Family_History_T2D"
    ]:
        patient[feature] = st.number_input(
            feature, min_value=0, max_value=1, value=0
        )

    else:
        patient[feature] = st.number_input(
            feature, value=0.0
        )

if st.button("Assess Health Risk"):

    X = pd.DataFrame([patient])[features]

    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    st.subheader("Risk Assessment")

    st.write(f"### Risk Category: {prediction}")

    probability_df = pd.DataFrame({
        "Risk Category": model.classes_,
        "Probability": probabilities
    })

    st.dataframe(
        probability_df.style.format(
            {"Probability": "{:.2%}"}
        ),
        use_container_width=True
    )

    st.warning(
        "This is a research prototype. "
        "It should not be used for diagnosis or treatment decisions."
    )
