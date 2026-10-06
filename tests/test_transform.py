import pandas as pd
from transform import transform


def test_transform_removes_duplicates():
    df = pd.DataFrame({
        "name": ["A", "A", "B"],
        "salary": [10000, 10000, 20000]
    })

    result = transform(df)

    assert len(result) == 2