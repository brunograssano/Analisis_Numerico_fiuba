import matplotlib.pyplot as plt
import numpy as np


#Falta toquetear cómo queremos que aparezca la información.
#(Sí, son las mismas funciones con distintos title, si quieren lo reworkeamos, pero dsp [por eso el #]).

def graficarMetodo(historia,metodo):
    plt.figure()
    plt.plot(historia[:,0],historia[:,1],\
             '-', lw=1, label = metodo)
    plt.xlabel('Iteración')
    plt.title('Raiz estimada')
    plt.grid(True)
    plt.show()

def graficarOrdenDeConvergencia(historia):
    plt.figure()
    plt.plot(historia[:,0],historia[:,1],\
             '-', lw=1, label = 'Alfa')
    plt.xlabel('Iteración')
    plt.title('Alfa estimado')
    plt.grid(True)
    plt.show()

def graficarConstanteAsintotica(historia):
    plt.figure()
    plt.plot(historia[:,0],historia[:,1],\
             '-', lw=1, label = 'Lambda')
    plt.xlabel('Iteración')
    plt.title('Constante asintótica aproximada')
    plt.grid(True)
    plt.show()