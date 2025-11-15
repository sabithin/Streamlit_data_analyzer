import pandas as pd
import streamlit as st  
import numpy as np
def show_column_selector():
    st.title("📌 Select Columns")

    if 'df' in st.session_state:
        df = st.session_state.get('df_cleaned', st.session_state.df)
        
        selected_cols = st.multiselect("Choose columns to display", options=df.columns.tolist())

        if selected_cols:
            st.subheader("Selected Columns")
            st.dataframe(df[selected_cols])
            st.caption("Showing first 5 rows of selected columns")
        else:
            st.info("Select one or more columns to view the data.")
    else:
        st.warning("Please upload a CSV file first from the Home page.")