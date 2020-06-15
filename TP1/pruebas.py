from TP1.metodos_numericos import Biseccion
from TP1.metodos_numericos import Secante
from TP1.metodos_numericos import NewtonRaphson
from TP1.metodos_numericos import NewtonRaphsonModificado
from TP1.Graficador import *
#from calculadoraAlfaLambda import *
from TP1.calculadora_nueva import *

import numpy as np
from sympy import *

def funcionPrueba1():
    x = symbols('x')
    return x**2 - 2
def funcionPrueba2():
    x = symbols('x') 
    return x**3 - 2
def funcionPrueba3():
    x = symbols('x')    
    return x**4 - 2
def funcionPrueba4():
    x = symbols('x')
    return x**5 - 2

def funcionPrueba5():# entre 1 y 3 esta la raiz esta deberia de ser 2,36...
    x = symbols('x')
    return x**5 + x**3 - x - 84

def funcionClase():
    x = symbols('x')
    return x**3 + 4*x**2 - 10

#Pruebas de uso
def prueba1():
    print("BISECCION")
    raizB, historiaB = Biseccion(funcionPrueba1(), 0, 2, 1e-5, 50)
    #print(raizB)
    #print(historiaB)
    
    print("NR")
    
    raizNR, historiaNR = NewtonRaphson(funcionPrueba1(), 1e-5, 30, 1)
    #print(raizNR)
    #print(historiaNR)
    
    print("NRM")
    
    raizNRM, historiaNRM = NewtonRaphsonModificado(funcionPrueba1(), 1e-5, 30, 1)
    #print(raizNRM)
    #print(historiaNRM)
    
    print("SECANTE F1")
    
    raizSEC, historiaSEC = Secante(funcionPrueba1(), 2, 0, 1e-15, 50)
    print(raizSEC)
    print(historiaSEC)
    
    print ("HISTORIA DE ORDEN F1")
    #alfaB, ordenB =calcularHistoriaDeOrden(historiaB)
    #print(alfaB)
    #print(ordenB)
    
    alfaSEC, ordenSEC =CalcularHistoriaDeOrden(historiaSEC)
    print(alfaSEC)
    print(ordenSEC)
    
    
    print("SECANTE F2")
    raizSEC, historiaSEC = Secante(funcionPrueba2(), 2, 0, 1e-15, 50)
    print(raizSEC)
    print(historiaSEC)
    
    print ("HISTORIA DE ORDEN F2")
    alfaSEC, ordenSEC =CalcularHistoriaDeOrden(historiaSEC)
    print(alfaSEC)
    print(ordenSEC)
    
    print("SECANTE F3")
    raizSEC, historiaSEC = Secante(funcionPrueba3(), 1.5, 0.5, 1e-15, 50)
    print(raizSEC)
    print(historiaSEC)
    
    print ("HISTORIA DE ORDEN F3")
    alfaSEC, ordenSEC =CalcularHistoriaDeOrden(historiaSEC)
    print(alfaSEC)
    print(ordenSEC)
    
    print("CONSTANTE ASINTOTICA SEC F3")
    constAsintSEC, histConstAsintSEC = CalcularHistoriaConstanteAsintotica(ordenSEC, alfaSEC)
    print(constAsintSEC) #estaria llegando a 0.5?
    print(histConstAsintSEC)
    
    print("SECANTE F4")
    raizSEC, historiaSEC = Secante(funcionPrueba4(), 1.5, 0.5, 1e-15, 50)
    print(raizSEC)
    print(historiaSEC)
    
    print ("HISTORIA DE ORDEN F4")
    alfaSEC, ordenSEC =CalcularHistoriaDeOrden(historiaSEC)
    print(alfaSEC)
    print(ordenSEC)
    
    print("CONSTANTE ASINTOTICA SEC F4")
    constAsintSEC, histConstAsintSEC = CalcularHistoriaConstanteAsintotica(ordenSEC, alfaSEC)
    print(constAsintSEC) #aca no se acerca a 0.5
    print(histConstAsintSEC)
    
    print("SECANTE F5")
    raizSEC, historiaSEC = Secante(funcionPrueba5(), 2.8, 2.2, 1e-15, 50)
    print(raizSEC)
    print(historiaSEC)
    
    print ("HISTORIA DE ORDEN F5")
    alfaSEC, ordenSEC =CalcularHistoriaDeOrden(historiaSEC)
    print(alfaSEC)
    print(ordenSEC)
    
    print("CONSTANTE ASINTOTICA SEC F5")
    constAsintSEC, histConstAsintSEC = CalcularHistoriaConstanteAsintotica(ordenSEC, alfaSEC)
    print(constAsintSEC) #tendria que dar mas cercano a 0.5, quizas con mas iteraciones llega
    print(histConstAsintSEC)
    
    
    print("NR F5")
    raizNR, historiaNR = NewtonRaphson(funcionPrueba5(), 1e-15, 50, 1.8)
    print(raizNR)
    print(historiaNR)
    
    print ("HISTORIA DE ORDEN NR F5")
    alfaNR, ordenNR =CalcularHistoriaDeOrden(historiaNR)
    print(alfaNR)
    print(ordenNR)
    
    print("CONSTANTE ASINTOTICA NR F5")
    constAsintNR, histConstAsintNR = CalcularHistoriaConstanteAsintotica(ordenNR, alfaNR)
    print(constAsintNR) #tendria que dar mas cercano a 0.5
    print(histConstAsintNR)
    
    print("NR F4")
    raizNR, historiaNR = NewtonRaphson(funcionPrueba4(), 1e-15, 50, 0.5)
    print(raizNR)
    print(historiaNR)
    
    print ("HISTORIA DE ORDEN NR F4")
    alfaNR, ordenNR =CalcularHistoriaDeOrden(historiaNR)
    print(alfaNR)
    print(ordenNR)
    
    print("CONSTANTE ASINTOTICA NR F4")
    constAsintNR, histConstAsintNR = CalcularHistoriaConstanteAsintotica(ordenNR, alfaNR)
    print(constAsintNR) #tendria que dar mas cercano a 0.5
    print(histConstAsintNR)
    
    
    
    
    
def pruebaBiseccion1_SiElMaximoDeIteracionesEsMenorQueLasIteracionesNecesariasParaCalcularLaRaizNoDebeHaberUnOutOfBounds():    
    raizB, historiaB = Biseccion(funcionPrueba1(),0, 2, 1e-13, 10)    
    assert(len(historiaB)==10)
    
    
def pruebaBiseccion2_DadaLaFuncion1_LaRaizEsLaCorrectaParaLaTolerancia():
    raizB, historiaB = Biseccion(funcionPrueba1(), 0, 2, 1e-3, 30)
    #(0, 1)
    #(1, 1.5)
    #(2, 1.25)
    #(3, 1.375)
    #(4, 1.4375)
    #(5, 1.40625)
    #(6, 1.421875)
    #(7, 1.4140625)
    #(8, 1.41796875)
    #(9, 1.416015625)
    #(10,1.4150390625)
    assert(raizB == 1.4150390625)


def pruebasBiseccion():
    pruebaBiseccion1_SiElMaximoDeIteracionesEsMenorQueLasIteracionesNecesariasParaCalcularLaRaizNoDebeHaberUnOutOfBounds()
    pruebaBiseccion2_DadaLaFuncion1_LaRaizEsLaCorrectaParaLaTolerancia()
   
    
    
def pruebaNewtonRaphson1_DadaLaFuncion2_SiElMáximoDeIteracionesEsMenorQueLasIteracionesNecesariasParaCalcularLaRaizNoDebeHaberUnOutOfBounds():
    raizNR, historiaNR = NewtonRaphson(funcionPrueba2(), 1e-13, 3, 1)
    #assert(len(historiaNR) == 3)

def pruebaNewtonRaphson2_DadaLaFuncion2_LaRaizEsLaCorrectaParaLaTolerancia():
    raizNR, historiaNR = NewtonRaphson(funcionPrueba2(), 1e-4, 5, 1)
    #(0, 1)
    #(1, 4/3)
    #(2, 1.263888889)
    #(3, 1.259933493)
    #(4, 1.25992105)
    assert(historiaNR[0][1] == 1)
    assert(historiaNR[1][1] == 4/3)
    assert(historiaNR[2][1] == 91/72)
    assert(historiaNR[3][1] == 91/72 - (((91/72)**3) - 2)/(3 * (91/72)**2))
    assert(historiaNR[3][1] - historiaNR[4][1] < 1e-4)
    
    
def pruebasNewtonRaphson():
    pruebaNewtonRaphson1_DadaLaFuncion2_SiElMáximoDeIteracionesEsMenorQueLasIteracionesNecesariasParaCalcularLaRaizNoDebeHaberUnOutOfBounds()
    pruebaNewtonRaphson2_DadaLaFuncion2_LaRaizEsLaCorrectaParaLaTolerancia()
    
def pruebaClase():
    raizB, histB = Biseccion(funcionClase(),0,2,1e-10,50)
    raizNR,histNR = NewtonRaphson(funcionClase(),1e-10,50,1)
    raizNRM, histNRM = NewtonRaphsonModificado(funcionClase(),1e-10,50,1)
    raizS, histS = Secante(funcionClase(), 0,2,1e-10,50)

    print(raizB)
    #print(raizNR)
    print("Hist NR prueba clase")
    print(histNR)
    #print(raizNRM)
    print("Hist NRM prueba clase")
    print(histNRM)
    #print(raizS)
    print("Hist Secante prueba clase")
    print(histS)

    alfaB, histAlfaB = CalcularHistoriaDeOrden2(histB)
    alfaNR,histAlfaNR = CalcularHistoriaDeOrden2(histNR)
    alfaNRM,histAlfaNRM = CalcularHistoriaDeOrden2(histNRM)
    alfaS, histAlfaS = CalcularHistoriaDeOrden2(histS)

    GraficarOrdenDeConvergencia(histAlfaB,histAlfaNR,histAlfaNRM, histAlfaS, funcionClase())

    lB,histLB = CalcularHistoriaConstanteAsintotica(histAlfaB, alfaB)
    lNR, histLNR = CalcularHistoriaConstanteAsintotica(histAlfaNR, alfaNR)
    lNRM, histLNRM = CalcularHistoriaConstanteAsintotica(histAlfaNRM, alfaNRM)
    lS, histLS = CalcularHistoriaConstanteAsintotica(histAlfaS, alfaS)

    GraficarConstantesAsintoticas(histLB, histLNR, histLNRM, histLS, funcionClase())

def funcionPruebaCercaCero():
    x = symbols('x')
    return x**3 + x**2 - 10**(-5)


def funcionEzequiel():
    x = symbols('x')
    return (x ** 2) / 4 - sin(x)

def pruebaDatosEzequiel():
    #comparar con los datos del campus, da lo mismo basicamente
    raizS,histS = Secante(funcionEzequiel(), 1.6, 2.6, 1e-13, 50)
    print("APARECE EL ALFA S")
    alfaS,histAlfaS = CalcularHistoriaDeOrden(histS)
    print("\n \nAPARECE EL LAMBDA S")
    lambdaS,histLambdaS = CalcularHistoriaConstanteAsintotica(histS, alfaS)

    raizNR, histNR = NewtonRaphson(funcionEzequiel(), 1e-13, 50, 1.6)
    print("\n \nAPARECE EL ALFA NR")
    alfaNR, histAlfaNR = CalcularHistoriaDeOrden(histNR)
    print("\n \nAPARECE EL LAMBDA NR")
    lambdaNR, histLambdaNR = CalcularHistoriaConstanteAsintotica(histNR, alfaNR)



#raizB, histB = Biseccion(funcionPruebaCercaCero(),-2,2,1e-11,50)
#print(histB)

pruebasBiseccion()

pruebasNewtonRaphson()

#prueba1()

#pruebaClase()

pruebaDatosEzequiel()


