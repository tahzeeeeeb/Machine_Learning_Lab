import numpy as np

matrix = np.eye(6)
print("Identity matrix:")
print(matrix)

values = [1, 2, 3, 4, 5, 6]
for i in range(6):
    matrix[i][i] = values[i]

print("After replacing the diagonal:")
print(matrix)
