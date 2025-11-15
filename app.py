import pandas as pd
import numpy as np
import streamlit as st
from cleaning import clean_data
from pages.home import show_home
from pages.column_selector import show_column_selector
from pages.cleaned_data import show_cleaning


st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["🏠Home", "🧹Clean", "📌Select Columns"])

if page == "🏠Home":
    show_home()
elif page == "🧹Clean":
    show_cleaning()
elif page == "📌Select Columns":
    show_column_selector()

