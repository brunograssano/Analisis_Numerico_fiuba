from sympy import *
from scipy import optimize
import numpy as np

from metodos_numericos import Biseccion
from metodos_numericos import Secante
from metodos_numericos import NewtonRaphson
from metodos_numericos import NewtonRaphsonModificado

#from calculadoraAlfaLambda import CalcularHistoriaDeOrden
#from calculadoraAlfaLambda import CalcularHistoriaConstanteAsintotica

from calculadora_nueva import *

from Graficador import *

from printer import formatear


# Convencion utilizada a lo largo del trabajo
# camelCase para variables
# CamelCase para funciones



def Funcion1():
    x = symbols('x')
    funcion = (x ** 2) - 2
    return funcion


def Funcion2():
    x = symbols('x')
    funcion = (x ** 5) - 6.6 * (x ** 4) + 5.12 * (x ** 3) + 21.312 * (x ** 2) - 38.016 * x + 17.28
    return funcion


def Funcion3():
    x = symbols('x')
    funcion = (x - 1.5) * exp(-4 * ((x - 1.5) ** 2))
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
    """
    Mostrara por pantalla las raices obtenidas dependiendo de los dos tipos distintos de tolerancia.
    Si no se obtuvo raiz durante su busqueda, se mostrara un mensaje indicando el metodo que fallo
    """
    if tolerancia == 1e-5:
        if raizBiseccion is not None:
            print("* Raiz Biseccion = {0} +- {1}".format('{0:.5f}'.format(raizBiseccion), '{0:.5f}'.format(tolerancia)))
        else:
            print("El Metodo de Biseccion no converge")
        if raizNewton is not None:
            print("* Raiz Newton = {0} +- {1}".format('{0:.5f}'.format(raizNewton), '{0:.5f}'.format(tolerancia)))
        else:
            print("El Metodo de Newton Raphson no converge")
        if raizNewtonModificado is not None:
            print("* Raiz Newton modificado = {0} +- {1}".format('{0:.5f}'.format(raizNewtonModificado),
                                                                 '{0:.5f}'.format(tolerancia)))
        else:
            print("El Metodo de Newton Raphson modificado no converge")
        if raizSecante is not None:
            print("* Raiz Secante = {0} +- {1}".format('{0:.5f}'.format(raizSecante), '{0:.5f}'.format(tolerancia)))
        else:
            print("El Metodo de la secante no converge")
    if tolerancia == 1e-13:
        if raizBiseccion is not None:
            print(
                "* Raiz Biseccion = {0} +- {1}".format('{0:.13f}'.format(raizBiseccion), '{0:.13f}'.format(tolerancia)))
        else:
            print("El Metodo de Biseccion no converge")
        if raizNewton is not None:
            print("* Raiz Newton = {0} +- {1}".format('{0:.13f}'.format(raizNewton), '{0:.13f}'.format(tolerancia)))
        else:
            print("El Metodo de Newton Raphson no converge")
        if raizNewtonModificado is not None:
            print("* Raiz Newton modificado = {0} +- {1}".format('{0:.13f}'.format(raizNewtonModificado),
                                                                 '{0:.13f}'.format(tolerancia)))
        else:
            print("El Metodo de Newton Raphson modificado no converge")
        if raizSecante is not None:
            print("* Raiz Secante = {0} +- {1}".format('{0:.13f}'.format(raizSecante), '{0:.13f}'.format(tolerancia)))
        else:
            print("El Metodo de la secante no converge")


def BuscarRaices(Funcion, tolerancia, semillaNewton):
    """
    Recibe la funcion en su forma de simbolos y una tolerancia valida.
    Necesita tambien de una semilla cercana a la raiz para el metodo de Newton Raphson.
    """
    raizBiseccion, historiaBiseccion = Biseccion(Funcion, 0.0, 2.0, tolerancia, 100)
    raizNewton, historiaNewton = NewtonRaphson(Funcion, tolerancia, 100, semillaNewton)
    raizNewtonModificado, historiaNewtonModificado = NewtonRaphsonModificado(Funcion, tolerancia, 100, semillaNewton)
    raizSecante, historiaSecante = Secante(Funcion, 1.0, 1.6, tolerancia, 100)

    MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante, tolerancia)
    GraficarMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante, Funcion)
    return historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante


def ComparacionDeMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante, Funcion):
    """
    Calculara los ordenes de convergencia y las constantes asintoticas para la funcion indicada en su forma de simbolos.
    Necesita tambien de las historias de la busqueda con cada metodo.
    """
    #print("\n \n ------------APARECEN ALFAS -----------")
    #print("\n \n BISECCION")
    ordenBiseccion, historiaOrdenBiseccion = CalcularHistoriaDeOrden(historiaBiseccion)

    #print("\n \n NEWTON")
    ordenNewton, historiaOrdenNewton = CalcularHistoriaDeOrden(historiaNewton)

    #print("\n \n NRM")
    ordenNewtonModificado, historiaOrdenNewtonModificado = CalcularHistoriaDeOrden(historiaNewtonModificado)

    #print("\n \n SECANTE")
    ordenSecante, historiaOrdenSecante = CalcularHistoriaDeOrden(historiaSecante)

    #print("\n \n ------------APARECEN LAMBDAS -----------")

    #print("\n \n BISECCION")
    constanteBis, historiaConstanteBiseccion = CalcularHistoriaConstanteAsintotica(historiaBiseccion, ordenBiseccion)

    #print("\n \n NEWTON")
    constanteNR, historiaConstanteNewton = CalcularHistoriaConstanteAsintotica(historiaNewton, ordenNewton)

    #print("\n \n NRM")
    constanteNRM, historiaConstanteNewtonModificado = CalcularHistoriaConstanteAsintotica(historiaNewtonModificado,ordenNewtonModificado)

    #print("\n \n SECANTE")  
    constanteSEC, historiaConstanteSecante = CalcularHistoriaConstanteAsintotica(historiaSecante, ordenSecante)

    #print("\nApareceran ahora los graficos con las comparaciones de los ordenes de convergencia y la constante asintotica para los 4 metodos.")

    GraficarOrdenDeConvergencia(historiaOrdenBiseccion, historiaOrdenNewton, historiaOrdenNewtonModificado, historiaOrdenSecante, Funcion)

    GraficarConstantesAsintoticas(historiaConstanteBiseccion, historiaConstanteNewton, historiaConstanteNewtonModificado, historiaConstanteSecante, Funcion)


def BuscarYComparar(Funcion, tolerancia, semillaNewton):
    historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante = BuscarRaices(Funcion, tolerancia, semillaNewton)
    ComparacionDeMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante, Funcion)


def BusquedaDeRaices(tolerancia):
    print("\nBuscamos y comparamos las constantes para la primera funcion\n")
    BuscarYComparar(Funcion1(), tolerancia, 1.0)

    print("\nBuscamos y comparamos las constantes para la segunda funcion\n")

    BuscarYComparar(Funcion2(), tolerancia, 1.0)

    print("\nBuscamos y comparamos las constantes para la tercera funcion\n")
    BuscarYComparar(Funcion3(), tolerancia, 1.3)



def Funcion1ParaProgramaExterno(x):
    return x ** 2 - 2


def Funcion2ParaProgramaExterno(x):
    return (x ** 5) - 6.6 * (x ** 4) + 5.12 * (x ** 3) + 21.312 * (x ** 2) - 38.016 * x + 17.28


def Funcion3ParaProgramaExterno(x):
    return (x - 1.5) * np.exp(-4 * ((x - 1.5) ** 2))


def ComprobacionConProgramaExterno():
    print("\n~~~~~~~~~~~Punto C del TP1~~~~~~~~~~~~~\n")
    print("Se mostraran ahora las raices calculadas por los metodos implementados en otras bibliotecas, en este caso de sympy.\n (Solo biseccion y NR)")

    print("\n~~~~Para la funcion 1~~~~")
    raizBiseccion = optimize.bisect(Funcion1ParaProgramaExterno, 0, 2)
    raizNewton = optimize.newton(Funcion1ParaProgramaExterno, 1)
    print("Usando biseccion: ", raizBiseccion)
    print("Usando Newton Raphson: ", raizNewton)

    print("\n~~~~Para la funcion 2~~~~")
    raizBiseccion = optimize.bisect(Funcion2ParaProgramaExterno, 0, 2)
    raizNewton = optimize.newton(Funcion2ParaProgramaExterno, 1)
    print("Usando biseccion: ", raizBiseccion)
    print("Usando Newton Raphson: ", raizNewton)

    print("\n~~~~Para la funcion 3~~~~")
    raizBiseccion = optimize.bisect(Funcion3ParaProgramaExterno, 0, 2)
    raizNewton = optimize.newton(Funcion3ParaProgramaExterno, 1.3)
    print("Usando biseccion: ", raizBiseccion)
    print("Usando Newton Raphson: ", raizNewton)

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")



def main():
    Introduccion()
    #BusquedaDeRaices(1e-5)
    #print("\n~~~~~Repetimos con mayor tolerancia~~~~~")
    #BusquedaDeRaices(1e-13)
    #ComprobacionConProgramaExterno()
    hB, hNR, hNRM, hSEC = BuscarRaices(Funcion2(), 1e-13, 1.3)
    formatear(hNR)
if __name__ == "__main__":
    main()
