import pandas as pd
import streamlit as st
st.title("📊Data Analyzer")

uploaded_file = st.file_uploader("Upload your CSV file here",type=["csv"])

if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.header("Preview of your data:")
    st.dataframe(df.head())
    st.caption("First 5 rows of the dataset")
