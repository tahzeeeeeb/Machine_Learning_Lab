def htheta(m, x, b):
    predictedValues = []
    for i in range(len(x)):
        val = m*x[i] + b
        predictedValues.append(val)
    return predictedValues


def errors(m, x, b, y):
    errorValues = []
    for i in range(len(x)):
        val = (htheta(m, x[i], b) - y[i])
        errorValues.append(val)
    return errorValues


def costFunction (m, x, b, y):
    total = 0
    for i in range(len(x)):
        error = errors(m, x[i], b, y[i])**2
        total += error

    return 1/(2*len(x))* total

def derivativem (m, x, b, y):
    total = 0
    for i in range(len(x)):
        error = errors(m, x[i], b, y[i]) * x[i]
        total += error

    return 1/(len(x)) * total

def derivativeb (m, x, b, y):
    total = 0
    for i in range(len(x)):
        error = errors(m, x[i], b, y[i])
        total += error

    return 1/(len(x)) * total

def newM (m, x, b, y, learningRate):
    return m - learningRate * (derivativem (m, x, b, y))

def newB (m, x, b, y, learningRate):
    return b - learningRate * (derivativeb(m, x, b, y))