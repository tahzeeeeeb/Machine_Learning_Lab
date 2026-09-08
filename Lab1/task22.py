import numpy as np

numbers = []
for i in range(10):
    value = float(input("Enter number " + str(i + 1) + ": "))
    numbers.append(value)

array = np.array(numbers)
sortedArray = np.sort(array)

print("Original numbers:", array)
print("Sorted array:", sortedArray)
print("Median:", np.median(array))
