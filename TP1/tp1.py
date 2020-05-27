from metodos_numericos import biseccion
import numpy as np


def funcion1(x):
    return (x ** 2) - 2


def funcion2(x):
    return (x ** 5) - 6.6 * (x ** 4) + 21.312 * (x ** 2) - 38.016 * x + 17.28


def funcion3(x):
    return (x - 1.5) * np.exp(-4 * ((x - 1.5) ** 2))


def introduccion():
    print("~~~~~~ TP 1 - Analisis Numerico ~~~~~~ ")
    print("Integrantes grupo 1")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

def grafico_de_las_funciones():

def buscar_raices(funcion, tolerancia):
    raiz_biseccion, historia_biseccion = biseccion(funcion, 0, 2, tolerancia, 50)
    raiz_newton, historia_newton = newton_raphson()
    raiz_newton_modificado, historia_newton_modificado = newton_raphson()
    raiz_secante, historia_secante = secante()

    # return de todo?


def busqueda_de_raices(tolerancia):
    buscar_raices(funcion1, tolerancia)
    buscar_raices(funcion2, tolerancia)
    buscar_raices(funcion3, tolerancia)



def busqueda_con_programa():

def comparacion_de_metodos(historia):


def main():
    introduccion()
    grafico_de_las_funciones()
    historia_con_poca_tolerancia = busqueda_de_raices(1e-5)
    historia_con_mucha_tolerancia = busqueda_de_raices(1e-13)
    busqueda_con_programa()
    comparacion_de_metodos(historia_con_poca_tolerancia)
    comparacion_de_metodos(historia_con_mucha_tolerancia)



if __name__ == "__main__":
    main()
