from metodos_numericos import Biseccion
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

def MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante):
    print("Raiz Biseccion: ", raizBiseccion)
    print("Raiz Newton: ", raizNewton)
    print("Raiz Newton modificado:", raizNewtonModificado)
    print("Raiz Secante: ", raizSecante)

def BuscarRaices(Funcion, tolerancia):
    raizBiseccion, historiaBiseccion = Biseccion(Funcion, 0, 2, tolerancia, 50)
    raizNewton, historiaNewton = NewtonRaphson()
    raizNewtonModificado, historiaNewtonModificado = NewtonRaphson()
    raizSecante, historiaSecante = Secante()

    MostrarRaices(raizBiseccion,raizNewton,raizNewtonModificado,raizSecante)
    return historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante

def busqueda_de_raices(tolerancia):
    BuscarRaices(Funcion1, tolerancia)
    BuscarRaices(Funcion2, tolerancia)
    BuscarRaices(Funcion3, tolerancia)
    comparacion_de_metodos(tolerancia)

def BusquedaConPrograma():

def ComparacionDeMetodos(historia):


def main():
    Introduccion()
    GraficoDeFunciones()
    BusquedaDeRaices(1e-5)
    BusquedaDeRaices(1e-13)
    BusquedaConPrograma()




if __name__ == "__main__":
    main()
