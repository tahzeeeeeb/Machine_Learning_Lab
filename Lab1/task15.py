import numpy as np

firstMatrix = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

secondMatrix = np.array([[9, 8, 7],
                         [6, 5, 4],
                         [3, 2, 1]])

print("First matrix:")
print(firstMatrix)
print("Second matrix:")
print(secondMatrix)

print("Element-wise multiplication (*):")
print(firstMatrix * secondMatrix)

print("Matrix multiplication (@):")
print(firstMatrix @ secondMatrix)

print("Element-wise multiplies matching positions, matrix multiplication multiplies rows by columns.")
