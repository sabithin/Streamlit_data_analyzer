import streamlit as st
import pandas as pd 
import numpy as np
def show_home():
    st.title("🏠 Welcome to Data Analyzer")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], key="file_uploader")

    # ✅ If user removed the file (clicked 'x'), clear session state
    if uploaded_file is None and 'df' in st.session_state:
        st.session_state.pop('df', None)
        st.session_state.pop('df_cleaned', None)
        st.session_state.pop('file_name', None)
        st.info("No Files uploaded. Please upload a new CSV.")

    # ✅ If a new file is uploaded, save it
    elif uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.session_state.file_name = uploaded_file.name
        st.success("File uploaded successfully!")

    # ✅ Show preview if data exists
    if 'df' in st.session_state:
        st.dataframe(st.session_state.df.head())
        st.caption("Showing first 5 rows of the dataset")