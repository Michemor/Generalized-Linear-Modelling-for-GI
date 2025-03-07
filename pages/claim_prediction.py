import pickle
import streamlit as st
import pandas as pd
import numpy as np


def claim_prediction():
    # Initialize session state variables
    if "claim_pred_in_progress" not in st.session_state:
        st.session_state.claim_pred_in_progress = False
    if "claim_pred_result" not in st.session_state:
        st.session_state.claim_pred_result = None

    df = pd.read_csv("car_insurance_dataset.csv")

    with open("claimPredictionModel.pkl", "rb") as f:
        model = pickle.load(f)

    # enter insurer details
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    vehicle_age = st.number_input("Vehicle Age (years)", min_value=0, max_value=30, value=5)
    claim_frequency = st.number_input("Claim Frequency", min_value=0, max_value=10, value=1)
    annual_premium = st.number_input("Annual Premium ($)", min_value=100, max_value=5000, value=1000)
    coverage_level_premium = st.radio("Coverage Level (Premium)", [0, 1], index=0)
    engine_capacity = st.number_input("Engine Capacity (L)", min_value=0.5, max_value=6.0, value=2.0)
    fuel_type_hybrid = st.radio("Fuel Type (Hybrid)", [0, 1], index=0)

    # Prediction Button
    if st.button("Predict Claim Cost"):
        input_data = pd.DataFrame({
            "Age": [age],
            "Vehicle_Age": [vehicle_age],
            "Claim_Frequency": [claim_frequency],
            "Annual_Premium": [annual_premium],
            "Coverage_Level_Premium": [coverage_level_premium],
            "Engine_Capacity": [engine_capacity],
            "Fuel_Type_Hybrid": [fuel_type_hybrid]
        })

        # Make prediction
        predicted_claim_cost = model.predict(input_data)[0]

        # Display result
        st.success(f"💰 **Predicted Claim Cost:** Kshs.{predicted_claim_cost:.2f}")

