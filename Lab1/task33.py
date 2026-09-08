import pandas as pd
import matplotlib.pyplot as plt

data = {
    "date": ["2026-01-05", "2026-01-02", "2026-01-08", "2026-01-01",
             "2026-01-06", "2026-01-03", "2026-01-07", "2026-01-04"],
    "sales": [220, 150, 310, 120, 260, 180, 290, 200]
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

print(df)

df.plot(x="date", y="sales", title="Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
