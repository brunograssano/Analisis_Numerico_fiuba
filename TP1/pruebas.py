from metodos_numericos import Biseccion
from metodos_numericos import Secante
from metodos_numericos import NewtonRaphson
from metodos_numericos import NewtonRaphsonModificado
from Graficador import *
from calculadoraAlfaLambda import calcularHistoriaDeOrden
from calculadoraAlfaLambda import calcularHistoriaConstanteAsintotica
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

def funcionPrueba5():# entre 1 y 3 esta la raiz esta deberia de ser 2,36...
    x = symbols('x')
    return x**5 + x**3 - x - 84

# Pruebas de uso
print("BISECCION")
raizB, historiaB = Biseccion(funcionPrueba1(), 0, 2, 1e-5, 50)
#print(raizB)
#print(historiaB)

print("NR")

raizNR, historiaNR = NewtonRaphson(funcionPrueba1(), 1e-5, 30, 1)
#print(raizNR)
#print(historiaNR)

print("NRM")

raizNRM, historiaNRM = NewtonRaphsonModificado(funcionPrueba1(), 1e-5, 30, 1)
#print(raizNRM)
#print(historiaNRM)

print("SECANTE F1")

raizSEC, historiaSEC = Secante(funcionPrueba1(), 2, 0, 1e-15, 50)
print(raizSEC)
print(historiaSEC)

print ("HISTORIA DE ORDEN F1")
#alfaB, ordenB =calcularHistoriaDeOrden(historiaB)
#print(alfaB)
#print(ordenB)

alfaSEC, ordenSEC =calcularHistoriaDeOrden(historiaSEC)
print(alfaSEC)
print(ordenSEC)


print("SECANTE F2")
raizSEC, historiaSEC = Secante(funcionPrueba2(), 2, 0, 1e-15, 50)
print(raizSEC)
print(historiaSEC)

print ("HISTORIA DE ORDEN F2")
alfaSEC, ordenSEC =calcularHistoriaDeOrden(historiaSEC)
print(alfaSEC)
print(ordenSEC)

print("SECANTE F3")
raizSEC, historiaSEC = Secante(funcionPrueba3(), 1.5, 0.5, 1e-15, 50)
print(raizSEC)
print(historiaSEC)

print ("HISTORIA DE ORDEN F3")
alfaSEC, ordenSEC =calcularHistoriaDeOrden(historiaSEC)
print(alfaSEC)
print(ordenSEC)

print("CONSTANTE ASINTOTICA SEC F3")
constAsintSEC, histConstAsintSEC = calcularHistoriaConstanteAsintotica(ordenSEC, alfaSEC)
print(constAsintSEC) #estaria llegando a 0.5?
print(histConstAsintSEC)

print("SECANTE F4")
raizSEC, historiaSEC = Secante(funcionPrueba4(), 1.5, 0.5, 1e-15, 50)
print(raizSEC)
print(historiaSEC)

print ("HISTORIA DE ORDEN F4")
alfaSEC, ordenSEC =calcularHistoriaDeOrden(historiaSEC)
print(alfaSEC)
print(ordenSEC)

print("CONSTANTE ASINTOTICA SEC F4")
constAsintSEC, histConstAsintSEC = calcularHistoriaConstanteAsintotica(ordenSEC, alfaSEC)
print(constAsintSEC) #aca no se acerca a 0.5
print(histConstAsintSEC)

print("SECANTE F5")
raizSEC, historiaSEC = Secante(funcionPrueba5(), 2.8, 2.2, 1e-15, 50)
print(raizSEC)
print(historiaSEC)

print ("HISTORIA DE ORDEN F5")
alfaSEC, ordenSEC =calcularHistoriaDeOrden(historiaSEC)
print(alfaSEC)
print(ordenSEC)

print("CONSTANTE ASINTOTICA SEC F5")
constAsintSEC, histConstAsintSEC = calcularHistoriaConstanteAsintotica(ordenSEC, alfaSEC)
print(constAsintSEC) #tendria que dar mas cercano a 0.5, quizas con mas iteraciones llega
print(histConstAsintSEC)


print("NR F5")
raizNR, historiaNR = NewtonRaphson(funcionPrueba5(), 1e-15, 50, 1.8)
print(raizNR)
print(historiaNR)

print ("HISTORIA DE ORDEN NR F5")
alfaNR, ordenNR =calcularHistoriaDeOrden(historiaNR)
print(alfaNR)
print(ordenNR)

print("CONSTANTE ASINTOTICA NR F5")
constAsintNR, histConstAsintNR = calcularHistoriaConstanteAsintotica(ordenNR, alfaNR)
print(constAsintNR) #tendria que dar mas cercano a 0.5
print(histConstAsintNR)

print("NR F4")
raizNR, historiaNR = NewtonRaphson(funcionPrueba4(), 1e-15, 50, 0.5)
print(raizNR)
print(historiaNR)

print ("HISTORIA DE ORDEN NR F4")
alfaNR, ordenNR =calcularHistoriaDeOrden(historiaNR)
print(alfaNR)
print(ordenNR)

print("CONSTANTE ASINTOTICA NR F4")
constAsintNR, histConstAsintNR = calcularHistoriaConstanteAsintotica(ordenNR, alfaNR)
print(constAsintNR) #tendria que dar mas cercano a 0.5
print(histConstAsintNR)

