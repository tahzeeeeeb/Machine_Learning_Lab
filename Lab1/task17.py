import numpy as np

numbers = np.array([10, 25, 40, 5, 60, 35, 80, 15])

minimum = numbers.min()
maximum = numbers.max()
normalized = (numbers - minimum) / (maximum - minimum)

print("Original array:", numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Normalized array:")
print(normalized)
