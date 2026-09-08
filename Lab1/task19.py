import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

result = np.where(numbers % 2 == 0, -1, numbers)

print("Original array:", numbers)
print("After replacing even numbers with -1:", result)
