def transform(df):
    df = df.copy()

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        print("Warning: NULL values found")

    # Fill missing values
    df = df.fillna(0)

    # Remove duplicate rows
    df = df.drop_duplicates()

    print(f"Rows after transformation: {len(df)}")

    return df