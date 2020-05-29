from metodos_numericos import Biseccion
from metodos_numericos import Secante
from Graficador import graficarMetodos, graficarOrdenDeConvergencia, graficarConstantesAsintoticas
from calculadoraAlfaLambda import calcularHistoriaDeOrden
from calculadoraAlfaLambda import calcularHistoraConstanteAsintotica
import matplotlib.pyplot as plt
import numpy as np

def funcionPrueba1(x):
    return x**2 - 2
def funcionPrueba2(x):
    return x**3 - 2
def funcionPrueba3(x):
    return x**4 - 2
def funcionPrueba4(x):
    return x**5 - 2


# Pruebas de uso
raizB, historiaBiseccion = Biseccion(funcionPrueba1, 0, 2, 1e-10, 50)
raizNR, historiaNR = Biseccion(funcionPrueba2, 0, 2, 1e-10, 50)     #Acá iría NR
raizNRM, historiaNRM = Biseccion(funcionPrueba3, 0, 2, 1e-10, 50)   #Acá iría NRM
raizSEC, historiaSEC = Secante(funcionPrueba1, 0, 2, 1e-10, 50)

graficarMetodos(historiaBiseccion, historiaNR, historiaNRM, historiaSEC)

alfaBIS,historiaOCBiseccion = calcularHistoriaDeOrden(historiaBiseccion)
alfaNR, historiaOCNR = calcularHistoriaDeOrden(historiaNR)
alfaNRM, historiaOCNRM = calcularHistoriaDeOrden(historiaNRM)
alfaSEC, historiaOCSecante = calcularHistoriaDeOrden(historiaSEC)

graficarOrdenDeConvergencia(historiaOCBiseccion, historiaOCNR,historiaOCNRM, historiaOCSecante)


lambdaBIS, historiaCABiseccion = calcularHistoraConstanteAsintotica(historiaBiseccion, alfaBIS)
lambdaNR, historiaCANR = calcularHistoraConstanteAsintotica(historiaOCNR, alfaNR)
lambdaNRM, historiaCANRM = calcularHistoraConstanteAsintotica(historiaOCNRM, alfaNRM)
lambdaSEC, historiaCASecante = calcularHistoraConstanteAsintotica(historiaOCSecante, alfaSEC)

graficarConstantesAsintoticas(historiaCABiseccion, historiaCANR, historiaCANRM, historiaCASecante)