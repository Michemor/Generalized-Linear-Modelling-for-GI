import streamlit as st
import pandas as pd
import process_file as pf
import pages.premium_prediction as premium
import pages.claim_prediction as claim 

import sys
sys.path.append("pages")

if 'page' not in st.session_state:
    st.session_state.page = 'App' 

# Navigation function
def set_page(page_name):
    st.session_state.page = page_name

# Navigation buttons
st.sidebar.button("App", on_click=lambda: set_page("App"))
st.sidebar.button("Premium", on_click=lambda: set_page("Premium"))
st.sidebar.button("Claim", on_click=lambda: set_page("Claim"))


if st.session_state.page == 'App':
    st.title(" 🚗 Auto InsurancePricing")
    st.text("You can have a view of the dataset below and make changes")
    pf.process_file()

elif st.session_state.page == 'Premium':
    st.title("Premium Prediction")
    st.write("This is the premium prediction page.")
    premium.premium_prediction()

elif st.session_state.page == 'Claim':
    st.title("Claim Prediction")
    claim.claim_prediction()
