import optimizedhelpers as oph
x = [1, 2, 3]
y = [3, 5, 7]
m = 0
b = 0
numIterations = int(input("Enter the number of Iteration for Linear Regression: "))
learningRate = float(input("Enter the value of learning rate: "))
print("\n\n")
for i in range (numIterations):
    predictedValues = oph.htheta(m, x, b)
    errorValues = oph.errors(predictedValues, x, y)

    print("Predicted values in iteration ", i+1)
    print("[", end="")
    for i in range(len(x)):
        print(predictedValues[i], end="")
        if i < (len(x) - 1):
            print(" ", end="")
    print("]")
    
    print("Error values in iteration ", i+1)
    print("[", end="")
    for i in range(len(x)):
        print(errorValues[i], end="")
        if i < (len(x) - 1):
            print(" ", end="")
    print("]")

    print("Cost in iteration ", i+1)
    print("[", oph.costFunction(errorValues), end="")
    print("]")

    #printing the derivative of cost with respect to m
    print("Derivative of Cost w.r.t m in iteration ", i+1)
    print("[", oph.derivativem(errorValues, x), end="")
    print("]")

    #printing the derivative of cost with respect to b
    print("Derivative of Cost w.r.t b in iteration ", i+1)
    print("[", oph.derivativeb(errorValues), end="")
    print("]")

    m = oph.newM(m, x, errorValues, learningRate)
    b = oph.newB(b, errorValues, learningRate)
    print("\n\n")

