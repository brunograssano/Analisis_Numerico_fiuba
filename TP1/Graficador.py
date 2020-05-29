import matplotlib.pyplot as plt

import numpy as np


# Recibe las 4 historias de los métodos y las grafica.
def graficarMetodos(historiaBiseccion, historiaNR, historiaNRM, historiaSecante):
    plt.figure()
    plt.plot(historiaBiseccion[:,0],historiaBiseccion[:,1],\
             '-', lw=1, label = "Método de la Biseccion", color = 'blue')
    plt.plot(historiaNR[:,0],historiaNR[:,1],\
             '-', lw=1, label = "Método de Newton Raphson", color = 'red')
    plt.plot(historiaNRM[:,0],historiaNRM[:,1],\
             '-', lw=1, label = "Método de Newton Raphson modificado", color = 'orange')
    plt.plot(historiaSecante[:,0],historiaSecante[:,1],\
             '-', lw=1, label = "Método de la Secante", color = 'green')
    
    plt.xlabel('Iteración')
    plt.title('Raiz estimada')
    plt.grid(True)
    plt.show()

    
#Recibe la historia de los órdenes de convergencia respecto a cada paso.
#OC: "Orden de convergencia"
def graficarOrdenDeConvergencia(historiaOCBiseccion, historiaOCNewtonRaphson,\
                                historiaOCNewtonRaphsonModif, historiaOCSec):
    plt.figure()
    plt.plot(historiaOCBiseccion[:,0],historiaOCBiseccion[:,1],\
             '-', lw=1, label = 'Método de la Bisección', color = 'blue')
    plt.plot(historiaOCNewtonRaphson[:,0],historiaOCNewtonRaphson[:,1],\
             '-', lw=1, label = 'Método de Newton Raphson', color = 'red')
    plt.plot(historiaOCNewtonRaphsonModif[:,0],historiaOCNewtonRaphsonModif[:,1],\
             '-', lw=1, label = 'Método de Newton Raphson modificado', color= 'orange')
    plt.plot(historiaOCSec[:,0],historiaOCSec[:,1],\
             '-', lw=1, label = 'Método de la Secante', color = 'green')
    
    plt.xlabel('Iteración')
    plt.title('Orden de convergencia estimado')
    plt.grid(True)
    plt.show()

## OJO, falta testearlo. Si bien teóricamente funciona, prácticamente no logra la convergencia teórica.
#Cuando tengamos los demás métodos deberíamos probarlo.
#Recibe como parámetros las historias de las constantes asintóticas respecto a cada paso.
# CA: "Constante asintótica"
def graficarConstantesAsintoticas(historiaCABIS, historiaCANR, historiaCANRM, historiaCASEC):
    plt.figure()
    plt.plot(historiaCABIS[:,0], historiaCABIS[:,1],\
             '-', lw=1, label = 'Método de la Bisección', color = 'blue')
        
    plt.plot(historiaCANR[:,0], historiaCANR[:,1],\
             '-', lw=1, label = 'Método de Newton Raphson', color = 'red')
    
    plt.plot(historiaCANRM[:,0],historiaCANRM[:,1],\
             '-', lw=1, label = 'Método de Newton Raphson modificado', color = 'orange')
        
    plt.plot(historiaCASEC[:,0],historiaCASEC[:,1],\
             '-', lw=1, label = 'Método de la Secante', color = 'green')
        
    plt.xlabel('Iteración')
    plt.title('Constante asintótica aproximada')
    plt.grid(True)
    plt.show()



def graficar(historiaBIS, historiaNR, historiaNRF, historiaSEC):
    
    graficarMetodos(historiaBIS, historiaNR, historiaNRF, historiaSEC);
    
    alfaBIS, historiaOCBIS = calcularHistoriaDeOrden(historiaBiseccion)
    alfaNR, historiaOCNR = calcularHistoriaDeOrden(historiaNR)
    alfaNRM, historiaOCNRM = calcularHistoriaDeOrden(historiaNRM)
    alfaSEC, historiaOCSEC = calcularHistoriaDeOrden(historiaSEC)
    
    graficarOrdenDeConvergencia(historiaOCBIS, historiaOCNR,historiaOCNRM, historiaOCSEC)
    
    lambdaBIS, historiaCABIS = calcularHistoraConstanteAsintotica(historiaBiseccion, alfaBIS)
    lambdaNR, historiaCANR = calcularHistoraConstanteAsintotica(historiaOCNR, alfaNR)
    lambdaNRM, historiaCANRM = calcularHistoraConstanteAsintotica(historiaOCNRM, alfaNRM)
    lambdaSEC, historiaCASEC = calcularHistoraConstanteAsintotica(historiaOCSecante, alfaSEC)
    
    graficarConstantesAsintoticas(historiaCABiseccion, historiaCANR, historiaCANRM, historiaCASecante)
    
    
    