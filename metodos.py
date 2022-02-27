import numpy as np

def calcularU (Wk, X):
    u = np.dot(Wk, X)
    return u

def yCalculada(Y,U):
    y=[]
    for i in range(len(U)):
        if(U[i]>=Y[i]):
            y.append(1)
        else:
           if(U[i]<Y[i]):
                y.append(0)
    return y

def calcularError(Y, yc):
    mat1 = np.matrix(Y)
    mat2 = np.matrix(yc)
    err = mat1-mat2
    e = (np.asarray(err)).flatten()
    return e

def multiplicarEX(e, X):
    a = np.dot(e, X)
    return a

def multiplicacionEta(eta, array):
    v = np.array(array)
    vector = v * eta
    return vector

def nuevoW(Wk, Wn):
    mat1 = np.matrix(Wk)
    mat2 = np.matrix(Wn)
    err = mat1+mat2
    w = (np.asarray(err)).flatten()
    return w