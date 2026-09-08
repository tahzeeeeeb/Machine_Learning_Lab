import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Sara", "Omar", "Hina", "Zain", "Ayesha"],
    "score": [85, np.nan, 70, np.nan, 95, 78]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("Missing values before filling:", df["score"].isnull().sum())

meanScore = df["score"].mean()
df["score"] = df["score"].fillna(meanScore)

print("Mean used for filling:", meanScore)
print("DataFrame after filling:")
print(df)
print("Missing values after filling:", df["score"].isnull().sum())
