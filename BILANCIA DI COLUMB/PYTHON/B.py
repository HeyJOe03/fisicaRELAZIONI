import numpy as np

def calcB(X, Y) -> float:
    if len(X) != len(Y):
        raise "Non hanno la stessa lunghezza coglione"
    N = len(Y)
    X = np.array(X)
    Y = np.array(Y)
    num = N*np.sum(X*Y) - X.sum() * Y.sum()
    delta = calcDelta(X)
    A = num/delta
    return A

def calcDelta(X):
    return len(X)*np.sum(X*X)-np.power(X.sum(),2)

def calcDeltaB(X, Y) -> float:
    if len(X) != len(Y):
        raise "Non hanno la stessa lunghezza coglione"
    return np.sqrt(float(len(Y))/calcDelta(X))*np.sqrt(((Y - calcB(X, Y) * X) ** 2).sum() / len(Y))