import pandas as pd
from transform import transform
from load import load


def extract(file_path):
    df = pd.read_csv(file_path)
    print(f"Extracted rows: {len(df)}")

    df = transform(df)

    print(f"Rows after transformation: {len(df)}")

    return df


if __name__ == "__main__":
    df = extract("data/sample.csv")
    load(df, "output.csv")