import pandas as pd
import numpy as np

def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Drop rows with missing critical IDs
    id_cols = [col for col in df.columns if 'id' in col]
    if id_cols:
        df = df.dropna(subset=id_cols)

    # Drop columns and rows with >50% missing
    df = df.loc[:, df.isnull().mean() < 0.5]
    df = df[df.isnull().mean(axis=1) < 0.5]

    # Filter gender/sex columns to only allow 'M' and 'F'
    for col in df.columns:
        if col in ['gender', 'sex']:
            df[col] = df[col].astype(str).str.upper().str.strip()
            df = df[df[col].isin(['M', 'F'])]

    # Convert name-like columns to title case (first letter uppercase)
    for col in df.columns:
        if 'name' in col and df[col].dtype == object:
            df[col] = df[col].str.strip().str.title()

    # Remove outliers using IQR
    for col in df.select_dtypes(include=np.number).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        df = df[(df[col] >= lower) & (df[col] <= upper)]

    return df.reset_index(drop=True)