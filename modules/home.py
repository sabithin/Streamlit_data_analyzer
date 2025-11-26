import streamlit as st
import pandas as pd 
import numpy as np
def show_home():
    st.title("🏠 Welcome to Data Analyzer")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], key="file_uploader")

    # If a new file is uploaded → save it
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.session_state.file_name = uploaded_file.name
        st.success("File uploaded successfully!")

    # ✅ Show preview if data exists
    if 'df' in st.session_state:
        st.dataframe(st.session_state.df.head())
        st.markdown(f"**File Name:** {st.session_state.file_name}")
        st.caption("Showing first 5 rows of the dataset")

        # 🔽 Add remove button
        if st.button("🗑️ Remove Data"):
            st.session_state.pop('df', None)
            st.session_state.pop('df_cleaned', None)
            st.session_state.pop('file_name', None)
            st.success("Data removed successfully!")