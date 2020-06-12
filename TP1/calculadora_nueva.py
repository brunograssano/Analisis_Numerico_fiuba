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
        e_n_mas_1 = historiaRaices[n+1][1] - historiaRaices[n][1]
        e_n = historiaRaices[n][1] - historiaRaices[n - 1][1]
        e_n_menos_1 = historiaRaices[n - 1][1] - historiaRaices[n - 2][1]

        if (np.abs(np.log10(np.abs(e_n / e_n_menos_1))) < 1e-13) or (np.abs(e_n) < 1e-13) or (np.abs(e_n_menos_1) < 1e-13) or (np.abs(e_n_mas_1) < 1e-13):
            continue
        else:
            alfa[j] = j, np.log10(np.abs(e_n_mas_1 / e_n)) / np.log10(np.abs(e_n / e_n_menos_1))
            j = j+1

    alfa = alfa[:j]
    print(alfa)

    return alfa[j - 1][1], alfa



def CalcularHistoriaConstanteAsintotica(historia, alfa):
    """
    Calcula la constante lambda, necesita de la historia de la busqueda de la raiz y del alfa obtenido previamente
    Devuelve la historia del lambda y el lambda final conseguido
    """
    if alfa <= 0:
        return 0, np.array([])
    tope = len(historia)
    raiz = historia[tope - 1][1]

    historiaConstanteAsintotica = np.zeros((tope - 2, 2))
    j = 0
    for i in range(1, tope - 2):
        xMas1 = historia[i+1][1]
        x = historia[i][1]
        xMenos1 = historia[i-1][1]

        numerador = abs(xMas1 - x)
        denominador = abs(x - xMenos1) ** alfa

        constanteActual = numerador / denominador

        if not (constanteActual == 0):
            historiaConstanteAsintotica[j][1] = constanteActual
            historiaConstanteAsintotica[j][0] = j
            j = j + 1

    historiaConstanteAsintotica = historiaConstanteAsintotica[:j]

    print(historiaConstanteAsintotica)

    return historiaConstanteAsintotica[j - 1][1], historiaConstanteAsintotica
