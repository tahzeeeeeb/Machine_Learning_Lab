#This is the optimized code for Linear Regression helper functions for main.py
#This calculates the predicted values based on theta naught, and theta 1 provided. where theta naught = b, theta 1 = m
#did not initialize val variable with 0 value before this bcz, I am assigning it directly predicted value at x[i]
#Had to initialize the error with a value of 0, because i was using it to store the sum, cannot sum a variable w no value.
def htheta(m, x, b):        
    predictedValues = []    
    for i in range(len(x)):
        val = m*x[i] + b 
       
        predictedValues.append(val)
    return predictedValues

#This function returns an array of Error for each x
def errors(predictedValues, x, y):
    errorValues = []
    for i in range(len(x)):
        val = (predictedValues[i] - y[i])
        errorValues.append(val)
    return errorValues


def costFunction (errorValues):
    error = 0
    for i in range(len(errorValues)):
        error += (errorValues[i])**2

    return 1/(2*len(errorValues))* error

def derivativem (errorValues, x):
    error = 0
    for i in range(len(x)):
        error += errorValues[i] * x[i]

    return 1/(len(x)) * error

def derivativeb (errorValues):
    error = 0
    for i in range(len(errorValues)):
        error += errorValues[i]

    return 1/(len(errorValues)) * error

def newM (m, x, errorValues, learningRate):
    return m - learningRate * (derivativem (errorValues, x))

def newB (b, errorValues, learningRate):
    return b - learningRate * (derivativeb(errorValues)) 