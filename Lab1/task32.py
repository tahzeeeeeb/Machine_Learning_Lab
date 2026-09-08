import pandas as pd

data = {
    "name": ["Ali", "Sara", "Omar", "Hina", "Zain",
             "Ayesha", "Bilal", "Fatima", "Usman", "Noor"],
    "math": [85, 90, 70, 60, 95, 78, 88, 92, 65, 80],
    "science": [78, 88, 75, 72, 91, 84, 79, 95, 70, 86],
    "english": [92, 80, 68, 74, 89, 90, 82, 87, 76, 83]
}

df = pd.DataFrame(data)
df["average"] = df[["math", "science", "english"]].mean(axis=1)

print(df)

topPerformer = df.sort_values("average", ascending=False).iloc[0]

print("Top performer:", topPerformer["name"])
print("Average marks:", topPerformer["average"])
