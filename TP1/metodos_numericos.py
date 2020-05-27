import numpy as np
import matplotlib.pyplot as plt


"""Implementacion del algoritmo de biseccion de forma recursiva.
    Los valores enviados son validos."""
def biseccion_recursivo(funcion, a, b, tolerancia, iteracion, max_n_iteraciones, historia):
    punto_medio = a + (b - a) / 2
    historia[iteracion] = (iteracion, punto_medio)
    if funcion(punto_medio) == 0 or (b - a) / 2 < tolerancia or iteracion == max_n_iteraciones:
        historia = historia[:iteracion+1]
        return punto_medio, historia
    elif funcion(a) * funcion(punto_medio) > 0:
        return biseccion_recursivo(funcion, punto_medio, b, tolerancia, iteracion + 1, max_n_iteraciones, historia)
    else:
        return biseccion_recursivo(funcion, a, punto_medio, tolerancia, iteracion + 1, max_n_iteraciones, historia)


"""Funcion que da inicio al algoritmo de biseccion implementado de forma recursiva.
    El intervalo enviado debe de ser valido.
    La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado a la raiz y la historia de iteraciones."""
def biseccion(funcion, a, b, tolerancia, max_n_iteraciones):
    historia = np.zeros((max_n_iteraciones, 2))
    if funcion(a) * funcion(b) > 0 or tolerancia < 0 or max_n_iteraciones < 0:
        print(" No puede existir raiz en este intervalo")
        return None
    return biseccion_recursivo(funcion, a, b, tolerancia, 0,max_n_iteraciones, historia)
