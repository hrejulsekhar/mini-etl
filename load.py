def load(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Data loaded to: {output_path}")