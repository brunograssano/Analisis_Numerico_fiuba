import numpy as np
import matplotlib.pyplot as plt


"""Implementacion del algoritmo de biseccion de forma recursiva"""
def biseccion_rec(funcion, a, b, tolerancia, iteracion):
    punto_medio = a + (b - a) / 2
    if funcion(punto_medio) == 0 or (b - a) / 2 < tolerancia or iteracion == 0:
        return punto_medio
    elif funcion(a) * funcion(punto_maedio) > 0:
        return biseccion_rec(funcion, punto_medio, b, tolerancia, iteracion - 1)
    else:
        return biseccion_rec(funcion, a, punto_medio, tolerancia, iteracion - 1)


"""Funcion que da inicio al algoritmo de biseccion implementado de forma recursiva"""
def biseccion_recursivo(funcion, a, b, tolerancia, max_n_iteraciones):
    if funcion(a) * funcion(b) > 0:
        print(" No puede existir raiz en este intervalo")
        return None
    return biseccion_rec(funcion, a, b, tolerancia, max_n_iteraciones)
