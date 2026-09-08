import numpy as np

def isSymmetric(matrix):
    transpose = matrix.T
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != transpose[i][j]:
                return False
    return True

symmetricMatrix = np.array([[1, 7, 3],
                            [7, 4, 5],
                            [3, 5, 6]])

normalMatrix = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

print("First matrix:")
print(symmetricMatrix)
print("Is symmetric:", isSymmetric(symmetricMatrix))

print("Second matrix:")
print(normalMatrix)
print("Is symmetric:", isSymmetric(normalMatrix))
