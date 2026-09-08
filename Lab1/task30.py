import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6]
sales = [120, 150, 130, 170, 160, 190]

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0][0].plot(months, sales, color="blue")
ax[0][0].set_title("Line Plot")

ax[0][1].bar(months, sales, color="orange")
ax[0][1].set_title("Bar Chart")

ax[1][0].scatter(months, sales, color="green")
ax[1][0].set_title("Scatter Plot")

ax[1][1].hist(sales, bins=5, color="purple", edgecolor="black")
ax[1][1].set_title("Histogram")

plt.suptitle("Monthly Sales Shown in Four Chart Types")
plt.tight_layout()
plt.show()
