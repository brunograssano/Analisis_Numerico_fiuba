import numpy as np
from sympy import *
def Derivar(expresion):
    x = symbols('x')
    expresionDerivada = Derivative(expresion,x)
    expresionDerivada = expresionDerivada.doit()
    return expresionDerivada

def Evaluar(expresion,valor):
    valor = expresion.subs(x,valor)
    return valor


"""Implementacion del algoritmo de biseccion de forma recursiva.
    Los valores enviados son validos."""

"Prueba Commits"
def BiseccionRecursivo(Funcion, a, b, tolerancia, iteracion, maxIteraciones, historia):
    puntoMedio = a + (b - a) / 2
    historia[iteracion] = (iteracion, puntoMedio)
    if Funcion(puntoMedio) == 0 or (b - a) / 2 < tolerancia or iteracion == maxIteraciones:
        historia = historia[:iteracion+1]
        return puntoMedio, historia
    elif Funcion(a) * Funcion(puntoMedio) > 0:
        return BiseccionRecursivo(Funcion, puntoMedio, b, tolerancia, iteracion + 1, maxIteraciones, historia)
    else:
        return BiseccionRecursivo(Funcion, a, puntoMedio, tolerancia, iteracion + 1, maxIteraciones, historia)


"""Funcion que da inicio al algoritmo de biseccion implementado de forma recursiva.
    El intervalo enviado debe de ser valido.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado a la raiz y la historia de iteraciones."""
def Biseccion(Funcion, a, b, tolerancia, maxIteraciones):
    historia = np.zeros((maxIteraciones, 2))
    if Funcion(a) * Funcion(b) > 0 or tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo no provee información suficiente para asegurar una raiz")
        return None
    return BiseccionRecursivo(Funcion, a, b, tolerancia, 0, maxIteraciones, historia)

"""Implementacion del algoritmo del metodo de la secante de forma recursiva.
    Los valores enviados son validos."""
def SecanteRecursivo(Funcion,x1,x0,tolerancia,iteracion,maxIteraciones,historia):
    historia[iteracion]=(iteracion,x1)
    if(abs(x0-x1)<tolerancia):
        historia = historia[:iteracion+1]
        return x1,historia
    x2=x1-Funcion(x1)*(x1-x0)/(Funcion(x1)-Funcion(x0))
    return SecanteRecursivo(Funcion,x2,x1,tolerancia,iteracion+1,maxIteraciones,historia)

"""Funcion que da inicio al algoritmo del metodo de la secante implementado de forma recursiva.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado a la raiz y la historia de iteraciones."""
def Secante(Funcion,x1,x0,tolerancia,maxIteraciones):
    historia=np.zeros((maxIteraciones,2))
    if(tolerancia<0 or maxIteraciones<0):
        print(" El intervalo no provee información suficiente para asegurar una raiz")
        return None
    return SecanteRecursivo(Funcion,x1,x0,tolerancia,0,maxIteraciones,historia)

def NewtonRaphson(funcion,tolerancia,maxIteraciones,semilla):
    historia = np.zeros((maxIteraciones, 2))
    if(tolerancia<0 or maxIteraciones<0):
        print(" El intervalo no provee información suficiente para asegurar una raiz")
        return None
    i = 0
    historia[i] = (i, semilla)
    derivada = Derivar(funcion)
    while( i < maxIteraciones):
        i=i+1
        valorFuncion = Evaluar(funcion, semilla)
        valorDerivada= Evaluar(derivada, semilla)
        semilla = semilla - (valorFuncion/valorDerivada)
        historia[i]=(i,semilla)
        if (abs(semilla-historia[i-1][1]) < tolerancia):
            historia = historia[:i + 1]
            return semilla, historia
    return semilla,historia

def NewtonRaphsonModificado(funcion, tolerancia, maxIteraciones, semilla):
    derivada = Derivar(funcion)
    funcionNRM = funcion/derivada
    return NewtonRaphson(funcionNRM,tolerancia,maxIteraciones,semilla)
