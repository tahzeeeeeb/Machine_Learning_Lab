def fibbonacciNumbers (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibbonacciNumbers(n -1) + fibbonacciNumbers (n-2)

fibbonacciArray = []
numberOfSequence = int(input("Enter the number of sequences you want: "))
for i in range (numberOfSequence):
    fibbonacciArray.append(fibbonacciNumbers(i))

for i in range (numberOfSequence):
    print(fibbonacciArray[i], end=", ")
