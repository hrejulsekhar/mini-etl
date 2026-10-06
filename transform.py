import pandas as pd


def transform(df):
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    return df