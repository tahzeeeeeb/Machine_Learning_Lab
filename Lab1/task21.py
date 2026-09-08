import numpy as np

firstVector = np.array([1, 2, 3, 4])
secondVector = np.array([5, 6, 7, 8])

manualResult = 0
for i in range(len(firstVector)):
    manualResult = manualResult + firstVector[i] * secondVector[i]

libraryResult = np.dot(firstVector, secondVector)

print("First vector:", firstVector)
print("Second vector:", secondVector)
print("Dot product using loop:", manualResult)
print("Dot product using np.dot():", libraryResult)
print("Both results match:", manualResult == libraryResult)
