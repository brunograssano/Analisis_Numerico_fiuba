from metodos_numericos import Biseccion
from calculadoraAlfaLambda import calcularHistoraConstanteAsintotica
from calculadoraAlfaLambda import calcularHistoriaDeOrden
import numpy as np


def Funcion1(x):
    return (x ** 2) - 2


def Funcion2(x):
    return (x ** 5) - 6.6 * (x ** 4) + 21.312 * (x ** 2) - 38.016 * x + 17.28


def Funcion3(x):
    return (x - 1.5) * np.exp(-4 * ((x - 1.5) ** 2))


def Introduccion():
    print("~~~~~~ TP 1 - Analisis Numerico ~~~~~~ ")
    print("Integrantes grupo 1")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

def GraficoDeFunciones():

def BuscarRaices(Funcion, tolerancia):
    raizBiseccion, historiaBiseccion = Biseccion(Funcion, 0, 2, tolerancia, 50)
    raizNewton, historiaNewton = NewtonRaphson()
    raizNewtonModificado, historiaNewtonModificado = NewtonRaphson()
    raizSecante, historiaSecante = Secante()

    # return de todo?

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

def BusquedaDeRaices(tolerancia):
    print("Buscamos y comparamos las constantes para la primera funcion")
    BuscarYComparar(Funcion1,tolerancia)

    print("Buscamos y comparamos las constantes para la segunda funcion")
    BuscarYComparar(Funcion2,tolerancia)

    print("Buscamos y comparamos las constantes para la tercera funcion")
    BuscarYComparar(Funcion3,tolerancia)


def BusquedaConPrograma():

def main():
    Introduccion()
    GraficoDeFunciones()
    BusquedaDeRaices(1e-5)
    BusquedaDeRaices(1e-13)
    BusquedaConPrograma()




if __name__ == "__main__":
    main()
