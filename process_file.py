import pandas as pd
import streamlit as st



def process_file():

    
    df = pd.read_csv("car_insurance_dataset.csv")
    num_rows = st.slider("Select number of rows to display", 1, len(df), 250)
    # drop unrelated columns

    st.dataframe(df, use_container_width=True)

    edited_df = st.data_editor(data=df, num_rows="dynamic")

    # User selects number of rows to display
    
    # Show the selected number of rows
    st.dataframe(df.head(num_rows))

    return edited_df

