import streamlit as st
import pandas as pd
import numpy as np


def show_row_filter():
    st.title("🔎 Filter Rows")

    if 'df' in st.session_state:
        df = st.session_state.get('df_cleaned', st.session_state.df)

        col_to_filter = st.selectbox("Select column to filter by", df.columns)

        if col_to_filter:
            unique_values = df[col_to_filter].dropna().unique().tolist()
            selected_values = st.multiselect("Choose values to filter", unique_values)

            if selected_values:
                filtered_df = df[df[col_to_filter].isin(selected_values)]
                st.subheader(f"Filtered Rows: {col_to_filter} in {selected_values}")
                st.dataframe(filtered_df.head())
                st.caption(f"Showing first 5 rows out of {len(filtered_df)} matching rows")
            else:
                st.info("Select one or more values to filter the rows.")
    else:
        st.warning("Please upload a CSV file first from the Home page.")