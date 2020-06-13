import numpy as np


def CalcularHistoriaDeOrden(historiaRaices):
    """
    Calcula la constante alfa, necesita de la historia de la busqueda de la raiz.
    Devuelve la historia del alfa y el alfa final conseguido
    """

    if len(historiaRaices) < 5:
        return 0, np.array([])

    nIteraciones = len(historiaRaices)
    alfa = np.zeros((nIteraciones - 1, 2))

    j = 0
    for n in range(2, nIteraciones - 1):
        a = historiaRaices[n+1][1] - historiaRaices[n][1]
        b = historiaRaices[n][1] - historiaRaices[n - 1][1]
        c = historiaRaices[n - 1][1] - historiaRaices[n - 2][1]

        if (np.abs(np.log10(np.abs(b / c))) < 1e-13) or (np.abs(b) < 1e-13) or (np.abs(c) < 1e-13) or (np.abs(a) < 1e-13) or (np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))) > 3 \
                or (np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))) < 0:
            continue
        else:
            alfa[j] = j, np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))
            j = j+1

    alfa = alfa[:j]
    print(alfa)
    if j == 0:
        return 0,alfa
    return alfa[j - 1][1], alfa



def CalcularHistoriaConstanteAsintotica(historia, alfa):
    """
    Calcula la constante lambda, necesita de la historia de la busqueda de la raiz y del alfa obtenido previamente
    Devuelve la historia del lambda y el lambda final conseguido
    """
    if alfa <= 0:
        return 0, np.array([])
    tope = len(historia)

    historiaConstanteAsintotica = np.zeros((tope - 2, 2))
    j = 0
    for i in range(1, tope - 1):
        xMas1 = historia[i+1][1]
        x = historia[i][1]
        xMenos1 = historia[i-1][1]

        numerador = abs(xMas1 - x)
        denominador = abs(x - xMenos1) ** alfa

        if numerador < 1e-13 or denominador < 1e-13 or xMas1< 1e-13 or x<1e-13 or xMenos1<1e-13 or (numerador / denominador)<1e-13 or (numerador / denominador)>1 or (numerador / denominador)<0:
            continue
        else:
            constanteActual = numerador / denominador
            historiaConstanteAsintotica[j][1] = constanteActual
            historiaConstanteAsintotica[j][0] = j
            j = j + 1


    historiaConstanteAsintotica = historiaConstanteAsintotica[:j]

    print(historiaConstanteAsintotica)

    if j == 0:
        return 0,historiaConstanteAsintotica
    return historiaConstanteAsintotica[j - 1][1], historiaConstanteAsintotica
