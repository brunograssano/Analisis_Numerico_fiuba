from metodos_numericos import Biseccion
from metodos_numericos import Secante
import numpy as np


def Funcion1(x):
    return (x ** 2) - 2


def Funcion2(x):
    return (x ** 5) - 6.6 * (x ** 4) + 21.312 * (x ** 2) - 38.016 * x + 17.28


def Funcion3(x):
    return (x - 1.5) * np.exp(-4 * ((x - 1.5) ** 2))


def Introduccion():
    print("~~~~~~ TP 1 - Analisis Numerico ~~~~~~ ")
    print("/\/\ Integrantes grupo 1 /\/\ ")
    print("* Adrian Romero 103371")
    print("* Andres Guillemi 104006")
    print("* Bruno Grassano 103855")
    print("* Ezequiel Rodriguez 103976")
    print("* Joaquin Gomez 103735")
    print("* Lukas De Angelis Riva 103784")

    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    print("Se realizaran primero los calculos de la busqueda de raices y comparacion de metodos para la tolerancia 1e-5\n y despues para 1e-13 ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")


def MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante,tolerancia):
    print("Raiz Biseccion = {0} +- {1}".format(raizBiseccion, tolerancia))
    print("Raiz Newton = {0} +- {1}".format(raizNewton, tolerancia))
    print("Raiz Newton modificado = {0} +- {1}".format(raizNewtonModificado, tolerancia))
    print("Raiz Secante = {0} +- {1}".format(raizSecante, tolerancia))

def BuscarRaices(Funcion, tolerancia):
    raizBiseccion, historiaBiseccion = Biseccion(Funcion, 0, 2, tolerancia, 50)
    raizNewton, historiaNewton = NewtonRaphson()
    raizNewtonModificado, historiaNewtonModificado = NewtonRaphson()
    raizSecante, historiaSecante = Secante()

    MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante, tolerancia)
    return historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante

def ComparacionDeMetodos(historiaBiseccion,historiaNewton,historiaNewtonModificado,historiaSecante):
    ordenBiseccion = calcularHistoriaDeOrden(historiaBiseccion)
    ordenNewton = calcularHistoriaDeOrden(historiaNewton)
    ordenNewtonModificado = calcularHistoriaDeOrden(historiaNewtonModificado)
    ordenSecante = calcularHistoriaDeOrden(historiaSecante)

    constanteBiseccion = calcularHistoraConstanteAsintotica(historia, alfa)
    constanteNewton = calcularHistoraConstanteAsintotica(historia, alfa)
    constanteNewtonModificado = calcularHistoraConstanteAsintotica(historia, alfa)
    constanteSecante = calcularHistoraConstanteAsintotica(historia, alfa)

    print("Se mostraran ahora las comparaciones de los ordenes de convergencia y la constante asintotica para los 4 metodos")
    graficarOrdenDeConvergencia(ordenBiseccion,ordenNewton,ordenNewtonModificado,ordenSecante)
    graficarConstanteAsintotica(constanteBiseccion,constanteNewton,constanteNewtonModificado,constanteSecante)

def BuscarYComparar(Funcion, tolerancia): #mejor nombre?
    historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante = BuscarRaices(Funcion, tolerancia)
    ComparacionDeMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante)
    MostrarRaices(raizBiseccion,raizNewton,raizNewtonModificado,raizSecante)


def BusquedaDeRaices(tolerancia):
    print("Buscamos y comparamos las constantes para la primera funcion")
    BuscarYComparar(Funcion1,tolerancia)

    print("Buscamos y comparamos las constantes para la segunda funcion")
    BuscarYComparar(Funcion2,tolerancia)

    print("Buscamos y comparamos las constantes para la tercera funcion")
    BuscarYComparar(Funcion3,tolerancia)


def main():
    Introduccion()
    BusquedaDeRaices(1e-5)
    BusquedaDeRaices(1e-13)





if __name__ == "__main__":
    main()
