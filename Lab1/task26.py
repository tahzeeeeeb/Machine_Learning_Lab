import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 31)
temperatures = np.array([30, 32, 31, 29, 33, 35, 34, 36, 38, 37,
                         35, 33, 32, 30, 29, 31, 34, 36, 39, 40,
                         38, 37, 35, 34, 33, 31, 30, 32, 35, 36])

plt.plot(days, temperatures)
plt.title("Temperature Readings for 30 Days")
plt.xlabel("Day Number")
plt.ylabel("Temperature (Celsius)")
plt.grid(True)
plt.show()
