import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.linalg import norm
from metodos import *

def randomsW(longitud):
    w= []
    for i in range(0,longitud-1):
        w.append(np.random.uniform(0,1))
    return w

def etaR():
    return np.random.uniform(0,1)

def umbralR():
    return np.random.uniform(0,1)

def inicioR(X,Y,Wcero,umbral):
    r =[]
    for i in range(0, 5):
        eta = etaR()
        iteracion = entrenamiento(Wcero, eta, umbral, X, Y)
        grafIteracion(iteracion)
        r.append(iteracion)
    graficacionEtas(r)
    final = peso_final(r)
    return final

def inicio(Wcero,eta,umbral,X,Y):
    r = entrenamiento(Wcero, eta, umbral, X, Y)
    lista = grafIteracion(r)
    return lista

def entrenamiento(Wcero, eta, umbral, X, Y):
    iteracion = 0
    l = []
    while True:
        Wk = []
        if (iteracion == 0):
            Wk = Wcero
        else:
            Wk = wk.copy()

        Uk = calcularU(X, Wk)
        yc = yCalculada(Y, Uk)
        error = calcularError(Y, yc)
        ex = multiplicarEX(error, X)
        p = multiplicacionEta(eta, ex)
        wk = nuevoW(Wk, p)
        norma = np.linalg.norm(error)
        dic = {
            "iteracion": iteracion,
            "norma": norma,
            "wk": Wk,
            "eta": eta
        }
        l.append(dic)
        iteracion += 1
        try:
            if norma < umbral:
                break
            else:
                print("norma no es menor a umbral: ","norma es: ",norma," umbral es: ",umbral)
                #break
        except:
            print("Ocurrio un ciclo")
    return l

def grafIteracion(lista):
    df = pd.DataFrame(lista)
    fig, ax = plt.subplots()
    ax.plot(df.index.values, df["norma"])
    plt.xlabel('Iteraciones')  # override the xlabel
    plt.ylabel('Norma Error')  # override the ylabel
    plt.title('Grafica de norma de error eta: '+ str(df["eta"][0]))  # override the title
    plt.show()
    return df


def graficacionEtas(lista):
    l = []
    for i in lista:
        df = pd.DataFrame(i)
        mostrarGrafica = {
            "iteracion": df.index.values,
            "eta": df["eta"][0],
            "norma": df["norma"],
        }
        l.append(mostrarGrafica)

    df = pd.DataFrame(l)

    plt.figure(figsize=[6, 6])
    plt.plot(df["iteracion"][0], df["norma"][0], label="Eta numero1: " + str(df["eta"][0]))
    plt.plot(df["iteracion"][1], df["norma"][1], label="Eta numero2: " + str(df["eta"][1]))
    plt.plot(df["iteracion"][2], df["norma"][2], label="Eta numero3: " + str(df["eta"][2]))
    plt.plot(df["iteracion"][3], df["norma"][3], label="Eta numero4: " + str(df["eta"][3]))
    plt.plot(df["iteracion"][4], df["norma"][4], label="Eta numero5: " + str(df["eta"][4]))
    plt.xlabel('Iteraciones')  # override the xlabel
    plt.ylabel('Norma Error')  # override the ylabel
    plt.title('Grafica de norma de error')  # override the title
    plt.legend()
    plt.show()

def peso_final(lista):
    n = []
    for i in lista:
        dic = i.pop()
        #print("eta:{0} pesosfinales {1} ".format(dic["eta"], dic["wk"]))
        n.append([dic["eta"], dic["wk"]])
    return n