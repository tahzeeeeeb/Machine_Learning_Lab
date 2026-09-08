import numpy as np

temperatures = np.array([30, 36, 38, 33, 29, 41, 35, 37, 40, 32,
                         28, 39, 34, 36, 42, 31, 30, 38, 37, 33,
                         27, 35, 44, 39, 36, 30, 32, 41, 38, 34])

hotDays = temperatures[temperatures > 35]

print("Temperatures:")
print(temperatures)
print("Days above 35 degrees:", hotDays)
print("Number of such days:", len(hotDays))
