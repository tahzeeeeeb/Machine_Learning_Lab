import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")

print("Expenses data:")
print(df)

categoryTotals = df.groupby("category")["amount"].sum()

print("Total by category:")
print(categoryTotals)

plt.pie(categoryTotals, labels=categoryTotals.index, autopct="%1.1f%%")
plt.title("Monthly Expenses by Category")
plt.show()
