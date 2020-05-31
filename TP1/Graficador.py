import matplotlib.pyplot as plt
import numpy as np

def maximoLen(historiaBIS, historiaNR, historiaNRM, historiaSEC):
    bis = len(historiaBIS)
    nr = len(historiaNR)
    nrm = len(historiaNRM)
    sec = len(historiaSEC)
    return max(bis, nr, nrm, sec)

def extenderHistoria(historia, tope):
    if(historia.size == 0):
        return historia
    long = len(historia)
    
    historiaExtendida = np.zeros((tope,2))
    
    raiz = historia[long - 1][1]
    
    for i in range(0, tope):

        if i < long:
            historiaExtendida[i][0] = i
            historiaExtendida[i][1] = historia[i][1]
        else:
            historiaExtendida[i][0] = i
            historiaExtendida[i][1] = raiz

    return historiaExtendida



def extenderHistorias(historiaBIS, historiaNR, historiaNRM, historiaSEC):
    tope = maximoLen(historiaBIS, historiaNR, historiaNRM, historiaSEC)
    return extenderHistoria(historiaBIS, tope)\
        , extenderHistoria(historiaNR, tope)\
        , extenderHistoria(historiaNRM, tope)\
        , extenderHistoria(historiaSEC, tope)

def graficar(historia, nombre, color):
    if(historia.size != 0):
        plt.plot(historia[:, 0], historia[:, 1], \
                 '-', lw=1, label=nombre, color=color)
    else:
        plt.plot(0,0,'*',lw=0, label = nombre +'; no suf datos.', color = color)




# Recibe las 4 historias de los métodos y las grafica.
def graficarMetodos(historiaBiseccion, historiaNR, historiaNRM, historiaSecante, funcion):
    plt.figure()
    historiaBiseccion, historiaNR, historiaNRM, historiaSecante = \
        extenderHistorias(historiaBiseccion, historiaNR, historiaNRM, historiaSecante)
    
    graficar(historiaBiseccion, 'Biseccion', 'blue')
    graficar(historiaNR, 'Newton-Raphson', 'red')
    graficar(historiaNRM, 'NR modificado', 'orange')
    graficar(historiaSecante, 'Secante', 'green')
    
    plt.xlabel('Iteración')
    plt.ylabel('Raiz')
    plt.legend(loc='best')
    plt.title(funcion)
    plt.grid(True)
    plt.show()


# Recibe la historia de los órdenes de convergencia respecto a cada paso.
# OC: "Orden de convergencia"
def graficarOrdenDeConvergencia(historiaOCBiseccion, historiaOCNewtonRaphson, \
                                historiaOCNewtonRaphsonModif, historiaOCSec, funcion):
    plt.figure()
    axes = plt.gca()
    axes.set_ylim([0,3])  
    graficar(historiaOCBiseccion, 'Biseccion', 'blue')
    graficar(historiaOCNewtonRaphson, 'Newton-Raphson', 'red')
    graficar(historiaOCNewtonRaphsonModif, 'NR modificado', 'orange')
    graficar(historiaOCSec, 'Secante', 'green')
    
    plt.xlabel('Iteración')
    plt.xlabel('Iteración')
    plt.ylabel('Alfa')
    plt.legend(loc='best')
    plt.title(funcion)
    plt.grid(True)
    plt.show()    


## OJO, falta testearlo. Si bien teóricamente funciona, prácticamente no logra la convergencia teórica.
# Cuando tengamos los demás métodos deberíamos probarlo.
# Recibe como parámetros las historias de las constantes asintóticas respecto a cada paso.
# CA: "Constante asintótica"
def graficarConstantesAsintoticas(historiaCABIS, historiaCANR, historiaCANRM, historiaCASEC, funcion):
    plt.figure()
    axes = plt.gca()
    axes.set_ylim([0,3])
    graficar(historiaCABIS , 'Biseccion', 'blue')
    graficar(historiaCANR, 'Newton-Raphson', 'red')
    graficar(historiaCANRM , 'NR modificado', 'orange')
    graficar(historiaCASEC, 'Secante', 'green')


    plt.xlabel('Iteración')
    plt.ylabel('Lambda')
    plt.legend(loc='best')
    plt.title(funcion)
    plt.grid(True)
    plt.show()
