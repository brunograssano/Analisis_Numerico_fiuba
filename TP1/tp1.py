from sympy import *
from scipy import optimize
from TP1.metodos_numericos import Biseccion
from TP1.metodos_numericos import Secante
from TP1.metodos_numericos import NewtonRaphson
from TP1.metodos_numericos import NewtonRaphsonModificado

from TP1.calculadoraAlfaLambda import calcularHistoriaDeOrden
from TP1.calculadoraAlfaLambda import calcularHistoraConstanteAsintotica

from TP1.Graficador import *

#%% Funciones varias


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



#%%% Punto B y D - Buscar raices y graficar ordenes

def MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante, tolerancia):
    if (tolerancia==1e-5):
        if raizBiseccion is not None:
            print("* Raiz Biseccion = {0} +- {1}".format('{0:.5f}'.format(raizBiseccion), '{0:.5f}'.format(tolerancia)))
        else:
            print("El Metodo de Biseccion no converge")
        if raizNewton is not None:
            print("* Raiz Newton = {0} +- {1}".format('{0:.5f}'.format(raizNewton), '{0:.5f}'.format(tolerancia)))
        else:
            print("El Metodo de Newton Raphson no converge")
        if raizNewtonModificado is not None:
            print("* Raiz Newton modificado = {0} +- {1}".format('{0:.5f}'.format(raizNewtonModificado), '{0:.5f}'.format(tolerancia)))
        else:
             print("El Metodo de Newton Raphson modificado no converge")
        if raizSecante is not None:
            print("* Raiz Secante = {0} +- {1}".format('{0:.5f}'.format(raizSecante), '{0:.5f}'.format(tolerancia)))
        else:
            print("El Metodo de la secante no converge")
    if (tolerancia==1e-13):
        if raizBiseccion is not None:
            print("* Raiz Biseccion = {0} +- {1}".format('{0:.13f}'.format(raizBiseccion), '{0:.13f}'.format(tolerancia)))
        else:
            print("El Metodo de Biseccion no converge")
        if raizNewton is not None:
            print("* Raiz Newton = {0} +- {1}".format('{0:.13f}'.format(raizNewton), '{0:.13f}'.format(tolerancia)))
        else:
            print("El Metodo de Newton Raphson no converge")
        if raizNewtonModificado is not None:
            print("* Raiz Newton modificado = {0} +- {1}".format('{0:.13f}'.format(raizNewtonModificado), '{0:.13f}'.format(tolerancia)))
        else:
             print("El Metodo de Newton Raphson modificado no converge")
        if raizSecante is not None:
            print("* Raiz Secante = {0} +- {1}".format('{0:.13f}'.format(raizSecante), '{0:.13f}'.format(tolerancia)))
        else:
            print("El Metodo de la secante no converge")



def BuscarRaices(Funcion, tolerancia, semillaNewton):
    raizBiseccion, historiaBiseccion = Biseccion(Funcion, 0.0, 2.0, tolerancia, 100)
    raizNewton, historiaNewton = NewtonRaphson(Funcion, tolerancia, 100, 1.0)
    raizNewtonModificado, historiaNewtonModificado = NewtonRaphsonModificado(Funcion, tolerancia, 100, semillaNewton)
    raizSecante, historiaSecante = Secante(Funcion, 2.0, 0.0, tolerancia, 100)
    MostrarRaices(raizBiseccion, raizNewton, raizNewtonModificado, raizSecante, tolerancia)
    graficarMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante, Funcion)

    return historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante



def ComparacionDeMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante, Funcion):
    ordenBiseccion, historiaOrdenBiseccion = calcularHistoriaDeOrden(historiaBiseccion)
    ordenNewton, historiaOrdenNewton = calcularHistoriaDeOrden(historiaNewton)
    ordenNewtonModificado, historiaOrdenNewtonModificado = calcularHistoriaDeOrden(historiaNewtonModificado)
    ordenSecante, historiaOrdenSecante = calcularHistoriaDeOrden(historiaSecante)

    constanteBis, historiaConstanteBiseccion = calcularHistoraConstanteAsintotica(historiaBiseccion, ordenBiseccion)
    constanteNR, historiaConstanteNewton = calcularHistoraConstanteAsintotica(historiaNewton, ordenNewton)
    constanteNRM, historiaConstanteNewtonModificado = calcularHistoraConstanteAsintotica(historiaNewtonModificado,
                                                                                                      ordenNewtonModificado)
    constanteSEC, historiaConstanteSecante = calcularHistoraConstanteAsintotica(historiaSecante, ordenSecante)

    print("\nApareceran ahora los graficos con las comparaciones de los ordenes de convergencia y la constante asintotica para los 4 metodos.")

    graficarOrdenDeConvergencia(historiaOrdenBiseccion, historiaOrdenNewton, \
                                historiaOrdenNewtonModificado, historiaOrdenSecante, Funcion)

    graficarConstantesAsintoticas(historiaConstanteBiseccion, historiaConstanteNewton, \
                                historiaConstanteNewtonModificado, historiaConstanteSecante, Funcion)



def BuscarYComparar(Funcion, tolerancia,semillaNewton):
    historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante = BuscarRaices(Funcion, tolerancia, semillaNewton)
    ComparacionDeMetodos(historiaBiseccion, historiaNewton, historiaNewtonModificado, historiaSecante, Funcion)



def BusquedaDeRaices(tolerancia):
    print("\nBuscamos y comparamos las constantes para la primera funcion\n")
    BuscarYComparar(Funcion1(), tolerancia, 1.0)

    print("\nBuscamos y comparamos las constantes para la segunda funcion\n")
    BuscarYComparar(Funcion2(), tolerancia, 1.0)

    print("\nBuscamos y comparamos las constantes para la tercera funcion\n")
    BuscarYComparar(Funcion3(), tolerancia, 1.3)




#%%% Punto C - Comprobacion con programa externo

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



#%% Main

def main():
    Introduccion()
    #BusquedaDeRaices(1e-5)
    #BusquedaDeRaices(1e-13)
    ComprobacionConProgramaExterno()



if __name__ == "__main__":
    main()