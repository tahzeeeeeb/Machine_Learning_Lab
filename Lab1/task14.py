import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

diagonal = np.diag(matrix)

print("Matrix:")
print(matrix)
print("Diagonal elements:", diagonal)
print("Sum of diagonal:", diagonal.sum())
