import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)

print("Matrix:")
print(matrix)

print("Transpose:")
print(matrix.T)

determinant = np.linalg.det(matrix)
print("Determinant:", round(determinant, 2))

if round(determinant, 6) != 0:
    print("Inverse:")
    print(np.linalg.inv(matrix))
else:
    print("The matrix is not invertible because its determinant is 0.")
