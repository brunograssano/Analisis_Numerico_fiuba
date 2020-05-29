import numpy as np



"""Implementacion del algoritmo de biseccion de forma recursiva.
    Los valores enviados son validos."""
def BiseccionRecursivo(Funcion, a, b, tolerancia, iteracion, maxIteraciones, historia):
    puntoMedio = a + (b - a) / 2
    historia[iteracion] = (iteracion, punatoMedio)
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
def SecanteRecursivo(funcion,x1,x0,tolerancia,iteracion,maxIteraciones,historia):
    historia[iteracion]=(iteracion,x1)
    if(abs(x0-x1)<tolerancia):
        historia = historia[:iteracion+1]
        return x1,historia
    x2=x1-funcion(x1)*(x1-x0)/(funcion(x1)-funcion(x0))
    return SecanteRecursivo(funcion,x2,x1,tolerancia,iteracion+1,maxIteraciones,historia)

"""Funcion que da inicio al algoritmo del metodo de la secante implementado de forma recursiva.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado a la raiz y la historia de iteraciones."""

def Secante(funcion,x1,x0,tolerancia,maxIteraciones):
    historia=np.zeros((maxIteraciones,2))
    if(tolerancia<0 or maxIteraciones<0):
        print(" El intervalo no provee información suficiente para asegurar una raiz")
        return None
    return SecanteRecursivo(funcion,x1,x0,tolerancia,0,maxIteraciones,historia)

