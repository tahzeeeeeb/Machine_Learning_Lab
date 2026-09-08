import pandas as pd

data = {
    "name": ["Pen", "Notebook", "Bag", "Bottle", "Calculator", "Lamp"],
    "price": [20, 80, 1200, 350, 900, 600],
    "quantity": [10, 5, 2, 3, 1, 4]
}

df = pd.DataFrame(data)
df["total"] = df["price"] * df["quantity"]

print(df)
