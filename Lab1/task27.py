import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
sinValues = np.sin(x)
cosValues = np.cos(x)

plt.plot(x, sinValues, color="blue", label="sin(x)")
plt.plot(x, cosValues, color="red", label="cos(x)")
plt.title("Sine and Cosine Curves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
