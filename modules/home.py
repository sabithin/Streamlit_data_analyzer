import streamlit as st
import pandas as pd 
import numpy as np
def show_home():
    st.title("📊 Data Analyzer")
    st.write("Welcome to your Streamlit Data Analyzer!")
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.success("File uploaded successfully!")
        st.header("Preview of your data:")
        st.dataframe(df.head())
        st.caption("First 5 rows of the dataset")
