from metodos_numericos import Biseccion
from metodos_numericos import Secante
from metodos_numericos import NewtonRaphson
from metodos_numericos import NewtonRaphsonModificado
from Graficador import graficarMetodos, graficarOrdenDeConvergencia, graficarConstantesAsintoticas
from calculadoraAlfaLambda import calcularHistoriaDeOrden
from calculadoraAlfaLambda import calcularHistoraConstanteAsintotica
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def funcionPrueba1():
    x = symbols('x')
    return x**2 - 2
def funcionPrueba2():
    x = symbols('x') 
    return x**3 - 2
def funcionPrueba3():
    x = symbols('x')    
    return x**4 - 2
def funcionPrueba4():
    x = symbols('x')
    return x**5 - 2

# Pruebas de uso
raizB, historiaB = Biseccion(funcionPrueba1(), 0, 2, 1e-5, 50)

raizNR, historiaNR = NewtonRaphson(funcionPrueba1(), 1e-5, 30, 1)

raizNRM, historiaNRM = NewtonRaphsonModificado(funcionPrueba1(), 1e-5, 30, 1)

raizSEC, historiaSEC = Secante(funcionPrueba1(), 0, 2, 1e-5, 50)
