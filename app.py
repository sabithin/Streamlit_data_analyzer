import pandas as pd
import numpy as np
import streamlit as st
from cleaning import clean_data
from modules.home import show_home
from modules.column_selector import show_column_selector
from modules.cleaned_data import show_cleaning
from modules.show_summary import show_summary_stats
from modules.filter_rows import show_row_filter


#Sidebar navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["🏠Home","📊Summary Statistics", "📌Select Columns", "🔎 Filter Rows","🧹Clean"])
if page == "🏠Home":
    show_home()
elif page == "🧹Clean":
    show_cleaning()
elif page == "📌Select Columns":
    show_column_selector()
elif page == "📊Summary Statistics":
    show_summary_stats()
elif page == "🔎 Filter Rows":
    show_row_filter()