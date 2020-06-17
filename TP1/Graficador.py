import matplotlib.pyplot as plt
import numpy as np


def MaximoLen(historiaBIS, historiaNR, historiaNRM, historiaSEC):
    """
    Identificara la historia con mas iteraciones.
    """
    bis = len(historiaBIS)
    nr = len(historiaNR)
    nrm = len(historiaNRM)
    sec = len(historiaSEC)
    return max(bis, nr, nrm, sec)


def ExtenderHistoria(historia, tope):
    """
    Extiende las historias de las raices para que queden uniformes en el grafico.
    """

    if historia.size == 0:
        return historia
    long = len(historia)

    historiaExtendida = np.zeros((tope, 2))

    raiz = historia[long - 1][1]

    for i in range(0, tope):

        if i < long:
            historiaExtendida[i][0] = i
            historiaExtendida[i][1] = historia[i][1]
        else:
            historiaExtendida[i][0] = i
            historiaExtendida[i][1] = raiz

    return historiaExtendida


def ExtenderHistorias(historiaBIS, historiaNR, historiaNRM, historiaSEC):
    """
    Extendera las historias de las raices para que queden uniformes en el grafico.
    """
    tope = MaximoLen(historiaBIS, historiaNR, historiaNRM, historiaSEC)
    return ExtenderHistoria(historiaBIS, tope) \
        , ExtenderHistoria(historiaNR, tope) \
        , ExtenderHistoria(historiaNRM, tope) \
        , ExtenderHistoria(historiaSEC, tope)


def graficar(historia, nombre, color):
    """
    Agrega al grafico los datos correspondientes a un metodo.
    """
    if historia.size != 0:
        plt.plot(historia[:, 0], historia[:, 1], '-', lw=1, label=nombre, color=color)
    else:
        plt.plot(0, 0, '*', lw=0, label=nombre + '; no suf datos.', color=color)


def GraficarMetodos(historiaBiseccion, historiaNR, historiaNRM, historiaSecante, funcion):
    """
    Recibe las historias de cada metodo, estas deben de ser validas, caso contrario, se indicara en el grafico la falta de datos.
    Necesita tambien de la funcion para usarlo como titulo identificatorio del grafico.
    """
    plt.figure()
    historiaBiseccion, historiaNR, historiaNRM, historiaSecante = ExtenderHistorias(historiaBiseccion, historiaNR, historiaNRM, historiaSecante)

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


def GraficarOrdenDeConvergencia(historiaOCBiseccion, historiaOCNewtonRaphson, historiaOCNewtonRaphsonModif, historiaOCSec, funcion):
    """
    Recibe las historias de de las constantes de ordenes de convergencia, estas deben de ser validas, caso contrario,
    se indicara en el grafico la falta de datos.
    Necesita tambien de la funcion para usarlo como titulo identificatorio del grafico.
    """
    plt.figure()
    axes = plt.gca()
    axes.set_ylim([0, 2.5])
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


def GraficarConstantesAsintoticas(historiaCABIS, historiaCANR, historiaCANRM, historiaCASEC, funcion):
    """
    Recibe las historias de de las constantes de ordenes de convergencia, estas deben de ser validas, caso contrario,
    se indicara en el grafico la falta de datos.
    Necesita tambien de la funcion para usarlo como titulo identificatorio del grafico.
    """
    plt.figure()
    axes = plt.gca()
    axes.set_ylim([0, 1.5])
    graficar(historiaCABIS, 'Biseccion', 'blue')
    graficar(historiaCANR, 'Newton-Raphson', 'red')
    graficar(historiaCANRM, 'NR modificado', 'orange')
    graficar(historiaCASEC, 'Secante', 'green')

    plt.xlabel('Iteración')
    plt.ylabel('Lambda')
    plt.legend(loc='best')
    plt.title(funcion)
    plt.grid(True)
    plt.show()
