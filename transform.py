def transform(df):
    df = df.copy()

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        print("Warning: NULL values found")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    print(f"Rows after transformation: {len(df)}")

    return df