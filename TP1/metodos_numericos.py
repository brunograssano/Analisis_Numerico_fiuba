import numpy as np
from sympy import *


def Derivar(expresion):
    x = symbols('x')
    expresionDerivada = Derivative(expresion, x)
    return expresionDerivada.doit()


def Evaluar(expresion, valor):
    x = symbols('x')
    return expresion.subs(x, valor)


"""Implementacion del algoritmo de biseccion de forma recursiva.
    Los valores enviados son validos."""
def BiseccionRecursivo(Funcion, a, b, tolerancia, iteracion, maxIteraciones, historia):
    puntoMedio = a + (b - a) / 2
    historia[iteracion] = (iteracion, puntoMedio)
    if Evaluar(Funcion, puntoMedio) == 0 or (b - a) / 2 < tolerancia or iteracion >= maxIteraciones:
        historia = historia[:iteracion + 1]
        return puntoMedio, historia
    elif Evaluar(Funcion, a) * Evaluar(Funcion, puntoMedio) > 0:
        return BiseccionRecursivo(Funcion, puntoMedio, b, tolerancia, iteracion + 1, maxIteraciones, historia)
    else:
        return BiseccionRecursivo(Funcion, a, puntoMedio, tolerancia, iteracion + 1, maxIteraciones, historia)


"""Funcion que da inicio al algoritmo de biseccion implementado de forma recursiva.
    El intervalo enviado debe de ser valido.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado a la raiz y la historia de iteraciones."""
def Biseccion(Funcion, a, b, tolerancia, maxIteraciones):
    historia = np.zeros((maxIteraciones, 2))
    if Evaluar(Funcion, a) * Evaluar(Funcion, b) > 0 or tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo en biseccion no provee información suficiente para asegurar una raiz")
        return None, np.array([])
    return BiseccionRecursivo(Funcion, a, b, tolerancia, 0, maxIteraciones, historia)


"""Implementacion del algoritmo del metodo de la secante de forma recursiva.
    Los valores enviados son validos."""
def SecanteRecursivo(Funcion, x1, x0, tolerancia, iteracion, maxIteraciones, historia):
    if iteracion >= maxIteraciones - 1:
        return None, historia
    
    historia[iteracion] = (iteracion, x1)
    if abs(x0 - x1) < tolerancia or iteracion >= maxIteraciones:
        historia = historia[:iteracion + 1]
        return x1, historia
    fx1 = Evaluar(Funcion, x1)
    fx0 = Evaluar(Funcion, x0)
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    return SecanteRecursivo(Funcion, x2, x1, tolerancia, iteracion + 1, maxIteraciones, historia)


"""Funcion que da inicio al algoritmo del metodo de la secante implementado de forma recursiva.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado a la raiz y la historia de iteraciones."""
def Secante(Funcion, x1, x0, tolerancia, maxIteraciones):
    historia = np.zeros((maxIteraciones, 2))
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo en secante no provee información suficiente para asegurar una raiz")
        return None, np.array([])
    return SecanteRecursivo(Funcion, x1, x0, tolerancia, 0, maxIteraciones, historia)

def NewtonRaphsonRecursivo(funcion, derivada, tolerancia, maxIteraciones, pN, iteracion, historia):
    
    if iteracion >= maxIteraciones - 1:
        return None, historia
    
    historia[iteracion] = (iteracion, pN)
    valorFuncion = Evaluar(funcion, pN)
    valorDerivada = Evaluar(derivada, pN)
    if(valorDerivada == 0):
        return None, historia
    pNmas1 = pN - (valorFuncion / valorDerivada)
    if pNmas1 == pN:
        historia = historia[:iteracion + 1]
        return pN, historia
    if abs(pNmas1 - historia[iteracion][1]) < tolerancia:
        historia = historia[:iteracion + 1]
        return pNmas1, historia
    
    return NewtonRaphsonRecursivo(funcion, derivada, tolerancia, maxIteraciones, pNmas1, iteracion + 1, historia)

def NewtonRaphson(funcion, tolerancia, maxIteraciones, semilla):
    historia = np.zeros((maxIteraciones, 2))
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo en Newton Raphson no provee información suficiente para asegurar una raiz")
        return None, np.array([])
    derivada = Derivar(funcion)
    return NewtonRaphsonRecursivo(funcion, derivada, tolerancia, maxIteraciones, semilla, 0, historia)


def NewtonRaphsonModificado(funcion, tolerancia, maxIteraciones, semilla):
    derivada = Derivar(funcion)
    funcionNRM = funcion / derivada
    return NewtonRaphson(funcionNRM, tolerancia, maxIteraciones, semilla)


