import numpy as np
from sympy import *


def Derivar(expresion):
    """
    Recibe una expresion que va a derivar en funcion de 'x'
    """
    x = symbols('x')
    expresionDerivada = Derivative(expresion, x)
    return expresionDerivada.doit()



def Evaluar(expresion, valor):
    """
    Recibe una expresion y la va a evaluar remplanzo en las 'x' que contenga con el valor indicado.
    """
    x = symbols('x')
    return expresion.subs(x, valor)



def BiseccionRecursivo(Funcion, a, b, tolerancia, iteracion, maxIteraciones, historia):
    """
    Implementacion del algoritmo de biseccion de forma recursiva.
    Los valores recibidos son validos.
    """
    puntoMedio = a + (b - a) / 2
    error = abs(puntoMedio - historia[iteracion - 1][1])
    historia[iteracion] = (iteracion, puntoMedio, error)
    if error < tolerancia or iteracion >= maxIteraciones-1:
        historia = historia[:iteracion + 1]
        return puntoMedio, historia
    elif Evaluar(Funcion, a) * Evaluar(Funcion, puntoMedio) > 0:
        return BiseccionRecursivo(Funcion, puntoMedio, b, tolerancia, iteracion + 1, maxIteraciones, historia)
    else:
        return BiseccionRecursivo(Funcion, a, puntoMedio, tolerancia, iteracion + 1, maxIteraciones, historia)



def Biseccion(Funcion, a, b, tolerancia, maxIteraciones):
    """
    Funcion que da inicio al algoritmo de biseccion implementado de forma recursiva.
    El intervalo enviado debe de ser valido.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado de la raiz y la historia de iteraciones.
    """
    historia = np.zeros((maxIteraciones, 3))
    if Evaluar(Funcion, a) * Evaluar(Funcion, b) > 0 or tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo en biseccion no provee información suficiente para asegurar una raiz")
        return None, np.array([])
    return BiseccionRecursivo(Funcion, a, b, tolerancia, 0, maxIteraciones, historia)



def SecanteRecursivo(Funcion, x1, x0, tolerancia, iteracion, maxIteraciones, historia):
    """
    Implementacion del algoritmo del metodo de la secante de forma recursiva.
    Los valores recibidos son validos.
    """
    if iteracion >= maxIteraciones - 1:
        return None, np.array([])

    error = abs(x0 - x1)
    historia[iteracion] = (iteracion, x1, error)
    if error < tolerancia or iteracion >= maxIteraciones-1:
        historia = historia[:iteracion + 1]
        return x1, historia
    fx1 = Evaluar(Funcion, x1)
    fx0 = Evaluar(Funcion, x0)
    if(fx1 == fx0):
        return x1, historia
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    return SecanteRecursivo(Funcion, x2, x1, tolerancia, iteracion + 1, maxIteraciones, historia)



def Secante(Funcion, x1, x0, tolerancia, maxIteraciones):
    """
    Funcion que da inicio al algoritmo del metodo de la secante implementado de forma recursiva.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado de la raiz y la historia de iteraciones.
    """
    historia = np.zeros((maxIteraciones, 3))
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo en secante no provee información suficiente para asegurar una raiz")
        return None, np.array([])
    return SecanteRecursivo(Funcion, x1, x0, tolerancia, 0, maxIteraciones, historia)



def NewtonRaphsonRecursivo(funcion, derivada, tolerancia, maxIteraciones, pN, iteracion, historia):
    """
    Implementacion de NewtonRaphson recursivo, los valores recibidos son validos
    Si se cumplen las condiciones, y la derivada no se anula, se devolvera la raiz,
    caso contrario, se devuelve None como raiz y la historia que se tenga.
    """
    if iteracion >= maxIteraciones - 1:
        return None, np.array([])


    valorFuncion = Evaluar(funcion, pN)
    valorDerivada = Evaluar(derivada, pN)

    if valorDerivada == 0:
        return None, np.array([])

    pNmas1 = pN - (valorFuncion / valorDerivada)

    error = abs(pNmas1 - pN)

    historia[iteracion] = (iteracion, pN, error)

    if pNmas1 == pN:
        historia = historia[:iteracion + 1]
        return pN, historia

    if error < tolerancia:
        historia[iteracion + 1] = (iteracion + 1, pNmas1,error)
        historia = historia[:iteracion + 2]
        return pNmas1, historia

    return NewtonRaphsonRecursivo(funcion, derivada, tolerancia, maxIteraciones, pNmas1, iteracion + 1, historia)



def NewtonRaphson(funcion, tolerancia, maxIteraciones, semilla):
    """
    La tolerancia y numero de iteraciones tienen que ser positivos.
    La semilla debe de estar cerca del intervalo, caso contrario no va a converger.
    """
    historia = np.zeros((maxIteraciones, 3))
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo en Newton Raphson no provee información suficiente para asegurar una raiz")
        return None, np.array([])
    derivada = Derivar(funcion)
    return NewtonRaphsonRecursivo(funcion, derivada, tolerancia, maxIteraciones, semilla, 0, historia)



def NewtonRaphsonModificado(funcion, tolerancia, maxIteraciones, semilla):
    """
    La tolerancia y numero de iteraciones tienen que ser positivos.
    La semilla debe de estar cerca del intervalo, caso contrario no va a converger.
    """
    derivada = Derivar(funcion)
    funcionNRM = funcion / derivada
    return NewtonRaphson(funcionNRM, tolerancia, maxIteraciones, semilla)


