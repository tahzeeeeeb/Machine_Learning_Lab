import numpy as np

matrix = np.arange(1, 13).reshape(3, 4)

selectedRows = [0, 2]
selectedColumns = [1, 3]
result = matrix[np.ix_(selectedRows, selectedColumns)]

print("Matrix:")
print(matrix)
print("Rows 0 and 2 with columns 1 and 3:")
print(result)
