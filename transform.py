def transform(df):
    df = df.copy()

    # Fill missing values
    df = df.fillna(0)

    # Remove duplicate rows
    df = df.drop_duplicates()

    print(f"Rows after transformation: {len(df)}")

    return df