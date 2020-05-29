import matplotlib.pyplot as plt
import numpy as np


def ordenDeConvergencia(xNmenos2, xNmenos1, xN, xNmas1):
    a = xNmas1 - xN
    b = xN - xNmenos1
    numerador = np.log(abs(a/b))    

    c = xN - xNmenos1
    d = xNmenos1 - xNmenos2
    denominador = np.log(abs(c/d))

    return numerador/denominador

def calcularHistoriaDeOrden(historia): 
    tope = len(historia)
    if(tope < 5):
        raise Exception("No hay suficientes datos para calcular la historia de orden.")
    historiaDeOrden = np.zeros((tope-4, 2))

    for i in range(2, tope-2):
        historiaDeOrden[i - 2][1] = ordenDeConvergencia(historia[i-2][1], historia[i-1][1], historia[i][1], historia[i+1][1])
        historiaDeOrden[i - 2][0] = i
    
    return historiaDeOrden[tope-5][1], historiaDeOrden


def constanteAsintotica(xN, xNmas1, alfa, raiz):
    numerador = abs((xNmas1 - raiz))
    denominador = abs((xN - raiz)**alfa)
    return numerador/denominador

def calcularHistoraConstanteAsintotica(historia, alfa):
    tope = len(historia)
    raiz = historia[tope-1][1]
    
    historiaConstanteAsintotica = np.zeros((tope-2,2))
    for i in range(0, tope-2):
        historiaConstanteAsintotica[i][1] = constanteAsintotica(historia[i][1], historia[i+1][1], alfa, raiz)
        historiaConstanteAsintotica[i][0] = i
    return historiaConstanteAsintotica[tope-3][1], historiaConstanteAsintotica