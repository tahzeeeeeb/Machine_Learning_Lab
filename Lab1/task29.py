import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.randn(500)
meanValue = numbers.mean()

plt.hist(numbers, bins=20, color="skyblue", edgecolor="black")
plt.axvline(meanValue, color="red", linestyle="--", label="Mean")
plt.title("Histogram of 500 Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

print("Mean:", meanValue)
