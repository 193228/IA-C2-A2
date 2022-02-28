import random
import sys
import PyQt5
import pandas as pd
import openpyxl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from algoritmo import *
from vista.main import Ui_MainWindow as ventanaPrincipal
X = []

class MyApp(PyQt5.QtWidgets.QMainWindow, ventanaPrincipal):
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        ventanaPrincipal.__init__(self)
        self.setupUi(self)
        acciones(self)

def acciones(ventana):
    ventana.botonValores.clicked.connect(lambda: leerArchivo(ventana))
    ventana.botonResultados.clicked.connect(lambda: ajusteValores(ventana))
    #ventana.aleatorioW.

def leerArchivo(ventana):
    eleccion = PyQt5.QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione Archivo", "", "CSV FILES (*.xlsx)")
    x = pd.read_excel(eleccion[0], sheet_name="X", header=None).to_numpy().tolist()
    return X.append(x)

def ajusteValores(ventana):
    Y = []
    if ventana.aleatorioW.isChecked():
        w0 = randomsW(len(X[0]))
    else:
        w0 = ventana.valorW.text().split(',')

    if ventana.aleatorioValores_2.isChecked():
        for i in range(0,len(X[0])):
            Y.append(random.randint(0, 1))
    else:
        valorY = ventana.valorY.text().split(',')
        Y = [int(x) for x in valorY]

    if ventana.aleatorioUmbral.isChecked():
        umbral = umbralR()
    else:
        umbral = float(ventana.umbral.text())

    if ventana.aleatorioAprendizaje.isChecked():
        aprendizaje = etaR()
    else:
        if not ventana.diversasTasas.isChecked():
            aprendizaje = float(ventana.umbral_2.text())

    if ventana.diversasTasas.isChecked():
        graficacion = inicioR(X[0], Y, w0, umbral)
        hacerTabla(ventana, graficacion)

    if not ventana.diversasTasas.isChecked():
        graficacion = inicio(w0,aprendizaje,umbral,X[0],Y)
        hacerTabla2(ventana,graficacion)

def hacerTabla2(ventana,lista):
    ventana.tabla.setRowCount(1)
    ventana.tabla.setItem(0,0,QtWidgets.QTableWidgetItem(str(lista["eta"].iloc[-1])))
    ventana.tabla.setItem(0,1,QtWidgets.QTableWidgetItem(str(lista["wk"].iloc[-1])))



def hacerTabla(ventana,lista):
    l = []
    for i in lista:
        estado = str(i[0]), str(i[1])
        l.append(estado)

    ventana.tabla.setRowCount(0)  # limpia la tabla
    #ventana.tabla.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # no edita la tabla
    fila = 0
    for registro in l:
        columna = 0
        ventana.tabla.insertRow(fila)
        for elemento in registro:
            celda = QTableWidgetItem(elemento)
            ventana.tabla.setItem(fila, columna, celda)
            columna += 1
        fila += 1

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # crea un objeto de aplicación (Argumentos de sys)
    window = MyApp()
    window.show()
    window.setFixedSize(window.size())
    app.exec_()