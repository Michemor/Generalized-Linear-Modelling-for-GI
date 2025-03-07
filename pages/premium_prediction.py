import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import streamlit as st


def premium_prediction():
    with open("premiumModel.pkl", "rb") as model_file:
        premium_model = pickle.load(model_file)

    df = pd.read_csv("car_insurance_dataset.csv")

     # User Input Form
    with st.form("premium_form"):
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        gender_male = st.radio("Gender", ["Female (0)", "Male (1)"], index=1)
        driving_experience = st.number_input("Driving Experience (years)", min_value=0, max_value=50, value=5)
        marital_status_widowed = st.radio("Marital Status (Widowed)", ["No (0)", "Yes (1)"], index=0)
        vehicle_age = st.number_input("Vehicle Age (years)", min_value=0, max_value=30, value=5)
        coverage_level_premium = st.radio("Coverage Level Premium", ["No (0)", "Yes (1)"], index=1)
        claim_cost = st.number_input("Claim Cost ($)", min_value=0, max_value=50000, value=5000)

        gender_male = 1 if gender_male == "Male (1)" else 0
        marital_status_widowed = 1 if marital_status_widowed == "Yes (1)" else 0
        coverage_level_premium = 1 if coverage_level_premium == "Yes (1)" else 0

        # Submit Button
        submit = st.form_submit_button("Predict Premium")
    
     # When user submits form, make a prediction
    if submit:
        input_data = pd.DataFrame({
            "Age": [age],
            "Gender_Male": [gender_male],  # Extract number from string
            "Driving_Experience": [driving_experience],
            "Marital_Status_Widowed": [marital_status_widowed],
            "Vehicle_Age": [vehicle_age],
            "Coverage_Level_Premium": [coverage_level_premium],
            "Claim_Cost": [claim_cost]
        })

        # Make prediction
        predicted_premium = premium_model.predict(input_data)[0]

        # Display predicted premium
        st.success(f"💰 **Predicted Annual Premium:** Kshs.{predicted_premium:.2f}")

      