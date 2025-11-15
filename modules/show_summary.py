import pandas as pd
import streamlit as st
import numpy as np
def show_summary_stats():
    st.title("📊 Summary Statistics")

    if 'df' in st.session_state:
        df = st.session_state.get('df_cleaned', st.session_state.df)
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if not numeric_cols:
            st.info("No numeric columns found in the dataset.")
            return

        selected_cols = st.multiselect("Select numeric columns", numeric_cols, default=numeric_cols)

        if selected_cols:
            st.subheader("Descriptive Statistics")
            st.dataframe(df[selected_cols].describe().T)

            st.subheader("Mode (Most Frequent Value)")
            mode_df = df[selected_cols].mode().T
            st.dataframe(mode_df.rename(columns={0: 'Mode'}))
        else:
            st.info("Please select at least one column to view statistics.")
    else:
        st.warning("Please upload a CSV file first from the Home page.")
