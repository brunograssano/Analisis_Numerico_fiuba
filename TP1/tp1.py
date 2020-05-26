from metodos_numericos import biseccion_recursivo
import numpy as np


def funcion1(x):
    return (x ** 2) - 2


def funcion2(x):
    return (x ** 5) - 6.6 * (x ** 4) + 21.312 * (x ** 2) - 38.016 * x + 17.28


def funcion3(x):
    return (x - 1.5) * np.exp(-4 * ((x - 1.5) ** 2))


if __name__ == "__main__":
    raiz = biseccion_recursivo(funcion1, 0, 2, 0.2, 20)  # prueba
    print(raiz)
