import numpy as np

firstArray = np.array([[1, 2], [3, 4]])
secondArray = np.array([[5, 6], [7, 8]])
thirdArray = np.array([[9, 10], [11, 12]])

verticalStack = np.vstack([firstArray, secondArray, thirdArray])
horizontalStack = np.hstack([firstArray, secondArray, thirdArray])

print("Vertical stack:")
print(verticalStack)
print("Shape:", verticalStack.shape)

print("Horizontal stack:")
print(horizontalStack)
print("Shape:", horizontalStack.shape)

print("vstack adds the arrays below each other so the number of rows grows.")
print("hstack adds the arrays beside each other so the number of columns grows.")
