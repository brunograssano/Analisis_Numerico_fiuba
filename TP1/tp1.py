import numpy as np
from sympy import *

from metodos_numericos import Biseccion
from metodos_numericos import Secante
from metodos_numericos import NewtonRaphson
from metodos_numericos import NewtonRaphsonModificado

from calculadoraAlfaLambda import calcularHistoriaDeOrden
from calculadoraAlfaLambda import calcularHistoraConstanteAsintotica

from Graficador import *


def Funcion1():
    x = symbols('x')
    funcion = (x ** 2) - 2
    return funcion


def Funcion2():
    x = symbols('x')
    funcion = (x ** 5) - 6.6 * (x ** 4) + 21.312 * (x ** 2) - 38.016 * x + 17.28
    return funcion


def Funcion3():
    x = symbols('x')
    funcion = (x - 1.5) * np.exp(-4 * ((x - 1.5) ** 2))
    return funcion


def Introduccion():
    print("\n\n~~~~~~ TP 1 - Analisis Numerico ~~~~~~ ")
    print("/\/\ Integrantes grupo 1 /\/\ ")
    print("* Adrian Romero 103371")
    print("* Andres Guillemi 104006")
    print("* Bruno Grassano 103855")
    print("* Ezequiel Rodriguez 103976")
    print("* Joaquin Gomez 103735")
    print("* Lukas De Angelis Riva 103784")

    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    print("Se realizaran primero los calculos de la busqueda de raices y\
     comparacion de metodos para la tolerancia 1e-5\n y despues para 1e-13 ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n")


def MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante, tolerancia):
    print("* Raiz Biseccion = {0} +- {1}".format(raizBiseccion, tolerancia))
    print("* Raiz Newton = {0} +- {1}".format(raizNewton, tolerancia))
    print("* Raiz Newton modificado = {0} +- {1}".format(raizNewtonModificado, tolerancia))
    print("* Raiz Secante = {0} +- {1}".format(raizSecante, tolerancia))


def BuscarRaices(Funcion, tolerancia):
    raizBiseccion, historiaBiseccion = Biseccion(Funcion, 0, 2, tolerancia, 50)
    raizNewton, historiaNewton = NewtonRaphson(Funcion, tolerancia, 50, 1)
    raizNewtonModificado, historiaNewtonModificado = NewtonRaphsonModificado(Funcion, tolerancia, 50, 1)
    raizSecante, historiaSecante = Secante(Funcion, 2, 0, tolerancia, 50)

    MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante, tolerancia)
    return historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante


def ComparacionDeMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante):
    ordenBiseccion, historiaOrdenBiseccion = calcularHistoriaDeOrden(historiaBiseccion)
    ordenNewton, historiaOrdenNewton = calcularHistoriaDeOrden(historiaNewton)
    ordenNewtonModificado, historiaOrdenNewtonModificado = calcularHistoriaDeOrden(historiaNewtonModificado)
    ordenSecante, historiaOrdenSecante = calcularHistoriaDeOrden(historiaSecante)

    constanteBiseccion, historiaConstanteBiseccion = calcularHistoraConstanteAsintotica(historiaBiseccion,
                                                                                        ordenBiseccion)
    constanteNewton, historiaConstanteNewton = calcularHistoraConstanteAsintotica(historiaNewton, ordenNewton)
    constanteNewtonModificado, historiaConstanteNewtonModificado = calcularHistoraConstanteAsintotica(
        historiaNewtonModificado, ordenNewtonModificado)
    constanteSecante, historiaConstanteSecante = calcularHistoraConstanteAsintotica(historiaSecante, ordenSecante)

    print("\nApareceran ahora los graficos con las comparaciones de los ordenes de convergencia y la constante asintotica para los 4 metodos.")

    graficarOrdenDeConvergencia(historiaOrdenBiseccion, historiaOrdenNewton, \
                                historiaOrdenNewtonModificado, historiaOrdenSecante)

    graficarConstantesAsintoticas(historiaConstanteBiseccion, historiaConstanteNewton, \
                                historiaConstanteNewtonModificado, historiaConstanteSecante)


def BuscarYComparar(Funcion, tolerancia):  # mejor nombre?
    historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante = BuscarRaices(Funcion, tolerancia)
    ComparacionDeMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante)


def BusquedaDeRaices(tolerancia):
    print("\nBuscamos y comparamos las constantes para la primera funcion\n")
    BuscarYComparar(Funcion1(), tolerancia)

    print("\nBuscamos y comparamos las constantes para la segunda funcion\n")
    BuscarYComparar(Funcion2(), tolerancia)

    print("\nBuscamos y comparamos las constantes para la tercera funcion\n")
    BuscarYComparar(Funcion3(), tolerancia)


def main():
    Introduccion()
    BusquedaDeRaices(1e-5)
    BusquedaDeRaices(1e-13)


if __name__ == "__main__":
    main()
