import streamlit as st
import pandas as pd
import numpy as np
from cleaning import clean_data

def show_cleaning():
    if 'df' in st.session_state:
        if st.button("Clean Data"):
            df_cleaned = clean_data(st.session_state.df)
            st.session_state.df_cleaned = df_cleaned
 
            st.header("Cleaned Data:")
            st.dataframe(df_cleaned)
            st.caption("First 5 rows of the cleaned dataset")
    else:
        st.warning("Please upload a CSV file first from the Home page.")
